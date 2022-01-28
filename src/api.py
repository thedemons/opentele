from __future__ import annotations
import os

import platform

from typing import Any, List, Dict, Type, TypeVar, Union, Optional
from .devices import *
from .exception import *
from .utils import *

import typing


_T = TypeVar("_T")
_RT = TypeVar("_RT")


class BaseAPIMetaClass(BaseMetaClass):
    """Super high level tactic metaclass"""

    def __new__(
        cls: Type[_T], clsName: str, bases: Tuple[type], attrs: Dict[str, Any]
    ) -> _T:

        result = super().__new__(cls, clsName, bases, attrs)
        result._clsMakePID()  # type: ignore
        result.__str__ = BaseAPIMetaClass.__str__  # type: ignore

        return result

    @sharemethod
    def __str__(glob) -> str:

        if isinstance(glob, type):
            cls = glob
            result = f"{cls.__name__} {{\n"
        else:
            cls = glob.__class__
            result = f"{cls.__name__}() = {{\n"

        for attr, val in glob.__dict__.items():

            if (
                attr.startswith(f"_{cls.__base__.__name__}__")
                or attr.startswith(f"_{cls.__name__}__")
                or attr.startswith("__")
                and attr.endswith("__")
                or type(val) == classmethod
                or callable(val)
            ):
                continue

            result += f"    {attr}: {val}\n"

        return result + "}"


