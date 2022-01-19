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
    """
    Telegram Desktop client.
    
    A client can have multiple accounts, up to 3 - according to official Telegram Desktop client.

    ### Attributes:
        api (`API`):
            The API this client is using.
        
        accountsCount (`int`):
            The numbers of accounts in this client.

        accounts (`List[Account]`):
            List of accounts in this client.

        mainAccount (`Account`):
            The main account of this client.
        
        basePath (`str`):
            The path to `tdata folder`.

        passcode (`str`):
            Passcode of the client, the same as Local Passcode on `Telegram Desktop`.\\
            Use to encrypt and decrypt `tdata files`.

        AppVersion (`int`):
            App version of the client.
        
        kMaxAccounts (`int`):
            See `kMaxAccounts`.

        keyFile (`str`):
            See `keyFile`.
        
        kDefaultKeyFile (`str`):
            Default value for `keyFile`.
    
    ### Methods:
        LoadTData():
            Load the client from `tdata folder`. \\
            Use this if you didn't set the `basePath` when initializing the client.

        SaveTData():
            Save the client session to `tdata folder` - which can be used by `Telegram Desktop`.

        isLoaded():
            Return `True` if the client has successfully loaded accounts from `tdata` or `TelegramClient`.

        ToTelethon():
            Convert this session to `TelegramClient`.

        FromTelethon():
            Create a new session from `TelegramClient`.

    """
    
    @typing.overload
    def __init__(self) -> None:
        pass

    @typing.overload
    def __init__(self,  basePath : str = None,
                        api : Union[Type[APIData], APIData] = API.TelegramDesktop) -> None:
        pass
                        
    @typing.overload
    def __init__(self,  basePath : str = None,
                        api : Union[Type[APIData], APIData] = API.TelegramDesktop,
                        passcode : str = None,
                        keyFile : str = None) -> None:
        pass

    def __init__(self,  basePath : str = None,
                        api : Union[Type[APIData], APIData] = API.TelegramDesktop,
                        passcode : str = None,
                        keyFile : str = None) -> None:
        """
        Initialize a `TDesktop` client

        ### Arguments:
            basePath (`str`, default=`None`):
                The path to the `tdata folder`.
                If the path doesn't exists or its data is corrupted, a new instance will be created.
            
            api (`API`, default=`TelegramDesktop`):
                Which API to use. Read more `[here](API)`.

            passcode (str, default=`None`):
                The passcode for tdata, same as the Local Passcode on `Telegram Desktop`.
        
            keyFile (str, default="data"):
                See `keyFile`.
        """
        self.__accounts : typing.List[td.Account] = []
        self.__basePath = basePath
        self.__keyFile = keyFile if (keyFile != None) else TDesktop.kDefaultKeyFile
        self.__passcode = passcode if (passcode != None) else str("")
        self.__passcodeBytes = self.__passcode.encode("ascii")
        self.__mainAccount : Optional[td.Account] = None
        self.__active_index = -1
        self.__passcodeKey = None
        self.__localKey = None
        self.__AppVersion = None
        self.__isLoaded = False
        self.__api  = api.copy()

        if basePath != None:
            self.__basePath = td.Storage.GetAbsolutePath(basePath)
            self.LoadTData()
 

    def isLoaded(self) -> bool:
        """
        Return `True` if the client has successfully loaded accounts from `tdata` or `TelegramClient`
        """
        return self.__isLoaded

    def LoadTData(self, basePath : str = None, passcode : str = None, keyFile : str = None):
        """
        Loads accounts from `tdata folder`

        ### Arguments:
            basePath (`str`, default=`None`):
                The path to the folder.
        
            passcode (`str`, default=`None`):
                Read more `[here](passcode)`.
        
            keyFile (`str`, default=`None`):
                Read more `[here](keyFile)`.
        
        ### Raises:
            `TDataBadDecryptKey`: The `tdata folder` is password-encrypted, please the set the argument `passcode` to decrypt it.

        ### Warning:
            This function is not recommended to use:
                You should load tdata using `TDesktop(basePath="path")`.
                Don't manually load tdata using this function, bugs might pop up out of nowhere.

        ### Examples:
        ```python
            # Using the API that we've generated before. Please refer to method API.Generate() to learn more.
            oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id="old.session")
            oldclient = TelegramClient("old.session", api=oldAPI)
            await oldClient.connect()

            # We can safely use CreateNewSession with a different API.
            # Be aware that you should not use UseCurrentSession with a different API than the one that first authorized it.
            newAPI = API.TelegramAndroid.Generate("new_tdata")
            tdesk = await TDesktop.FromTelethon(oldclient, flag=CreateNewSession, api=newAPI)

            # Save the new session to a folder named "new_tdata"
            tdesk.SaveTData("new_tdata")
        ```
        """
        
        if basePath == None: basePath = self.basePath
        
        Expects(basePath != None and basePath != "", "No folder provided to load tdata")
        
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
        Save the client session to a folder.

        ### Arguments:
            basePath (`str`, default=None):
                Path to the folder\\
                If None then the data will be saved at the basePath given at creation.

            passcode (`str`, default=`None`):
                Read more `[here](passcode)`.
        
            keyFile (`str`, default=`None`):
                Read more `[here](keyFile)`.

        ### Examples:
            Save a telethon session to tdata:
        ```python
            # Using the API that we've generated before. Please refer to method API.Generate() to learn more.
            oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id="old.session")
            oldclient = TelegramClient("old.session", api=oldAPI)
            await oldClient.connect()

            # We can safely CreateNewSession with a different API.
            # Be aware that you should not use UseCurrentSession with a different API than the one that first authorized it.
            newAPI = API.TelegramAndroid.Generate("new_tdata")
            tdesk = await TDesktop.FromTelethon(oldclient, flag=CreateNewSession, api=newAPI)

            # Save the new session to a folder named "new_tdata"
            tdesk.SaveTData("new_tdata")
        ```
        """
        if basePath == None: basePath = self.basePath
        
        self.__keyFile = keyFile if (keyFile != None and self.keyFile != keyFile) else self.keyFile

        Expects(basePath != None and basePath != "", "No folder provided to save tdata")
    
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
        # Intended for internal usage only

        Expects(len(self.accounts) > 0)
        Expects(basePath != None and basePath != "", "No folder provided to save tdata")

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
        key.writeEncrypted(keyData, self.__localKey) # type: ignore
        key.finish()

    def __generateLocalKey(self) -> None:
        # Intended for internal usage only

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
        # Intended for internal usage only

        # Expects(self.isLoaded(), "Could not add account because i haven't been loaded")
        Expects(account.isLoaded(), "Could not add account because the account hasn't been loaded")
        
        account.localKey = self.localKey
            
        self.__accounts.append(account)
    
        if self.mainAccount == None:
            self.__mainAccount = self.__accounts[0]

    def __loadFromTData(self) -> None:
        # Intended for internal usage only

        Expects(self.basePath != None and self.basePath != "", "No folder provided to load tdata")

        self.accounts.clear()

        # READ KEY_DATA
        keyData = td.Storage.ReadFile("key_" + self.keyFile, self.basePath) # type: ignore

        salt, keyEncrypted, infoEncrypted = QByteArray(), QByteArray(), QByteArray()

        keyData.stream >> salt >> keyEncrypted >> infoEncrypted

        Expects(keyData.stream.status() == QDataStream.Status.Ok, 
                QDataStreamFailed("Failed to stream keyData"))

        
        self.__AppVersion = keyData.version
        self.__passcodeKey = td.Storage.CreateLocalKey(salt, QByteArray(self.__passcodeBytes))

        keyInnerData = td.Storage.DecryptLocal(keyEncrypted, self.passcodeKey) # type: ignore

        self.__localKey = td.AuthKey(keyInnerData.stream.readRawData(256))
        self.__passcodeKeyEncrypted = keyEncrypted
        self.__passcodeKeySalt = salt

        info = td.Storage.DecryptLocal(infoEncrypted, self.localKey) # type: ignore
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
                    api             : Union[Type[APIData], APIData] = API.TelegramDesktop,
                    password        : str = None) -> tl.TelegramClient:
        """
        
        ### Arguments:
            session (`str`, `Session`, default=`None`):
                The file name of the `session file` to be used, if `None` then the session will not be saved.\\
                Read more [here](https://docs.telethon.dev/en/latest/concepts/sessions.html?highlight=session#what-are-sessions).
        
            flag (`LoginFlag`, default=`CreateNewSession`):
                The login flag. Read more `[here](LoginFlag)`.
        
            api (`APIData`, default=`TelegramDesktop`):
                Which API to use. Read more `[here](API)`.
        
            password (`str`, default=`None`):
                Two-step verification password if needed.
        
        ### Returns:
            - Return an instance of `TelegramClient` on success

        ### Examples:
            Create a telethon session from tdata folder:
        ```python
            # Using the API that we've generated before. Please refer to method API.Generate() to learn more.
            oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id="old_tdata")
            tdesk = TDesktop("old_tdata", api=oldAPI)

            # We can safely authorize the new client with a different API.
            newAPI = API.TelegramAndroid.Generate(unique_id="new.session")
            client = await tdesk.ToTelethon(session="new.session", flag=CreateNewSession, api=newAPI)
            await client.connect()
            await client.PrintSessions()
        ```
        """

    @typing.overload
    async def ToTelethon( self,
                    session         : Union[str, Session] = None,
                    flag            : Type[LoginFlag] = CreateNewSession,
                    api             : Union[Type[APIData], APIData] = API.TelegramDesktop,
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
                    api             : Union[Type[APIData], APIData] = API.TelegramDesktop,
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
        assert self.mainAccount
        
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
                    api             : Union[Type[APIData], APIData] = API.TelegramDesktop,
                    password        : str = None) -> TDesktop:
        """
        Create an instance of `TDesktop` from `TelegramClient`.

        ### Arguments:
            telethonClient (`TelegramClient`):
                The `TelegramClient` you want to convert from.
        
            flag (`LoginFlag`, default=`CreateNewSession`):
                The login flag. Read more `[here](LoginFlag)`.
        
            api (`APIData`, default=`API.TelegramDesktop`):
                Which API to use. Read more `[here](API)`.
        
            password (`str`, default=`None`):
                Two-step verification password if needed.

        ### Examples:
            Save a telethon session to tdata:
        ```python
            # Using the API that we've generated before. Please refer to method API.Generate() to learn more.
            oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id="old.session")
            oldclient = TelegramClient("old.session", api=oldAPI)
            await oldClient.connect()

            # We can safely CreateNewSession with a different API.
            # Be aware that you should not use UseCurrentSession with a different API than the one that first authorized it.
            newAPI = API.TelegramAndroid.Generate("new_tdata")
            tdesk = await TDesktop.FromTelethon(oldclient, flag=CreateNewSession, api=newAPI)

            # Save the new session to a folder named "new_tdata"
            tdesk.SaveTData("new_tdata")
        ```
        """
        
        Expects((flag == CreateNewSession) or (flag == UseCurrentSession), LoginFlagInvalid("LoginFlag invalid"))
        
        _self = TDesktop()
        _self.__isLoaded = True
        
        await td.Account.FromTelethon(telethonClient, flag=flag, api=api, password=password, owner=_self)

        return _self
         
    kMaxAccounts : int = int(3)
    """The maximum amount of accounts a client can have"""

    kDefaultKeyFile = "data"
    """See `TDesktop.keyFile`"""

    @property
    def api(self) -> APIData:
        """
        The API this client is using.
        """
        return self.__api

    @api.setter
    def api(self, value) -> None:
        self.__api = value
        for account in self.accounts:
            account.api = value
    
    @property
    def basePath(self) -> Optional[str]:
        """
        Base folder of `TDesktop`, this is where data stored
        Same as tdata folder of `Telegram Desktop`
        """
        return self.__basePath

    @property
    def passcode(self) -> str:
        """
        Passcode
        Passcode used to encrypt and decrypt data
        Same as the Local Passcode of `Telegram Desktop`
        """
        return self.__passcode

    @property
    def keyFile(self) -> str:
        """
        The default value is `"data"`, this argument is rarely ever used.
        It is used by `Telegram Desktop` by running it with the `"-key"` argument.
        I don't know what's the use cases of it, maybe this was a legacy feature of `Telegram Desktop`.
        """
        return self.__keyFile

    @property
    def passcodeKey(self) -> Optional[td.AuthKey]:
        return self.__passcodeKey

    @property
    def localKey(self) -> Optional[td.AuthKey]:
        """
        The key used to encrypt/decrypt data
        """
        return self.__localKey

    @property
    def AppVersion(self) -> Optional[int]:
        """
        App version of TDesktop client
        """
        return self.__AppVersion

    @property
    def AppVersionString(self) -> Optional[str]:
        raise NotImplementedError()
        return self.__AppVersion

    @property
    def accountsCount(self) -> int:
        """
        The number of accounts this client has
        """
        # return self.__accountsCount
        return len(self.__accounts)

    @property
    def accounts(self) -> List[td.Account]:
        """
        List of accounts this client has\n
        If you want to get the main account, please use .mainAccount instead
        """
        return self.__accounts

    @property
    def mainAccount(self) -> Optional[td.Account]:
        """
        The main account of the client
        """
        return self.__mainAccount