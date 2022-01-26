# Convert tdata to Telethon
This example will show you how to initialize a [TelegramClient][TelegramClient] from `tdata`.

## Preparing
- You need to have a `tdata` folder which is already authorized (have at least one logged-in account).
- The default path to `tdata` folder on Windows is located at `%appdata%\Telegram Desktop\tdata`.
- We need to import these things:
    ```python
    from opentele.td import TDesktop
    from opentele.tl import TelegramClient
    from opentele.api import API, UseCurrentSession, CreateNewSession
    import asyncio
    ```
- And we need to put the main code inside an async function:
    ```python
    async def main():
        # PUT EXAMPLE CODE HERE

    asyncio.run(main())
    ```


## Initialize [TDesktop][TDesktop] from tdata folder
- First we need to load the `tdata` folder into a `TDesktop` object:
    ```python
    # Load TDesktop client from tdata folder
    tdataFolder = r"C:\Users\<username>\AppData\Roaming\Telegram Desktop\tdata"
    tdesk = TDesktop(tdataFolder)
    
    # Check if we have loaded any accounts
    assert tdesk.isLoaded()
    ```

## Converting [TDesktop][TDesktop] to [TelegramClient][TelegramClient]
There are two ways we can do this, either by using the current session, or create (log in to) a new session.

- Use the current session:
    ```python
    # flag=UseCurrentSession
    #
    # Convert TDesktop to Telethon using the current session.
    client = await tdesk.ToTelethon(session="telethon.session", flag=UseCurrentSession)
    ```
- Create a new session:
    ```python
    # flag=CreateNewSession
    #
    # Convert TDesktop to Telethon by creating a new session.
    # CreateNewSession will use the current session (in tdata folder) to authorize a new session using QR Login.
    # If 2FA is enabled for this account, you must specify the password via the password argument.
    # This is of course slower than UseCurrentSession.
    client = await tdesk.ToTelethon(session="telethon.session", flag=CreateNewSession)
    ```

## Connect and print all logged-in sessions.
```python
# Connect and print all logged-in sessions of this client.
# Telethon will save the session to telethon.session on creation.
await client.connect()
await client.PrintSessions()
```

## Final result example
```python
from opentele.td import TDesktop
from opentele.tl import TelegramClient
from opentele.api import API, UseCurrentSession
import asyncio

async def main():

    # Load TDesktop client from tdata folder
    tdataFolder = r"C:\Users\<username>\AppData\Roaming\Telegram Desktop\tdata"
    tdesk = TDesktop(tdataFolder)
    
    # Check if we have loaded any accounts
    assert tdesk.isLoaded()

    # flag=UseCurrentSession
    #
    # Convert TDesktop to Telethon using the current session.
    client = await tdesk.ToTelethon(session="telethon.session", flag=UseCurrentSession)
    
    # Connect and print all logged-in sessions of this client.
    # Telethon will save the session to telethon.session on creation.
    await client.connect()
    await client.PrintSessions()

asyncio.run(main())
```

[TelegramClient]: https://opentele.readthedocs.io/en/latest/documentation/telethon/telegramclient/#class-telegramclient
[TDesktop]: https://opentele.readthedocs.io/en/latest/documentation/telegram-desktop/tdesktop/#class-tdesktop