class APIData(object, metaclass=BaseAPIMetaClass):
    """
    API configuration to connect to `TelegramClient` and `TDesktop`

    ### Attributes:
        api_id (`int`):
            [API_ID](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id)

        api_hash (`str`):
            [API_HASH](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id)

        device_model (`str`):
            Device model name

        system_version (`str`):
            Operating System version

        app_version (`str`):
            Current app version

        lang_code (`str`):
            Language code of the client

        system_lang_code (`str`):
            Language code of operating system

        lang_pack (`str`):
            Language pack

    ### Methods:
        `Generate()`: Generate random device model and system version
    """

    CustomInitConnectionList: List[Union[Type[APIData], APIData]] = []

    api_id: int = None  # type: ignore
    api_hash: str = None  # type: ignore
    device_model: str = None  # type: ignore
    system_version: str = None  # type: ignore
    app_version: str = None  # type: ignore
    lang_code: str = None  # type: ignore
    system_lang_code: str = None  # type: ignore
    lang_pack: str = None  # type: ignore

    @typing.overload
    def __init__(self, api_id: int, api_hash: str) -> None:
        pass

    @typing.overload
    def __init__(
        self,
        api_id: int,
        api_hash: str,
        device_model: str = None,
        system_version: str = None,
        app_version: str = None,
        lang_code: str = None,
        system_lang_code: str = None,
        lang_pack: str = None,
    ) -> None:
        """
        Create your own customized API

        ### Arguments:
            api_id (`int`):
                [API_ID](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id)

            api_hash (`str`):
                [API_HASH](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id)

            device_model (`str`, default=`None`):
                `[Device model name](API.device_model)`

            system_version (`str`, default=`None`):
                `[Operating System version](API.system_version)`

            app_version (`str`, default=`None`):
                `[Current app version](API.app_version)`

            lang_code (`str`, default=`"en"`):
                `[Language code of the client](API.app_version)`

            system_lang_code (`str`, default=`"en"`):
                `[Language code of operating system](API.system_lang_code)`

            lang_pack (`str`, default=`""`):
                `[Language pack](API.lang_pack)`

        ### Warning:
            Use at your own risk!:
                Using the wrong API can lead to your account banned.
                If the session was created using an official API, you must continue using official APIs for that session.
                Otherwise that account is at risk of getting banned.
        """

    def __init__(
        self,
        api_id: int = None,
        api_hash: str = None,
        device_model: str = None,
        system_version: str = None,
        app_version: str = None,
        lang_code: str = None,
        system_lang_code: str = None,
        lang_pack: str = None,
    ) -> None:

        Expects(
            (self.__class__ != APIData) or (api_id != None and api_hash != None),
            NoInstanceMatched("No instace of API matches the arguments"),
        )

        cls = self.get_cls()

        self.api_id = api_id if api_id else cls.api_id
        self.api_hash = api_hash if api_hash else cls.api_hash
        self.device_model = device_model if device_model else cls.device_model
        self.system_version = system_version if system_version else cls.system_version
        self.app_version = app_version if app_version else cls.app_version
        self.system_lang_code = (
            system_lang_code if system_lang_code else cls.system_lang_code
        )
        self.lang_pack = lang_pack if lang_pack else cls.lang_pack
        self.lang_code = lang_code if lang_code else cls.lang_code

        if self.device_model == None:
            system = platform.uname()

            if system.machine in ("x86_64", "AMD64"):
                self.device_model = "PC 64bit"
            elif system.machine in ("i386", "i686", "x86"):
                self.device_model = "PC 32bit"
            else:
                self.device_model = system.machine

        self._makePID()

    @sharemethod
    def copy(glob: Union[Type[_T], _T] = _T) -> _T:  # type: ignore

        cls = glob if isinstance(glob, type) else glob.__class__

        return cls(
            glob.api_id,  # type: ignore
            glob.api_hash,  # type: ignore
            glob.device_model,  # type: ignore
            glob.system_version,  # type: ignore
            glob.app_version,  # type: ignore
            glob.lang_code,  # type: ignore
            glob.system_lang_code,  # type: ignore
            glob.lang_pack,  # type: ignore
        )  # type: ignore

    @sharemethod
    def get_cls(glob: Union[Type[_T], _T]) -> Type[_T]:  # type: ignore
        return glob if isinstance(glob, type) else glob.__class__

    @sharemethod
    def destroy(glob: Union[Type[_T], _T]):  # type: ignore
        if isinstance(glob, type):
            return

        # might cause conflict, disabled for now, it won"t be a problem
        # if (API.findData(self.pid) != None):
        #     API.CustomInitConnectionList.remove(self)

    def __eq__(self, __o: APIData) -> bool:
        if type(__o) != APIData:
            return False
        return self.pid == __o.pid

    def __del__(self):
        self.destroy()

    @classmethod
    def _makePIDEnsure(cls) -> int:
        while True:
            pid = int.from_bytes(os.urandom(8), "little")
            if cls.findData(pid) == None:
                break
        return pid

    @classmethod
    def _clsMakePID(cls: Type[APIData]):
        cls.pid = cls._makePIDEnsure()
        cls.CustomInitConnectionList.append(cls)

    def _makePID(self):
        self.pid = self.get_cls()._makePIDEnsure()
        self.get_cls().CustomInitConnectionList.append(self)

    @classmethod
    def Generate(cls: Type[_T], unique_id: str = None) -> _T:
        """
        Generate random device model and system version

        ### Arguments:
            unique_id (`str`, default=`None`):
                The unique ID to generate - can be anything.\\
                This will be used to ensure that it will generate the same data everytime.\\
                If not set then the data will be randomized each time we runs it.
        
        ### Raises:
            `NotImplementedError`: Not supported for web browser yet

        ### Returns:
            `APIData`: Return a copy of the api with random device data

        ### Examples:
            Create a `TelegramClient` with custom API:
        ```python
            api = API.TelegramIOS.Generate(unique_id="new.session")
            client = TelegramClient(session="new.session" api=api)
            client.start()
        ```
        """
        if cls == API.TelegramAndroid or cls == API.TelegramAndroidX:
            deviceInfo = AndroidDevice.RandomDevice(unique_id)

        elif cls == API.TelegramIOS:
            deviceInfo = iOSDeivce.RandomDevice(unique_id)

        elif cls == API.TelegramMacOS:
            deviceInfo = macOSDevice.RandomDevice(unique_id)

        # elif cls == API.TelegramWeb_K or cls == API.TelegramWeb_Z or cls == API.Webogram:
        else:
            raise NotImplementedError(
                f"{cls.__name__} device not supported for randomize yet"
            )

        return cls(device_model=deviceInfo.model, system_version=deviceInfo.version)

    @classmethod
    def findData(cls: Type[_T], pid: int) -> Optional[_T]:
        for x in cls.CustomInitConnectionList:  # type: ignore
            if x.pid == pid:
                return x
        return None


