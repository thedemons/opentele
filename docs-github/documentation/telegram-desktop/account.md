<!-- vim: syntax=Markdown -->

# Account

<a id="td.account.Account"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">Account</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L580"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class Account(BaseObject)
```

Telegram Desktop account<br>
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <a class="codehl codehl_name" href="account.md#api"><b>api</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api.md#class-api"><b>API</b></a> | The API this acount is using. |
| <a class="codehl codehl_name" href="account.md#authkey"><b>authKey</b></a> | <a class="codehl codehl_obj" href="../telegram-desktop/authkey.md#class-authkey"><b>AuthKey</b></a> | The authorization key used to authorize this acocunt. |
| <a class="codehl codehl_name" href="account.md#userid"><b>UserId</b></a> | <span class="highlight"><span class="bp">int</span></span> | User ID of this account. |
| <a class="codehl codehl_name" href="account.md#maindcid"><b>MainDcId</b></a> | <span class="highlight"><span class="nc">DcId</span></span> | The main Data Center ID this account connects to. |
| <a class="codehl codehl_name" href="account.md#basepath"><b>basePath</b></a> | <span class="highlight"><span class="bp">str</span></span> | The folder where tdata is stored. |
| <a class="codehl codehl_name" href="account.md#localkey"><b>localKey</b></a> | <a class="codehl codehl_obj" href="../telegram-desktop/authkey.md#class-authkey"><b>AuthKey</b></a> | Key used to encrypt and decrypt tdata. |
| <a class="codehl codehl_name" href="account.md#owner"><b>owner</b></a> | <a class="codehl codehl_obj" href="../telegram-desktop/tdesktop.md#class-tdesktop"><b>TDesktop</b></a> | <span class="highlight"><span class="nn">td</span></span><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_obj" href="../telegram-desktop/tdesktop.md#class-tdesktop"><b>TDesktop</b></a> client owner of this account. |
| <a class="codehl codehl_name" href="account.md#keyfile"><b>keyFile</b></a> | <span class="highlight"><span class="bp">str</span></span> | See <span class="highlight"><span class="nn">td</span></span><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_obj" href="../telegram-desktop/tdesktop.md#class-tdesktop"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_name" href="../telegram-desktop/tdesktop.md#keyfile"><b>keyFile</b></a>. |



<a id="td.account.Account.__init__"></a>


---
### <span class="highlight"><span class="nc">Account</span></span><span class="highlight"><span class="o">()</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L613"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
def __init__(owner: td.TDesktop, basePath: str = None, api: Union[Type[APIData], APIData] = API.TelegramDesktop, keyFile: str = None, index: int = 0) -> None
```

Initialized a <a class="codehl codehl_obj" href="../telegram-desktop/tdesktop.md#class-tdesktop"><b>TDesktop</b></a> account.<br>
You should use <a class="codehl codehl_obj" href="../telegram-desktop/tdesktop.md#class-tdesktop"><b>TDesktop</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> or <a class="codehl codehl_obj" href="../telegram-desktop/tdesktop.md#class-tdesktop"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_function" href="../telegram-desktop/tdesktop.md#fromtelethon"><b>FromTelethon</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> instead.
Manually using <a class="codehl codehl_obj" href="account.md#class-account"><b>Account</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> is not recommended. But this is here for your need anyway.<br>
<h3>Arguments:</h3>

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <a class="codehl codehl_name" href="account.md#owner"><b>owner</b></a> | <a class="codehl codehl_obj" href="../telegram-desktop/tdesktop.md#class-tdesktop"><b>TDesktop</b></a> |  | <a class="codehl codehl_obj" href="../telegram-desktop/tdesktop.md#class-tdesktop"><b>TDesktop</b></a> client owner of this account. |
| <a class="codehl codehl_name" href="account.md#basepath"><b>basePath</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | The folder where <span class="highlight"><span class="n">tdata</span></span> is stored. |
| <a class="codehl codehl_name" href="account.md#api"><b>api</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api.md#class-api"><b>API</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api.md#class-telegramdesktop"><b>TelegramDesktop</b></a> | Which API to use. Read more <a class="codehl codehl_obj" href="../../documentation/authorization/api.md#class-api"><b>here</b></a>. |
| <a class="codehl codehl_name" href="account.md#keyfile"><b>keyFile</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | See <a class="codehl codehl_obj" href="../telegram-desktop/tdesktop.md#class-tdesktop"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_name" href="../telegram-desktop/tdesktop.md#keyfile"><b>keyFile</b></a>. |
| <span class="highlight"><span class="n">index</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">0</span></span> | Index of this account in the <a class="codehl codehl_obj" href="../telegram-desktop/tdesktop.md#class-tdesktop"><b>TDesktop</b></a> client. |


