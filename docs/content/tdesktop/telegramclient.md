# TelegramClient

## Table of Contents

* [tl.telethon](#tl.telethon)
  * [annotations](#tl.telethon.annotations)
  * [\*](#tl.telethon.*)
  * [tl](#tl.telethon.tl)
  * [PasswordHashInvalidError](#tl.telethon.PasswordHashInvalidError)
  * [AuthTokenAlreadyAcceptedError](#tl.telethon.AuthTokenAlreadyAcceptedError)
  * [AuthTokenExpiredError](#tl.telethon.AuthTokenExpiredError)
  * [AuthTokenInvalidError](#tl.telethon.AuthTokenInvalidError)
  * [FreshResetAuthorisationForbiddenError](#tl.telethon.FreshResetAuthorisationForbiddenError)
  * [HashInvalidError](#tl.telethon.HashInvalidError)
  * [TypeInputClientProxy](#tl.telethon.TypeInputClientProxy)
  * [TypeJSONValue](#tl.telethon.TypeJSONValue)
  * [logging](#tl.telethon.logging)
  * [warnings](#tl.telethon.warnings)
  * [TelegramClient](#tl.telethon.TelegramClient)
    * [\_\_init\_\_](#tl.telethon.TelegramClient.__init__)
    * [\_\_init\_\_](#tl.telethon.TelegramClient.__init__)
    * [FromTDesktop](#tl.telethon.TelegramClient.FromTDesktop)

<a id="tl.telethon"></a>

# tl.telethon

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\tl\telethon.py#L3)

<a id="tl.telethon.annotations"></a>

## annotations

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\tl\telethon.py#L3)

<a id="tl.telethon.*"></a>

## \*

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\tl\telethon.py#L5)

<a id="tl.telethon.tl"></a>

## tl

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\tl\telethon.py#L6)

<a id="tl.telethon.PasswordHashInvalidError"></a>

## PasswordHashInvalidError

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\tl\telethon.py#L8)

<a id="tl.telethon.AuthTokenAlreadyAcceptedError"></a>

## AuthTokenAlreadyAcceptedError

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\tl\telethon.py#L8)

<a id="tl.telethon.AuthTokenExpiredError"></a>

## AuthTokenExpiredError

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\tl\telethon.py#L8)

<a id="tl.telethon.AuthTokenInvalidError"></a>

## AuthTokenInvalidError

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\tl\telethon.py#L8)

<a id="tl.telethon.FreshResetAuthorisationForbiddenError"></a>

## FreshResetAuthorisationForbiddenError

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\tl\telethon.py#L8)

<a id="tl.telethon.HashInvalidError"></a>

## HashInvalidError

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\tl\telethon.py#L8)

<a id="tl.telethon.TypeInputClientProxy"></a>

## TypeInputClientProxy

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\tl\telethon.py#L9)

<a id="tl.telethon.TypeJSONValue"></a>

## TypeJSONValue

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\tl\telethon.py#L9)

<a id="tl.telethon.logging"></a>

## logging

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\tl\telethon.py#L11)

<a id="tl.telethon.warnings"></a>

## warnings

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\tl\telethon.py#L12)

<a id="tl.telethon.TelegramClient"></a>

## TelegramClient Objects

```python
@extend_class
class TelegramClient(telethon.TelegramClient,  BaseObject)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\tl\telethon.py#L45)

<a id="tl.telethon.TelegramClient.__init__"></a>

#### TelegramClient.\_\_init\_\_

```python
@typing.overload
def __init__(session: Union[str, Session] = None, api: Union[Type[APIData], APIData] = APITemplate.TelegramDesktop)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\tl\telethon.py#L49)

Start TelegramClient with customized api
Read more at [OpenTele GitHub](https://github.com/thedemons/opentele#authorization)

### Arguments
    1. session (`Union[str, Session]`):\n
         The file name of the session file to be used if a string is
        given (it may be a full path), or the Session instance to be
        used otherwise. If it's <span style="color:blue">**None**</span>, the session will not be saved,
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

<a id="tl.telethon.TelegramClient.__init__"></a>

#### TelegramClient.\_\_init\_\_

```python
@typing.overload
def __init__(session: Union[str, Session] = None, api: Union[Type[APIData], APIData] = None, api_id: int = 0, api_hash: str = None, *, connection: typing.Type[Connection] = ConnectionTcpFull, use_ipv6: bool = False, proxy: Union[tuple, dict] = None, local_addr: Union[str, tuple] = None, timeout: int = 10, request_retries: int = 5, connection_retries: int = 5, retry_delay: int = 1, auto_reconnect: bool = True, sequential_updates: bool = False, flood_sleep_threshold: int = 60, raise_last_call_error: bool = False, device_model: str = None, system_version: str = None, app_version: str = None, lang_code: str = 'en', system_lang_code: str = 'en', loop: asyncio.AbstractEventLoop = None, base_logger: Union[str, logging.Logger] = None, receive_updates: bool = True)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\tl\telethon.py#L85)

This is the abstract base class for the client. It defines some
basic stuff like connecting, switching data center, etc, and
leaves the `__call__` unimplemented.

Arguments
    session (<span style="color:green">**str**</span> | `telethon.sessions.abstract.Session`, <span style="color:blue">**None**</span>):
        The file name of the session file to be used if a string is
        given (it may be a full path), or the Session instance to be
        used otherwise. If it's <span style="color:blue">**None**</span>, the session will not be saved,
        and you should call :meth:`.log_out()` when you're done.

        Note that if you pass a string it will be a file in the current
        working directory, although you can also pass absolute paths.

        The session file contains enough information for you to login
        without re-sending the code, so if you have to enter the code
        more than once, maybe you're changing the working directory,
        renaming or removing the file, or using random names.

    api (**[APIData](../../APIData#apidata.APIData)**, optional):
        Use custom api_id and api_hash for better experience.\n
        These arguments will be ignored if it is set in the APIData: `api_id`, `api_hash`, `device_model`, `system_version`, `app_version`, `lang_code`, `system_lang_code`
        Read more at [OpenTele GitHub](https://github.com/thedemons/opentele#authorization)

    api_id (<span style="color:green">**int**</span> | <span style="color:green">**str**</span>, optional):
        The API ID you obtained from https://my.telegram.org.

    api_hash (<span style="color:green">**str**</span>, optional):
        The API hash you obtained from https://my.telegram.org.

    connection (`telethon.network.connection.common.Connection`, optional):
        The connection instance to be used when creating a new connection
        to the servers. It **must** be a type.

        Defaults to `telethon.network.connection.tcpfull.ConnectionTcpFull`.

    use_ipv6 (<span style="color:green">**bool**</span>, optional):
        Whether to connect to the servers through IPv6 or not.
        By default this is `False` as IPv6 support is not
        too widespread yet.

    proxy (`tuple` | <span style="color:green">**list**</span> | <span style="color:green">**dict**</span>, optional):
        An iterable consisting of the proxy info. If `connection` is
        one of `MTProxy`, then it should contain MTProxy credentials:
        ``('hostname', port, 'secret')``. Otherwise, it's meant to store
        function parameters for PySocks, like ``(type, 'hostname', port)``.
        See https://github.com/Anorov/PySocks#usage-1 for more.

    local_addr (<span style="color:green">**str**</span> | `tuple`, optional):
        Local host address (and port, optionally) used to bind the socket to locally.
        You only need to use this if you have multiple network cards and
        want to use a specific one.

    timeout (<span style="color:green">**int**</span> | <span style="color:green">**float**</span>, optional):
        The timeout in seconds to be used when connecting.
        This is **not** the timeout to be used when ``await``'ing for
        invoked requests, and you should use ``asyncio.wait`` or
        ``asyncio.wait_for`` for that.

    request_retries (<span style="color:green">**int**</span> | <span style="color:blue">**None**</span>, optional):
        How many times a request should be retried. Request are retried
        when Telegram is having internal issues (due to either
        ``errors.ServerError`` or ``errors.RpcCallFailError``),
        when there is a ``errors.FloodWaitError`` less than
        `flood_sleep_threshold`, or when there's a migrate error.

        May take a negative or <span style="color:blue">**None**</span> value for infinite retries, but
        this is not recommended, since some requests can always trigger
        a call fail (such as searching for messages).

    connection_retries (<span style="color:green">**int**</span> | <span style="color:blue">**None**</span>, optional):
        How many times the reconnection should retry, either on the
        initial connection or when Telegram disconnects us. May be
        set to a negative or <span style="color:blue">**None**</span> value for infinite retries, but
        this is not recommended, since the program can get stuck in an
        infinite loop.

    retry_delay (<span style="color:green">**int**</span> | <span style="color:green">**float**</span>, optional):
        The delay in seconds to sleep between automatic reconnections.

    auto_reconnect (<span style="color:green">**bool**</span>, optional):
        Whether reconnection should be retried `connection_retries`
        times automatically if Telegram disconnects us or not.

    sequential_updates (<span style="color:green">**bool**</span>, optional):
        By default every incoming update will create a new task, so
        you can handle several updates in parallel. Some scripts need
        the order in which updates are processed to be sequential, and
        this setting allows them to do so.

        If set to `True`, incoming updates will be put in a queue
        and processed sequentially. This means your event handlers
        should *not* perform long-running operations since new
        updates are put inside of an unbounded queue.

    flood_sleep_threshold (<span style="color:green">**int**</span> | <span style="color:green">**float**</span>, optional):
        The threshold below which the library should automatically
        sleep on flood wait and slow mode wait errors (inclusive). For instance, if a
        ``FloodWaitError`` for 17s occurs and `flood_sleep_threshold`
        is 20s, the library will ``sleep`` automatically. If the error
        was for 21s, it would ``raise FloodWaitError`` instead. Values
        larger than a day (like ``float('inf')``) will be changed to a day.

    raise_last_call_error (<span style="color:green">**bool**</span>, optional):
        When API calls fail in a way that causes Telethon to retry
        automatically, should the RPC error of the last attempt be raised
        instead of a generic ValueError. This is mostly useful for
        detecting when Telegram has internal issues.

    device_model (<span style="color:green">**str**</span>, optional):
        "Device model" to be sent when creating the initial connection.
        Defaults to 'PC (n)bit' derived from ``platform.uname().machine``, or its direct value if unknown.

    system_version (<span style="color:green">**str**</span>, optional):
        "System version" to be sent when creating the initial connection.
        Defaults to ``platform.uname().release`` stripped of everything ahead of -.

    app_version (<span style="color:green">**str**</span>, optional):
        "App version" to be sent when creating the initial connection.
        Defaults to `telethon.version.__version__`.

    lang_code (<span style="color:green">**str**</span>, optional):
        "Language code" to be sent when creating the initial connection.
        Defaults to ``'en'``.

    system_lang_code (<span style="color:green">**str**</span>, optional):
        "System lang code"  to be sent when creating the initial connection.
        Defaults to `lang_code`.

    loop (`asyncio.AbstractEventLoop`, optional):
        Asyncio event loop to use. Defaults to `asyncio.get_event_loop()`.
        This argument is ignored.

    base_logger (<span style="color:green">**str**</span> | `logging.Logger`, optional):
        Base logger name or instance to use.
        If a <span style="color:green">**str**</span> is given, it'll be passed to `logging.getLogger()`. If a
        `logging.Logger` is given, it'll be used directly. If something
        else or nothing is given, the default logger will be used.

    receive_updates (<span style="color:green">**bool**</span>, optional):
        Whether the client will receive updates or not. By default, updates
        will be received from Telegram as they occur.

        Turning this off means that Telegram will not send updates at all
        so event handlers, conversations, and QR login will not work.
        However, certain scripts don't need updates, so this will reduce
        the amount of bandwidth used.

<a id="tl.telethon.TelegramClient.FromTDesktop"></a>

#### TelegramClient.FromTDesktop

```python
@typing.overload
@staticmethod
async def FromTDesktop(account: Union[td.TDesktop, td.Account], session: Union[str, Session] = None, flag: Type[LoginFlag] = CreateNewSession, api: Union[Type[APIData], APIData] = APITemplate.TelegramDesktop, password: str = None) -> TelegramClient
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\tl\telethon.py#L500)

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


