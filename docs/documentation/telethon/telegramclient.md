<!-- vim: syntax=Markdown -->

# TelegramClient

<a id="tl.telethon.TelegramClient"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TelegramClient</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/tl/telethon.py#L66" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
@extend_class
class TelegramClient(telethon.TelegramClient,  BaseObject)
```

Extended version of [telethon.TelegramClient](https://github.com/LonamiWebs/Telethon/blob/master/telethon/_client/telegramclient.py#L23)
<h3>Methods:</h3>

- <a class="codehl codehl_function" href="#tl.telethon.TelegramClient.FromTDesktop"><b>FromTDesktop</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span><span class="highlight"><span class="p">:</span></span>\
Create an instance of <a class="codehl codehl_obj" href="#tl.telethon.TelegramClient"><b>TelegramClient</b></a> from <a class="codehl codehl_obj" href="../../telegram-desktop/tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a>.
- <a class="codehl codehl_function" href="#tl.telethon.TelegramClient.ToTDesktop"><b>ToTDesktop</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span><span class="highlight"><span class="p">:</span></span>\
Convert this <a class="codehl codehl_obj" href="#tl.telethon.TelegramClient"><b>TelegramClient</b></a> instance to <a class="codehl codehl_obj" href="../../telegram-desktop/tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a>.
- <a class="codehl codehl_function" href="#tl.telethon.TelegramClient.QRLoginToNewClient"><b>QRLoginToNewClient</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span><span class="highlight"><span class="p">:</span></span>\
Return <span class="highlight"><span class="kc">True</span></span> if logged-in using an <a class="codehl codehl_obj" href="../../authorization/api#api.API"><b>official API</b></a>.
- <a class="codehl codehl_function" href="#tl.telethon.TelegramClient.GetSessions"><b>GetSessions</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span><span class="highlight"><span class="p">:</span></span>\
Get all logged in sessions.
- <a class="codehl codehl_function" href="#tl.telethon.TelegramClient.GetCurrentSession"><b>GetCurrentSession</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span><span class="highlight"><span class="p">:</span></span>\
Get current logged-in session.
- <a class="codehl codehl_function" href="#tl.telethon.TelegramClient.TerminateSession"><b>TerminateSession</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span><span class="highlight"><span class="p">:</span></span>\
Terminate a specific session.
- <a class="codehl codehl_function" href="#tl.telethon.TelegramClient.TerminateAllSessions"><b>TerminateAllSessions</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span><span class="highlight"><span class="p">:</span></span>\
Terminate all other sessions.
- <a class="codehl codehl_function" href="#tl.telethon.TelegramClient.PrintSessions"><b>PrintSessions</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span><span class="highlight"><span class="p">:</span></span>\
Pretty-print all logged-in sessions.
- <a class="codehl codehl_function" href="#tl.telethon.TelegramClient.is_official_app"><b>is_official_app</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span><span class="highlight"><span class="p">:</span></span>\
Return <span class="highlight"><span class="kc">True</span></span> if logged-in using an <a class="codehl codehl_obj" href="../../authorization/api#api.API"><b>official API</b></a>.



<a id="tl.telethon.TelegramClient.__init__"></a>


---
### <span class="highlight"><span class="nc">TelegramClient</span></span><span class="highlight"><span class="o">()</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/tl/telethon.py#L101" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
@typing.overload
def __init__(session: Union[str, Session] = None, api: Union[Type[APIData], APIData] = API.TelegramDesktop)
```