class API(BaseObject):
    """
    #### Built-in templates for Telegram API
    - **`opentele`** offers the ability to use **`official APIs`**, which are used by `official apps`.
    - According to [Telegram TOS](https://core.telegram.org/api/obtaining_api_id#using-the-api-id): *all accounts that sign up or log in using unofficial Telegram API clients are automatically put under observation to avoid violations of the Terms of Service*.
    - It also uses the **[lang_pack](https://core.telegram.org/method/initConnection)** parameter, of which [telethon can't use](https://github.com/LonamiWebs/Telethon/blob/master/telethon/_client/telegrambaseclient.py#L192) because it's for official apps only.
    - Therefore, **there are no differences** between using `opentele` and `official apps`, the server can't tell you apart.
    - You can use `TelegramClient.PrintSessions()` to check this out.

    ### Attributes:
        TelegramDesktop (`API`):
            Official Telegram for Desktop (Windows, macOS and Linux) [View on GitHub](https://github.com/telegramdesktop/tdesktop)

        TelegramAndroid (`API`):
            Official Telegram for Android [View on GitHub](https://github.com/DrKLO/Telegram)

        TelegramAndroidX (`API`):
            Official TelegramX for Android [View on GitHub](https://github.com/DrKLO/Telegram)

        TelegramIOS (`API`):
            Official Telegram for iOS [View on GitHub](https://github.com/TelegramMessenger/Telegram-iOS)

        TelegramMacOS (`API`):
            Official Telegram-Swift For MacOS [View on GitHub](https://github.com/overtake/TelegramSwift)

        TelegramWeb_Z (`API`):
            Default Official Telegram Web Z For Browsers [View on GitHub](https://github.com/Ajaxy/telegram-tt) | [Visit on Telegram](https://web.telegram.org/z/)

        TelegramWeb_K (`API`):
            Official Telegram Web K For Browsers [View on GitHub](https://github.com/morethanwords/tweb) | [Visit on Telegram](https://web.telegram.org/k/)

        Webogram (`API`):
            Old Telegram For Browsers [View on GitHub](https://github.com/zhukov/webogram) | [Vist on Telegram](https://web.telegram.org/?legacy=1#/im)
    """

    class TelegramDesktop(APIData):
        """
        Official Telegram for Desktop (Windows, macOS and Linux)
        [View on GitHub](https://github.com/telegramdesktop/tdesktop)

        ### Attributes:
            api_id (`int`)           : `2040`
            api_hash (`str`)         : `"b18441a1ff607e10a989891a5462e627"`
            device_model (`str`)     : `"Desktop"`
            system_version (`str`)   : `"Windows 10"`
            app_version (`str`)      : `"3.4.3 x64"`
            lang_code (`str`)        : `"en"`
            system_lang_code (`str`) : `"en-US"`
            lang_pack (`str`)        : `"tdesktop"`

        ### Methods:
            `Generate()`: Generate random device data for `Windows`, `macOS` and `Linux`
        """

        api_id = 2040
        api_hash = "b18441a1ff607e10a989891a5462e627"
        device_model = "Desktop"
        system_version = "Windows 10"
        app_version = "3.4.3 x64"
        lang_code = "en"
        system_lang_code = "en-US"
        lang_pack = "tdesktop"

        @typing.overload
        @classmethod
        def Generate(
            cls: Type[_T], system: str = "windows", unique_id: str = None
        ) -> _T:
            """
            Generate random TelegramDesktop devices
            ### Arguments:
                system (`str`, default=`"random"`):
                    Which OS to generate, either `"windows"`, `"macos"`, or `"linux"`.\\
                    Default is `None` or `"random"` -  which means it will be selected randomly.
            
                unique_id (`str`, default=`None`):
                    The unique ID to generate - can be anything.\\
                    This ID will be used to ensure that it will generate the same data every single time.\\
                    If not set then the data will be randomized each time we runs it.
            
            ### Returns:
                `APIData`: Return a copy of the api with random device data
            
            ### Examples:
                Save a telethon session to tdata:
            ```python
                # unique_id will ensure that this data will always be the same (per unique_id).
                # You can use the session file name, or user_id as a unique_id.
                # If unique_id isn't specify, the device data will be randomized each time we runs it.
                oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id="old.session")
                oldclient = TelegramClient("old.session", api=oldAPI)
                await oldClient.connect()

                # We can safely CreateNewSession with a different API.
                # Be aware that you should not use UseCurrentSession with a different API than the one that first authorized it.
                # You can print(newAPI) to see what it had generated.
                newAPI = API.TelegramDesktop.Generate("macos", "new_tdata")
                tdesk = oldclient.ToTDesktop(oldclient, flag=CreateNewSession, api=newAPI)

                # Save the new session to a folder named "new_tdata"
                tdesk.SaveTData("new_tdata")
            ```
            """

        @typing.overload
        @classmethod
        def Generate(cls: Type[_T], system: str = "macos", unique_id: str = None) -> _T:
            pass

        @typing.overload
        @classmethod
        def Generate(cls: Type[_T], system: str = "linux", unique_id: str = None) -> _T:
            pass

        @typing.overload
        @classmethod
        def Generate(
            cls: Type[_T], system: str = "random", unique_id: str = None
        ) -> _T:
            pass

        @classmethod
        def Generate(cls: Type[_T], system: str = None, unique_id: str = None) -> _T:

            validList = ["windows", "macos", "linux"]
            if system == None or system not in validList:
                system = SystemInfo._hashtovalue(
                    SystemInfo._strtohashid(unique_id), validList
                )

            system = system.lower()

            if system == "windows":
                deviceInfo = WindowsDevice.RandomDevice(unique_id)

            elif system == "macos":
                deviceInfo = macOSDevice.RandomDevice(unique_id)

            else:
                deviceInfo = LinuxDevice.RandomDevice(unique_id)

            return cls(device_model=deviceInfo.model, system_version=deviceInfo.version)

    class TelegramAndroid(APIData):
        """
        Official Telegram for Android
        [View on GitHub](https://github.com/DrKLO/Telegram)

        ### Attributes:
            api_id (`int`)           : `6`
            api_hash (`str`)         : `"eb06d4abfb49dc3eeb1aeb98ae0f581e"`
            device_model (`str`)     : `"Samsung SM-G998B"`
            system_version (`str`)   : `"SDK 31"`
            app_version (`str`)      : `"8.4.1 (2522)"`
            lang_code (`str`)        : `"en"`
            system_lang_code (`str`) : `"en-US"`
            lang_pack (`str`)        : `"android"`
        """

        api_id = 6
        api_hash = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
        device_model = "Samsung SM-G998B"
        system_version = "SDK 31"
        app_version = "8.4.1 (2522)"
        lang_code = "en"
        system_lang_code = "en-US"
        lang_pack = "android"

    class TelegramAndroidX(APIData):
        """
        Official TelegramX for Android
        [View on GitHub](https://github.com/DrKLO/Telegram)

        ### Attributes:
            api_id (`int`)           : `21724`
            api_hash (`str`)         : `"3e0cb5efcd52300aec5994fdfc5bdc16"`
            device_model (`str`)     : `"Samsung SM-G998B"`
            system_version (`str`)   : `"SDK 31"`
            app_version (`str`)      : `"8.4.1 (2522)"`
            lang_code (`str`)        : `"en"`
            system_lang_code (`str`) : `"en-US"`
            lang_pack (`str`)        : `"android"`
        """

        api_id = 21724
        api_hash = "3e0cb5efcd52300aec5994fdfc5bdc16"
        device_model = "Samsung SM-G998B"
        system_version = "SDK 31"
        app_version = "8.4.1 (2522)"
        lang_code = "en"
        system_lang_code = "en-US"
        lang_pack = "android"

    class TelegramIOS(APIData):
        """
        Official Telegram for iOS
        [View on GitHub](https://github.com/TelegramMessenger/Telegram-iOS)

        ### Attributes:
            api_id (`int`)           : `10840`
            api_hash (`str`)         : `"33c45224029d59cb3ad0c16134215aeb"`
            device_model (`str`)     : `"iPhone 13 Pro Max"`
            system_version (`str`)   : `"14.8.1"`
            app_version (`str`)      : `"8.4"`
            lang_code (`str`)        : `"en"`
            system_lang_code (`str`) : `"en-US"`
            lang_pack (`str`)        : `"ios"`
        """

        # api_id           = 8
        # api_hash         = "7245de8e747a0d6fbe11f7cc14fcc0bb"
        api_id = 10840
        api_hash = "33c45224029d59cb3ad0c16134215aeb"
        device_model = "iPhone 13 Pro Max"
        system_version = "14.8.1"
        app_version = "8.4"
        lang_code = "en"
        system_lang_code = "en-US"
        lang_pack = "ios"

    class TelegramMacOS(APIData):
        """
        Official Telegram-Swift For MacOS
        [View on GitHub](https://github.com/overtake/TelegramSwift)

        ### Attributes:
            api_id (`int`)           : `2834`
            api_hash (`str`)         : `"68875f756c9b437a8b916ca3de215815"`
            device_model (`str`)     : `"MacBook Pro"`
            system_version (`str`)   : `"macOS 12.0.1"`
            app_version (`str`)      : `"8.4"`
            lang_code (`str`)        : `"en"`
            system_lang_code (`str`) : `"en-US"`
            lang_pack (`str`)        : `"macos"`
        """

        api_id = 2834
        api_hash = "68875f756c9b437a8b916ca3de215815"
        # api_id = 9                                    |
        # api_hash = "3975f648bb682ee889f35483bc618d1c" | Telegram for macOS uses this api, but it"s unofficial api, why?
        device_model = "MacBook Pro"
        system_version = "macOS 12.0.1"
        app_version = "8.4"
        lang_code = "en"
        system_lang_code = "en-US"
        lang_pack = "macos"

    class TelegramWeb_Z(APIData):
        """
        Default Official Telegram Web Z For Browsers
        [View on GitHub](https://github.com/Ajaxy/telegram-tt) | [Visit on Telegram](https://web.telegram.org/z/)

        ### Attributes:
            api_id (`int`)           : `2496`
            api_hash (`str`)         : `"8da85b0d5bfe62527e5b244c209159c3"`
            device_model (`str`)     : `"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"`
            system_version (`str`)   : `"Windows"`
            app_version (`str`)      : `"1.28.3 Z"`
            lang_code (`str`)        : `"en"`
            system_lang_code (`str`) : `"en-US"`
            lang_pack (`str`)        : `""`
        """

        api_id = 2496
        api_hash = "8da85b0d5bfe62527e5b244c209159c3"
        device_model = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
        system_version = "Windows"
        app_version = "1.28.3 Z"
        lang_code = "en"
        system_lang_code = "en-US"
        lang_pack = ""  # I don"t understand why Telegram Z doesn"t use langPack
        # You can read its source here: https://github.com/Ajaxy/telegram-tt/blob/f7bc473d51c0fe3a3e8b22678b62d2360225aa7c/src/lib/gramjs/client/TelegramClient.js#L131

    class TelegramWeb_K(APIData):
        """
        Official Telegram Web K For Browsers
        [View on GitHub](https://github.com/morethanwords/tweb) | [Visit on Telegram](https://web.telegram.org/k/)

        ### Attributes:
            api_id (`int`)           : `2496`
            api_hash (`str`)         : `"8da85b0d5bfe62527e5b244c209159c3"`
            device_model (`str`)     : `"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"`
            system_version (`str`)   : `"Win32"`
            app_version (`str`)      : `"1.0.1 K"`
            lang_code (`str`)        : `"en"`
            system_lang_code (`str`) : `"en-US"`
            lang_pack (`str`)        : `"macos"`
        """

        api_id = 2496
        api_hash = "8da85b0d5bfe62527e5b244c209159c3"
        device_model = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
        system_version = "Win32"
        app_version = "1.0.1 K"
        lang_code = "en"
        system_lang_code = "en-US"
        lang_pack = "macos"  # I"m totally confused, why macos? https://github.dev/morethanwords/tweb/blob/26582590e647766f5890c79e1611c54c1e6e800c/src/config/app.ts#L23

    class Webogram(APIData):
        """
        Old Telegram For Browsers
        [View on GitHub](https://github.com/zhukov/webogram) | [Vist on Telegram](https://web.telegram.org/?legacy=1#/im)

        ### Attributes:
            api_id (`int`)           : `2496`
            api_hash (`str`)         : `"8da85b0d5bfe62527e5b244c209159c3"`
            device_model (`str`)     : `"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"`
            system_version (`str`)   : `"Win32"`
            app_version (`str`)      : `"0.7.0"`
            lang_code (`str`)        : `"en"`
            system_lang_code (`str`) : `"en-US"`
            lang_pack (`str`)        : `""`
        """

        api_id = 2496
        api_hash = "8da85b0d5bfe62527e5b244c209159c3"
        device_model = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
        system_version = "Win32"
        app_version = "0.7.0"
        lang_code = "en"
        system_lang_code = "en-US"
        lang_pack = ""  # The same problem as TelegramWeb_K, as TelegramWeb_K was built on Webogram


