from __future__ import annotations


from .configs import *
from . import shared as td

import logging
from telethon.network.connection.connection import Connection
from telethon.network.connection.tcpfull import ConnectionTcpFull
from telethon.sessions.abstract import Session

# if TYPE_CHECKING:
#     from . import *


class TDesktop(BaseObject):

    kMaxAccounts : int = int(3)
    kDefaultKeyFile = "data"
    
    @typing.overload
    def __init__(self) -> None:
        """
        Create an empty instance
        """
        pass

    @typing.overload
    def __init__(self,  basePath : str = None,
                        api : Union[Type[APIData], APIData] = APITemplate.TelegramDesktop) -> None:
        pass
                        
    @typing.overload
    def __init__(self,  basePath : str = None,
                        api : Union[Type[APIData], APIData] = APITemplate.TelegramDesktop,
                        *,
                        passcode : str = None,
                        keyFile : str = None) -> None:
        pass

    def __init__(self,  basePath : str = None,
                        api : Union[Type[APIData], APIData] = APITemplate.TelegramDesktop,
                        *,
                        passcode : str = None,
                        keyFile : str = None) -> None:
        """
        
        ### Arguments
            1. basePath (str):\n
                The path to the tdata folder, if the path doesn't exists or its data is corrupted, a new instance is returned
        
        ### Optional
            2. passcode (str, default=""):\n
                The passcode for tdata, same as the Local Passcode on Telegram Desktop
        
            3. keyFile (str, default="data"):\n
                The gKeyFile data name, the same for `Telegram.exe -key gKeyFile`\n
                This argument is rarely used, you should only use this if you understand what it is
        
        ### Examples
        #### Load from a folder or create new instance at C:\\Telegram\\tdata:
        ```python
            td = TDesktop("C:\\Telegram\\tdata")
            print( td.isAuthorized() )
        ```
        """
        self.__accounts : typing.List[td.Account] = []
        self.__basePath = basePath
        self.__keyFile = keyFile if (keyFile != None) else TDesktop.kDefaultKeyFile
        self.__passcode = passcode if (passcode != None) else str("")
        self.__passcodeBytes = self.__passcode.encode("ascii")
        self.__mainAccount : td.Account = None
        self.__active_index = -1
        self.__passcodeKey = None
        self.__localKey = None
        self.__AppVersion = None
        self.__isLoaded = False
        self.__api  = api.copy()

        if basePath != None:
            self.__basePath = td.Storage.GetAbsolutePath(basePath)
            self.LoadData()
        
    @property
    def api(self) -> APIData:
        return self.__api

    @api.setter
    def api(self, value) -> None:
        self.__api = value
        for account in self.accounts:
            account.api = value
    
    @property
    def basePath(self) -> str:
        """
        Base folder of TDesktop, this is where data stored\n
        Same as tdata folder of Telegram Desktop
        """
        return self.__basePath

    @property
    def passcode(self) -> str:
        """
        Passcode used to encrypt and decrypt data\n
        Same as the Local Passcode of Telegram Desktop
        """
        return self.__passcode

    @property
    def keyFile(self) -> str:
        return self.__keyFile

    @property
    def passcodeKey(self) -> td.AuthKey:
        return self.__passcodeKey

    @property
    def localKey(self) -> td.AuthKey:
        """
        The key used to encrypt/decrypt data
        """
        return self.__localKey

    @property
    def AppVersion(self) -> int:
        """
        App version of TDesktop client
        """
        return self.__AppVersion

    @property
    def AppVersionString(self) -> int:
        """
        App version of TDesktop client
        """
        return self.__AppVersion

    @property
    def accountsCount(self) -> int:
        """
        The number of accounts this client has
        """
        # return self.__accountsCount
        return len(self.__accounts)

    @property
    def accounts(self) -> typing.List[td.Account]:
        """
        List of accounts this client has\n
        If you want to get the main account, please use .mainAccount instead
        """
        return self.__accounts

    @property
    def mainAccount(self) -> td.Account:
        """
        The main account of the client
        """
        return self.__mainAccount

    def isLoaded(self) -> bool:
        """
        Return True if the client has loaded tdata
        """
        return self.__isLoaded

    def LoadData(self, basePath : str = None, passcode : str = None, keyFile : str = None) -> bool:
        
        if basePath == None: basePath = self.basePath
        
        Expects(basePath, "No folder provided to load tdata")
        
        if keyFile != None and self.__keyFile != keyFile:
            self.__keyFile = keyFile

        if passcode != None and self.__passcode != passcode:
            self.__passcode = passcode
            self.__passcodeBytes = passcode.encode("ascii")
        
        try:
            self.__loadFromTData()
            
        except OpenTeleException as e:
            if isinstance(e, TDataBadDecryptKey):
                if self.passcode == "":
                    raise TDataBadDecryptKey("The tdata folder is password-encrypted, please the set the argument 'passcode' to decrypt it")
                else:
                    raise TDataBadDecryptKey("Failed to decrypt tdata folder because of invalid passcode")
            else:
                raise e
        
        Expects(self.isLoaded(), "Failed to load? Something went seriously wrong")


    def SaveTData(self, basePath : str = None, passcode : str = None, keyFile : str = None) -> bool:
        """
        Save the login information to a folder
        ### Optional
            1. basePath (str | None, default=None):\n
                Path to the folder\n
                If None then the data will be saved at the basePath given at creation\n
                If None and no basePath was given at creation, it will raises an OpenTeleException
        
        ### Examples
        #### Import an account from telethon session and save it as tdata:
        ```python
            telethon_client = TelegramClient("SessionFile")
            td = TDesktop("NewFolder")
            td.ImportTelethonAccount(telethon_client)
            td.SaveTData()
        ```
        """
        if basePath == None: basePath = self.basePath
        
        self.__keyFile = keyFile if (keyFile != None and self.keyFile != keyFile) else self.keyFile

        Expects(basePath, "No folder provided to save tdata")
    
        if passcode != None and self.__passcode != passcode:
            self.__passcode = passcode
            self.__passcodeBytes = passcode.encode("ascii")
            self.__isLoaded = False # to generate new localKey

        if not self.isLoaded(): self.__generateLocalKey()
        Expects(self.isLoaded(), "Failed to load? Something went seriously wrong")

        try:

            basePath = td.Storage.GetAbsolutePath(basePath)
            if not self.basePath: self.__basePath = basePath

            self.__writeAccounts(basePath, keyFile)
            return True

        except OpenTeleException as e:
            raise TDataSaveFailed("Could not save tdata, something went wrong") from e

    def __writeAccounts(self, basePath : str, keyFile : str = None) -> None:
        """Warning: For internal usage only"""

        Expects(len(self.accounts) > 0)
        Expects(basePath)

        for account in self.accounts:
            account._writeData(basePath, keyFile)

        key = td.Storage.FileWriteDescriptor("key_" + self.keyFile, basePath)
        key.writeData(self.__passcodeKeySalt)        
        key.writeData(self.__passcodeKeyEncrypted)

        keySize = sizeof(int32) + sizeof(int32) * len(self.accounts)
        keyData = td.Storage.EncryptedDescriptor(keySize)
        keyData.stream.writeInt32(len(self.accounts))

        for account in self.accounts:
            keyData.stream.writeInt32(account.index)

        keyData.stream.writeInt32(self.__active_index)
        key.writeEncrypted(keyData, self.__localKey)
        key.finish()

    def __generateLocalKey(self) -> None:
        """Warning: For internal usage only"""

        Expects(not self.isLoaded())

        LocalEncryptSaltSize = 32

        _pass = td.Storage.RandomGenerate(td.AuthKey.kSize)
        _salt = td.Storage.RandomGenerate(LocalEncryptSaltSize)
        self.__localKey = td.Storage.CreateLocalKey(_salt, _pass)

        self.__passcodeKeySalt = td.Storage.RandomGenerate(LocalEncryptSaltSize) # LocalEncryptSaltSize = 32
        self.__passcodeKey = td.Storage.CreateLocalKey(self.__passcodeKeySalt, QByteArray(self.__passcodeBytes))

        passKeyData = td.Storage.EncryptedDescriptor(td.AuthKey.kSize)
        self.__localKey.write(passKeyData.stream)

        self.__passcodeKeyEncrypted = td.Storage.PrepareEncrypted(passKeyData, self.__passcodeKey)

        # set new local key for self.accounts
        for account in self.accounts:
            account.localKey = self.localKey

        self.__isLoaded = True

    def _addSingleAccount(self, account : td.Account):
        """Warning: For internal usage only"""

        # Expects(self.isLoaded(), "Could not add account because i haven't been loaded")
        Expects(account.isLoaded(), "Could not add account because the account hasn't been loaded")
        
        account.localKey = self.localKey
            
        self.__accounts.append(account)
    
        if self.mainAccount == None:
            self.__mainAccount = self.__accounts[0]

    def __loadFromTData(self) -> None:
        """Warning: For internal usage only"""

        Expects(self.basePath)

        self.accounts.clear()

        # READ KEY_DATA
        keyData = td.Storage.ReadFile("key_" + self.keyFile, self.basePath)

        salt, keyEncrypted, infoEncrypted = QByteArray(), QByteArray(), QByteArray()

        keyData.stream >> salt >> keyEncrypted >> infoEncrypted

        Expects(keyData.stream.status() == QDataStream.Status.Ok, 
                QDataStreamFailed("Failed to stream keyData"))

        
        self.__AppVersion = keyData.version
        self.__passcodeKey = td.Storage.CreateLocalKey(salt, QByteArray(self.__passcodeBytes))

        keyInnerData = td.Storage.DecryptLocal(keyEncrypted, self.passcodeKey)

        self.__localKey = td.AuthKey(keyInnerData.stream.readRawData(256))
        self.__passcodeKeyEncrypted = keyEncrypted
        self.__passcodeKeySalt = salt

        info = td.Storage.DecryptLocal(infoEncrypted, self.localKey)
        count = info.stream.readInt32()

        Expects(count > 0, "accountsCount is zero, the data might has been corrupted")

        for i in range(count):
            index = info.stream.readInt32()
            if (index >= 0) and (index < TDesktop.kMaxAccounts):
                try:
                    account = td.Account(self, basePath=self.basePath, api=self.api, keyFile=self.keyFile, index=index)
                    account.prepareToStart(self.__localKey)

                    if account.isLoaded():
                        self.accounts.append(account)
                        
                except OpenTeleException as e:
                    pass
        
        Expects(len(self.accounts) > 0, "No account has been loaded")
        
        self.__active_index = 0
        if (not info.stream.atEnd()):
            self.__active_index = info.stream.readInt32()
        
        for account in self.accounts:
            if (account.index == self.__active_index):
                self.__mainAccount = account
                break

        if not self.__mainAccount:
            self.__mainAccount = self.accounts[0]
        
        self.__isLoaded = True
        






