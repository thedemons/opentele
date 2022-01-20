

import sys, pathlib
base_dir = pathlib.Path(__file__).parent.parent.absolute().__str__()
sys.path.insert(1, base_dir)

from src.td import TDesktop
from src.api import API, CreateNewSession, UseCurrentSession

import pytest
import asyncio

async def tdata_to_telethon():
    

    api_desktop = API.TelegramDesktop.Generate("windows", "!thedemons#opentele")
    api_ios = API.TelegramIOS.Generate("!thedemons#opentele")

    tdesk = TDesktop("tests/tdata_test_profile", api_desktop, "!thedemons#opentele", "opentele#thedemons!")
    assert tdesk.isLoaded()
    

    oldClient = await tdesk.ToTelethon(flag=UseCurrentSession, api=api_desktop)
    await oldClient.connect()
    assert await oldClient.is_user_authorized()

    await oldClient.PrintSessions()


    newClient = await tdesk.ToTelethon(flag=CreateNewSession,  api=api_ios, password="!thedemons#opentele")
    await newClient.connect()
    assert await newClient.is_user_authorized()

    await newClient.PrintSessions()

    await oldClient.TerminateAllSessions()

    tdesk = await oldClient.ToTDesktop(UseCurrentSession, api=api_desktop)
    tdesk.SaveTData("tests/tdata_test_profile", "!thedemons#opentele", "opentele#thedemons!")

def test_entry_point():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tdata_to_telethon())
