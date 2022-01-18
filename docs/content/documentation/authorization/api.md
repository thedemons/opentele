<!-- vim: syntax=Markdown -->

# API

<a id="api.API"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/api.py#L54"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">API</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">object</span></span><span class="highlight"><span class="o">, </span></span><span class="highlight"><span class="nc">metaclass</span></span><span class="highlight"><span class="o">=</span></span><span class="highlight"><span class="nc">BaseAPIMetaClass</span></span><span class="highlight"><span class="o">)</span></span>

```python
class API(object, metaclass=BaseAPIMetaClass)
```

API configuration to connect to <a class="codehl codehl_obj" href="../../documentation/telethon/telegramclient.md#telegramclient-objects"><b>TelegramClient</b></a> and <a class="codehl codehl_obj" href="../../documentation/telegram-desktop/tdesktop.md#tdesktop-objects"><b>TDesktop</b></a>

- <span class="highlight"><span class="o">*</span></span><span class="highlight"><span class="o">*</span></span><span class="highlight"><span class="n">opentele</span></span><span class="highlight"><span class="o">*</span></span><span class="highlight"><span class="o">*</span></span> offers the ability to use **<span class="highlight"><span class="n">official</span></span> <span class="highlight"><span class="n">APIs</span></span>**, which are used by <span class="highlight"><span class="n">official</span></span> <span class="highlight"><span class="n">apps</span></span>. You can check that out in <a class="codehl codehl_obj" href="api.md#apitemplate-objects"><b>APITemplate</b></a>.

- According to [Telegram TOS](https://core.telegram.org/api/obtaining_api_id#using-the-api-id): *all accounts that sign up or log in using unofficial Telegram API clients are automatically put under observation to avoid violations of the Terms of Service*.

- It also uses the **[lang_pack](https://core.telegram.org/method/initConnection)** parameter, of which [telethon can't use](https://github.com/LonamiWebs/Telethon/blob/master/telethon/client/telegrambaseclient.py#L375) because it's for official apps only.

- Therefore, **there are no differences** between using <span class="highlight"><span class="n">opentele</span></span> and <span class="highlight"><span class="n">official</span></span> <span class="highlight"><span class="n">apps</span></span>, the server can't tell you apart.

- You can use <a class="codehl codehl_obj" href="../../documentation/telethon/telegramclient.md#telegramclient-objects"><b>TelegramClient</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_function" href="../../documentation/telethon/telegramclient.md#telegramclientprintsessions"><b>PrintSessions</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> to check this out.

### Attributes:
| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">api_id</span></span> | <span class="highlight"><span class="bp">int</span></span> | [API_ID](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id) |
| <span class="highlight"><span class="n">api_hash</span></span> | <span class="highlight"><span class="bp">str</span></span> | [API_HASH](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id) |
| <span class="highlight"><span class="n">device_model</span></span> | <span class="highlight"><span class="bp">str</span></span> | Device model name |
| <span class="highlight"><span class="n">system_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | Operating System version |
| <span class="highlight"><span class="n">app_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | Current app version |
| <span class="highlight"><span class="n">lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | Language code of the client |
| <span class="highlight"><span class="n">system_lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | Language code of operating system |
| <span class="highlight"><span class="n">lang_pack</span></span> | <span class="highlight"><span class="bp">str</span></span> | Language pack |


### Methods:

<a class="codehl codehl_function" href="api.md#apigenerate"><b>Generate</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span>: Generate random device model and system version





<a id="api.API.__init__"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/api.py#L107"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nc">API</span></span><span class="highlight"><span class="o">()</span></span>

```python
@typing.overload
def __init__(api_id: int, api_hash: str, device_model: str = None, system_version: str = None, app_version: str = None, lang_code: str = None, system_lang_code: str = None, lang_pack: str = None) -> None
```

Create your own customized API

### Arguments:
| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <span class="highlight"><span class="n">api_id</span></span> | <span class="highlight"><span class="bp">int</span></span> |  | [API_ID](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id) |
| <span class="highlight"><span class="n">api_hash</span></span> | <span class="highlight"><span class="bp">str</span></span> |  | [API_HASH](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id) |
| <span class="highlight"><span class="n">device_model</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | <span class="highlight"><span class="n">Device model name</span></span> |
| <span class="highlight"><span class="n">system_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | <span class="highlight"><span class="n">Operating System version</span></span> |
| <span class="highlight"><span class="n">app_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | <span class="highlight"><span class="n">Current app version</span></span> |
| <span class="highlight"><span class="n">lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en</span></span><span class="highlight"><span class="s2">"</span></span> | <span class="highlight"><span class="n">Language code of the client</span></span> |
| <span class="highlight"><span class="n">system_lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en</span></span><span class="highlight"><span class="s2">"</span></span> | <span class="highlight"><span class="n">Language code of operating system</span></span> |
| <span class="highlight"><span class="n">lang_pack</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">"</span></span> | <span class="highlight"><span class="n">Language pack</span></span> |


???+ warning "Use at your own risk!"
    Using the wrong API can lead to your account banned.<br/>
    If the session was created using an official API, you must continue using official APIs for that session.<br/>
    Otherwise that account is at risk of getting banned.




<a id="api.API.Generate"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/api.py#L238"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nf">Generate</span></span><span class="highlight"><span class="o">()</span></span>

```python
@classmethod
def Generate(cls: Type[_T], id: str = None) -> _T
```

Generate random device model and system version

### Arguments:
| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <span class="highlight"><span class="nb">id</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | The ID to generate - can be anything.\\<br/><br/>This will be used to ensure that it will generate the same data everytime.\\<br/><br/>If not set then it won't generate the same value again. |


### Raises:

<span class="highlight"><span class="ne">NotImplementedError</span></span>: Not supported for web browser yet



### Returns:

<a class="codehl codehl_obj" href="api.md#api-objects"><b>API</b></a>: Return a copy of the api with random device data





