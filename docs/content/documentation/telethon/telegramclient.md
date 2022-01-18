<!-- vim: syntax=Markdown -->

# TelegramClient

<a id="tl.telethon.TelegramClient"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/tl/telethon.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TelegramClient</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">telethon.TelegramClient</span></span><span class="highlight"><span class="o">, </span></span><span class="highlight"><span class="nc"> BaseObject</span></span><span class="highlight"><span class="o">)</span></span>

```python
@extend_class
class TelegramClient(telethon.TelegramClient,  BaseObject)
```

Extended version of telethon.TelegramClient

### Methods:

FromTDesktop():

    Create an instance of <a class="codehl codehl_obj" href="telegramclient#telegramclient-objects"><b>TelegramClient</b></a> from <a class="codehl codehl_obj" href="../../documentation/telegram-desktop/tdesktop#tdesktop-objects"><b>TDesktop</b></a>.



ToTDesktop():

    Convert this <a class="codehl codehl_obj" href="telegramclient#telegramclient-objects"><b>TelegramClient</b></a> instance to <a class="codehl codehl_obj" href="../../documentation/telegram-desktop/tdesktop#tdesktop-objects"><b>TDesktop</b></a>.



QRLoginToNewClient():

    Return <span class="highlight"><span class="kc">True</span></span> if logged-in using an <a class="codehl codehl_obj" href="../../documentation/authorization/api#api-objects"><b>official API</b></a>.



GetSessions():

    Get all logged in sessions.



GetCurrentSession():

    Get current logged-in session.



TerminateSession():

    Terminate a specific session.



TerminateAllSessions():

    Terminate all other sessions.



PrintSessions():

    Pretty-print all logged-in sessions.



is_official_app():

    Return <span class="highlight"><span class="kc">True</span></span> if logged-in using an <a class="codehl codehl_obj" href="../../documentation/authorization/api#api-objects"><b>official API</b></a>.







<a id="tl.telethon.TelegramClient.__init__"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/tl/telethon.py#L79"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nc">TelegramClient</span></span><span class="highlight"><span class="o">()</span></span>

```python
@typing.overload
def __init__(session: Union[str, Session] = None, api: Union[Type[API], API] = APITemplate.TelegramDesktop)
```

Start TelegramClient with customized api.

