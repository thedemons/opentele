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

        kPerformanceMode (`bool`):
            Performance mode. When enabled, `SavaTData()` will be 200x faster. 
            See `kPerformanceMode`.
    
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

        PerformanceMode():
            Enable/disable performance mode. When enabled, `SavaTData()` will be 5000x faster.

    """

    @typing.overload
    def __init__(self) -> None:
        pass

    @typing.overload
    def __init__(
        self,
        basePath: str = None,
        api: Union[Type[APIData], APIData] = API.TelegramDesktop,
    ) -> None:
        pass

    @typing.overload
    def __init__(
        self,
        basePath: str = None,
        api: Union[Type[APIData], APIData] = API.TelegramDesktop,
        passcode: str = None,
        keyFile: str = None,
    ) -> None:
        pass

    def __init__(
        self,
        basePath: str = None,
        api: Union[Type[APIData], APIData] = API.TelegramDesktop,
        passcode: str = None,
        keyFile: str = None,
    ) -> None:
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
        self.__accounts: typing.List[td.Account] = []
        self.__basePath = basePath
        self.__keyFile = keyFile if (keyFile != None) else TDesktop.kDefaultKeyFile
        self.__passcode = passcode if (passcode != None) else str("")
        self.__passcodeBytes = self.__passcode.encode("ascii")
        self.__mainAccount: Optional[td.Account] = None
        self.__active_index = -1
        self.__passcodeKey = None
        self.__localKey = None
        self.__AppVersion = None
        self.__isLoaded = False
        self.__api = api.copy()

        if basePath != None:
            self.__basePath = td.Storage.GetAbsolutePath(basePath)
            self.LoadTData()

    def isLoaded(self) -> bool:
        """
        Return `True` if the client has successfully loaded accounts from `tdata` or `TelegramClient`
        """
        return self.__isLoaded

    def LoadTData(
        self, basePath: str = None, passcode: str = None, keyFile: str = None
    ):
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

        if basePath == None:
            basePath = self.basePath

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
                    raise TDataBadDecryptKey(
                        "The tdata folder is password-encrypted, please the set the argument 'passcode' to decrypt it"
                    )
                else:
                    raise TDataBadDecryptKey(
                        "Failed to decrypt tdata folder because of invalid passcode"
                    )
            else:
                raise e

        Expects(self.isLoaded(), "Failed to load? Something went seriously wrong")

    def SaveTData(
        self, basePath: str = None, passcode: str = None, keyFile: str = None
    ) -> bool:
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
        if basePath == None:
            basePath = self.basePath

        self.__keyFile = (
            keyFile if (keyFile != None and self.keyFile != keyFile) else self.keyFile
        )

        Expects(basePath != None and basePath != "", "No folder provided to save tdata")

        if passcode != None and self.__passcode != passcode:
            self.__passcode = passcode
            self.__passcodeBytes = passcode.encode("ascii")
            self.__isLoaded = False  # to generate new localKey

        if not self.isLoaded():
            self.__generateLocalKey()
        Expects(self.isLoaded(), "Failed to load? Something went seriously wrong")

        try:

            basePath = td.Storage.GetAbsolutePath(basePath)
            if not self.basePath:
                self.__basePath = basePath

            self.__writeAccounts(basePath, keyFile)
            return True

        except OpenTeleException as e:
            raise TDataSaveFailed("Could not save tdata, something went wrong") from e

    def __writeAccounts(self, basePath: str, keyFile: str = None) -> None:
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
        key.writeEncrypted(keyData, self.__localKey)  # type: ignore
        key.finish()

    def __generateLocalKey(self) -> None:
        # Intended for internal usage only

        Expects(not self.isLoaded())

        if self.kPerformanceMode and len(self.__passcodeBytes) == 0:

            self.__localKey = td.AuthKey(
                b"\xd8\x74\x59\x44\x51\x9e\x0d\x2d\x71\x30\x9d\x6c\x8d\x27\x2d\xc6\x49\x48\xf5\xe3\xeb\xa7\x68\x53\x24\xd5\xc6\x91\xad\x81\x0c\x20"
                b"\x3b\x31\xd1\x9d\x29\xae\xd6\xac\x33\xc0\x14\xbe\x6e\x09\x84\x32\x93\xf6\xfa\x32\xdb\xe4\x2b\x6a\x04\xe0\x04\x81\xfa\xe9\x95\x11"
                b"\x4c\xaf\x63\x42\xbd\x98\xe9\x6d\x29\x3d\xd0\x62\xc4\x58\x68\x9b\x3a\xbd\x23\xa5\xcf\x23\x0c\x75\x52\x7c\x05\xbf\x5f\x90\xf3\x8c"
                b"\xd9\x39\x52\xcf\x61\xaa\xac\x1c\xfe\xaa\xe4\x60\x85\x92\xe3\x63\xde\xd3\x5f\x8d\x8c\x45\x23\x4d\xef\x53\x23\x1d\xec\xb3\x55\x92"
                b"\xaf\xc4\x0d\x06\x01\xbb\xed\x11\x09\x09\x69\xf7\x4d\x9a\xb0\xcc\x97\x82\x75\x46\xf4\x41\x24\x2d\x2c\xfb\x8e\x05\xa0\x61\x0e\x97"
                b"\x66\x9c\x0d\xa1\xad\xcc\xb5\x6e\x39\xe1\x0c\x69\xe2\x94\x23\x87\xff\x49\x22\xf8\xc5\x5d\xcb\x88\x90\xe3\x45\xef\x31\x82\x66\xf4"
                b"\xb3\x83\x14\x30\xea\x21\x0c\x86\x3c\x17\x62\x4c\x04\x94\xcd\xea\xd8\x1f\x52\x34\x30\xb5\xf7\x4c\x15\xda\x32\x3d\x76\x6b\xd0\x1c"
                b"\xb5\xb8\x8b\x9d\x2a\x73\x1f\x6d\x85\x33\x80\xad\x30\x6a\x86\x47\xfa\x61\x4c\xc4\x01\x7f\x08\x90\x2c\x1e\x1f\x99\x7e\xe1\x2e\x3c"
            )
            self.__passcodeKeySalt = QByteArray(
                b"\xae\xd1\xe0\x82\x99\x42\x81\xd9\x75\x76\x0e\x72\x95\x60\xd2\xc8\xd0\x08\xf2\xa9\xdd\x3f\xf4\xd8\x32\x45\xe2\x2e\xed\xb6\x67\x16"
            )
            self.__passcodeKey = td.AuthKey(
                b"\x27\x3e\x64\x83\xb3\x13\xc9\xdb\xc4\xac\xd9\x17\x38\x64\xc0\x42\x2f\x17\x28\x81\xbf\xe1\xc6\x64\x9c\xa5\x53\x86\x54\xd0\xbd\x6e"
                b"\xbc\xfb\xcc\x8d\xab\xbb\x66\x97\x17\xce\x53\xb4\x1c\xa8\xaf\xbf\x9d\x15\xc2\x3f\xa2\xb0\x6a\x6e\x16\x6c\xc6\x1f\x62\xe9\x98\x05"
                b"\x58\xcd\x42\xcf\x10\x22\xe0\x5b\x46\x68\x11\xea\x29\xe9\x35\x9f\xc1\xf9\x46\x68\xe5\xc8\x51\x55\xbc\xe6\x38\xfe\x7a\xa4\x2a\xa8"
                b"\x80\xca\x83\xe0\xd2\xe5\x34\x19\x8a\x0a\x89\x01\x39\xc8\xf6\x79\xa5\x7d\x3b\xa0\x6d\x75\xfe\x5f\xaa\x6e\x25\x01\x01\xa5\x8b\xc6"
                b"\xe4\x2b\x96\x96\x60\x4d\xe1\xe3\x4a\xe4\x0f\x6b\xba\x14\x4a\x28\x4f\x3a\xd8\x84\x32\x53\xec\x9b\x39\x71\x86\x3a\x2c\x40\x92\x08"
                b"\xc2\x56\x39\x67\xb3\x58\x7e\x50\x9b\x42\xa4\x2a\x60\x40\xd2\x3f\xf6\x96\xad\x55\x2a\x24\x00\x84\xfa\x3f\x95\x02\x40\xf4\x99\xb2"
                b"\x3c\xd6\xd2\x7e\x70\x10\xcb\xde\x07\xda\xae\x06\x67\xa7\xdf\x8a\x51\x15\xa6\x0b\x26\x5c\x58\xf5\xd9\x29\x1f\x7a\x98\xfc\x3c\x60"
                b"\x1e\x2a\x4a\x32\xf1\x88\x1b\x82\x18\xc8\x55\x23\x9d\x7b\x53\x29\x59\x60\x9e\x6a\xb5\x2e\x48\xad\x69\x1c\x25\x83\xb5\x66\xc8\xf9"
            )
            self.__passcodeKeyEncrypted = QByteArray(
                b"\x97\xdf\x0c\xd2\xe3\x10\x91\x49\xb7\x7b\x52\x87\x99\x4d\x9c\x1c\xa2\x40\xc5\x1e\x87\x48\x8e\x79"
                b"\xdd\x02\x9b\xea\x65\xfb\x9d\x27\x89\xbb\x5a\xbc\xfe\x65\xe8\x71\xd7\x52\xbd\x93\x8d\x83\x31\x3c"
                b"\x79\x4c\x89\x93\xa7\x34\xce\x12\x16\xf2\xe6\x60\x47\x3f\x31\x43\xaf\x9a\x33\x36\x10\xa1\x79\x95"
                b"\x87\x6e\x17\x21\xce\x1f\x61\x1d\x1c\x69\xd8\xc1\xa2\xf5\x9f\x94\x93\x11\x97\x04\x27\x4e\x2c\xb5"
                b"\xf3\x6c\x20\xdf\x43\x9d\x15\x6d\xef\xf7\xa3\x43\x71\xdc\x44\xbc\x86\xf8\x73\x0c\xeb\xf9\xb0\x28"
                b"\xeb\x7a\x1e\xd6\x62\x1d\x99\xad\xb6\x2b\x3b\x2c\xf2\x29\x5d\xbb\xb2\x4b\xf1\x32\xd3\x7f\xff\xc1"
                b"\x7a\x0b\xdc\xcc\x84\xbb\xea\x6e\xa3\x47\x37\xa2\x36\xb5\x82\x48\xa7\xab\x4c\x14\x36\x3c\x20\x54"
                b"\x1c\xb4\x53\x38\x67\x7f\x33\x97\x82\xb2\x05\xe3\x55\x18\x96\x58\xdd\x45\xea\x3e\x80\x05\xf8\x51"
                b"\x14\x8e\x7e\x15\xf4\x31\x90\x4f\xa7\x9c\x68\x27\xee\x42\x6d\x3a\xb9\xcb\xa9\x36\xeb\x33\xd4\x85"
                b"\xdb\x88\xa6\xf0\xff\x97\x22\xa6\xd6\x2f\xf7\x88\x34\x7e\x27\xc8\x2e\x9e\x13\x9e\xb0\x3a\xe5\x21"
                b"\x53\x9b\xf3\xd3\x63\xb4\xba\xea\x76\xe5\xe8\x84\xcf\x66\xfe\x6b\xcd\x8a\x9e\x08\x9d\x36\x40\x5d"
                b"\xb9\x9d\x01\xdb\x20\x46\x4f\xb6\xca\xbb\xdc\xe4\xf6\x7e\x4e\xc3\x74\x2f\x91\x3a\x1d\xd2\xda\xc5"
            )

        else:
            LocalEncryptSaltSize = 32

            _pass = td.Storage.RandomGenerate(td.AuthKey.kSize)
            _salt = td.Storage.RandomGenerate(LocalEncryptSaltSize)
            self.__localKey = td.Storage.CreateLocalKey(_salt, _pass)

            self.__passcodeKeySalt = td.Storage.RandomGenerate(
                LocalEncryptSaltSize
            )  # LocalEncryptSaltSize = 32
            self.__passcodeKey = td.Storage.CreateLocalKey(
                self.__passcodeKeySalt, QByteArray(self.__passcodeBytes)
            )

            passKeyData = td.Storage.EncryptedDescriptor(td.AuthKey.kSize)
            self.__localKey.write(passKeyData.stream)

            self.__passcodeKeyEncrypted = td.Storage.PrepareEncrypted(
                passKeyData, self.__passcodeKey
            )

            # set new local key for self.accounts
            for account in self.accounts:
                account.localKey = self.localKey

        self.__isLoaded = True

    def _addSingleAccount(self, account: td.Account):
        # Intended for internal usage only

        # Expects(self.isLoaded(), "Could not add account because i haven't been loaded")
        Expects(
            account.isLoaded(),
            "Could not add account because the account hasn't been loaded",
        )

        account.localKey = self.localKey

        self.__accounts.append(account)

        if self.mainAccount == None:
            self.__mainAccount = self.__accounts[0]

    def __loadFromTData(self) -> None:
        # Intended for internal usage only

        Expects(
            self.basePath != None and self.basePath != "",
            "No folder provided to load tdata",
        )

        self.accounts.clear()

        # READ KEY_DATA
        keyData = td.Storage.ReadFile("key_" + self.keyFile, self.basePath)  # type: ignore

        salt, keyEncrypted, infoEncrypted = QByteArray(), QByteArray(), QByteArray()

        keyData.stream >> salt >> keyEncrypted >> infoEncrypted

        Expects(
            keyData.stream.status() == QDataStream.Status.Ok,
            QDataStreamFailed("Failed to stream keyData"),
        )

        self.__AppVersion = keyData.version
        self.__passcodeKey = td.Storage.CreateLocalKey(
            salt, QByteArray(self.__passcodeBytes)
        )

        keyInnerData = td.Storage.DecryptLocal(keyEncrypted, self.passcodeKey)  # type: ignore

        self.__localKey = td.AuthKey(keyInnerData.stream.readRawData(256))
        self.__passcodeKeyEncrypted = keyEncrypted
        self.__passcodeKeySalt = salt

        info = td.Storage.DecryptLocal(infoEncrypted, self.localKey)  # type: ignore
        count = info.stream.readInt32()

        Expects(count > 0, "accountsCount is zero, the data might has been corrupted")

        for i in range(count):
            index = info.stream.readInt32()
            if (index >= 0) and (index < TDesktop.kMaxAccounts):
                try:
                    account = td.Account(
                        self,
                        basePath=self.basePath,
                        api=self.api,
                        keyFile=self.keyFile,
                        index=index,
                    )
                    account.prepareToStart(self.__localKey)

                    if account.isLoaded():
                        self.accounts.append(account)

                except OpenTeleException as e:
                    pass

        Expects(len(self.accounts) > 0, "No account has been loaded")

        self.__active_index = 0
        if not info.stream.atEnd():
            self.__active_index = info.stream.readInt32()

        for account in self.accounts:
            if account.index == self.__active_index:
                self.__mainAccount = account
                break

        if not self.__mainAccount:
            self.__mainAccount = self.accounts[0]

        self.__isLoaded = True

    # EXTENDED FUNCTION ====================================================================
    # @extend_classs
    # class TDesktop:

    @typing.overload
    async def ToTelethon(
        self,
        session: Union[str, Session] = None,
        flag: Type[LoginFlag] = CreateNewSession,
        api: Union[Type[APIData], APIData] = API.TelegramDesktop,
        password: str = None,
    ) -> tl.TelegramClient:
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
    async def ToTelethon(
        self,
        session: Union[str, Session] = None,
        flag: Type[LoginFlag] = CreateNewSession,
        api: Union[Type[APIData], APIData] = API.TelegramDesktop,
        password: str = None,
        *,
        connection: typing.Type[Connection] = ConnectionTcpFull,
        use_ipv6: bool = False,
        proxy: Union[tuple, dict] = None,
        local_addr: Union[str, tuple] = None,
        timeout: int = 10,
        request_retries: int = 5,
        connection_retries: int = 5,
        retry_delay: int = 1,
        auto_reconnect: bool = True,
        sequential_updates: bool = False,
        flood_sleep_threshold: int = 60,
        raise_last_call_error: bool = False,
        loop: asyncio.AbstractEventLoop = None,
        base_logger: Union[str, logging.Logger] = None,
        receive_updates: bool = True
    ) -> tl.TelegramClient:
        pass

    async def ToTelethon(
        self,
        session: Union[str, Session] = None,
        flag: Type[LoginFlag] = CreateNewSession,
        api: Union[Type[APIData], APIData] = API.TelegramDesktop,
        password: str = None,
        **kwargs
    ) -> tl.TelegramClient:

        Expects(
            self.isLoaded(),
            TDesktopNotLoaded("You need to load accounts from a tdata folder first"),
        )
        Expects(
            self.accountsCount > 0,
            TDesktopHasNoAccount("There is no account in this instance of TDesktop"),
        )
        assert self.mainAccount

        return await tl.TelegramClient.FromTDesktop(
            self.mainAccount,
            session=session,
            flag=flag,
            api=api,
            password=password,
            **kwargs
        )

    @staticmethod
    async def FromTelethon(
        telethonClient: tl.TelegramClient,
        flag: Type[LoginFlag] = CreateNewSession,
        api: Union[Type[APIData], APIData] = API.TelegramDesktop,
        password: str = None,
    ) -> TDesktop:
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

        Expects(
            (flag == CreateNewSession) or (flag == UseCurrentSession),
            LoginFlagInvalid("LoginFlag invalid"),
        )

        _self = TDesktop()
        _self.__generateLocalKey()

        await td.Account.FromTelethon(
            telethonClient, flag=flag, api=api, password=password, owner=_self
        )

        return _self

    @classmethod
    def PerformanceMode(cls, enabled: bool = True):
        """
        Enable or disable performance mode. See `kPerformanceMode`.
        It is enabled by default.

        ### Arguments:
            enabled (`bool`, default=`True`):
                Either enable or disable performance mode.

        """
        cls.kPerformanceMode = enabled

    kMaxAccounts: int = int(3)
    """The maximum amount of accounts a client can have"""

    kDefaultKeyFile: str = "data"
    """See `TDesktop.keyFile`"""

    kPerformanceMode: bool = True
    """
    When enabled, `SaveTData()` will be 5000x faster.
    - What it does is using a constant `localKey` rather than generating it everytime when saving tdata.
    - The average time for generating `localKey` is about `250` to `350` ms, depend on your CPU.
    - When in performance mode, the average time to generate `localKey` is `0.0628` ms. Which is 5000x faster
    - Of course this comes with a catch, your `tdata files` will always use a same constant `localKey`. Basicly no protection at all, but who cares?
    
    ### Notes:
        Note: Performance mode will be disabled if `passcode` is set.
    """

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