| :blue_book: TODO |
| :--- |
|     <a class="codehl codehl_function" href="account.md#preparetostart"><b>prepareToStart</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> must be call after initalizing the object. |



<a id="td.account.Account.api"></a>


---
### <span class="highlight"><span class="n">api</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L669"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
@property
def api() -> APIData
```

The API this acount is using.<br>


<a id="td.account.Account.owner"></a>


---
### <span class="highlight"><span class="n">owner</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L682"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
@property
def owner() -> td.TDesktop
```

TDesktop client owner of this account.<br>


<a id="td.account.Account.basePath"></a>


---
### <span class="highlight"><span class="n">basePath</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L689"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
@property
def basePath() -> str
```

The folder where tdata is stored.<br>


<a id="td.account.Account.keyFile"></a>


---
### <span class="highlight"><span class="n">keyFile</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L696"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
@property
def keyFile() -> str
```

See <a class="codehl codehl_obj" href="../telegram-desktop/tdesktop.md#class-tdesktop"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_name" href="../telegram-desktop/tdesktop.md#keyfile"><b>keyFile</b></a><br>


<a id="td.account.Account.localKey"></a>


---
### <span class="highlight"><span class="n">localKey</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L708"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
@property
def localKey() -> Optional[td.AuthKey]
```

Key used to encrypt and decrypt tdata.<br>


<a id="td.account.Account.authKey"></a>


---
### <span class="highlight"><span class="n">authKey</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L720"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
@property
def authKey() -> Optional[td.AuthKey]
```

The authorization key used to authorize this acocunt.<br>


<a id="td.account.Account.UserId"></a>


---
### <span class="highlight"><span class="n">UserId</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L727"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
@property
def UserId() -> int
```

User ID of this account.<br>


<a id="td.account.Account.MainDcId"></a>


---
### <span class="highlight"><span class="n">MainDcId</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L734"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
@property
def MainDcId() -> DcId
```

The main Data Center ID this account connects to.<br>


<a id="td.account.Account.prepareToStart"></a>


---
### <span class="highlight"><span class="nf">prepareToStart</span></span><span class="highlight"><span class="o">()</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L758"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
def prepareToStart(localKey: td.AuthKey) -> td.MTP.Config
```

Prepare the account before starting it<br>
<h3>Arguments:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <a class="codehl codehl_name" href="account.md#localkey"><b>localKey</b></a> | <a class="codehl codehl_obj" href="../telegram-desktop/authkey.md#class-authkey"><b>AuthKey</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api.md#class-api"><b>API</b></a> |

<h3>Returns:</h3>

<a class="codehl codehl_obj" href="../telegram-desktop/mtp.md#class-mtp"><b>MTP</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_obj" href="../telegram-desktop/mtp.md#class-config"><b>Config</b></a> : [description]



<a id="td.account.Account.SaveTData"></a>


---
### <span class="highlight"><span class="nf">SaveTData</span></span><span class="highlight"><span class="o">()</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L889"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
def SaveTData(basePath: str = None, passcode: str = None, keyFile: str = None) -> None
```

Save this account to a folder<br>
<h3>Arguments:</h3>

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <a class="codehl codehl_name" href="account.md#basepath"><b>basePath</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | The path to the folder. Defaults to None. |
| <a class="codehl codehl_name" href="../telegram-desktop/tdesktop.md#passcode"><b>passcode</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | Lock the data with a passcode. Defaults to None. |
| <a class="codehl codehl_name" href="account.md#keyfile"><b>keyFile</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | See <a class="codehl codehl_obj" href="../telegram-desktop/tdesktop.md#class-tdesktop"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_name" href="../telegram-desktop/tdesktop.md#keyfile"><b>keyFile</b></a> |

<h3>Examples</h3>

Add an account to <a class="codehl codehl_obj" href="../telegram-desktop/tdesktop.md#class-tdesktop"><b>TDesktop</b></a> and save it to <span class="highlight"><span class="n">tdata</span></span>:

```python
telethonClient = TelegramClient("sessionFile", API_ID, API_HASH)
td = TDesktop("new_tdata")
account = Account.FromTelethon(telethonClient, owner=td) # add this account to td
td.SaveTData()
```


