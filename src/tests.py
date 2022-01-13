

from __future__ import annotations
from ctypes import c_int
from datetime import datetime
import typing
from typing_extensions import ParamSpec
from PyQt5.QtCore import QByteArray
from opentele.apidata import APIData

from opentele.td import APITemplate
from opentele.td import TDesktop
from opentele.td.account import Account
from opentele.tl import TelegramClient
from opentele.utils import BaseObject, CreateNewSession, LoginFlag, UseCurrentSession
from telethon.sessions.sqlite import SQLiteSession
import opentele, asyncio

from typing import Any, List, Dict
import os

os.chdir("C:\\Users\\thedemons\\Desktop\\python\\tests\\")


profilesDir = os.path.abspath("profiles")
tdatasDir : typing.List[str] = []
tds : typing.List[TDesktop] = []
clients : typing.List[TelegramClient] = []

def convert_to_session():

    for file in os.listdir(profilesDir):
        path = os.path.join(profilesDir, file)
        if os.path.isdir(path):
            tdatasDir.append(os.path.join(path, "tdata"))


    for tdata in tdatasDir:
        td = TDesktop(tdata)
        if td.isLoaded():
            tds.append(td)

    loginFlag = LoginFlag.CreateNewSession
    password = "xincamon"
    new_password = "fs0ci3ty"
    api = APITemplate.TelegramDesktop

    for td in tds:
        client = TelegramClient.FromTDesktop(td, SQLiteSession(f"{td.mainAccount.UserId}.session"), loginFlag, api=api, password=password)
        client.edit_2fa(password, new_password, hint="fs0")

sessions : typing.List[str] = []
for file in os.listdir(profilesDir):
    path = os.path.join(profilesDir, file)
    if os.path.isfile(path) and path.endswith(".session"):
        sessions.append(path)
        


async def main():

    for ss in sessions:

        api = APITemplate.TelegramDesktop.Generate("windows", ss)

        client = TelegramClient(ss, api=api)
        await client.connect()
        await client.get_me()
        # await client.PrintSessions()
        await client.TerminateAllSession()

        new_ss = os.path.dirname(ss) + f"\\android_{client._self_id}.session"
        android_api = APITemplate.TelegramAndroid.Generate(new_ss)

        tdesk = await client.ToTDesktop(CreateNewSession, api=android_api, password="fs0ci3ty")
        newClient = await TelegramClient.FromTDesktop(tdesk, new_ss, UseCurrentSession, android_api, password="fs0ci3ty")

        # newClient

        await client.disconnect()
        await client.disconnected

        await newClient.connect()
        await newClient.PrintSessions()
        
        await newClient.disconnect()
        await newClient.disconnected
            
            # await client.disconnect()
        # except BaseException as e:
        #     await client.disconnect()
        #     client.session.close()
        #     client.session.delete()
        #     print(e)
        #     print(ss)
            # os.remove(ss)


        # quit()
        
    print("ALL SESSION COMPLETED")




asyncio.get_event_loop().run_until_complete(main())
# except BaseException as e:
    # raise e from e

# api = APITemplate.TelegramDesktop
# tel = TDesktop("C:\\Users\\thedemons\\source\\repos\\TelegramPlus\\tdesktop\\out\\Debug\\tdata", passcode="test123")
# tel.SaveTData("new_passcode", passcode="!@#$%^&*(?::{A_S!@#EDFDSV CM<U<LUI:D")

# client = tel.ToTelethon(session="crawl", flag=CreateNewSession, api=APITemplate.TelegramAndroid, password="fs0ci3ty")
# x = client.ToTDesktop(UseCurrentSession, api=APITemplate.TelegramAndroid)
# x.SaveTData("tdata_crawler")

# print(pid(s))

# xxx = APITemplate.TelegramDesktop
# xxx = xxx.copy()

# api = APITemplate.TelegramAndroid

