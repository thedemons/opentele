<!-- vim: syntax=Markdown -->

# TelegramClient

## Table of Contents

* [TelegramClient](#tl.telethon.TelegramClient)
  * [\_\_init\_\_](#tl.telethon.TelegramClient.__init__)
  * [\_\_init\_\_](#tl.telethon.TelegramClient.__init__)
  * [ToTDesktop](#tl.telethon.TelegramClient.ToTDesktop)
  * [FromTDesktop](#tl.telethon.TelegramClient.FromTDesktop)

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\tl\telethon.py#L3)

<a id="tl.telethon.TelegramClient"></a>

## TelegramClient Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\tl\telethon.py#L45)

```python
@extend_class
class TelegramClient(telethon.TelegramClient,  BaseObject)
```

Extended version of telethon.TelegramClient

#### Methods:

- <a class="md-typeset__a_obj" href="../telegramclient#tl.telethon.TelegramClient.FromTDesktop">FromTDesktop()</a> - Create an instance of <a class="md-typeset__a_obj" href="../telegramclient#tl.telethon.TelegramClient">TelegramClient</a> from <a class="md-typeset__a_obj" href="../../telegram-desktop/tdesktop#td.tdesktop.TDesktop">TDesktop</a>
- <a class="md-typeset__a_obj" href="../telegramclient#tl.telethon.TelegramClient.ToTDesktop">ToTDesktop()</a> - Convert this <a class="md-typeset__a_obj" href="../telegramclient#tl.telethon.TelegramClient">TelegramClient</a> instance to <a class="md-typeset__a_obj" href="../../telegram-desktop/tdesktop#td.tdesktop.TDesktop">TDesktop</a>


<a id="tl.telethon.TelegramClient.__init__"></a>

#### TelegramClient.\_\_init\_\_

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\tl\telethon.py#L55)

```python
@typing.overload
def __init__(session: Union[str, Session] = None, api: Union[Type[APIData], APIData] = APITemplate.TelegramDesktop)
```

Start TelegramClient with customized api.

Read more at [OpenTele GitHub](https://github.com/thedemons/opentele#authorization)

### Arguments
    session (`Union[str, Session]`):
         The file name of the session file to be used if a string is
        given (it may be a full path), or the Session instance to be
        used otherwise. If it's <span class="md-typeset__const">None</span>, the session will not be saved,
        and you should call :meth:`.log_out()` when you're done.

        Note that if you pass a string it will be a file in the current
        working directory, although you can also pass absolute paths.

        The session file contains enough information for you to login
        without re-sending the code, so if you have to enter the code
        more than once, maybe you're changing the working directory,
        renaming or removing the file, or using random names.

    api (APIData):
        Which <a class="md-typeset__a_obj" href="../../authorization/apidata#apidata.APIData">APIData</a> to use, use `APITemPlate.TelegramDesktop` by default

### Examples
#### Start TelegramClient from an instance of TDesktop:
```python
    from opentele.tl import TelegramClient
    from opentele.td import APITemplate

    client = TelegramClient("data.session", api=APITemplate.TelegramDesktop)
```

<a id="tl.telethon.TelegramClient.__init__"></a>

#### TelegramClient.\_\_init\_\_

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\tl\telethon.py#L90)

```python
@typing.overload
def __init__(session: Union[str, Session] = None, api: Union[Type[APIData], APIData] = None, api_id: int = 0, api_hash: str = None, *, connection: typing.Type[Connection] = ConnectionTcpFull, use_ipv6: bool = False, proxy: Union[tuple, dict] = None, local_addr: Union[str, tuple] = None, timeout: int = 10, request_retries: int = 5, connection_retries: int = 5, retry_delay: int = 1, auto_reconnect: bool = True, sequential_updates: bool = False, flood_sleep_threshold: int = 60, raise_last_call_error: bool = False, device_model: str = None, system_version: str = None, app_version: str = None, lang_code: str = 'en', system_lang_code: str = 'en', loop: asyncio.AbstractEventLoop = None, base_logger: Union[str, logging.Logger] = None, receive_updates: bool = True)
```

This is the abstract base class for the client. It defines some
basic stuff like connecting, switching data center, etc, and
leaves the `__call__` unimplemented.

Arguments
    session (<span class="md-typeset__obj">str</span> | `telethon.sessions.abstract.Session`, <span class="md-typeset__const">None</span>):
        The file name of the session file to be used if a string is
        given (it may be a full path), or the Session instance to be
        used otherwise. If it's <span class="md-typeset__const">None</span>, the session will not be saved,
        and you should call :meth:`.log_out()` when you're done.

        Note that if you pass a string it will be a file in the current
        working directory, although you can also pass absolute paths.

        The session file contains enough information for you to login
        without re-sending the code, so if you have to enter the code
        more than once, maybe you're changing the working directory,
        renaming or removing the file, or using random names.

    api (<a class="md-typeset__a_obj" href="../../authorization/apidata#apidata.APIData">APIData</a>, optional):
        Use custom api_id and api_hash for better experience.\n
        These arguments will be ignored if it is set in the APIData: `api_id`, `api_hash`, `device_model`, `system_version`, `app_version`, `lang_code`, `system_lang_code`
        Read more at [OpenTele GitHub](https://github.com/thedemons/opentele#authorization)

    api_id (<span class="md-typeset__obj">int</span> | <span class="md-typeset__obj">str</span>, optional):
        The API ID you obtained from https://my.telegram.org.

    api_hash (<span class="md-typeset__obj">str</span>, optional):
        The API hash you obtained from https://my.telegram.org.

    connection (`telethon.network.connection.common.Connection`, optional):
        The connection instance to be used when creating a new connection
        to the servers. It **must** be a type.

        Defaults to `telethon.network.connection.tcpfull.ConnectionTcpFull`.

    use_ipv6 (<span class="md-typeset__obj">bool</span>, optional):
        Whether to connect to the servers through IPv6 or not.
        By default this is `False` as IPv6 support is not
        too widespread yet.

    proxy (`tuple` | <span class="md-typeset__obj">list</span> | <span class="md-typeset__obj">dict</span>, optional):
        An iterable consisting of the proxy info. If `connection` is
        one of `MTProxy`, then it should contain MTProxy credentials:
        ``('hostname', port, 'secret')``. Otherwise, it's meant to store
        function parameters for PySocks, like ``(type, 'hostname', port)``.
        See https://github.com/Anorov/PySocks#usage-1 for more.

    local_addr (<span class="md-typeset__obj">str</span> | `tuple`, optional):
        Local host address (and port, optionally) used to bind the socket to locally.
        You only need to use this if you have multiple network cards and
        want to use a specific one.

    timeout (<span class="md-typeset__obj">int</span> | <span class="md-typeset__obj">float</span>, optional):
        The timeout in seconds to be used when connecting.
        This is **not** the timeout to be used when `<span class="md-typeset__const">await</span>`'ing for
        invoked requests, and you should use ``asyncio.wait`` or
        ``asyncio.wait_for`` for that.

    request_retries (<span class="md-typeset__obj">int</span> | <span class="md-typeset__const">None</span>, optional):
        How many times a request should be retried. Request are retried
        when Telegram is having internal issues (due to either
        ``errors.ServerError`` or ``errors.RpcCallFailError``),
        when there is a ``errors.FloodWaitError`` less than
        `flood_sleep_threshold`, or when there's a migrate error.

        May take a negative or <span class="md-typeset__const">None</span> value for infinite retries, but
        this is not recommended, since some requests can always trigger
        a call fail (such as searching for messages).

    connection_retries (<span class="md-typeset__obj">int</span> | <span class="md-typeset__const">None</span>, optional):
        How many times the reconnection should retry, either on the
        initial connection or when Telegram disconnects us. May be
        set to a negative or <span class="md-typeset__const">None</span> value for infinite retries, but
        this is not recommended, since the program can get stuck in an
        infinite loop.

    retry_delay (<span class="md-typeset__obj">int</span> | <span class="md-typeset__obj">float</span>, optional):
        The delay in seconds to sleep between automatic reconnections.

    auto_reconnect (<span class="md-typeset__obj">bool</span>, optional):
        Whether reconnection should be retried `connection_retries`
        times automatically if Telegram disconnects us or not.

    sequential_updates (<span class="md-typeset__obj">bool</span>, optional):
        By default every incoming update will create a new task, so
        you can handle several updates in parallel. Some scripts need
        the order in which updates are processed to be sequential, and
        this setting allows them to do so.

        If set to `True`, incoming updates will be put in a queue
        and processed sequentially. This means your event handlers
        should *not* perform long-running operations since new
        updates are put inside of an unbounded queue.

    flood_sleep_threshold (<span class="md-typeset__obj">int</span> | <span class="md-typeset__obj">float</span>, optional):
        The threshold below which the library should automatically
        sleep on flood wait and slow mode wait errors (inclusive). For instance, if a
        ``FloodWaitError`` for 17s occurs and `flood_sleep_threshold`
        is 20s, the library will ``sleep`` automatically. If the error
        was for 21s, it would ``raise FloodWaitError`` instead. Values
        larger than a day (like ``float('inf')``) will be changed to a day.

    raise_last_call_error (<span class="md-typeset__obj">bool</span>, optional):
        When API calls fail in a way that causes Telethon to retry
        automatically, should the RPC error of the last attempt be raised
        instead of a generic ValueError. This is mostly useful for
        detecting when Telegram has internal issues.

    device_model (<span class="md-typeset__obj">str</span>, optional):
        "Device model" to be sent when creating the initial connection.
        Defaults to 'PC (n)bit' derived from ``platform.uname().machine``, or its direct value if unknown.

    system_version (<span class="md-typeset__obj">str</span>, optional):
        "System version" to be sent when creating the initial connection.
        Defaults to ``platform.uname().release`` stripped of everything ahead of -.

    app_version (<span class="md-typeset__obj">str</span>, optional):
        "App version" to be sent when creating the initial connection.
        Defaults to `telethon.version.__version__`.

    lang_code (<span class="md-typeset__obj">str</span>, optional):
        "Language code" to be sent when creating the initial connection.
        Defaults to ``'en'``.

    system_lang_code (<span class="md-typeset__obj">str</span>, optional):
        "System lang code"  to be sent when creating the initial connection.
        Defaults to `lang_code`.

    loop (`asyncio.AbstractEventLoop`, optional):
        Asyncio event loop to use. Defaults to `asyncio.get_event_loop()`.
        This argument is ignored.

    base_logger (<span class="md-typeset__obj">str</span> | `logging.Logger`, optional):
        Base logger name or instance to use.
        If a <span class="md-typeset__obj">str</span> is given, it'll be passed to `logging.getLogger()`. If a
        `logging.Logger` is given, it'll be used directly. If something
        else or nothing is given, the default logger will be used.

    receive_updates (<span class="md-typeset__obj">bool</span>, optional):
        Whether the client will receive updates or not. By default, updates
        will be received from Telegram as they occur.

        Turning this off means that Telegram will not send updates at all
        so event handlers, conversations, and QR login will not work.
        However, certain scripts don't need updates, so this will reduce
        the amount of bandwidth used.

<a id="tl.telethon.TelegramClient.ToTDesktop"></a>

#### TelegramClient.ToTDesktop

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\tl\telethon.py#L504)

```python
async def ToTDesktop(flag: Type[LoginFlag] = CreateNewSession, api: Union[Type[APIData], APIData] = APITemplate.TelegramDesktop, password: str = None) -> TDesktop
```

Convert this instance of <a class="md-typeset__a_obj" href="../telegramclient#tl.telethon.TelegramClient">TelegramClient</a> to <a class="md-typeset__a_obj" href="../../telegram-desktop/tdesktop#td.tdesktop.TDesktop">TDesktop</a>

#### Arguments:

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| flag | `Type[LoginFlag]` \| `CreateNewSession` | __required__ | See `LoginFlag` to learn more |
| api | `Union[Type[APIData] |  APIData]` | <a class="md-typeset__a_obj" href="../../authorization/apitemplate#apidata.APITemplate.TelegramDesktop">APITemplate.TelegramDesktop</a> | See <a class="md-typeset__a_obj" href="../../authorization/apidata#apidata.APIData">APIData</a> to learn more |
| password | <span class="md-typeset__obj">str</span> \| <span class="md-typeset__const">None</span> | __required__ | Two-step verification password if needed |

#### Returns:

- <a class="md-typeset__a_obj" href="../../telegram-desktop/tdesktop#td.tdesktop.TDesktop">TDesktop</a> - [description]


<a id="tl.telethon.TelegramClient.FromTDesktop"></a>

#### TelegramClient.FromTDesktop

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\tl\telethon.py#L529)

```python
@typing.overload
@staticmethod
async def FromTDesktop(account: Union[TDesktop, td.Account], session: Union[str, Session] = None, flag: Type[LoginFlag] = CreateNewSession, api: Union[Type[APIData], APIData] = APITemplate.TelegramDesktop, password: str = None) -> TelegramClient
```

FromTDesktop [summary]
[extended_summary]

Args:
    account (Union[TDesktop, td.Account]): [description]
    session (Union[str, Session], optional): [description]. Defaults to None.
    flag (Type[LoginFlag], optional): [description]. Defaults to CreateNewSession.
    api (Union[Type[APIData], APIData], optional): [description]. Defaults to APITemplate.TelegramDesktop.
    password (str, optional): [description]. Defaults to None.

Returns:
```python
    import os
```


