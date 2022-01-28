<!-- vim: syntax=Markdown -->

# TDesktop

<a id="td.tdesktop.TDesktop"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDesktop</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/tdesktop.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class TDesktop(BaseObject)
```

Telegram Desktop client.<br>
A client can have multiple accounts, up to 3 - according to official Telegram Desktop client.
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <a class="codehl codehl_name" href="tdesktop.md#api"><b>api</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api.md#class-api"><b>API</b></a> | The API this client is using. |
| <a class="codehl codehl_name" href="tdesktop.md#accountscount"><b>accountsCount</b></a> | <span class="highlight"><span class="bp">int</span></span> | The numbers of accounts in this client. |
| <a class="codehl codehl_name" href="tdesktop.md#accounts"><b>accounts</b></a> | <span class="highlight"><span class="nc">List</span></span>[<a class="codehl codehl_obj" href="../telegram-desktop/account.md#class-account"><b>Account</b></a>] | List of accounts in this client. |
| <a class="codehl codehl_name" href="tdesktop.md#mainaccount"><b>mainAccount</b></a> | <a class="codehl codehl_obj" href="../telegram-desktop/account.md#class-account"><b>Account</b></a> | The main account of this client. |
| <a class="codehl codehl_name" href="tdesktop.md#basepath"><b>basePath</b></a> | <span class="highlight"><span class="bp">str</span></span> | The path to <span class="highlight"><span class="n">tdata</span></span> <span class="highlight"><span class="n">folder</span></span>. |
| <a class="codehl codehl_name" href="tdesktop.md#passcode"><b>passcode</b></a> | <span class="highlight"><span class="bp">str</span></span> | Passcode of the client, the same as Local Passcode on <span class="highlight"><span class="n">Telegram</span></span> <span class="highlight"><span class="n">Desktop</span></span>.<br/>Use to encrypt and decrypt <span class="highlight"><span class="n">tdata</span></span> <span class="highlight"><span class="n">files</span></span>. |
| <a class="codehl codehl_name" href="tdesktop.md#appversion"><b>AppVersion</b></a> | <span class="highlight"><span class="bp">int</span></span> | App version of the client. |
| <a class="codehl codehl_name" href="tdesktop.md#kmaxaccounts"><b>kMaxAccounts</b></a> | <span class="highlight"><span class="bp">int</span></span> | See <a class="codehl codehl_name" href="tdesktop.md#kmaxaccounts"><b>kMaxAccounts</b></a>. |
| <a class="codehl codehl_name" href="tdesktop.md#keyfile"><b>keyFile</b></a> | <span class="highlight"><span class="bp">str</span></span> | See <a class="codehl codehl_name" href="tdesktop.md#keyfile"><b>keyFile</b></a>. |
| <a class="codehl codehl_name" href="tdesktop.md#kdefaultkeyfile"><b>kDefaultKeyFile</b></a> | <span class="highlight"><span class="bp">str</span></span> | Default value for <a class="codehl codehl_name" href="tdesktop.md#keyfile"><b>keyFile</b></a>. |
| <a class="codehl codehl_name" href="tdesktop.md#kperformancemode"><b>kPerformanceMode</b></a> | <span class="highlight"><span class="bp">bool</span></span> | Performance mode. When enabled, <span class="highlight"><span class="nf">SavaTData</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> will be 200x faster.<br/>See <a class="codehl codehl_name" href="tdesktop.md#kperformancemode"><b>kPerformanceMode</b></a>. |

<h3>Methods:</h3>

- <a class="codehl codehl_function" href="tdesktop.md#loadtdata"><b>LoadTData</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span><span class="highlight"><span class="p">:</span></span>\
Load the client from <span class="highlight"><span class="n">tdata</span></span> <span class="highlight"><span class="n">folder</span></span>. <br>
Use this if you didn't set the <a class="codehl codehl_name" href="tdesktop.md#basepath"><b>basePath</b></a> when initializing the client.
- <a class="codehl codehl_function" href="tdesktop.md#savetdata"><b>SaveTData</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span><span class="highlight"><span class="p">:</span></span>\
Save the client session to <span class="highlight"><span class="n">tdata</span></span> <span class="highlight"><span class="n">folder</span></span> - which can be used by <span class="highlight"><span class="n">Telegram</span></span> <span class="highlight"><span class="n">Desktop</span></span>.
- <a class="codehl codehl_function" href="tdesktop.md#isloaded"><b>isLoaded</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span><span class="highlight"><span class="p">:</span></span>\
Return <span class="highlight"><span class="kc">True</span></span> if the client has successfully loaded accounts from <span class="highlight"><span class="n">tdata</span></span> or <a class="codehl codehl_obj" href="../../documentation/telethon/telegramclient.md#class-telegramclient"><b>TelegramClient</b></a>.
- <a class="codehl codehl_function" href="tdesktop.md#totelethon"><b>ToTelethon</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span><span class="highlight"><span class="p">:</span></span>\
Convert this session to <a class="codehl codehl_obj" href="../../documentation/telethon/telegramclient.md#class-telegramclient"><b>TelegramClient</b></a>.
- <a class="codehl codehl_function" href="tdesktop.md#fromtelethon"><b>FromTelethon</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span><span class="highlight"><span class="p">:</span></span>\
Create a new session from <a class="codehl codehl_obj" href="../../documentation/telethon/telegramclient.md#class-telegramclient"><b>TelegramClient</b></a>.
- <a class="codehl codehl_function" href="tdesktop.md#performancemode"><b>PerformanceMode</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span><span class="highlight"><span class="p">:</span></span>\
Enable/disable performance mode. When enabled, <span class="highlight"><span class="nf">SavaTData</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> will be 5000x faster.



<a id="td.tdesktop.TDesktop.__init__"></a>


---
### <span class="highlight"><span class="nc">TDesktop</span></span><span class="highlight"><span class="o">()</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/tdesktop.py#L102"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
def __init__(basePath: str = None, api: Union[Type[APIData], APIData] = API.TelegramDesktop, passcode: str = None, keyFile: str = None) -> None
```

