
from opentele.td import TDesktop
from opentele.api import API, CreateNewSession

import pytest

@pytest.mark.asyncio
async def test_tdata_to_telethon():
    

    api_desktop = API.TelegramDesktop.Generate("windows", "!thedemons#opentele")
    api_ios = API.TelegramIOS.Generate("!thedemons#opentele")

    tdesk = TDesktop("tests/tdata_test_profile", api_desktop, "!thedemons#opentele", "opentele#thedemons!")
    assert tdesk.isLoaded()

    client = await tdesk.ToTelethon("tests/session_test.session", CreateNewSession, API.TelegramIOS.Generate(), "fs0ci3ty")
    await client.connect()
    assert client.is_user_authorized()

    await client.PrintSessions()

    tdesk.SaveTData("tests/tdata_test_profile", "!thedemons#opentele", "opentele#thedemons!")