Start TelegramClient with customized api.<br>
Read more at [opentele GitHub](https://github.com/thedemons/opentele#authorization)
<h3>Arguments:</h3>

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <span class="highlight"><span class="n">session</span></span> | <span class="highlight"><span class="bp">str</span></span>, <span class="highlight"><span class="nc">Session</span></span> |  | The file name of the <span class="highlight"><span class="n">session</span></span> <span class="highlight"><span class="n">file</span></span> to be used, if a string is<br/>given (it may be a full path), or the <span class="highlight"><span class="nc">Session</span></span> instance to be used<br/>Otherwise, if it's <span class="highlight"><span class="kc">None</span></span>, the <span class="highlight"><span class="n">session</span></span> will not be saved,<br/>and you should call method <span class="highlight"><span class="o">.</span></span><span class="highlight"><span class="nf">log_out</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> when you're done.<br/>Read more [here](https://docs.telethon.dev/en/latest/concepts/sessions.html?highlight=session#what-are-sessions). |
| <a class="codehl codehl_name" href="../../telegram-desktop/account#td.account.Account.api"><b>api</b></a> | <a class="codehl codehl_obj" href="../../authorization/api#api.API"><b>API</b></a> | <a class="codehl codehl_obj" href="../../authorization/api#api.API.TelegramDesktop"><b>TelegramDesktop</b></a> | Which API to use. Read more <a class="codehl codehl_obj" href="../../authorization/api#api.API"><b>here</b></a>. |



<a id="tl.telethon.TelegramClient.GetSessions"></a>


---
### <span class="highlight"><span class="nf">GetSessions</span></span><span class="highlight"><span class="o">()</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/tl/telethon.py#L355" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
async def GetSessions() -> Optional[types.account.Authorizations]
```

Get all logged-in sessions.
<h3>Returns:</h3>


- Return an instance of <span class="highlight"><span class="n">Authorizations</span></span> on success



<a id="tl.telethon.TelegramClient.GetCurrentSession"></a>


---
### <span class="highlight"><span class="nf">GetCurrentSession</span></span><span class="highlight"><span class="o">()</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/tl/telethon.py#L364" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
async def GetCurrentSession() -> Optional[types.Authorization]
```

Get current logged-in session.
<h3>Returns:</h3>

Return <span class="highlight"><span class="nc">telethon</span></span><span class="highlight"><span class="o">.</span></span><span class="highlight"><span class="nc">types</span></span><span class="highlight"><span class="o">.</span></span><span class="highlight"><span class="nc">Authorization</span></span> on success.<br>
Return <span class="highlight"><span class="kc">None</span></span> on failure.<br>



<a id="tl.telethon.TelegramClient.TerminateSession"></a>


---
### <span class="highlight"><span class="nf">TerminateSession</span></span><span class="highlight"><span class="o">()</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/tl/telethon.py#L380" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
async def TerminateSession(hash: int)
```

Terminate a specific session<br>
<h3>Arguments:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="nb">hash</span></span> | <span class="highlight"><span class="bp">int</span></span> | The <span class="highlight"><span class="n">session</span></span>'s hash to terminate |

<h3>Raises:</h3>

<span class="highlight"><span class="nc">FreshResetAuthorisationForbiddenError</span></span> : You can't log out other <span class="highlight"><span class="n">sessions</span></span> if less than <span class="highlight"><span class="mi">24</span></span> <span class="highlight"><span class="n">hours</span></span> have passed since you logged on to the <span class="highlight"><span class="n">current</span></span> <span class="highlight"><span class="n">session</span></span>.
<span class="highlight"><span class="nc">HashInvalidError</span></span> : The provided hash is invalid.



<a id="tl.telethon.TelegramClient.TerminateAllSessions"></a>


---
### <span class="highlight"><span class="nf">TerminateAllSessions</span></span><span class="highlight"><span class="o">()</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/tl/telethon.py#L404" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
async def TerminateAllSessions() -> bool
```

Terminate all other sessions.<br>


<a id="tl.telethon.TelegramClient.PrintSessions"></a>


---
### <span class="highlight"><span class="nf">PrintSessions</span></span><span class="highlight"><span class="o">()</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/tl/telethon.py#L418" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
async def PrintSessions(sessions: types.account.Authorizations = None)
```

Pretty-print all logged-in sessions.
<h3>Arguments:</h3>

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <span class="highlight"><span class="n">sessions</span></span> | <span class="highlight"><span class="n">Authorizations</span></span> | <span class="highlight"><span class="kc">None</span></span> | <span class="highlight"><span class="n">Sessions</span></span> that return by <a class="codehl codehl_function" href="#tl.telethon.TelegramClient.GetSessions"><b>GetSessions</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span>, if <span class="highlight"><span class="kc">None</span></span> then it will <a class="codehl codehl_function" href="#tl.telethon.TelegramClient.GetSessions"><b>GetSessions</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> first. |

<h3>Returns:</h3>

On success, it should prints the sessions table as the code below.<br>

```
|---------+-----------------------------+----------+----------------+--------+----------------------------+--------------|
|         |           Device            | Platform |     System     | API_ID |          App name          | Official App |
|---------+-----------------------------+----------+----------------+--------+----------------------------+--------------|
| Current |         MacBook Pro         |  macOS   |    10.15.6     |  2834  |     Telegram macOS 8.4     |      ✔       |
|---------+-----------------------------+----------+----------------+--------+----------------------------+--------------|
|    1    |          Chrome 96          | Windows  |                |  2496  |   Telegram Web 1.28.3 Z    |      ✔       |
|    2    |            iMac             |  macOS   |     11.3.1     |  2834  |     Telegram macOS 8.4     |      ✔       |
|    3    |         MacBook Pro         |  macOS   |     10.12      |  2834  |     Telegram macOS 8.4     |      ✔       |
|    4    |       Huawei Y360-U93       | Android  | 7.1 N MR1 (25) | 21724  |  Telegram Android X 8.4.1  |      ✔       |
|    5    |    Samsung Galaxy Spica     | Android  |   6.0 M (23)   |   6    |   Telegram Android 8.4.1   |      ✔       |
|    6    |     Xiaomi Redmi Note 8     | Android  |   10 Q (29)    |   6    |   Telegram Android 8.4.1   |      ✔       |
|    7    | Samsung Galaxy Tab A (2017) | Android  |   7.0 N (24)   |   6    |   Telegram Android 8.4.1   |      ✔       |
|    8    |  Samsung Galaxy XCover Pro  | Android  |   8.0 O (26)   |   6    |   Telegram Android 8.4.1   |      ✔       |
|    9    |          iPhone X           |   iOS    |     13.1.3     | 10840  |      Telegram iOS 8.4      |      ✔       |
|   10    |        iPhone XS Max        |   iOS    |    12.11.0     | 10840  |      Telegram iOS 8.4      |      ✔       |
|   11    |      iPhone 11 Pro Max      |   iOS    |     14.4.2     | 10840  |      Telegram iOS 8.4      |      ✔       |
|---------+-----------------------------+----------+----------------+--------+----------------------------+--------------|
```


<a id="tl.telethon.TelegramClient.is_official_app"></a>


---
### <span class="highlight"><span class="nf">is_official_app</span></span><span class="highlight"><span class="o">()</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/tl/telethon.py#L473" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
async def is_official_app() -> bool
```

Return <span class="highlight"><span class="kc">True</span></span> if this session was logged-in using an official app (<a class="codehl codehl_obj" href="../../authorization/api#api.API"><b>API</b></a>).


<a id="tl.telethon.TelegramClient.QRLoginToNewClient"></a>


---
### <span class="highlight"><span class="nf">QRLoginToNewClient</span></span><span class="highlight"><span class="o">()</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/tl/telethon.py#L482" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
@typing.overload
async def QRLoginToNewClient(session: Union[str, Session] = None, api: Union[Type[APIData], APIData] = API.TelegramDesktop, password: str = None) -> TelegramClient
```

Create a new session using the current session.<br>
<h3>Arguments:</h3>

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <span class="highlight"><span class="n">session</span></span> | <span class="highlight"><span class="bp">str</span></span>, <span class="highlight"><span class="nc">Session</span></span> | <span class="highlight"><span class="kc">None</span></span> | description |
| <a class="codehl codehl_name" href="../../telegram-desktop/account#td.account.Account.api"><b>api</b></a> | <a class="codehl codehl_obj" href="../../authorization/api#api.API"><b>API</b></a> | <a class="codehl codehl_obj" href="../../authorization/api#api.API.TelegramDesktop"><b>TelegramDesktop</b></a> | Which API to use. Read more <a class="codehl codehl_obj" href="../../authorization/api#api.API"><b>here</b></a>. |
| <span class="highlight"><span class="n">password</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | Two-step verification password, set if needed. |

<h3>Raises:</h3>


- <a class="codehl codehl_obj" href="../../exceptions/home#exception.NoPasswordProvided"><b>NoPasswordProvided</b></a> : The account's two-step verification is enabled and no <span class="highlight"><span class="n">password</span></span> was provided. Please set the <span class="highlight"><span class="n">password</span></span> parameters.

- <a class="codehl codehl_obj" href="../../exceptions/home#exception.PasswordIncorrect"><b>PasswordIncorrect</b></a> : The two-step verification <span class="highlight"><span class="n">password</span></span> is incorrect.

- <span class="highlight"><span class="ne">TimeoutError</span></span> : Time out waiting for the client to be authorized.

<h3>Returns:</h3>


- Return an instance of <a class="codehl codehl_obj" href="#tl.telethon.TelegramClient"><b>TelegramClient</b></a> on success.

<h3>Examples:</h3>

Use to current session to authorize a new session:

```python
# Using the API that we've generated before. Please refer to method API.Generate() to learn more.
oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id="old.session")
oldclient = TelegramClient("old.session", api=oldAPI)
await oldClient.connect()

# We can safely authorize the new client with a different API.
newAPI = API.TelegramAndroid.Generate(unique_id="new.session")
newClient = await client.QRLoginToNewClient(session="new.session", api=newAPI)
await newClient.connect()
await newClient.PrintSessions()
```


<a id="tl.telethon.TelegramClient.ToTDesktop"></a>


---
### <span class="highlight"><span class="nf">ToTDesktop</span></span><span class="highlight"><span class="o">()</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/tl/telethon.py#L701" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
async def ToTDesktop(flag: Type[LoginFlag] = CreateNewSession, api: Union[Type[APIData], APIData] = API.TelegramDesktop, password: str = None) -> td.TDesktop
```

Convert this instance of <a class="codehl codehl_obj" href="#tl.telethon.TelegramClient"><b>TelegramClient</b></a> to <a class="codehl codehl_obj" href="../../telegram-desktop/tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a><br>
<h3>Arguments:</h3>

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <span class="highlight"><span class="n">flag</span></span> | <a class="codehl codehl_obj" href="../../authorization/loginflag#api.LoginFlag"><b>LoginFlag</b></a> | <a class="codehl codehl_obj" href="../../authorization/loginflag#api.CreateNewSession"><b>CreateNewSession</b></a> | The login flag. Read more <a class="codehl codehl_obj" href="../../authorization/loginflag#api.LoginFlag"><b>here</b></a>. |
| <a class="codehl codehl_name" href="../../telegram-desktop/account#td.account.Account.api"><b>api</b></a> | <a class="codehl codehl_obj" href="../../authorization/api#api.API"><b>API</b></a> | <a class="codehl codehl_obj" href="../../authorization/api#api.API.TelegramDesktop"><b>TelegramDesktop</b></a> | Which API to use. Read more <a class="codehl codehl_obj" href="../../authorization/api#api.API"><b>here</b></a>. |
| <span class="highlight"><span class="n">password</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | Two-step verification <span class="highlight"><span class="n">password</span></span> if needed. |

<h3>Returns:</h3>


- Return an instance of <a class="codehl codehl_obj" href="../../telegram-desktop/tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a> on success

<h3>Examples:</h3>

Save a telethon session to tdata:

```python
# Using the API that we've generated before. Please refer to method API.Generate() to learn more.
oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id="old.session")
oldclient = TelegramClient("old.session", api=oldAPI)
await oldClient.connect()

# We can safely CreateNewSession with a different API.
# Be aware that you should not use UseCurrentSession with a different API than the one that first authorized it.
newAPI = API.TelegramAndroid.Generate(unique_id="new_tdata")
tdesk = await oldClient.ToTDesktop(flag=CreateNewSession, api=newAPI)

# Save the new session to a folder named "new_tdata"
tdesk.SaveTData("new_tdata")
```


<a id="tl.telethon.TelegramClient.FromTDesktop"></a>


---
### <span class="highlight"><span class="nf">FromTDesktop</span></span><span class="highlight"><span class="o">()</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/tl/telethon.py#L747" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
@typing.overload
@staticmethod
async def FromTDesktop(account: Union[td.TDesktop, td.Account], session: Union[str, Session] = None, flag: Type[LoginFlag] = CreateNewSession, api: Union[Type[APIData], APIData] = API.TelegramDesktop, password: str = None) -> TelegramClient
```

<h3>Arguments:</h3>

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <span class="highlight"><span class="n">account</span></span> | <a class="codehl codehl_obj" href="../../telegram-desktop/tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a>, <a class="codehl codehl_obj" href="../../telegram-desktop/account#td.account.Account"><b>Account</b></a> |  | The <a class="codehl codehl_obj" href="../../telegram-desktop/tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a> or <a class="codehl codehl_obj" href="../../telegram-desktop/account#td.account.Account"><b>Account</b></a> you want to convert from. |
| <span class="highlight"><span class="n">session</span></span> | <span class="highlight"><span class="bp">str</span></span>, <span class="highlight"><span class="nc">Session</span></span> | <span class="highlight"><span class="kc">None</span></span> | The file name of the <span class="highlight"><span class="n">session</span></span> <span class="highlight"><span class="n">file</span></span> to be used, if <span class="highlight"><span class="kc">None</span></span> then the session will not be saved.<br/>Read more [here](https://docs.telethon.dev/en/latest/concepts/sessions.html?highlight=session#what-are-sessions). |
| <span class="highlight"><span class="n">flag</span></span> | <a class="codehl codehl_obj" href="../../authorization/loginflag#api.LoginFlag"><b>LoginFlag</b></a> | <a class="codehl codehl_obj" href="../../authorization/loginflag#api.CreateNewSession"><b>CreateNewSession</b></a> | The login flag. Read more <a class="codehl codehl_obj" href="../../authorization/loginflag#api.LoginFlag"><b>here</b></a>. |
| <a class="codehl codehl_name" href="../../telegram-desktop/account#td.account.Account.api"><b>api</b></a> | <a class="codehl codehl_obj" href="../../authorization/api#api.API"><b>API</b></a> | <a class="codehl codehl_obj" href="../../authorization/api#api.API.TelegramDesktop"><b>TelegramDesktop</b></a> | Which API to use. Read more <a class="codehl codehl_obj" href="../../authorization/api#api.API"><b>here</b></a>. |
| <span class="highlight"><span class="n">password</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | Two-step verification password if needed. |

<h3>Returns:</h3>


- Return an instance of <a class="codehl codehl_obj" href="#tl.telethon.TelegramClient"><b>TelegramClient</b></a> on success

<h3>Examples:</h3>

Create a telethon session using tdata folder:

```python
# Using the API that we've generated before. Please refer to method API.Generate() to learn more.
oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id="old_tdata")
tdesk = TDesktop("old_tdata", api=oldAPI)

# We can safely authorize the new client with a different API.
newAPI = API.TelegramAndroid.Generate(unique_id="new.session")
client = await TelegramClient.FromTDesktop(tdesk, session="new.session", flag=CreateNewSession, api=newAPI)
await client.connect()
await client.PrintSessions()
```


