<!-- vim: syntax=Markdown -->

# TDesktop

<a id="td.tdesktop.TDesktop"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/td/tdesktop.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDesktop</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">BaseObject</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TDesktop(BaseObject)
```

Telegram Desktop client.

A client can have multiple account, up to 3 - according to official Telegram Desktop client.

### Attributes:
| Name | Type | Description |
| :--- | :--: | :---------- |
| <a class="codehl codehl_name" href="tdesktop.md#tdesktopapi"><b>api</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api.md#api-objects"><b>API</b></a> | The API this client is using. |
| <a class="codehl codehl_name" href="tdesktop.md#tdesktopaccountscount"><b>accountsCount</b></a> | <span class="highlight"><span class="bp">int</span></span> | The numbers of accounts in this client. |
| <a class="codehl codehl_name" href="tdesktop.md#tdesktopaccounts"><b>accounts</b></a> | <span class="highlight"><span class="nc">List</span></span>[<a class="codehl codehl_obj" href="../telegram-desktop/account.md#account-objects"><b>Account</b></a>] | List of accounts in this client |
| <a class="codehl codehl_name" href="tdesktop.md#tdesktopmainaccount"><b>mainAccount</b></a> | <a class="codehl codehl_obj" href="../telegram-desktop/account.md#account-objects"><b>Account</b></a> | The main account of this client |
| <a class="codehl codehl_name" href="tdesktop.md#tdesktopbasepath"><b>basePath</b></a> | <span class="highlight"><span class="bp">str</span></span> | The path to <span class="highlight"><span class="n">tdata</span></span> <span class="highlight"><span class="n">folder</span></span>. |
| <a class="codehl codehl_name" href="tdesktop.md#tdesktoppasscode"><b>passcode</b></a> | <span class="highlight"><span class="bp">str</span></span> | Passcode of the client, the same as Local Passcode on <span class="highlight"><span class="n">Telegram</span></span> <span class="highlight"><span class="n">Desktop</span></span>.\\<br/><br/>Use to encrypt and decrypt <span class="highlight"><span class="n">tdata</span></span> <span class="highlight"><span class="n">files</span></span>. |
| <a class="codehl codehl_name" href="tdesktop.md#tdesktopappversion"><b>AppVersion</b></a> | <span class="highlight"><span class="bp">int</span></span> | App version of the client. |
| <a class="codehl codehl_name" href="tdesktop.md#tdesktopkmaxaccounts"><b>kMaxAccounts</b></a> | <span class="highlight"><span class="bp">int</span></span> | See <a class="codehl codehl_name" href="tdesktop.md#tdesktopkmaxaccounts"><b>kMaxAccounts</b></a>. |
| <a class="codehl codehl_name" href="tdesktop.md#tdesktopkeyfile"><b>keyFile</b></a> | <span class="highlight"><span class="bp">str</span></span> | See <a class="codehl codehl_name" href="tdesktop.md#tdesktopkeyfile"><b>keyFile</b></a>. |
| <a class="codehl codehl_name" href="tdesktop.md#tdesktopkdefaultkeyfile"><b>kDefaultKeyFile</b></a> | <span class="highlight"><span class="bp">str</span></span> | Default value for <a class="codehl codehl_name" href="tdesktop.md#tdesktopkeyfile"><b>keyFile</b></a>. |


### Methods:

LoadTData():

    Load the client from <span class="highlight"><span class="n">tdata</span></span> <span class="highlight"><span class="n">folder</span></span>. \\

    Use this if you didn't set the <a class="codehl codehl_name" href="tdesktop.md#tdesktopbasepath"><b>basePath</b></a> when initializing the client.



SaveTData():

    Save the client session to <span class="highlight"><span class="n">tdata</span></span> <span class="highlight"><span class="n">folder</span></span> - which can be used by <span class="highlight"><span class="n">Telegram</span></span> <span class="highlight"><span class="n">Desktop</span></span>.



isLoaded():

    Return <span class="highlight"><span class="kc">True</span></span> if the client has successfully loaded accounts from <span class="highlight"><span class="n">tdata</span></span> or from <a class="codehl codehl_obj" href="../../documentation/telethon/telegramclient.md#telegramclient-objects"><b>TelegramClient</b></a>







<a id="td.tdesktop.TDesktop.__init__"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/td/tdesktop.py#L68"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nc">TDesktop</span></span><span class="highlight"><span class="o">()</span></span>

```python
@typing.overload
def __init__() -> None
```

Create an empty instance



<a id="td.tdesktop.TDesktop.__init__"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/td/tdesktop.py#L86"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nc">TDesktop</span></span><span class="highlight"><span class="o">()</span></span>

```python
def __init__(basePath: str = None, api: Union[Type[API], API] = APITemplate.TelegramDesktop, *, passcode: str = None, keyFile: str = None) -> None
```

Initialize a <a class="codehl codehl_obj" href="tdesktop.md#tdesktop-objects"><b>TDesktop</b></a> client

### Arguments:
| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <a class="codehl codehl_name" href="tdesktop.md#tdesktopbasepath"><b>basePath</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | The path to the <span class="highlight"><span class="n">tdata</span></span> <span class="highlight"><span class="n">folder</span></span>.<br/><br/>If the path doesn't exists or its data is corrupted, a new instance will be created. |
| <a class="codehl codehl_name" href="tdesktop.md#tdesktopapi"><b>api</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api.md#api-objects"><b>API</b></a> | <a class="codehl codehl_obj" href="../../documentation/authorization/api.md#telegramdesktop-objects"><b>TelegramDesktop</b></a> | Which API to use. Read more <a class="codehl codehl_obj" href="../../documentation/authorization/api.md#api-objects"><b>here</b></a>. |
| <a class="codehl codehl_name" href="tdesktop.md#tdesktoppasscode"><b>passcode</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | The passcode for tdata, same as the Local Passcode on <span class="highlight"><span class="n">Telegram</span></span> <span class="highlight"><span class="n">Desktop</span></span>. |
| <a class="codehl codehl_name" href="tdesktop.md#tdesktopkeyfile"><b>keyFile</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">data</span></span><span class="highlight"><span class="s2">"</span></span> | See <a class="codehl codehl_name" href="tdesktop.md#tdesktopkeyfile"><b>keyFile</b></a>. |


### Examples:

```python
        from opentele.td import TDesktop
        tdataFolder = "Path\\To\\tdata"
        tdesktop = TDesktop(tdataFolder)
