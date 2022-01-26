import os, sys, pathlib
import re
import atexit

base_dir = pathlib.Path(__file__).parent.parent.absolute().__str__()
sys.path.insert(1, base_dir)

debug_py = os.path.join(base_dir, "src", "debug.py")
debug_bk_py = os.path.join(base_dir, "src", "debug_bk.py")


def on_exit():
    os.remove(debug_py)
    os.rename(debug_bk_py, debug_py)


def on_init():

    os.rename(debug_py, debug_bk_py)
    src = open(debug_bk_py, "r")
    dst = open(debug_py, "w")
    content = src.read()
    content = re.sub(r"IS_DEBUG_MODE =(.*)", "IS_DEBUG_MODE = True", content)
    dst.write(content)
    src.close()
    dst.close()
    atexit.register(on_exit)


on_init()


from src.td import TDesktop
from src.td.account import Account
from src.tl.telethon import TelegramClient
from src.api import API, APIData, CreateNewSession, UseCurrentSession
from telethon.errors.rpcerrorlist import FreshResetAuthorisationForbiddenError

import pytest
import typing as t
from _pytest._io import TerminalWriter

X1 = "!thedemons#opentele"
X2 = "opentele#thedemons!"


def PythonVersion():
    return "{}.{}".format(sys.version_info.major, sys.version_info.minor)


def profile_path():
    return "tests/test_profile{}".format(PythonVersion())


def test_random_api():

    API_TYPE = t.Union[APIData, t.Type[APIData]]

    def cmp(src: API_TYPE, dst: API_TYPE) -> bool:
        return (
            src.api_id == dst.api_id
            and src.api_hash == dst.api_hash
            and src.device_model == dst.device_model
            and src.system_version == dst.system_version
            and src.app_version == dst.app_version
            and src.lang_code == dst.lang_code
            and src.system_lang_code == dst.system_lang_code
            and src.lang_pack == dst.lang_pack
        )

    apis: t.List[API_TYPE] = [
        API.TelegramDesktop,
        API.TelegramAndroid,
        API.TelegramAndroidX,
        API.TelegramIOS,
        API.TelegramMacOS,
        API.TelegramWeb_Z,
        API.TelegramWeb_K,
        API.Webogram,
    ]
    for api in apis:
        assert cmp(api, api())

        # not support .Generate() yet
        if (
            api != API.TelegramWeb_Z
            and api != API.TelegramWeb_K
            and api != API.Webogram
        ):
            check = False

            for x in range(10):
                check |= not cmp(api.Generate(), api.Generate())

            assert check

    assert cmp(
        API.TelegramDesktop.Generate("windows", "opentele"),
        API.TelegramDesktop.Generate("windows", "opentele"),
    )

    assert not cmp(
        API.TelegramDesktop.Generate("windows", "opentele"),
        API.TelegramDesktop.Generate("linux", "opentele"),
    )

    assert not cmp(
        API.TelegramDesktop.Generate("macos", "opentele"),
        API.TelegramDesktop.Generate("linux", "opentele"),
    )

    assert not cmp(
        API.TelegramDesktop.Generate("windows", "opentele"),
        API.TelegramDesktop.Generate("windows", "opentele2"),
    )


async def tdata_to_telethon():

    api_ios = API.TelegramIOS.Generate(X1)
    api_android = API.TelegramAndroid.Generate()

    tdesk = TDesktop(profile_path(), api_ios, X1, X2)
    assert tdesk.isLoaded()

    oldClient = await tdesk.ToTelethon(flag=UseCurrentSession, api=api_ios)
    tdesk = await oldClient.ToTDesktop(UseCurrentSession, api=api_ios)

    await oldClient.connect()
    assert await oldClient.is_user_authorized()
    await oldClient.PrintSessions()

    newClient = await oldClient.QRLoginToNewClient(api=api_android, password=X1)

    await newClient.connect()
    assert await newClient.is_user_authorized()
    await newClient.PrintSessions()

    # try:
    #     await oldClient.TerminateAllSessions()
    # except FreshResetAuthorisationForbiddenError as e:
    #     pass

    tdesk = await oldClient.ToTDesktop(UseCurrentSession, api=api_ios)
    oldClient = await tdesk.ToTelethon(flag=UseCurrentSession, api=api_ios)

    tdesk = await oldClient.ToTDesktop(UseCurrentSession, api=api_ios)
    tdesk.SaveTData(profile_path(), X1, X2)

    await oldClient.disconnect()
    await newClient.disconnect()
    await oldClient.disconnected
    await newClient.disconnected


async def telethon_from_tdata():

    api_ios = API.TelegramIOS.Generate(X1)
    api_android = API.TelegramAndroid.Generate()

    tdesk = TDesktop(profile_path(), api_ios, X1, X2)
    assert tdesk.isLoaded()

    oldClient = await TelegramClient.FromTDesktop(
        tdesk, flag=UseCurrentSession, api=api_ios
    )
    tdesk = await TDesktop.FromTelethon(oldClient, UseCurrentSession, api=api_ios)

    await oldClient.connect()
    assert await oldClient.is_user_authorized()
    await oldClient.PrintSessions()

    newClient = await oldClient.QRLoginToNewClient(api=api_android, password=X1)

    await newClient.connect()
    assert await newClient.is_user_authorized()
    await newClient.PrintSessions()

    # try:
    #     await oldClient.TerminateAllSessions()
    # except FreshResetAuthorisationForbiddenError as e:
    #     pass

    tdesk = await TDesktop.FromTelethon(oldClient, UseCurrentSession, api=api_ios)
    oldClient = await TelegramClient.FromTDesktop(
        tdesk, flag=UseCurrentSession, api=api_ios
    )

    tdesk = await TDesktop.FromTelethon(oldClient, UseCurrentSession, api=api_ios)
    tdesk.SaveTData(profile_path(), X1, X2)

    await oldClient.disconnect()
    await newClient.disconnect()
    await oldClient.disconnected
    await newClient.disconnected


async def check_telegramclient():
    api_ios = API.TelegramIOS.Generate(X1)

    tdesk = TDesktop(profile_path(), api_ios, X1, X2)
    assert tdesk.isLoaded()

    assert (
        TelegramClient().api_id == API.TelegramDesktop.api_id
        and TelegramClient().api_hash == API.TelegramDesktop.api_hash
    )
    assert TelegramClient(None, 1234, "opentele").api_id == 1234
    assert TelegramClient(None, None, 1234, "opentele").api_id == 1234

    oldClient = await TelegramClient.FromTDesktop(
        tdesk, flag=UseCurrentSession, api=api_ios
    )

    try:
        await oldClient.TerminateSession(0)
    except BaseException as e:
        pass

    await oldClient.connect()
    assert await oldClient.is_user_authorized()
    assert await oldClient.is_official_app()
    assert await oldClient.GetCurrentSession()

    account = await Account.FromTelethon(oldClient, flag=UseCurrentSession, api=api_ios)

    try:
        await oldClient.TerminateSession(0)
    except BaseException as e:
        pass

    assert await oldClient.TerminateAllSessions()

    await oldClient.disconnect()
    await oldClient.disconnected


@pytest.mark.asyncio
async def test_entry_point(event_loop):

    ter = TerminalWriter(sys.stdout)
    ter.hasmarkup = True
    event_loop._close = event_loop.close
    event_loop.close = lambda: None

    ter.write("\n\n")
    ter.sep("=", "Begin testing for Python {}".format(PythonVersion()), cyan=True)

    await tdata_to_telethon()
    await telethon_from_tdata()
    await check_telegramclient()
