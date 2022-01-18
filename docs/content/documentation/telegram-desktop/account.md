<!-- vim: syntax=Markdown -->

# Account

<a id="td.account.Account"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/td/account.py#L509"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">Account</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">BaseObject</span></span><span class="highlight"><span class="o">)</span></span>

```python
class Account(BaseObject)
```

Telegram Desktop account

### Attributes:
| Name | Type | Description |
| :--- | :--: | :---------- |
| <a class="codehl codehl_name" href="account#accountapi"><b>api</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api#api-objects"><b>API</b></a> | The API this acount is using. |
| <a class="codehl codehl_name" href="account#accountauthkey"><b>authKey</b></a> | <a class="codehl codehl_obj" href="../telegram-desktop/authkey#authkey-objects"><b>AuthKey</b></a> | The authorization key used to authorize this acocunt. |
| <a class="codehl codehl_name" href="account#accountuserid"><b>UserId</b></a> | <span class="highlight"><span class="bp">int</span></span> | User ID of this account. |
| <a class="codehl codehl_name" href="account#accountmaindcid"><b>MainDcId</b></a> | <span class="highlight"><span class="nc">DcId</span></span> | The main Data Center ID this account connects to. |
| <a class="codehl codehl_name" href="account#accountbasepath"><b>basePath</b></a> | <span class="highlight"><span class="bp">str</span></span> | The folder where tdata is stored. |
| <a class="codehl codehl_name" href="account#accountlocalkey"><b>localKey</b></a> | <a class="codehl codehl_obj" href="../telegram-desktop/authkey#authkey-objects"><b>AuthKey</b></a> | Key used to encrypt and decrypt tdata. |
| <a class="codehl codehl_name" href="account#accountowner"><b>owner</b></a> | <a class="codehl codehl_obj" href="../telegram-desktop/tdesktop#tdesktop-objects"><b>TDesktop</b></a> | <span class="highlight"><span class="nn">td</span></span><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_obj" href="../telegram-desktop/tdesktop#tdesktop-objects"><b>TDesktop</b></a> client owner of this account. |
| <a class="codehl codehl_name" href="account#accountkeyfile"><b>keyFile</b></a> | <span class="highlight"><span class="bp">str</span></span> | See <span class="highlight"><span class="nn">td</span></span><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_obj" href="../telegram-desktop/tdesktop#tdesktop-objects"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_name" href="../telegram-desktop/tdesktop#tdesktopkeyfile"><b>keyFile</b></a>. |




<a id="td.account.Account.__init__"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/td/account.py#L542"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nc">Account</span></span><span class="highlight"><span class="o">()</span></span>

```python
def __init__(owner: td.TDesktop, basePath: str = None, api: Union[Type[API], API] = APITemplate.TelegramDesktop, keyFile: str = None, index: int = 0) -> None
```

Initialized a <a class="codehl codehl_obj" href="../telegram-desktop/tdesktop#tdesktop-objects"><b>TDesktop</b></a> account.

You should use <a class="codehl codehl_obj" href="../telegram-desktop/tdesktop#tdesktop-objects"><b>TDesktop</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> or <a class="codehl codehl_obj" href="../telegram-desktop/tdesktop#tdesktop-objects"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_function" href="../telegram-desktop/tdesktop#tdesktopfromtelethon"><b>FromTelethon</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> instead.

Manually using <a class="codehl codehl_obj" href="account#account-objects"><b>Account</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> is not recommended. But this is here for your need anyway.

### Arguments:
| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <a class="codehl codehl_name" href="account#accountowner"><b>owner</b></a> | <a class="codehl codehl_obj" href="../telegram-desktop/tdesktop#tdesktop-objects"><b>TDesktop</b></a> |  | <a class="codehl codehl_obj" href="../telegram-desktop/tdesktop#tdesktop-objects"><b>TDesktop</b></a> client owner of this account. |
| <a class="codehl codehl_name" href="account#accountbasepath"><b>basePath</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | The folder where <span class="highlight"><span class="n">tdata</span></span> is stored. |
| <a class="codehl codehl_name" href="account#accountapi"><b>api</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api#api-objects"><b>API</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api#telegramdesktop-objects"><b>TelegramDesktop</b></a> | Which API to use. Read more <a class="codehl codehl_obj" href="../../documentation/authorization/api#api-objects"><b>here</b></a>. |
| <a class="codehl codehl_name" href="account#accountkeyfile"><b>keyFile</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | See <a class="codehl codehl_obj" href="../telegram-desktop/tdesktop#tdesktop-objects"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_name" href="../telegram-desktop/tdesktop#tdesktopkeyfile"><b>keyFile</b></a>. |
| <span class="highlight"><span class="n">index</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">0</span></span> | Index of this account in the <a class="codehl codehl_obj" href="../telegram-desktop/tdesktop#tdesktop-objects"><b>TDesktop</b></a> client. |