# EXTENDED FUNCTION ====================================================================
# @extend_classs
# class TDesktop:

    @typing.overload
    async def ToTelethon(self,
                    session         : Union[str, Session] = None,
                    flag            : Type[LoginFlag] = CreateNewSession,
                    api             : Union[Type[APIData], APIData] = APITemplate.TelegramDesktop,
                    password        : str = None) -> tl.TelegramClient:
        pass

    @typing.overload
    async def ToTelethon( self,
                    session         : Union[str, Session] = None,
                    flag            : Type[LoginFlag] = CreateNewSession,
                    api             : Union[Type[APIData], APIData] = APITemplate.TelegramDesktop,
                    password                : str = None,
                    *,
                    connection              : typing.Type[Connection] = ConnectionTcpFull,
                    use_ipv6                : bool = False,
                    proxy                   : Union[tuple, dict] = None,
                    local_addr              : Union[str, tuple] = None,
                    timeout                 : int = 10,
                    request_retries         : int = 5,
                    connection_retries      : int = 5,
                    retry_delay             : int = 1,
                    auto_reconnect          : bool = True,
                    sequential_updates      : bool = False,
                    flood_sleep_threshold   : int = 60,
                    raise_last_call_error   : bool = False,
                    loop                    : asyncio.AbstractEventLoop = None,
                    base_logger             : Union[str, logging.Logger] = None,
                    receive_updates         : bool = True) -> tl.TelegramClient:
        pass

    async def ToTelethon( self,
                    session         : Union[str, Session] = None,
                    flag            : Type[LoginFlag] = CreateNewSession,
                    api             : Union[Type[APIData], APIData] = APITemplate.TelegramDesktop,
                    password        : str = None,
                    *,
                    connection              : typing.Type[Connection] = ConnectionTcpFull,
                    use_ipv6                : bool = False,
                    proxy                   : Union[tuple, dict] = None,
                    local_addr              : Union[str, tuple] = None,
                    timeout                 : int = 10,
                    request_retries         : int = 5,
                    connection_retries      : int = 5,
                    retry_delay             : int = 1,
                    auto_reconnect          : bool = True,
                    sequential_updates      : bool = False,
                    flood_sleep_threshold   : int = 60,
                    raise_last_call_error   : bool = False,
                    loop                    : asyncio.AbstractEventLoop = None,
                    base_logger             : Union[str, logging.Logger] = None,
                    receive_updates         : bool = True) -> tl.TelegramClient:

        Expects(self.isLoaded(), TDesktopNotLoaded("You need to load accounts from a tdata folder first"))
        Expects(self.accountsCount > 0, TDesktopHasNoAccount("There is no account in this instance of TDesktop"))
        
        return await tl.TelegramClient.FromTDesktop(self.mainAccount, session=session, flag=flag, api=api, password=password,
                                            connection=connection, use_ipv6=use_ipv6,
                                            proxy=proxy, local_addr=local_addr, timeout=timeout, request_retries=request_retries,
                                            connection_retries=connection_retries, retry_delay=retry_delay, auto_reconnect=auto_reconnect,
                                            sequential_updates=sequential_updates, flood_sleep_threshold=flood_sleep_threshold,
                                            raise_last_call_error=raise_last_call_error, loop=loop, base_logger=base_logger,
                                            receive_updates=receive_updates)

    @staticmethod
    async def FromTelethon(telethonClient : tl.TelegramClient,
                    flag            : Type[LoginFlag] = CreateNewSession,
                    api             : Union[Type[APIData], APIData] = APITemplate.TelegramDesktop,
                    password        : str = None) -> TDesktop:
        """
        Create an instance of `TDesktop` from `telethon.TelegramClient`\n
        
        ### Arguments
            1. telethonClient (telethon.TelegramClient):\n
                The client need to be authorized (logged in) first.
        
        
        ### Remark
            - If you don't set the basePath, you will have to set it when saving tdata

        ### Examples
        #### Saving a telethon client to tdata:
        ```python
            telethonClient = TelegramClient("sessionFile", API_ID, API_HASH)
            account = Account.FromTelethon(telethonClient, basePath="new_tdata")
            account.saveTData()
        ```
        """
        
        Expects((flag == CreateNewSession) or (flag == UseCurrentSession), LoginFlagInvalid("LoginFlag invalid"))
        
        _self = TDesktop()
        _self.__isLoaded = True
        
        await td.Account.FromTelethon(telethonClient, flag=flag, api=api, password=password, owner=_self)

        return _self
