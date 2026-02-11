from __future__ import annotations

import base64
import struct
from typing import Type, Union

from .configs import *

try:
    from pyrogram import Client as _PyrogramNativeClient
except ImportError:  # pragma: no cover - optional dependency
    _PyrogramNativeClient = None


@extend_class
class PyrogramClient(BaseObject):
    """Helpers for converting sessions to and from ``pyrogram.Client``."""

    @staticmethod
    def _require_pyrogram() -> Type:
        Expects(
            _PyrogramNativeClient is not None,
            exception=OpenTeleException(
                "Pyrogram is not installed. Install it with `pip install pyrogram`."
            ),
        )
        return _PyrogramNativeClient

    @staticmethod
    def SessionStringFromAccount(
        account: td.Account,
        api: Union[Type[APIData], APIData] = API.TelegramDesktop,
        is_bot: bool = False,
        test_mode: bool = False,
    ) -> str:

        Expects(
            account.authKey is not None,
            exception=OpenTeleException("Account has no auth key"),
        )

        if isinstance(api, type):
            api = api()

        packed = struct.pack(
            ">BI?256sQ?",
            int(account.MainDcId),
            int(api.api_id),
            bool(test_mode),
            account.authKey.key,
            int(account.UserId),
            bool(is_bot),
        )
        return base64.urlsafe_b64encode(packed).decode().rstrip("=")

    @staticmethod
    def FromTDesktop(
        account: Union[td.Account, td.TDesktop],
        session_name: str = "opentele_pyrogram",
        api: Union[Type[APIData], APIData] = API.TelegramDesktop,
        **kwargs,
    ):
        Client = PyrogramClient._require_pyrogram()

        if isinstance(account, td.TDesktop):
            Expects(
                account.mainAccount is not None,
                exception=TDesktopHasNoAccount(
                    "There is no account in this instance of TDesktop"
                ),
            )
            account = account.mainAccount

        session_string = PyrogramClient.SessionStringFromAccount(account, api=api)

        if isinstance(api, type):
            api = api()

        return Client(
            session_name,
            api_id=api.api_id,
            api_hash=api.api_hash,
            session_string=session_string,
            **kwargs,
        )

    @staticmethod
    async def ToTDesktop(
        pyrogramClient,
        flag: Type[LoginFlag] = UseCurrentSession,
        api: Union[Type[APIData], APIData] = API.TelegramDesktop,
    ) -> td.TDesktop:
        return await td.TDesktop.FromPyrogram(pyrogramClient, flag=flag, api=api)