???+ note "TODO"
     <a class="codehl codehl_function" href="account#accountpreparetostart"><b>prepareToStart</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> must be call after initalizing the object.




<a id="td.account.Account.api"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/td/account.py#L595"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="n">api</span></span>

```python
@property
def api() -> API
```

The API this acount is using.



<a id="td.account.Account.owner"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/td/account.py#L607"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="n">owner</span></span>

```python
@property
def owner() -> td.TDesktop
```

TDesktop client owner of this account.



<a id="td.account.Account.basePath"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/td/account.py#L614"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="n">basePath</span></span>

```python
@property
def basePath() -> str
```

The folder where tdata is stored.



<a id="td.account.Account.keyFile"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/td/account.py#L621"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="n">keyFile</span></span>

```python
@property
def keyFile() -> str
```

See <a class="codehl codehl_obj" href="../telegram-desktop/tdesktop#tdesktop-objects"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_name" href="../telegram-desktop/tdesktop#tdesktopkeyfile"><b>keyFile</b></a>



<a id="td.account.Account.localKey"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/td/account.py#L633"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="n">localKey</span></span>

```python
@property
def localKey() -> Optional[td.AuthKey]
```

Key used to encrypt and decrypt tdata.



<a id="td.account.Account.authKey"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/td/account.py#L645"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="n">authKey</span></span>

```python
@property
def authKey() -> Optional[td.AuthKey]
```

The authorization key used to authorize this acocunt.



<a id="td.account.Account.UserId"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/td/account.py#L652"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="n">UserId</span></span>

```python
@property
def UserId() -> int
```

User ID of this account.



<a id="td.account.Account.MainDcId"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/td/account.py#L659"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="n">MainDcId</span></span>

```python
@property
def MainDcId() -> DcId
```

The main Data Center ID this account connects to.



<a id="td.account.Account.prepareToStart"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/td/account.py#L683"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nf">prepareToStart</span></span><span class="highlight"><span class="o">()</span></span>

```python
def prepareToStart(localKey: td.AuthKey) -> td.MTP.Config
```

Prepare the account before starting it

### Arguments:
| Name | Type | Description |
| :--- | :--: | :---------- |
| <a class="codehl codehl_name" href="account#accountlocalkey"><b>localKey</b></a> | <a class="codehl codehl_obj" href="../telegram-desktop/authkey#authkey-objects"><b>AuthKey</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api#api-objects"><b>API</b></a> |


### Returns:

<a class="codehl codehl_obj" href="../telegram-desktop/mtp#mtp-objects"><b>MTP</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_obj" href="../telegram-desktop/mtp#config-objects"><b>Config</b></a>: [description]





<a id="td.account.Account.SaveTData"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/td/account.py#L791"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nf">SaveTData</span></span><span class="highlight"><span class="o">()</span></span>

```python
def SaveTData(basePath: str = None, passcode: str = None, keyFile: str = None) -> None
```

Save this account to a folder

### Arguments:
| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <a class="codehl codehl_name" href="account#accountbasepath"><b>basePath</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | The path to the folder. Defaults to None. |
| <a class="codehl codehl_name" href="../telegram-desktop/tdesktop#tdesktoppasscode"><b>passcode</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | Lock the data with a passcode. Defaults to None. |
| <a class="codehl codehl_name" href="account#accountkeyfile"><b>keyFile</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | See <a class="codehl codehl_obj" href="../telegram-desktop/tdesktop#tdesktop-objects"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_name" href="../telegram-desktop/tdesktop#tdesktopkeyfile"><b>keyFile</b></a> |


### Examples

Add an account to <a class="codehl codehl_obj" href="../telegram-desktop/tdesktop#tdesktop-objects"><b>TDesktop</b></a> and save it to <span class="highlight"><span class="n">tdata</span></span>:



```python
    telethonClient = TelegramClient("sessionFile", API_ID, API_HASH)
    td = TDesktop("new_tdata")
    account = Account.FromTelethon(telethonClient, owner=td) # add this account to td
    td.SaveTData()
```