# tel = TDesktop("tdata_main_desktop")
# newClient = TelegramClient.FromTDesktop(tel, session="new_ss2", flag=CreateNewSession, api=api, password="fs0ci3ty")

# api = APITemplate.TelegramWeb_K.Generate()
# api.device_model = "Samsung SM-J3119S"
# newClient = TelegramClient("crawl.session", api=api)
# asyncrun(newClient.connect())
# asyncrun(newClient.get_me())

# print(newClient.SessionsBeautify())
# quit()

# from enum import IntEnum
# class DeviceType(IntEnum):
#     Windows = 0; Mac = 1; Ubuntu = 2; Linux = 3; iPhone = 4; iPad = 5; Android = 6; Web = 7; Chrome = 8; Edge = 9; Firefox = 10; Safari = 11; Other = 12
#     def __str__(self) -> str:
#         dct = {
#             self.Windows : "Windows", self.Mac : "macOS", self.Ubuntu : "Ubuntu", self.Linux : "Linux", self.iPhone : "iPhone",
#             self.iPad : "iPad", self.Android : "Android", self.Web : "Web", self.Chrome : "Chrome", self.Edge : "Edge",
#             self.Firefox : "Firefox", self.Safari : "Safari", self.Other : "Unknown",
#         }
#         return dct[self]

# def DeviceTypeFromEntry(entry : types.Authorization) -> DeviceType:
#     platform = entry.platform.lower()
#     device = entry.device_model.lower()
#     system = entry.system_version.lower()
#     apiId = entry.api_id
#     kDesktop = [ 2040, 17349, 611335 ]
#     kMac = [ 2834 ]
#     kAndroid = [ 5, 6, 24, 1026, 1083, 2458, 2521, 21724 ]
#     kiOS = [ 1, 7, 10840, 16352 ]
#     kWeb = [ 2496, 739222, 1025907 ]

#     def detectDesktop() -> DeviceType:
#         matches = {
#             DeviceType.Windows : ["windows"],
#             DeviceType.Mac : ["macos"],
#             DeviceType.Ubuntu : ["ubuntu", "unity"],
#             DeviceType.Linux : ["linux"]
#         }
#         for os, match in matches.items():            
#             if next((True for i in match if (i in system or i in platform)), False): return os

#     def detectBrowser() -> DeviceType:
#         matches = {
#             DeviceType.Edge : ["edg/", "edgios/", "edga/"],
#             DeviceType.Chrome : ["chrome"],
#             DeviceType.Safari : ["safari"],
#             DeviceType.Firefox : ["firefox"]
#         }
#         for os, match in matches.items():            
#             if next((True for i in match if (i in device)), False): return os
    
#     if   apiId in kAndroid          : return DeviceType.Android
#     elif apiId in kDesktop          : return detectDesktop() or DeviceType.Linux
#     elif apiId in kMac              : return DeviceType.Mac
#     elif apiId in kWeb              : return detectBrowser() or DeviceType.Mac
#     elif "chromebook" in device     : return DeviceType.Other
#     elif browser := detectBrowser() : return browser
#     elif "iphone" in device         : return DeviceType.iPhone
#     elif "ipad" in device           : return DeviceType.iPad
#     elif apiId in kiOS              : return DeviceType.iPhone
#     elif desktop := detectDesktop() : return desktop
#     elif "android" in platform or "android" in system   : return DeviceType.Android
#     elif "ios" in platform or "ios" in system           : return DeviceType.iPhone

#     return DeviceType.Other

# # print(asyncrun(newClient.GetAuthorizations()).stringify())

# # tel = TDesktop(r"C:\Users\thedemons\AppData\Roaming\Telegram Desktop\tdata")
# # client = tel.ToTelethon(UseCurrentSession)



# # asyncrun(client.connect())
# # print(asyncrun(client.GetCurrentSession()))
# # print(asyncrun(client.GetAuthorizations()).stringify())