class LoginFlag(int):
    """
    Login flag for converting sessions between `TDesktop` and `TelegramClient`.

    ### Attributes:
        UseCurrentSession (LoginFlag): Use the current session.
        CreateNewSession (LoginFlag): Create a new session.

    ### Related:
        - `TDesktop.ToTelethon()`
        - `TDesktop.FromTelethon()`
        - `TelegramClient.ToTDesktop()`
        - `TelegramClient.FromTDesktop()`

    """


class UseCurrentSession(LoginFlag):
    """
    Use the current session.
    - Convert an already-logged in session of `Telegram Desktop` to `Telethon` and vice versa.
    - The "session" is just an 256-bytes `AuthKey` that get stored in `tdata folder` or Telethon `session files` [(under sqlite3 format)](https://docs.telethon.dev/en/latest/concepts/sessions.html?highlight=sqlite3#what-are-sessions).
    - `UseCurrentSession`'s only job is to read this key and convert it to one another.

    ### Warning:
        Use at your own risk!:
            You should only use the same consistant API through out the session.
            Don't use a same session with multiple different APIs, you might be banned.


    """


class CreateNewSession(LoginFlag):
    """
    Create a new session.
    - Use the `current session` to authorize the `new session` by [Login via QR code](https://core.telegram.org/api/qr-login).
    - This works just like when you signing into `Telegram` using `QR Login` on mobile devices.
    - Although `Telegram Desktop` doesn't let you authorize other sessions via `QR Code` *(or it doesn't have that feature)*, it is still available across all platforms `(``[APIs](API)``)`.

    ### Done:
        Safe to use:
            You can always use `CreateNewSessions` with any APIs, it can be different from the API that originally created the session.
    """