Initialize a <a class="codehl codehl_obj" href="tdesktop.md#class-tdesktop"><b>TDesktop</b></a> client<br>
<h3>Arguments:</h3>

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <a class="codehl codehl_name" href="tdesktop.md#basepath"><b>basePath</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | The path to the <span class="highlight"><span class="n">tdata</span></span> <span class="highlight"><span class="n">folder</span></span>.<br/>If the path doesn't exists or its data is corrupted, a new instance will be created. |
| <a class="codehl codehl_name" href="tdesktop.md#api"><b>api</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api.md#class-api"><b>API</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api.md#class-telegramdesktop"><b>TelegramDesktop</b></a> | Which API to use. Read more <a class="codehl codehl_obj" href="../../documentation/authorization/api.md#class-api"><b>here</b></a>. |
| <a class="codehl codehl_name" href="tdesktop.md#passcode"><b>passcode</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | The passcode for tdata, same as the Local Passcode on <span class="highlight"><span class="n">Telegram</span></span> <span class="highlight"><span class="n">Desktop</span></span>. |
| <a class="codehl codehl_name" href="tdesktop.md#keyfile"><b>keyFile</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">data</span></span><span class="highlight"><span class="s2">"</span></span> | See <a class="codehl codehl_name" href="tdesktop.md#keyfile"><b>keyFile</b></a>. |



<a id="td.tdesktop.TDesktop.isLoaded"></a>


---
### <span class="highlight"><span class="nf">isLoaded</span></span><span class="highlight"><span class="o">()</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/tdesktop.py#L143"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
def isLoaded() -> bool
```

Return <span class="highlight"><span class="kc">True</span></span> if the client has successfully loaded accounts from <span class="highlight"><span class="n">tdata</span></span> or <a class="codehl codehl_obj" href="../../documentation/telethon/telegramclient.md#class-telegramclient"><b>TelegramClient</b></a><br>


<a id="td.tdesktop.TDesktop.LoadTData"></a>


---
### <span class="highlight"><span class="nf">LoadTData</span></span><span class="highlight"><span class="o">()</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/tdesktop.py#L149"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
def LoadTData(basePath: str = None, passcode: str = None, keyFile: str = None)
```

