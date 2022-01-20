
import sys, pathlib
base_dir = pathlib.Path(__file__).parent.parent.absolute().__str__()
sys.path.insert(1, base_dir)


from src.td import TDesktop
from src.tl.telethon import TelegramClient
from src.api import API, CreateNewSession, UseCurrentSession
from telethon.errors.rpcerrorlist import FreshResetAuthorisationForbiddenError

import asyncio
import pytest
import pytest_asyncio
from _pytest._io import TerminalWriter

@pytest.mark.asyncio
async def test_entry_point(event_loop):

    ter = TerminalWriter(sys.stdout)
    ter.hasmarkup = True
    event_loop._close = event_loop.close
    event_loop.close = lambda: None

    ter.write("\n\n")
    ter.sep("=", "Begin testing", cyan=True)

    try:
        await tdata_to_telethon()

    except (asyncio.CancelledError, asyncio.TimeoutError) as e:
        ter.sep("-", "Catched Exception: {}".format(e.__str__()), red=True)
    

async def tdata_to_telethon():

    def profile_path():
        return "tests/test_profile{}".format(sys.version.split(" ")[0])


    api_desktop = API.TelegramDesktop.Generate("windows", "!thedemons#opentele")
    api_ios = API.TelegramIOS.Generate("!thedemons#opentele")


    tdesk = TDesktop(profile_path(), api_desktop, "!thedemons#opentele", "opentele#thedemons!")
    assert tdesk.isLoaded()
    

    oldClient = await tdesk.ToTelethon(flag=UseCurrentSession, api=api_desktop)

    await oldClient.connect()
    assert await oldClient.is_user_authorized()
    await oldClient.PrintSessions()
    

    newClient = await tdesk.ToTelethon(flag=CreateNewSession,  api=api_ios, password="!thedemons#opentele")

    await newClient.connect()
    assert await newClient.is_user_authorized()
    await newClient.PrintSessions()


    # try: 
    #     await oldClient.TerminateAllSessions()
    # except FreshResetAuthorisationForbiddenError as e:
    #     pass


    tdesk = await newClient.ToTDesktop(UseCurrentSession, api=api_desktop)
    tdesk.SaveTData(profile_path(), "!thedemons#opentele", "opentele#thedemons!")


    await oldClient.disconnect()
    await newClient.disconnect()
    await oldClient.disconnected
    await newClient.disconnected
    

