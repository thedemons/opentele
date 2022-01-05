
from .tdesktop import *

from telethon.client.telegramclient import TelegramClient
from telethon.sessions import StringSession

from telethon import tl, functions, sync, utils, password as pwd_mod
from telethon.tl.tlobject import TLRequest, TLObject
from telethon.tl.types import TypeInputClientProxy, TypeJSONValue

from typing import Optional

import struct
import os


class APIData(object):
    CustomInitConnectionList = []
    def __init__(self, api_id, api_hash, device_model, system_version, app_version, system_lang_code, lang_pack, lang_code) -> None:
        self.api_id = api_id
        self.api_hash = api_hash
        self.device_model = device_model
        self.system_version = system_version
        self.app_version = app_version
        self.system_lang_code = system_lang_code
        self.lang_pack = lang_pack
        self.lang_code = lang_code
        self.__pid = os.urandom(32)
        APIData.CustomInitConnectionList.append(self)

    @property
    def pid(self):
        return self.__pid

    def destroy(self):
        self.__del__()

    def __eq__(self, __o: object) -> bool:
        if (type(__o) != APIData): return False
        return self.pid == __o.pid
    
    def findData(pid : int) -> object:
        for x in APIData.CustomInitConnectionList:
            if x.pid == pid: return x
        return None
    
    def __del__(self):
        # might cause conflict, disabled for now, it won't be a problem
        # if (APIData.findData(self.pid) != None):
        #     APIData.CustomInitConnectionList.remove(self)
        
        pass

class APIData(APIData):
    
    TelegramDesktop = APIData(
        api_id=2040,
        api_hash="b18441a1ff607e10a989891a5462e627",
        device_model='Desktop',
        system_version='Windows 10',
        app_version='3.4.3 x64',
        lang_code='en',
        system_lang_code='en-US',
        lang_pack='tdesktop',
    )

    TelegramAndroid = APIData(
        api_id=6,
        api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e",
        device_model='Samsung SM-G998B',
        system_version='12 S? (31)',
        app_version='8.4.1 (2522)',
        lang_code='en',
        system_lang_code='en-US',
        lang_pack='android',
    )

    TelegramIOS = APIData(
        api_id=8,
        api_hash="7245de8e747a0d6fbe11f7cc14fcc0bb",
        device_model='iPhone 13 Pro Max',
        system_version='14.4.2',
        app_version='8.3',
        lang_code='en',
        system_lang_code='en-US',
        lang_pack='ios',
    )