Loads accounts from <span class="highlight"><span class="n">tdata</span></span> <span class="highlight"><span class="n">folder</span></span><br>
<h3>Arguments:</h3>

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <a class="codehl codehl_name" href="tdesktop.md#basepath"><b>basePath</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | The path to the folder. |
| <a class="codehl codehl_name" href="tdesktop.md#passcode"><b>passcode</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | Read more <a class="codehl codehl_name" href="tdesktop.md#passcode"><b>here</b></a>. |
| <a class="codehl codehl_name" href="tdesktop.md#keyfile"><b>keyFile</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | Read more <a class="codehl codehl_name" href="tdesktop.md#keyfile"><b>here</b></a>. |

<h3>Raises:</h3>

<a class="codehl codehl_obj" href="../../documentation/exceptions/home.md#class-tdatabaddecryptkey"><b>TDataBadDecryptKey</b></a> : The <span class="highlight"><span class="n">tdata</span></span> <span class="highlight"><span class="n">folder</span></span> is password-encrypted, please the set the argument <a class="codehl codehl_name" href="tdesktop.md#passcode"><b>passcode</b></a> to decrypt it.


| :warning: This function is not recommended to use |
| :--- |
|     You should load tdata using <a class="codehl codehl_obj" href="tdesktop.md#class-tdesktop"><b>TDesktop</b></a><span class="highlight"><span class="o">(</span></span><a class="codehl codehl_name" href="tdesktop.md#basepath"><b>basePath</b></a><span class="highlight"><span class="o">=</span></span><span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">path</span></span><span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="p">)</span></span>.<br/>    Don't manually load tdata using this function, bugs might pop up out of nowhere. |

<h3>Examples:</h3>

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


<a id="td.tdesktop.TDesktop.SaveTData"></a>


---
### <span class="highlight"><span class="nf">SaveTData</span></span><span class="highlight"><span class="o">()</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/tdesktop.py#L220"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
def SaveTData(basePath: str = None, passcode: str = None, keyFile: str = None) -> bool
```

Save the client session to a folder.<br>
<h3>Arguments:</h3>

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <a class="codehl codehl_name" href="tdesktop.md#basepath"><b>basePath</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | Path to the folder<br/>If None then the data will be saved at the basePath given at creation. |
| <a class="codehl codehl_name" href="tdesktop.md#passcode"><b>passcode</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | Read more <a class="codehl codehl_name" href="tdesktop.md#passcode"><b>here</b></a>. |
| <a class="codehl codehl_name" href="tdesktop.md#keyfile"><b>keyFile</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | Read more <a class="codehl codehl_name" href="tdesktop.md#keyfile"><b>here</b></a>. |

<h3>Examples:</h3>

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


<a id="td.tdesktop.TDesktop.ToTelethon"></a>


---
### <span class="highlight"><span class="nf">ToTelethon</span></span><span class="highlight"><span class="o">()</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/tdesktop.py#L474"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
@typing.overload
async def ToTelethon(session: Union[str, Session] = None, flag: Type[LoginFlag] = CreateNewSession, api: Union[Type[APIData], APIData] = API.TelegramDesktop, password: str = None) -> tl.TelegramClient
```

<h3>Arguments:</h3>

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <span class="highlight"><span class="n">session</span></span> | <span class="highlight"><span class="bp">str</span></span>, <span class="highlight"><span class="nc">Session</span></span> | <span class="highlight"><span class="kc">None</span></span> | The file name of the <span class="highlight"><span class="n">session</span></span> <span class="highlight"><span class="n">file</span></span> to be used, if <span class="highlight"><span class="kc">None</span></span> then the session will not be saved.<br/>Read more [here](https://docs.telethon.dev/en/latest/concepts/sessions.html?highlight=session#what-are-sessions). |
| <span class="highlight"><span class="n">flag</span></span> | <a class="codehl codehl_obj" href="../../documentation/authorization/loginflag.md#class-loginflag"><b>LoginFlag</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/loginflag.md#class-createnewsession"><b>CreateNewSession</b></a> | The login flag. Read more <a class="codehl codehl_obj" href="../../documentation/authorization/loginflag.md#class-loginflag"><b>here</b></a>. |
| <a class="codehl codehl_name" href="tdesktop.md#api"><b>api</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api.md#class-apidata"><b>APIData</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api.md#class-telegramdesktop"><b>TelegramDesktop</b></a> | Which API to use. Read more <a class="codehl codehl_obj" href="../../documentation/authorization/api.md#class-api"><b>here</b></a>. |
| <span class="highlight"><span class="n">password</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | Two-step verification password if needed. |

<h3>Returns:</h3>


- Return an instance of <a class="codehl codehl_obj" href="../../documentation/telethon/telegramclient.md#class-telegramclient"><b>TelegramClient</b></a> on success

<h3>Examples:</h3>

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


<a id="td.tdesktop.TDesktop.FromTelethon"></a>


---
### <span class="highlight"><span class="nf">FromTelethon</span></span><span class="highlight"><span class="o">()</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/tdesktop.py#L570"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
@staticmethod
async def FromTelethon(telethonClient: tl.TelegramClient, flag: Type[LoginFlag] = CreateNewSession, api: Union[Type[APIData], APIData] = API.TelegramDesktop, password: str = None) -> TDesktop
```

Create an instance of <a class="codehl codehl_obj" href="tdesktop.md#class-tdesktop"><b>TDesktop</b></a> from <a class="codehl codehl_obj" href="../../documentation/telethon/telegramclient.md#class-telegramclient"><b>TelegramClient</b></a>.<br>
<h3>Arguments:</h3>

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <span class="highlight"><span class="n">telethonClient</span></span> | <a class="codehl codehl_obj" href="../../documentation/telethon/telegramclient.md#class-telegramclient"><b>TelegramClient</b></a> |  | The <a class="codehl codehl_obj" href="../../documentation/telethon/telegramclient.md#class-telegramclient"><b>TelegramClient</b></a> you want to convert from. |
| <span class="highlight"><span class="n">flag</span></span> | <a class="codehl codehl_obj" href="../../documentation/authorization/loginflag.md#class-loginflag"><b>LoginFlag</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/loginflag.md#class-createnewsession"><b>CreateNewSession</b></a> | The login flag. Read more <a class="codehl codehl_obj" href="../../documentation/authorization/loginflag.md#class-loginflag"><b>here</b></a>. |
| <a class="codehl codehl_name" href="tdesktop.md#api"><b>api</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api.md#class-apidata"><b>APIData</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api.md#class-api"><b>API</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_obj" href="../../documentation/authorization/api.md#class-telegramdesktop"><b>TelegramDesktop</b></a> | Which API to use. Read more <a class="codehl codehl_obj" href="../../documentation/authorization/api.md#class-api"><b>here</b></a>. |
| <span class="highlight"><span class="n">password</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | Two-step verification password if needed. |

<h3>Examples:</h3>

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


<a id="td.tdesktop.TDesktop.PerformanceMode"></a>


---
### <span class="highlight"><span class="nf">PerformanceMode</span></span><span class="highlight"><span class="o">()</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/tdesktop.py#L625"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
@classmethod
def PerformanceMode(cls, enabled: bool = True)
```

Enable or disable performance mode. See <a class="codehl codehl_name" href="tdesktop.md#kperformancemode"><b>kPerformanceMode</b></a>.<br>
It is enabled by default.<br>
<h3>Arguments:</h3>

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <span class="highlight"><span class="n">enabled</span></span> | <span class="highlight"><span class="bp">bool</span></span> | <span class="highlight"><span class="kc">True</span></span> | Either enable or disable performance mode. |



<a id="td.tdesktop.TDesktop.kMaxAccounts"></a>


---
### <span class="highlight"><span class="n">kMaxAccounts</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/tdesktop.py#L637"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

The maximum amount of accounts a client can have<br>


<a id="td.tdesktop.TDesktop.kDefaultKeyFile"></a>


---
### <span class="highlight"><span class="n">kDefaultKeyFile</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/tdesktop.py#L640"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

See <a class="codehl codehl_obj" href="tdesktop.md#class-tdesktop"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_name" href="tdesktop.md#keyfile"><b>keyFile</b></a><br>


<a id="td.tdesktop.TDesktop.kPerformanceMode"></a>


---
### <span class="highlight"><span class="n">kPerformanceMode</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/tdesktop.py#L643"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

When enabled, <a class="codehl codehl_function" href="tdesktop.md#savetdata"><b>SaveTData</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> will be 5000x faster.<br>

- What it does is using a constant <a class="codehl codehl_name" href="tdesktop.md#localkey"><b>localKey</b></a> rather than generating it everytime when saving tdata.

- The average time for generating <a class="codehl codehl_name" href="tdesktop.md#localkey"><b>localKey</b></a> is about <span class="highlight"><span class="mi">250</span></span> to <span class="highlight"><span class="mi">350</span></span> ms, depend on your CPU.

- When in performance mode, the average time to generate <a class="codehl codehl_name" href="tdesktop.md#localkey"><b>localKey</b></a> is <span class="highlight"><span class="mf">0.0628</span></span> ms. Which is 5000x faster

- Of course this comes with a catch, your <span class="highlight"><span class="n">tdata</span></span> <span class="highlight"><span class="n">files</span></span> will always use a same constant <a class="codehl codehl_name" href="tdesktop.md#localkey"><b>localKey</b></a>. Basicly no protection at all, but who cares?

| :blue_book: Note |
| :--- |
|     Performance mode will be disabled if <a class="codehl codehl_name" href="tdesktop.md#passcode"><b>passcode</b></a> is set. |



<a id="td.tdesktop.TDesktop.api"></a>


---
### <span class="highlight"><span class="n">api</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/tdesktop.py#L656"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
@property
def api() -> APIData
```

The API this client is using.<br>


<a id="td.tdesktop.TDesktop.basePath"></a>


---
### <span class="highlight"><span class="n">basePath</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/tdesktop.py#L669"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
@property
def basePath() -> Optional[str]
```

Base folder of <a class="codehl codehl_obj" href="tdesktop.md#class-tdesktop"><b>TDesktop</b></a>, this is where data stored<br>
Same as tdata folder of <span class="highlight"><span class="n">Telegram</span></span> <span class="highlight"><span class="n">Desktop</span></span><br>


<a id="td.tdesktop.TDesktop.passcode"></a>


---
### <span class="highlight"><span class="n">passcode</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/tdesktop.py#L677"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
@property
def passcode() -> str
```

Passcode used to encrypt and decrypt data<br>
Same as the Local Passcode of <span class="highlight"><span class="n">Telegram</span></span> <span class="highlight"><span class="n">Desktop</span></span><br>


<a id="td.tdesktop.TDesktop.keyFile"></a>


---
### <span class="highlight"><span class="n">keyFile</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/tdesktop.py#L685"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
@property
def keyFile() -> str
```

The default value is <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">data</span></span><span class="highlight"><span class="s2">"</span></span>, this argument is rarely ever used.<br>
It is used by <span class="highlight"><span class="n">Telegram</span></span> <span class="highlight"><span class="n">Desktop</span></span> by running it with the <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">-key</span></span><span class="highlight"><span class="s2">"</span></span> argument.
I don't know what's the use cases of it, maybe this was a legacy feature of <span class="highlight"><span class="n">Telegram</span></span> <span class="highlight"><span class="n">Desktop</span></span>.<br>


<a id="td.tdesktop.TDesktop.localKey"></a>


---
### <span class="highlight"><span class="n">localKey</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/tdesktop.py#L698"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
@property
def localKey() -> Optional[td.AuthKey]
```

The key used to encrypt/decrypt data<br>


<a id="td.tdesktop.TDesktop.AppVersion"></a>


---
### <span class="highlight"><span class="n">AppVersion</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/tdesktop.py#L705"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
@property
def AppVersion() -> Optional[int]
```

App version of TDesktop client<br>


<a id="td.tdesktop.TDesktop.accountsCount"></a>


---
### <span class="highlight"><span class="n">accountsCount</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/tdesktop.py#L717"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
@property
def accountsCount() -> int
```

The number of accounts this client has<br>


<a id="td.tdesktop.TDesktop.accounts"></a>


---
### <span class="highlight"><span class="n">accounts</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/tdesktop.py#L725"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
@property
def accounts() -> List[td.Account]
```

List of accounts this client has\n<br>
If you want to get the main account, please use .mainAccount instead<br>


<a id="td.tdesktop.TDesktop.mainAccount"></a>


---
### <span class="highlight"><span class="n">mainAccount</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/tdesktop.py#L733"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
@property
def mainAccount() -> Optional[td.Account]
```

The main account of the client<br>