```



<a id="td.tdesktop.TDesktop.isLoaded"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/td/tdesktop.py#L133"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nf">isLoaded</span></span><span class="highlight"><span class="o">()</span></span>

```python
def isLoaded() -> bool
```

Return <span class="highlight"><span class="kc">True</span></span> if the client has successfully loaded accounts from <span class="highlight"><span class="n">tdata</span></span> or from <a class="codehl codehl_obj" href="../../documentation/telethon/telegramclient.md#telegramclient-objects"><b>TelegramClient</b></a>



<a id="td.tdesktop.TDesktop.LoadTData"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/td/tdesktop.py#L139"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nf">LoadTData</span></span><span class="highlight"><span class="o">()</span></span>

```python
def LoadTData(basePath: str = None, passcode: str = None, keyFile: str = None)
```

Loads accounts from <span class="highlight"><span class="n">tdata</span></span> <span class="highlight"><span class="n">folder</span></span>

### Arguments:
| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <a class="codehl codehl_name" href="tdesktop.md#tdesktopbasepath"><b>basePath</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | The path to the folder. |
| <a class="codehl codehl_name" href="tdesktop.md#tdesktoppasscode"><b>passcode</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | See <a class="codehl codehl_name" href="tdesktop.md#tdesktoppasscode"><b>passcode</b></a> |
| <a class="codehl codehl_name" href="tdesktop.md#tdesktopkeyfile"><b>keyFile</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | See <a class="codehl codehl_name" href="tdesktop.md#tdesktopkeyfile"><b>keyFile</b></a> |


### Raises:

<a class="codehl codehl_obj" href="../../documentation/exceptions.md#tdatabaddecryptkey-objects"><b>TDataBadDecryptKey</b></a>:

    The <span class="highlight"><span class="n">tdata</span></span> <span class="highlight"><span class="n">folder</span></span> is password-encrypted, please the set the argument <a class="codehl codehl_name" href="tdesktop.md#tdesktoppasscode"><b>passcode</b></a> to decrypt it.







<a id="td.tdesktop.TDesktop.SaveTData"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/td/tdesktop.py#L184"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nf">SaveTData</span></span><span class="highlight"><span class="o">()</span></span>

```python
def SaveTData(basePath: str = None, passcode: str = None, keyFile: str = None) -> bool
```

Save the client session to a folder.

### Arguments:
| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <a class="codehl codehl_name" href="tdesktop.md#tdesktopbasepath"><b>basePath</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | Path to the folder\\<br/><br/>If None then the data will be saved at the basePath given at creation |




<a id="td.tdesktop.TDesktop.kMaxAccounts"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/td/tdesktop.py#L343"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="n">kMaxAccounts</span></span>

Maximum amount of accounts a client can have



<a id="td.tdesktop.TDesktop.kDefaultKeyFile"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/td/tdesktop.py#L346"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="n">kDefaultKeyFile</span></span>

See <a class="codehl codehl_obj" href="tdesktop.md#tdesktop-objects"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_name" href="tdesktop.md#tdesktopkeyfile"><b>keyFile</b></a>



<a id="td.tdesktop.TDesktop.api"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/td/tdesktop.py#L350"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="n">api</span></span>

```python
@property
def api() -> API
```

The API this client is using.



<a id="td.tdesktop.TDesktop.basePath"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/td/tdesktop.py#L363"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="n">basePath</span></span>

```python
@property
def basePath() -> Optional[str]
```

Base folder of TDesktop, this is where data stored

Same as tdata folder of Telegram Desktop



<a id="td.tdesktop.TDesktop.passcode"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/td/tdesktop.py#L371"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="n">passcode</span></span>

```python
@property
def passcode() -> str
```

Passcode

Passcode used to encrypt and decrypt data

Same as the Local Passcode of Telegram Desktop



<a id="td.tdesktop.TDesktop.keyFile"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/td/tdesktop.py#L380"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="n">keyFile</span></span>

```python
@property
def keyFile() -> str
```

Default value is <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">data</span></span><span class="highlight"><span class="s2">"</span></span>, this argument is rarely ever used.

It is used by <span class="highlight"><span class="n">Telegram</span></span> <span class="highlight"><span class="n">Desktop</span></span> by running it with the <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">-key</span></span><span class="highlight"><span class="s2">"</span></span> argument.

I don't know what's the use cases of it, maybe this was a legacy feature of <span class="highlight"><span class="n">Telegram</span></span> <span class="highlight"><span class="n">Desktop</span></span>.



<a id="td.tdesktop.TDesktop.localKey"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/td/tdesktop.py#L393"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="n">localKey</span></span>

```python
@property
def localKey() -> Optional[td.AuthKey]
```

The key used to encrypt/decrypt data



<a id="td.tdesktop.TDesktop.AppVersion"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/td/tdesktop.py#L400"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="n">AppVersion</span></span>

```python
@property
def AppVersion() -> Optional[int]
```

App version of TDesktop client



<a id="td.tdesktop.TDesktop.accountsCount"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/td/tdesktop.py#L412"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="n">accountsCount</span></span>

```python
@property
def accountsCount() -> int
```

The number of accounts this client has



<a id="td.tdesktop.TDesktop.accounts"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/td/tdesktop.py#L420"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="n">accounts</span></span>

```python
@property
def accounts() -> List[td.Account]
```

List of accounts this client has\n

If you want to get the main account, please use .mainAccount instead



<a id="td.tdesktop.TDesktop.mainAccount"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/td/tdesktop.py#L428"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="n">mainAccount</span></span>

```python
@property
def mainAccount() -> Optional[td.Account]
```

The main account of the client



<a id="td.tdesktop.TDesktop.FromTelethon"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/td/tdesktop.py#L509"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nf">FromTelethon</span></span><span class="highlight"><span class="o">()</span></span>

```python
@staticmethod
async def FromTelethon(telethonClient: tl.TelegramClient, flag: Type[LoginFlag] = CreateNewSession, api: Union[Type[API], API] = APITemplate.TelegramDesktop, password: str = None) -> TDesktop
```

Create an instance of <a class="codehl codehl_obj" href="tdesktop.md#tdesktop-objects"><b>TDesktop</b></a> from <span class="highlight"><span class="n">telethon</span></span><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_obj" href="../../documentation/telethon/telegramclient.md#telegramclient-objects"><b>TelegramClient</b></a>

### Arguments
| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="mf">1.</span></span> <span class="highlight"><span class="n">telethonClient</span></span> | <span class="highlight"><span class="n">telethon</span></span><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_obj" href="../../documentation/telethon/telegramclient.md#telegramclient-objects"><b>TelegramClient</b></a> | The client need to be authorized (logged in) first. |


### Remark

- If you don't set the basePath, you will have to set it when saving tdata



### Examples

#### Saving a telethon client to tdata:

```python
    telethonClient = TelegramClient("sessionFile", API_ID, API_HASH)
    account = Account.FromTelethon(telethonClient, basePath="new_tdata")
    account.saveTData()
```