Read more at [OpenTele GitHub](https://github.com/thedemons/opentele#authorization)

### Arguments:
| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <span class="highlight"><span class="n">session</span></span> | <span class="highlight"><span class="bp">str</span></span>, <span class="highlight"><span class="nc">Session</span></span> |  | The file name of the <span class="highlight"><span class="n">session</span></span> <span class="highlight"><span class="n">file</span></span> to be used, if a string is\\<br/><br/>given (it may be a full path), or the <span class="highlight"><span class="nc">Session</span></span> instance to be used\\<br/><br/>Otherwise, if it's <span class="highlight"><span class="kc">None</span></span>, the <span class="highlight"><span class="n">session</span></span> will not be saved,\\<br/><br/>and you should call method <span class="highlight"><span class="o">.</span></span><span class="highlight"><span class="nf">log_out</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> when you're done.<br/><br/>Read more [here](https://docs.telethon.dev/en/latest/concepts/sessions.html?highlight=session#what-are-sessions). |
| <a class="codehl codehl_name" href="../../documentation/telegram-desktop/account#accountapi"><b>api</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api#api-objects"><b>API</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api#telegramdesktop-objects"><b>TelegramDesktop</b></a> | Which API to use. Read more <a class="codehl codehl_obj" href="../../documentation/authorization/api#api-objects"><b>here</b></a>. |


### Examples:

Start TelegramClient from an instance of TDesktop:



```python
    from opentele.tl import TelegramClient
    from opentele.td import APITemplate
    client = TelegramClient("data.session", api=APITemplate.TelegramDesktop)
```



<a id="tl.telethon.TelegramClient.GetSessions"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/tl/telethon.py#L338"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nf">GetSessions</span></span><span class="highlight"><span class="o">()</span></span>

```python
async def GetSessions() -> Optional[types.account.Authorizations]
```

Get all logged-in sessions.

### Returns:

- Return an instance of <span class="highlight"><span class="n">Authorizations</span></span> on success





<a id="tl.telethon.TelegramClient.GetCurrentSession"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/tl/telethon.py#L347"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nf">GetCurrentSession</span></span><span class="highlight"><span class="o">()</span></span>

```python
async def GetCurrentSession() -> Optional[types.Authorization]
```

Get current logged-in session.

### Returns:

Authorization: On success it will returns <span class="highlight"><span class="nc">telethon</span></span><span class="highlight"><span class="o">.</span></span><span class="highlight"><span class="nc">types</span></span><span class="highlight"><span class="o">.</span></span><span class="highlight"><span class="nc">Authorization</span></span>.

None: Return <span class="highlight"><span class="kc">None</span></span> on failure.





<a id="tl.telethon.TelegramClient.TerminateSession"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/tl/telethon.py#L367"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nf">TerminateSession</span></span><span class="highlight"><span class="o">()</span></span>

```python
async def TerminateSession(hash: int)
```

Terminate a specific session

### Arguments:
| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="nb">hash</span></span> | <span class="highlight"><span class="bp">int</span></span> | The <span class="highlight"><span class="n">session</span></span>'s hash to terminate |


### Raises:

<span class="highlight"><span class="nc">FreshResetAuthorisationForbiddenError</span></span>: You can't logout other <span class="highlight"><span class="n">sessions</span></span> if less than <span class="highlight"><span class="mi">24</span></span> <span class="highlight"><span class="n">hours</span></span> have passed since you logged on the <span class="highlight"><span class="n">current</span></span> <span class="highlight"><span class="n">session</span></span>.

<span class="highlight"><span class="nc">HashInvalidError</span></span>: The provided hash is invalid.





<a id="tl.telethon.TelegramClient.TerminateAllSessions"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/tl/telethon.py#L393"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nf">TerminateAllSessions</span></span><span class="highlight"><span class="o">()</span></span>

```python
async def TerminateAllSessions() -> bool
```

Terminate all other sessions.



<a id="tl.telethon.TelegramClient.PrintSessions"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/tl/telethon.py#L406"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nf">PrintSessions</span></span><span class="highlight"><span class="o">()</span></span>

```python
async def PrintSessions(sessions: types.account.Authorizations = None)
```

Pretty-print all logged-in sessions.

### Arguments:
| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <span class="highlight"><span class="n">sessions</span></span> | <span class="highlight"><span class="n">Authorizations</span></span> | <span class="highlight"><span class="kc">None</span></span> | <span class="highlight"><span class="n">Sessions</span></span> that return by <a class="codehl codehl_function" href="telegramclient#telegramclientgetsessions"><b>GetSessions</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span>, if <span class="highlight"><span class="kc">None</span></span> then it will <a class="codehl codehl_function" href="telegramclient#telegramclientgetsessions"><b>GetSessions</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> first. |


### Examples:

Example return:

    ```
    testest
    ```







<a id="tl.telethon.TelegramClient.is_official_app"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/tl/telethon.py#L441"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nf">is_official_app</span></span><span class="highlight"><span class="o">()</span></span>

```python
async def is_official_app() -> bool
```

Return <span class="highlight"><span class="kc">True</span></span> if this session was logged-in using an official app (<a class="codehl codehl_obj" href="../../documentation/authorization/api#api-objects"><b>API</b></a>).



<a id="tl.telethon.TelegramClient.QRLoginToNewClient"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/tl/telethon.py#L449"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nf">QRLoginToNewClient</span></span><span class="highlight"><span class="o">()</span></span>

```python
async def QRLoginToNewClient(session: Union[str, Session] = None, api: Union[Type[API], API] = APITemplate.TelegramDesktop, password: str = None, *, connection: typing.Type[Connection] = ConnectionTcpFull, use_ipv6: bool = False, proxy: Union[tuple, dict] = None, local_addr: Union[str, tuple] = None, timeout: int = 10, request_retries: int = 5, connection_retries: int = 5, retry_delay: int = 1, auto_reconnect: bool = True, sequential_updates: bool = False, flood_sleep_threshold: int = 60, raise_last_call_error: bool = False, loop: asyncio.AbstractEventLoop = None, base_logger: Union[str, logging.Logger] = None, receive_updates: bool = True) -> TelegramClient
```

### Arguments:
| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <span class="highlight"><span class="n">session</span></span> | <span class="highlight"><span class="bp">str</span></span>, <span class="highlight"><span class="nc">Session</span></span> | <span class="highlight"><span class="kc">None</span></span> | description |
| <a class="codehl codehl_name" href="../../documentation/telegram-desktop/account#accountapi"><b>api</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api#api-objects"><b>API</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api#telegramdesktop-objects"><b>TelegramDesktop</b></a> | Which API to use. Read more <a class="codehl codehl_obj" href="../../documentation/authorization/api#api-objects"><b>here</b></a>. |
| <span class="highlight"><span class="n">password</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | Two-step verification password, set if needed. |


### Raises:

- <a class="codehl codehl_obj" href="../../documentation/exceptions#nopasswordprovided-objects"><b>NoPasswordProvided</b></a>: The account's two-step verification is enabled and no <span class="highlight"><span class="n">password</span></span> was provided. Please set the <span class="highlight"><span class="n">password</span></span> parameters.

- <a class="codehl codehl_obj" href="../../documentation/exceptions#passwordincorrect-objects"><b>PasswordIncorrect</b></a>: The two-step verification <span class="highlight"><span class="n">password</span></span> is incorrect

- <span class="highlight"><span class="ne">TimeoutError</span></span>: Time out waiting for the client to be authorized.



### Returns:

- Return an instance of <a class="codehl codehl_obj" href="telegramclient#telegramclient-objects"><b>TelegramClient</b></a> on success





<a id="tl.telethon.TelegramClient.ToTDesktop"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/tl/telethon.py#L582"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nf">ToTDesktop</span></span><span class="highlight"><span class="o">()</span></span>

```python
async def ToTDesktop(flag: Type[LoginFlag] = CreateNewSession, api: Union[Type[API], API] = APITemplate.TelegramDesktop, password: str = None) -> td.TDesktop
```

Convert this instance of <a class="codehl codehl_obj" href="telegramclient#telegramclient-objects"><b>TelegramClient</b></a> to <a class="codehl codehl_obj" href="../../documentation/telegram-desktop/tdesktop#tdesktop-objects"><b>TDesktop</b></a>

### Arguments:
| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <span class="highlight"><span class="n">flag</span></span> | <a class="codehl codehl_obj" href="../../documentation/authorization/loginflag#loginflag-objects"><b>LoginFlag</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/loginflag#createnewsession-objects"><b>CreateNewSession</b></a> | The login flag. Read more <a class="codehl codehl_obj" href="../../documentation/authorization/loginflag#loginflag-objects"><b>here</b></a>. |
| <a class="codehl codehl_name" href="../../documentation/telegram-desktop/account#accountapi"><b>api</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api#api-objects"><b>API</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api#telegramdesktop-objects"><b>TelegramDesktop</b></a> | Which API to use. Read more <a class="codehl codehl_obj" href="../../documentation/authorization/api#api-objects"><b>here</b></a>. |
| <span class="highlight"><span class="n">password</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | Two-step verification <span class="highlight"><span class="n">password</span></span> if needed. |


### Returns:

- Return an instance of <a class="codehl codehl_obj" href="../../documentation/telegram-desktop/tdesktop#tdesktop-objects"><b>TDesktop</b></a> on success





<a id="tl.telethon.TelegramClient.FromTDesktop"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/tl/telethon.py#L607"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nf">FromTDesktop</span></span><span class="highlight"><span class="o">()</span></span>

```python
@typing.overload
@staticmethod
async def FromTDesktop(account: Union[td.TDesktop, td.Account], session: Union[str, Session] = None, flag: Type[LoginFlag] = CreateNewSession, api: Union[Type[API], API] = APITemplate.TelegramDesktop, password: str = None) -> TelegramClient
```

### Arguments:
| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <span class="highlight"><span class="n">account</span></span> | <a class="codehl codehl_obj" href="../../documentation/telegram-desktop/tdesktop#tdesktop-objects"><b>TDesktop</b></a>, <a class="codehl codehl_obj" href="../../documentation/telegram-desktop/account#account-objects"><b>Account</b></a> |  | The <span class="highlight"><span class="nn">td</span></span><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_obj" href="../../documentation/telegram-desktop/tdesktop#tdesktop-objects"><b>TDesktop</b></a> or <span class="highlight"><span class="nn">td</span></span><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_obj" href="../../documentation/telegram-desktop/account#account-objects"><b>Account</b></a> you want to convert from. |
| <span class="highlight"><span class="n">session</span></span> | <span class="highlight"><span class="bp">str</span></span>, <span class="highlight"><span class="nc">Session</span></span> | <span class="highlight"><span class="kc">None</span></span> | The file name of the <span class="highlight"><span class="n">session</span></span> <span class="highlight"><span class="n">file</span></span> to be used, if <span class="highlight"><span class="kc">None</span></span> then the session will not be saved.\\<br/><br/>Read more [here](https://docs.telethon.dev/en/latest/concepts/sessions.html?highlight=session#what-are-sessions). |
| <span class="highlight"><span class="n">flag</span></span> | <a class="codehl codehl_obj" href="../../documentation/authorization/loginflag#loginflag-objects"><b>LoginFlag</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/loginflag#createnewsession-objects"><b>CreateNewSession</b></a> | The login flag. Read more <a class="codehl codehl_obj" href="../../documentation/authorization/loginflag#loginflag-objects"><b>here</b></a>. |
| <a class="codehl codehl_name" href="../../documentation/telegram-desktop/account#accountapi"><b>api</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api#api-objects"><b>API</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api#telegramdesktop-objects"><b>TelegramDesktop</b></a> | Which API to use. Read more <a class="codehl codehl_obj" href="../../documentation/authorization/api#api-objects"><b>here</b></a>. |
| <span class="highlight"><span class="n">password</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | Two-step verification password if needed. |


### Returns:

- Return an instance of <a class="codehl codehl_obj" href="telegramclient#telegramclient-objects"><b>TelegramClient</b></a> on success





