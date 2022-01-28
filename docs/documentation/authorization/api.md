<!-- vim: syntax=Markdown -->

# API

<a id="api.APIData"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">APIData</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/api.py#L58" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
class APIData(object, metaclass=BaseAPIMetaClass)
```

API configuration to connect to <a class="codehl codehl_obj" href="../../telethon/telegramclient#tl.telethon.TelegramClient"><b>TelegramClient</b></a> and <a class="codehl codehl_obj" href="../../telegram-desktop/tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a><br>
<h3>Attributes:</h3>

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

<h3>Methods:</h3>

- <a class="codehl codehl_function" href="#api.APIData.Generate"><b>Generate</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> <span class="highlight"><span class="p">:</span></span> \
Generate random device model and system version



<a id="api.APIData.__init__"></a>


---
### <span class="highlight"><span class="nc">APIData</span></span><span class="highlight"><span class="o">()</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/api.py#L107" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
@typing.overload
def __init__(api_id: int, api_hash: str, device_model: str = None, system_version: str = None, app_version: str = None, lang_code: str = None, system_lang_code: str = None, lang_pack: str = None) -> None
```

Create your own customized API<br>
<h3>Arguments:</h3>

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



<a id="api.APIData.Generate"></a>


---
### <span class="highlight"><span class="nf">Generate</span></span><span class="highlight"><span class="o">()</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/api.py#L250" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
@classmethod
def Generate(cls: Type[_T], unique_id: str = None) -> _T
```

Generate random device model and system version<br>
<h3>Arguments:</h3>

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <span class="highlight"><span class="n">unique_id</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | The unique ID to generate - can be anything.<br/>This will be used to ensure that it will generate the same data everytime.<br/>If not set then the data will be randomized each time we runs it. |

<h3>Raises:</h3>

<span class="highlight"><span class="ne">NotImplementedError</span></span> : Not supported for web browser yet

<h3>Returns:</h3>

<a class="codehl codehl_obj" href="#api.APIData"><b>APIData</b></a> : Return a copy of the api with random device data

<h3>Examples:</h3>

Create a <a class="codehl codehl_obj" href="../../telethon/telegramclient#tl.telethon.TelegramClient"><b>TelegramClient</b></a> with custom API:

```python
api = API.TelegramIOS.Generate(unique_id="new.session")
client = TelegramClient(session="new.session" api=api)
client.start()
```


<a id="api.API"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">API</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/api.py#L299" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
class API(BaseObject)
```

<h4>Built-in templates for Telegram API</h4>


- **<span class="highlight"><span class="n">opentele</span></span>** offers the ability to use **<span class="highlight"><span class="n">official</span></span> <span class="highlight"><span class="n">APIs</span></span>**, which are used by <span class="highlight"><span class="n">official</span></span> <span class="highlight"><span class="n">apps</span></span>.

