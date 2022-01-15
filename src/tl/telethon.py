

from __future__ import annotations

from .configs import *
from . import shared as tl

from telethon.errors.rpcerrorlist import PasswordHashInvalidError, AuthTokenAlreadyAcceptedError, AuthTokenExpiredError, AuthTokenInvalidError, FreshResetAuthorisationForbiddenError, HashInvalidError
from telethon.tl.types import TypeInputClientProxy, TypeJSONValue

import logging
import warnings

@extend_override_class
class CustomInitConnectionRequest(functions.InitConnectionRequest):
    def __init__(self, api_id: int, device_model: str, system_version: str, app_version: str, system_lang_code: str, lang_pack: str, lang_code: str, query, proxy: TypeInputClientProxy = None, params: TypeJSONValue =None):
        
        # our hook pass pid as device_model
        data = APIData.findData(device_model) # type: ignore
        if data != None:
            self.api_id = data.api_id
            self.device_model = data.device_model           if data.device_model     else device_model
            self.system_version = data.system_version       if data.system_version   else system_version
            self.app_version = data.app_version             if data.app_version      else app_version
            self.system_lang_code = data.system_lang_code   if data.system_lang_code else system_lang_code
            self.lang_pack = data.lang_pack                 if data.lang_pack        else lang_pack
            self.lang_code = data.lang_code                 if data.lang_code        else lang_code
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



