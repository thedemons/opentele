from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .api import API, CreateNewSession, UseCurrentSession
from .td import TDesktop
from .tl import TelegramClient

try:
    from textual import on
    from textual.app import App, ComposeResult
    from textual.containers import Container, Horizontal, Vertical
    from textual.widgets import (
        Button,
        Footer,
        Header,
        Input,
        Label,
        RadioButton,
        RadioSet,
        RichLog,
        Select,
        Static,
    )
except ImportError as exc:  # pragma: no cover - runtime dependency
    raise ImportError(
        "opentele-tui requires `textual` to be installed. "
        "Install it with: pip install 'opentele[tui]'"
    ) from exc


API_OPTIONS = [
    ("Telegram Desktop", "desktop"),
    ("Telegram Android", "android"),
    ("Telegram iOS", "ios"),
]

FLAG_OPTIONS = [
    ("Create New Session", "new"),
    ("Use Current Session", "current"),
]


@dataclass
class ConversionConfig:
    mode: str
    source_path: str
    destination_path: str
    api: str
    login_flag: str
    password: str


class OpenTeleTui(App):
    """Beginner-friendly Textual app for converting Telegram sessions."""

    CSS = """
    Screen {
        layout: vertical;
    }

    #main {
        height: 1fr;
        padding: 1 2;
    }

    #title {
        margin-bottom: 1;
    }

    #form {
        height: auto;
        border: round $panel;
        padding: 1;
    }

    .field {
        margin-bottom: 1;
    }

    #run {
        margin-top: 1;
    }

    #logs {
        margin-top: 1;
        border: round $panel;
        height: 1fr;
    }
    """

    TITLE = "opentele-tui"

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Container(id="main"):
            yield Static(
                "[b]OpenTele TUI[/b] - friendly guided conversion for Telegram sessions",
                id="title",
            )
            with Vertical(id="form"):
                yield Label("Conversion mode", classes="field")
                with RadioSet(id="mode"):
                    yield RadioButton(
                        "tdata folder → telethon session", id="mode-tdata", value=True
                    )
                    yield RadioButton("telethon session → tdata folder", id="mode-session")

                yield Label("Source path", classes="field")
                yield Input(
                    placeholder="Path to source (tdata folder or .session file)",
                    id="source-path",
                )

                yield Label("Destination path", classes="field")
                yield Input(
                    placeholder="Output path (.session or tdata folder)",
                    id="dest-path",
                )

                with Horizontal(classes="field"):
                    yield Label("API profile")
                    yield Select(API_OPTIONS, value="desktop", id="api")

                with Horizontal(classes="field"):
                    yield Label("Login method")
                    yield Select(FLAG_OPTIONS, value="new", id="flag")

                yield Label("2FA password (optional)", classes="field")
                yield Input(password=True, id="password")

                yield Button("Run conversion", variant="success", id="run")

            yield RichLog(id="logs", auto_scroll=True, wrap=True, markup=True)
        yield Footer()

    def _log(self, message: str) -> None:
        self.query_one("#logs", RichLog).write(message)

    def _get_api(self, key: str):
        mapping = {
            "desktop": API.TelegramDesktop,
            "android": API.TelegramAndroid,
            "ios": API.TelegramIOS,
        }
        return mapping[key]

    def _get_flag(self, key: str):
        return CreateNewSession if key == "new" else UseCurrentSession

    def _read_form(self) -> Optional[ConversionConfig]:
        mode = "tdata_to_session"
        if self.query_one("#mode-session", RadioButton).value:
            mode = "session_to_tdata"

        source = self.query_one("#source-path", Input).value.strip()
        destination = self.query_one("#dest-path", Input).value.strip()

        if not source or not destination:
            self._log("[red]Source and destination paths are required.[/red]")
            return None

        return ConversionConfig(
            mode=mode,
            source_path=source,
            destination_path=destination,
            api=str(self.query_one("#api", Select).value),
            login_flag=str(self.query_one("#flag", Select).value),
            password=self.query_one("#password", Input).value,
        )

    async def _convert(self, config: ConversionConfig) -> None:
        api = self._get_api(config.api)
        flag = self._get_flag(config.login_flag)
        password = config.password or None

        if config.mode == "tdata_to_session":
            self._log("[yellow]Loading tdata...[/yellow]")
            tdesk = TDesktop(config.source_path)
            self._log("[yellow]Converting to telethon session...[/yellow]")
            client = await tdesk.ToTelethon(
                config.destination_path,
                flag=flag,
                api=api,
                password=password,
            )
            await client.connect()
            me = await client.get_me()
            await client.disconnect()
            self._log(
                f"[green]Success![/green] Session saved to [b]{config.destination_path}[/b] for {me.first_name}."
            )
            return

        self._log("[yellow]Connecting to telethon session...[/yellow]")
        client = TelegramClient(config.source_path, api=api)
        await client.connect()
        if not await client.is_user_authorized():
            await client.disconnect()
            self._log(
                "[red]Session is not authorized. Please login with Telethon first.[/red]"
            )
            return

        self._log("[yellow]Converting to tdata...[/yellow]")
        tdesk = await TDesktop.FromTelethon(
            client,
            flag=flag,
            api=api,
            password=password,
        )
        tdesk.SaveTData(config.destination_path)
        await client.disconnect()
        self._log(
            f"[green]Success![/green] tdata saved to [b]{config.destination_path}[/b]."
        )

    @on(Button.Pressed, "#run")
    def run_conversion(self) -> None:
        config = self._read_form()
        if not config:
            return

        self._log("[cyan]Starting conversion...[/cyan]")

        async def runner() -> None:
            try:
                await self._convert(config)
            except Exception as exc:  # pragma: no cover - defensive runtime handler
                self._log(f"[red]Conversion failed:[/red] {exc}")

        self.run_worker(runner(), exclusive=True)


def main() -> None:
    OpenTeleTui().run()


if __name__ == "__main__":
    main()