- According to [Telegram TOS](https://core.telegram.org/api/obtaining_api_id#using-the-api-id) : *all accounts that sign up or log in using unofficial Telegram API clients are automatically put under observation to avoid violations of the Terms of Service*.

- It also uses the **[lang_pack](https://core.telegram.org/method/initConnection)** parameter, of which [telethon can't use](https://github.com/LonamiWebs/Telethon/blob/master/telethon/_client/telegrambaseclient.py#L192) because it's for official apps only.

- Therefore, **there are no differences** between using <span class="highlight"><span class="n">opentele</span></span> and <span class="highlight"><span class="n">official</span></span> <span class="highlight"><span class="n">apps</span></span>, the server can't tell you apart.

- You can use <a class="codehl codehl_obj" href="../../telethon/telegramclient#tl.telethon.TelegramClient"><b>TelegramClient</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_function" href="../../telethon/telegramclient#tl.telethon.TelegramClient.PrintSessions"><b>PrintSessions</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> to check this out.
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <a class="codehl codehl_obj" href="#api.API.TelegramDesktop"><b>TelegramDesktop</b></a> | <a class="codehl codehl_obj" href="#api.API"><b>API</b></a> | Official Telegram for Desktop (Windows, macOS and Linux)[View on GitHub](https://github.com/telegramdesktop/tdesktop) |
| <a class="codehl codehl_obj" href="#api.API.TelegramAndroid"><b>TelegramAndroid</b></a> | <a class="codehl codehl_obj" href="#api.API"><b>API</b></a> | Official Telegram for Android [View on GitHub](https://github.com/DrKLO/Telegram) |
| <a class="codehl codehl_obj" href="#api.API.TelegramAndroidX"><b>TelegramAndroidX</b></a> | <a class="codehl codehl_obj" href="#api.API"><b>API</b></a> | Official TelegramX for Android [View on GitHub](https://github.com/DrKLO/Telegram) |
| <a class="codehl codehl_obj" href="#api.API.TelegramIOS"><b>TelegramIOS</b></a> | <a class="codehl codehl_obj" href="#api.API"><b>API</b></a> | Official Telegram for iOS [View on GitHub](https://github.com/TelegramMessenger/Telegram-iOS) |
| <a class="codehl codehl_obj" href="#api.API.TelegramMacOS"><b>TelegramMacOS</b></a> | <a class="codehl codehl_obj" href="#api.API"><b>API</b></a> | Official Telegram-Swift For MacOS [View on GitHub](https://github.com/overtake/TelegramSwift) |
| <a class="codehl codehl_obj" href="#api.API.TelegramWeb_Z"><b>TelegramWeb_Z</b></a> | <a class="codehl codehl_obj" href="#api.API"><b>API</b></a> | Default Official Telegram Web Z For Browsers [View on GitHub](https://github.com/Ajaxy/telegram-tt)| [Visit on Telegram](https://web.telegram.org/z/) |
| <a class="codehl codehl_obj" href="#api.API.TelegramWeb_K"><b>TelegramWeb_K</b></a> | <a class="codehl codehl_obj" href="#api.API"><b>API</b></a> | Official Telegram Web K For Browsers [View on GitHub](https://github.com/morethanwords/tweb)| [Visit on Telegram](https://web.telegram.org/k/) |
| <a class="codehl codehl_obj" href="#api.API.Webogram"><b>Webogram</b></a> | <a class="codehl codehl_obj" href="#api.API"><b>API</b></a> | Old Telegram For Browsers [View on GitHub](https://github.com/zhukov/webogram)| [Vist on Telegram](https://web.telegram.org/?legacy=1#/im) |



<a id="api.API.TelegramDesktop"></a>


---
### <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TelegramDesktop</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/api.py#L334" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
class TelegramDesktop(APIData)
```

Official Telegram for Desktop (Windows, macOS and Linux)
[View on GitHub](https://github.com/telegramdesktop/tdesktop)
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">api_id</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">2040</span></span> |
| <span class="highlight"><span class="n">api_hash</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">b18441a1ff607e10a989891a5462e627</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">device_model</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">Desktop</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">Windows 10</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">app_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">3.4.3 x64</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en-US</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_pack</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">tdesktop</span></span><span class="highlight"><span class="s2">"</span></span> |

<h3>Methods:</h3>

- <a class="codehl codehl_function" href="#api.API.TelegramDesktop.Generate"><b>Generate</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> <span class="highlight"><span class="p">:</span></span> \
Generate random device data for <span class="highlight"><span class="n">Windows</span></span>, <span class="highlight"><span class="n">macOS</span></span> and <span class="highlight"><span class="n">Linux</span></span>



<a id="api.API.TelegramDesktop.Generate"></a>


---
#### <span class="highlight"><span class="nf">Generate</span></span><span class="highlight"><span class="o">()</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/api.py#L364" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
@typing.overload
@classmethod
def Generate(cls: Type[_T], system: str = "windows", unique_id: str = None) -> _T
```

Generate random TelegramDesktop devices<br>
<h3>Arguments:</h3>

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <span class="highlight"><span class="n">system</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">random</span></span><span class="highlight"><span class="s2">"</span></span> | Which OS to generate, either <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">windows</span></span><span class="highlight"><span class="s2">"</span></span>, <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">macos</span></span><span class="highlight"><span class="s2">"</span></span>, or <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">linux</span></span><span class="highlight"><span class="s2">"</span></span>.<br/>Default is <span class="highlight"><span class="kc">None</span></span> or <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">random</span></span><span class="highlight"><span class="s2">"</span></span>  -  which means it will be selected randomly. |
| <span class="highlight"><span class="n">unique_id</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | The unique ID to generate - can be anything.<br/>This ID will be used to ensure that it will generate the same data every single time.<br/>If not set then the data will be randomized each time we runs it. |

<h3>Returns:</h3>

<a class="codehl codehl_obj" href="#api.APIData"><b>APIData</b></a> : Return a copy of the api with random device data

<h3>Examples:</h3>

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


<a id="api.API.TelegramAndroid"></a>


---
### <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TelegramAndroid</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/api.py#L442" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
class TelegramAndroid(APIData)
```

Official Telegram for Android<br>
[View on GitHub](https://github.com/DrKLO/Telegram)
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">api_id</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">6</span></span> |
| <span class="highlight"><span class="n">api_hash</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">eb06d4abfb49dc3eeb1aeb98ae0f581e</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">device_model</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">Samsung SM-G998B</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">SDK 31</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">app_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">8.4.1 (2522)</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en-US</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_pack</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">android</span></span><span class="highlight"><span class="s2">"</span></span> |



<a id="api.API.TelegramAndroidX"></a>


---
### <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TelegramAndroidX</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/api.py#L467" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
class TelegramAndroidX(APIData)
```

Official TelegramX for Android<br>
[View on GitHub](https://github.com/DrKLO/Telegram)
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">api_id</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">21724</span></span> |
| <span class="highlight"><span class="n">api_hash</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">3e0cb5efcd52300aec5994fdfc5bdc16</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">device_model</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">Samsung SM-G998B</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">SDK 31</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">app_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">8.4.1 (2522)</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en-US</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_pack</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">android</span></span><span class="highlight"><span class="s2">"</span></span> |



<a id="api.API.TelegramIOS"></a>


---
### <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TelegramIOS</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/api.py#L492" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
class TelegramIOS(APIData)
```

Official Telegram for iOS<br>
[View on GitHub](https://github.com/TelegramMessenger/Telegram-iOS)
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">api_id</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">10840</span></span> |
| <span class="highlight"><span class="n">api_hash</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">33c45224029d59cb3ad0c16134215aeb</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">device_model</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">iPhone 13 Pro Max</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">14.8.1</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">app_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">8.4</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en-US</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_pack</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">ios</span></span><span class="highlight"><span class="s2">"</span></span> |



<a id="api.API.TelegramMacOS"></a>


---
### <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TelegramMacOS</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/api.py#L519" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
class TelegramMacOS(APIData)
```

Official Telegram-Swift For MacOS
[View on GitHub](https://github.com/overtake/TelegramSwift)
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">api_id</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">2834</span></span> |
| <span class="highlight"><span class="n">api_hash</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">68875f756c9b437a8b916ca3de215815</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">device_model</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">MacBook Pro</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">macOS 12.0.1</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">app_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">8.4</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en-US</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_pack</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">macos</span></span><span class="highlight"><span class="s2">"</span></span> |



<a id="api.API.TelegramWeb_Z"></a>


---
### <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TelegramWeb_Z</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/api.py#L546" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
class TelegramWeb_Z(APIData)
```

Default Official Telegram Web Z For Browsers<br>
[View on GitHub](https://github.com/Ajaxy/telegram-tt)| [Visit on Telegram](https://web.telegram.org/z/)
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">api_id</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">2496</span></span> |
| <span class="highlight"><span class="n">api_hash</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">8da85b0d5bfe62527e5b244c209159c3</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">device_model</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">Windows</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">app_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">1.28.3 Z</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en-US</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_pack</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">"</span></span> |



<a id="api.API.TelegramWeb_K"></a>


---
### <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TelegramWeb_K</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/api.py#L572" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
class TelegramWeb_K(APIData)
```

Official Telegram Web K For Browsers<br>
[View on GitHub](https://github.com/morethanwords/tweb)| [Visit on Telegram](https://web.telegram.org/k/)
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">api_id</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">2496</span></span> |
| <span class="highlight"><span class="n">api_hash</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">8da85b0d5bfe62527e5b244c209159c3</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">device_model</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">Win32</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">app_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">1.0.1 K</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en-US</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_pack</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">macos</span></span><span class="highlight"><span class="s2">"</span></span> |



<a id="api.API.Webogram"></a>


---
### <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">Webogram</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/api.py#L597" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
class Webogram(APIData)
```

Old Telegram For Browsers<br>
[View on GitHub](https://github.com/zhukov/webogram)| [Vist on Telegram](https://web.telegram.org/?legacy=1#/im)
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">api_id</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">2496</span></span> |
| <span class="highlight"><span class="n">api_hash</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">8da85b0d5bfe62527e5b244c209159c3</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">device_model</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">Win32</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">app_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">0.7.0</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en-US</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_pack</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">"</span></span> |