@extend_class
class TelegramClient(telethon.TelegramClient, BaseObject):
# class TelegramClient(telethon.TelegramClient, BaseObject):

    @typing.overload
    def __init__(self : TelegramClient, session : Union[str, Session] = None, api : Union[Type[APIData], APIData] = APITemplate.TelegramDesktop):
        """
        Start TelegramClient with customized api
        Read more at [OpenTele GitHub](https://github.com/thedemons/opentele#authorization)
        
        ### Arguments
            1. session (`Union[str, Session]`):\n
                 The file name of the session file to be used if a string is
                given (it may be a full path), or the Session instance to be
                used otherwise. If it's `None`, the session will not be saved,
                and you should call :meth:`.log_out()` when you're done.

                Note that if you pass a string it will be a file in the current
                working directory, although you can also pass absolute paths.

                The session file contains enough information for you to login
                without re-sending the code, so if you have to enter the code
                more than once, maybe you're changing the working directory,
                renaming or removing the file, or using random names.
        
            2. api (APIData):\n
                Using API of Telegram Desktop by default
        
        ### Optional
        ### Examples
        #### Start TelegramClient from an instance of TDesktop:
        ```python
            from opentele.tl import TelegramClient
            from opentele.td import APITemplate
            
            client = TelegramClient("data.session", api=APITemplate.TelegramDesktop)
        ```
        """
        pass

    @typing.overload
    def __init__(
            self,
            session     : Union[str, Session] = None,
            api         : Union[Type[APIData], APIData] = None,
            api_id      : int = 0,
            api_hash    : str = None,
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
            device_model            : str = None,
            system_version          : str = None,
            app_version             : str = None,
            lang_code               : str = 'en',
            system_lang_code        : str = 'en',
            loop                    : asyncio.AbstractEventLoop = None,
            base_logger             : Union[str, logging.Logger] = None,
            receive_updates         : bool = True):

        """
        This is the abstract base class for the client. It defines some
        basic stuff like connecting, switching data center, etc, and
        leaves the `__call__` unimplemented.

        Arguments
            session (`str` | `telethon.sessions.abstract.Session`, `None`):
                The file name of the session file to be used if a string is
                given (it may be a full path), or the Session instance to be
                used otherwise. If it's `None`, the session will not be saved,
                and you should call :meth:`.log_out()` when you're done.

                Note that if you pass a string it will be a file in the current
                working directory, although you can also pass absolute paths.

                The session file contains enough information for you to login
                without re-sending the code, so if you have to enter the code
                more than once, maybe you're changing the working directory,
                renaming or removing the file, or using random names.

            api (`APIData`, optional):
                Use custom api_id and api_hash for better experience.\n
                These arguments will be ignored if it is set in the APIData: `api_id`, `api_hash`, `device_model`, `system_version`, `app_version`, `lang_code`, `system_lang_code`
                Read more at [OpenTele GitHub](https://github.com/thedemons/opentele#authorization)

            api_id (`int` | `str`, optional):
                The API ID you obtained from https://my.telegram.org.

            api_hash (`str`, optional):
                The API hash you obtained from https://my.telegram.org.

            connection (`telethon.network.connection.common.Connection`, optional):
                The connection instance to be used when creating a new connection
                to the servers. It **must** be a type.

                Defaults to `telethon.network.connection.tcpfull.ConnectionTcpFull`.

            use_ipv6 (`bool`, optional):
                Whether to connect to the servers through IPv6 or not.
                By default this is `False` as IPv6 support is not
                too widespread yet.

            proxy (`tuple` | `list` | `dict`, optional):
                An iterable consisting of the proxy info. If `connection` is
                one of `MTProxy`, then it should contain MTProxy credentials:
                ``('hostname', port, 'secret')``. Otherwise, it's meant to store
                function parameters for PySocks, like ``(type, 'hostname', port)``.
                See https://github.com/Anorov/PySocks#usage-1 for more.

            local_addr (`str` | `tuple`, optional):
                Local host address (and port, optionally) used to bind the socket to locally.
                You only need to use this if you have multiple network cards and
                want to use a specific one.

            timeout (`int` | `float`, optional):
                The timeout in seconds to be used when connecting.
                This is **not** the timeout to be used when ``await``'ing for
                invoked requests, and you should use ``asyncio.wait`` or
                ``asyncio.wait_for`` for that.

            request_retries (`int` | `None`, optional):
                How many times a request should be retried. Request are retried
                when Telegram is having internal issues (due to either
                ``errors.ServerError`` or ``errors.RpcCallFailError``),
                when there is a ``errors.FloodWaitError`` less than
                `flood_sleep_threshold`, or when there's a migrate error.

                May take a negative or `None` value for infinite retries, but
                this is not recommended, since some requests can always trigger
                a call fail (such as searching for messages).

            connection_retries (`int` | `None`, optional):
                How many times the reconnection should retry, either on the
                initial connection or when Telegram disconnects us. May be
                set to a negative or `None` value for infinite retries, but
                this is not recommended, since the program can get stuck in an
                infinite loop.

            retry_delay (`int` | `float`, optional):
                The delay in seconds to sleep between automatic reconnections.

            auto_reconnect (`bool`, optional):
                Whether reconnection should be retried `connection_retries`
                times automatically if Telegram disconnects us or not.

            sequential_updates (`bool`, optional):
                By default every incoming update will create a new task, so
                you can handle several updates in parallel. Some scripts need
                the order in which updates are processed to be sequential, and
                this setting allows them to do so.

                If set to `True`, incoming updates will be put in a queue
                and processed sequentially. This means your event handlers
                should *not* perform long-running operations since new
                updates are put inside of an unbounded queue.

            flood_sleep_threshold (`int` | `float`, optional):
                The threshold below which the library should automatically
                sleep on flood wait and slow mode wait errors (inclusive). For instance, if a
                ``FloodWaitError`` for 17s occurs and `flood_sleep_threshold`
                is 20s, the library will ``sleep`` automatically. If the error
                was for 21s, it would ``raise FloodWaitError`` instead. Values
                larger than a day (like ``float('inf')``) will be changed to a day.

            raise_last_call_error (`bool`, optional):
                When API calls fail in a way that causes Telethon to retry
                automatically, should the RPC error of the last attempt be raised
                instead of a generic ValueError. This is mostly useful for
                detecting when Telegram has internal issues.

            device_model (`str`, optional):
                "Device model" to be sent when creating the initial connection.
                Defaults to 'PC (n)bit' derived from ``platform.uname().machine``, or its direct value if unknown.

            system_version (`str`, optional):
                "System version" to be sent when creating the initial connection.
                Defaults to ``platform.uname().release`` stripped of everything ahead of -.

            app_version (`str`, optional):
                "App version" to be sent when creating the initial connection.
                Defaults to `telethon.version.__version__`.

            lang_code (`str`, optional):
                "Language code" to be sent when creating the initial connection.
                Defaults to ``'en'``.

            system_lang_code (`str`, optional):
                "System lang code"  to be sent when creating the initial connection.
                Defaults to `lang_code`.

            loop (`asyncio.AbstractEventLoop`, optional):
                Asyncio event loop to use. Defaults to `asyncio.get_event_loop()`.
                This argument is ignored.

            base_logger (`str` | `logging.Logger`, optional):
                Base logger name or instance to use.
                If a `str` is given, it'll be passed to `logging.getLogger()`. If a
                `logging.Logger` is given, it'll be used directly. If something
                else or nothing is given, the default logger will be used.

            receive_updates (`bool`, optional):
                Whether the client will receive updates or not. By default, updates
                will be received from Telegram as they occur.

                Turning this off means that Telegram will not send updates at all
                so event handlers, conversations, and QR login will not work.
                However, certain scripts don't need updates, so this will reduce
                the amount of bandwidth used.
                
        """
        pass

    @override
    def __init__(
            self,
            session     : Union[str, Session] = None,
            api         : Union[Type[APIData], APIData] = None,
            api_id      : int = 0,
            api_hash    : str = None,
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
            device_model            : str = None,
            system_version          : str = None,
            app_version             : str = None,
            lang_code               : str = 'en',
            system_lang_code        : str = 'en',
            loop                    : asyncio.AbstractEventLoop = None,
            base_logger             : Union[str, logging.Logger] = None,
            receive_updates         : bool = True):

        if api != None:
            if isinstance(api, APIData) or APIData.__subclasscheck__(api):
                api_id = api.api_id
                api_hash = api.api_hash
                device_model = api.pid  # type: ignore # pass our hook id through the device_model

            else:
                if isinstance(api, int) or isinstance(api, str):
                    if api_id and isinstance(api_id, str):
                        api_id = api
                        api_hash = api_id
                api = None
        
        self.__TelegramClient____init__(session, api_id, api_hash, connection=connection, # type: ignore
        use_ipv6=use_ipv6, proxy=proxy, local_addr=local_addr, timeout=timeout,
        request_retries=request_retries, connection_retries=connection_retries,
        retry_delay=retry_delay, auto_reconnect=auto_reconnect, sequential_updates=sequential_updates,
        flood_sleep_threshold=flood_sleep_threshold, raise_last_call_error=raise_last_call_error,
        device_model=device_model, system_version=system_version, app_version=app_version,
        lang_code=lang_code, system_lang_code=system_lang_code, loop=loop, base_logger=base_logger,
        receive_updates=receive_updates)

    async def TerminateSession(self, hash : int):

        try:
            await self(functions.account.ResetAuthorizationRequest(hash))
            import rich
            rich.print(f"Terminated: {hash}")

        except (FreshResetAuthorisationForbiddenError, HashInvalidError) as e:

            if isinstance(e, FreshResetAuthorisationForbiddenError):
                raise FreshResetAuthorisationForbiddenError("You can't logout other sessions if less than 24 hours have passed since you logged on the current session.")

            elif isinstance(e, HashInvalidError):
                raise HashInvalidError("The provided hash is invalid.")
            
            raise BaseException(e) 

    async def TerminateAllSession(self) -> bool:
        sessions = await self.GetSessions()
        if sessions == None: return False

        for ss in sessions.authorizations:
            if not ss.current:
                await self.TerminateSession(ss.hash)

        return True
        
            
    async def GetSessions(self) -> Optional[types.account.Authorizations]:
        return await self(functions.account.GetAuthorizationsRequest())  # type: ignore

    async def GetCurrentSession(self) -> Optional[types.Authorization]:
        results = await self.GetSessions()
        if results == None: return None

        if results.authorizations[0].current:
            return results.authorizations[0]
        
        for auth in results.authorizations:
            if auth.current:
                return auth
        
        return None

    async def PrintSessions(self, sessions : types.account.Authorizations = None):
        if (sessions == None) or not isinstance(sessions, types.account.Authorizations):
            sessions = await self.GetSessions()
        
        assert sessions

        table = []

        index = 0
        for session in sessions.authorizations:
            table.append({
                " " : "Current" if session.current else index,
                "Device" : session.device_model,
                "Platform" : session.platform,
                "System" : session.system_version,
                "API_ID" : session.api_id,
                "App name" : f"{session.app_name} {session.app_version}",
                "Official App" : "✔" if session.official_app else "✖"
            })
            index += 1
        
        print(PrettyTable(table, [1]))

    async def is_official_app(self) -> bool:
        auth = await self.GetCurrentSession()
        
        return False if auth == None else bool(auth.official_app)


    async def ToTDesktop(self        : TelegramClient,
                         flag        : Type[LoginFlag] = CreateNewSession,
                         api         : Union[Type[APIData], APIData] = APITemplate.TelegramDesktop,
                         password    : str = None) -> td.TDesktop:

        return await td.TDesktop.FromTelethon(self, flag=flag, api=api, password=password)
    
    async def _QRLoginToNewClient(self,
                                session                 : Union[str, Session] = None,
                                api                     : Union[Type[APIData], APIData] = APITemplate.TelegramDesktop,
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
                                receive_updates         : bool = True) -> TelegramClient:

        newClient = TelegramClient(session, api=api, connection=connection, use_ipv6=use_ipv6,
                                proxy=proxy, local_addr=local_addr, timeout=timeout, request_retries=request_retries,
                                connection_retries=connection_retries, retry_delay=retry_delay, auto_reconnect=auto_reconnect,
                                sequential_updates=sequential_updates, flood_sleep_threshold=flood_sleep_threshold,
                                raise_last_call_error=raise_last_call_error, loop=loop, base_logger=base_logger,
                                receive_updates=receive_updates)

        try:
            await newClient.connect()
        except OSError as e:
            raise BaseException("Cannot connect")
        
        if await newClient.is_user_authorized():
            
            currentAuth = await newClient.GetCurrentSession()
            if (currentAuth != None):

                if (currentAuth.api_id == api.api_id):
                    warnings.warn(
                        '\nCreateNewSession - a session file with the same name '
                        'is already existed, returning the old session'
                    )
                else:
                    warnings.warn(
                        '\nCreateNewSession - a session file with the same name '
                        'is already existed, but its api_id is different from '
                        'the current one, it will be overwritten'
                    )

                    disconnect = newClient.disconnect()
                    if disconnect:
                        await disconnect
                        await newClient.disconnected

                    newClient.session.close()
                    newClient.session.delete()

                    newClient = await self._QRLoginToNewClient(
                        session=session, api=api, password=password,
                        connection=connection, use_ipv6=use_ipv6,
                        proxy=proxy, local_addr=local_addr, timeout=timeout, request_retries=request_retries,
                        connection_retries=connection_retries, retry_delay=retry_delay, auto_reconnect=auto_reconnect,
                        sequential_updates=sequential_updates, flood_sleep_threshold=flood_sleep_threshold,
                        raise_last_call_error=raise_last_call_error, loop=loop, base_logger=base_logger,
                        receive_updates=receive_updates
                    )

                return newClient

        if not self._self_id:
            oldMe = await self.get_me()

        qr_login = await newClient.qr_login()

        try:
            resp = await self(functions.auth.AcceptLoginTokenRequest(qr_login.token))

        except (AuthTokenAlreadyAcceptedError, AuthTokenExpiredError, AuthTokenInvalidError) as e:
            # ! TO BE ADDED
            # ERROR HANDLER
            raise BaseException(e)
            

        try:
            await qr_login.wait()

        except (telethon.errors.SessionPasswordNeededError, TimeoutError) as e:
            
            if isinstance(e, TimeoutError):
                raise TimeoutError("Something went wrong, i couldn't perform QR login process")

            Expects(password != None,
            exception=NoPasswordProvided("Two-step verification is enabled for this account.\n"\
                                        "You need to provide the `password` to argument"))
            
            # two-step verification
            try:
                pwd : types.account.Password = await newClient(functions.account.GetPasswordRequest()) # type: ignore
                result = await newClient(
                    functions.auth.CheckPasswordRequest(
                        pwd_mod.compute_check(pwd, password) # type: ignore
                    )
                )
                    
                newClient._on_login(result.user) # type: ignore
                

            except PasswordHashInvalidError as e:
                raise Passwordincorrect(e.__str__()) from e

        return newClient

    @typing.overload
    @staticmethod
    async def FromTDesktop( account        : Union[td.TDesktop, td.Account],
                            session         : Union[str, Session] = None,
                            flag            : Type[LoginFlag] = CreateNewSession,
                            api             : Union[Type[APIData], APIData] = APITemplate.TelegramDesktop,
                            password        : str = None) -> TelegramClient:
        """
        FromTDesktop [summary]

        [extended_summary]

        Args:
            account (Union[td.TDesktop, td.Account]): [description]
            session (Union[str, Session], optional): [description]. Defaults to None.
            flag (Type[LoginFlag], optional): [description]. Defaults to CreateNewSession.
            api (Union[Type[APIData], APIData], optional): [description]. Defaults to APITemplate.TelegramDesktop.
            password (str, optional): [description]. Defaults to None.

        Returns:
        ```python
            import os
        ```
        """

        pass

    @typing.overload
    @staticmethod
    async def FromTDesktop( account        : Union[td.TDesktop, td.Account],
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
                            receive_updates         : bool = True) -> TelegramClient:
        pass

    @staticmethod
    async def FromTDesktop( account         : Union[td.TDesktop, td.Account],
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
                            receive_updates         : bool = True) -> TelegramClient:
        
        Expects((flag == CreateNewSession) or (flag == UseCurrentSession), LoginFlagInvalid("LoginFlag invalid"))

        if isinstance(account, td.TDesktop):
            Expects(account.isLoaded(), TDesktopNotLoaded("You need to load accounts from a tdata folder first"))
            Expects(account.accountsCount > 0, TDesktopHasNoAccount("There is no account in this instance of TDesktop"))
            assert account.mainAccount
            account = account.mainAccount
        
        if (flag == UseCurrentSession) and not (isinstance(api, APIData) or APIData.__subclasscheck__(api)):
            
            warnings.warn( # type: ignore
                '\nIf you use an existing Telegram Desktop session '
                'with unofficial API_ID and API_HASH, '
                'Telegram might ban your account because of suspicious activities.\n'
                'Please use the default APITemplates to get rid of this.'
            )
        
        endpoints = account._local.config.endpoints(account.MainDcId)
        address = td.MTP.DcOptions.Address.IPv4
        protocol = td.MTP.DcOptions.Protocol.Tcp

        Expects(connection==ConnectionTcpFull, "Other connection type is not supported yet")
        Expects(len(endpoints[address][protocol]) > 0, "Couldn't find endpoint for this account, something went wrong?") # type: ignore
        
        endpoint = endpoints[address][protocol][0] # type: ignore

        # If we're gonna create a new session any way, then this session is only
        # created to accept the qr login for the new session
        if flag == CreateNewSession:
            auth_session = MemorySession()
        else:
            # COPY STRAIGHT FROM TELETHON
            # Determine what session object we have
            if isinstance(session, str) or session is None:
                try:
                    auth_session = SQLiteSession(session)
                except ImportError:
                    import warnings
                    warnings.warn(
                        'The sqlite3 module is not available under this '
                        'Python installation and no custom session '
                        'instance was given; using MemorySession.\n'
                        'You will need to re-login every time unless '
                        'you use another session storage'
                    )
                    auth_session = MemorySession()
            elif not isinstance(session, Session):
                raise TypeError(
                    'The given session must be a str or a Session instance.'
                )
                
        auth_session.set_dc(endpoint.id, endpoint.ip, endpoint.port) # type: ignore
        auth_session.auth_key = AuthKey(account.authKey.key) # type: ignore

        client = TelegramClient(auth_session, api=account.api, connection=connection, use_ipv6=use_ipv6,  # type: ignore
                                proxy=proxy, local_addr=local_addr, timeout=timeout, request_retries=request_retries,
                                connection_retries=connection_retries, retry_delay=retry_delay, auto_reconnect=auto_reconnect,
                                sequential_updates=sequential_updates, flood_sleep_threshold=flood_sleep_threshold,
                                raise_last_call_error=raise_last_call_error, loop=loop, base_logger=base_logger,
                                receive_updates=receive_updates)

        if flag == UseCurrentSession: return client


        await client.connect()
        Expects(await client.is_user_authorized(), 
        exception=TDesktopUnauthorized("TDesktop client is unauthorized"))
        


        # create new session by qrlogin
        return await client._QRLoginToNewClient(
                            session=session, api=api, password=password,

                            connection=connection, use_ipv6=use_ipv6,
                            proxy=proxy, local_addr=local_addr, timeout=timeout, request_retries=request_retries,
                            connection_retries=connection_retries, retry_delay=retry_delay, auto_reconnect=auto_reconnect,
                            sequential_updates=sequential_updates, flood_sleep_threshold=flood_sleep_threshold,
                            raise_last_call_error=raise_last_call_error, loop=loop, base_logger=base_logger,
                            receive_updates=receive_updates
                        )