class CustomInitConnectionRequest(TLRequest):
    CONSTRUCTOR_ID = 0xc1cd5ea9
    SUBCLASS_OF_ID = 0xb7b2364b

    def __init__(self, api_id: int, device_model: str, system_version: str, app_version: str, system_lang_code: str, lang_pack: str, lang_code: str, query: 'TypeX', proxy: Optional['TypeInputClientProxy']=None, params: Optional['TypeJSONValue']=None):
        """
        :returns X: This type has no constructors.
        """
        
        # our hook pass pid as device_model
        data = APIData.findData(device_model)
        if data != None:
            self.api_id = data.api_id
            self.device_model = data.device_model
            self.system_version = data.system_version
            self.app_version = data.app_version
            self.system_lang_code = data.system_lang_code
            self.lang_pack = data.lang_pack
            self.lang_code = data.lang_code
            data.destroy()
        else:
            self.api_id = api_id
            self.device_model = device_model
            self.system_version = system_version
            self.app_version = app_version
            self.system_lang_code = system_lang_code
            self.lang_pack = lang_pack
            self.lang_code = lang_code
        
        self.query = query
        self.proxy = proxy
        self.params = params

    def to_dict(self):
        return {
            '_': 'InitConnectionRequest',
            'api_id': self.api_id,
            'device_model': self.device_model,
            'system_version': self.system_version,
            'app_version': self.app_version,
            'system_lang_code': self.system_lang_code,
            'lang_pack': self.lang_pack,
            'lang_code': self.lang_code,
            'query': self.query.to_dict() if isinstance(self.query, TLObject) else self.query,
            'proxy': self.proxy.to_dict() if isinstance(self.proxy, TLObject) else self.proxy,
            'params': self.params.to_dict() if isinstance(self.params, TLObject) else self.params
        }

    def _bytes(self):
        return b''.join((
            b'\xa9^\xcd\xc1',
            struct.pack('<I', (0 if self.proxy is None or self.proxy is False else 1) | (0 if self.params is None or self.params is False else 2)),
            struct.pack('<i', self.api_id),
            self.serialize_bytes(self.device_model),
            self.serialize_bytes(self.system_version),
            self.serialize_bytes(self.app_version),
            self.serialize_bytes(self.system_lang_code),
            self.serialize_bytes(self.lang_pack),
            self.serialize_bytes(self.lang_code),
            b'' if self.proxy is None or self.proxy is False else (self.proxy._bytes()),
            b'' if self.params is None or self.params is False else (self.params._bytes()),
            self.query._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _api_id = reader.read_int()
        _device_model = reader.tgread_string()
        _system_version = reader.tgread_string()
        _app_version = reader.tgread_string()
        _system_lang_code = reader.tgread_string()
        _lang_pack = reader.tgread_string()
        _lang_code = reader.tgread_string()
        if flags & 1:
            _proxy = reader.tgread_object()
        else:
            _proxy = None
        if flags & 2:
            _params = reader.tgread_object()
        else:
            _params = None
        _query = reader.tgread_object()
        return cls(api_id=_api_id, device_model=_device_model, system_version=_system_version, app_version=_app_version, system_lang_code=_system_lang_code, lang_pack=_lang_pack, lang_code=_lang_code, query=_query, proxy=_proxy, params=_params)


# Hook InitConnectionRequest to change API_ID API_HASH, device_model,... etc
oldInitConnectionRequest = tl.functions.InitConnectionRequest
tl.functions.InitConnectionRequest = CustomInitConnectionRequest


class TDesktop(TDesktop):
    def ToTelethon(self) -> TelegramClient:
        
        ss = StringSession()
        ss.set_dc(self.MainDcId, self.GetDcIp(self.MainDcId), 443)

        ss.auth_key = TelethonAuthKey(self.authKey.key)
        
        data = APIData.TelegramDesktop
        return TelegramClient(ss, data.api_id, data.api_hash, device_model=data.pid) # pass hook data pid through device_model
        
    async def ToNewTelethonSession(self, session_name : str, customAPI : APIData = None) -> TelegramClient:
        
        resolve_file_name = session_name
        if resolve_file_name[-8:] != ".session": resolve_file_name += ".session"

        if os.path.exists(resolve_file_name):
            os.remove(resolve_file_name)

        if customAPI != None:
            newClient = TelegramClient(session_name, customAPI.api_id, customAPI.api_hash, device_model=customAPI.pid) # pass hook data pid through device_model
        else:
            defaultAPI =  APIData.TelegramDesktop
            newClient = TelegramClient(session_name, defaultAPI.api_id, defaultAPI.api_hash, )
        
        oldClient = self.ToTelethon()

        await oldClient.connect()
        await newClient.connect()
        oldMe = await oldClient.get_me()
        
        qr_login = await newClient.qr_login()
        
        try:
            resp = await oldClient(tl.functions.auth.AcceptLoginTokenRequest(qr_login.token))
            print(resp)
        except BaseException as e:
            pass

        try:
            await qr_login.wait()
        except telethon.errors.SessionPasswordNeededError as e:

            # two-step verification
            username = oldMe.username if (oldMe.username != None) else utils.get_display_name(oldMe)
            password = input(f"Password for {username}: ")

            pwd = await newClient(tl.functions.account.GetPasswordRequest())
            result = await newClient(tl.functions.auth.CheckPasswordRequest(
                pwd_mod.compute_check(pwd, password)))
        
            newClient._on_login(result.user)

        await newClient.get_me()
        return newClient
