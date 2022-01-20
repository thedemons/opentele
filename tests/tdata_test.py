
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

def PythonVersion():
    return "3.10"
    return "{}.{}".format(sys.version_info.major, sys.version_info.minor)

def profile_path():
    return "tests/test_profile{}".format(PythonVersion())
    
async def tdata_to_telethon():



    api_ios = API.TelegramIOS.Generate(profile_path())
    api_android = API.TelegramAndroid.Generate()


    tdesk = TDesktop(profile_path(), api_ios, "!thedemons#opentele", "opentele#thedemons!")
    assert tdesk.isLoaded()
    

    oldClient = await tdesk.ToTelethon(flag=UseCurrentSession, api=api_ios)

    await oldClient.connect()
    assert await oldClient.is_user_authorized()
    await oldClient.PrintSessions()
    
    newClient = await oldClient.QRLoginToNewClient(api=api_android, password="!thedemons#opentele")

    await newClient.connect()
    assert await newClient.is_user_authorized()
    await newClient.PrintSessions()


    try: 
        await oldClient.TerminateAllSessions()
    except FreshResetAuthorisationForbiddenError as e:
        pass

    tdesk = await newClient.ToTDesktop(UseCurrentSession, api=api_android)
    tdesk.SaveTData(profile_path(), "!thedemons#opentele", "opentele#thedemons!")


    await oldClient.disconnect()
    await newClient.disconnect()
    await oldClient.disconnected
    await newClient.disconnected
    


@pytest.mark.asyncio
async def test_entry_point(event_loop):

    ter = TerminalWriter(sys.stdout)
    ter.hasmarkup = True
    event_loop._close = event_loop.close
    event_loop.close = lambda: None

    ter.write("\n\n")
    ter.sep("=", "Begin testing for Python {}".format(PythonVersion()) , cyan=True)

    try:
        await tdata_to_telethon()

    except asyncio.CancelledError as e:
        ter.sep("-", "Catched Exception: {}".format(e.__str__()), red=True)
    