def PrettyTable(table : List[Dict[str, Any]], addSplit : List[int] = []):
    
    # ! Warning: SUPER DIRTY CODE AHEAD
    padding = {}

    result = ""

    for label in table[0]:
        padding[label] = len(label)

    for row in table:
        for label, value in row.items():
            text = str(value)
            if padding[label] < len(text):
                padding[label] = len(text)

    def addpadding(text : str, spaces : int):
        if not isinstance(text, str): text = text.__str__()
        spaceLeft = spaces - len(text)
        padLeft = spaceLeft/2
        padLeft = round(padLeft - (padLeft % 1))
        padRight = spaceLeft - padLeft
        return padLeft * " " + text +  " " * padRight
    

    header = "|".join(addpadding(label, spaces + 2) for label, spaces in padding.items())
    splitter = "+".join(("-" * (spaces + 2)) for label, spaces in padding.items())
    rows = []
    for row in table:
        rows.append("|".join(addpadding(row[label], spaces + 2) for label, spaces in padding.items()))

    result += f"|{splitter}|\n"
    result += f"|{header}|\n"
    result += f"|{splitter}|\n"

    index = 0
    for row in rows:
        if index in addSplit:
            result += f"|{splitter}|\n"
        result += f"|{row}|\n"
        index += 1
        
    result += f"|{splitter}|"

    return result