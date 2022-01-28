<!-- vim: syntax=Markdown -->

# Account

<a id="td.account.Account"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">Account</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L580" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
class Account(BaseObject)
```

Telegram Desktop account<br>
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <a class="codehl codehl_name" href="#td.account.Account.api"><b>api</b></a> | <a class="codehl codehl_obj" href="../../authorization/api#api.API"><b>API</b></a> | The API this acount is using. |
| <a class="codehl codehl_name" href="#td.account.Account.authKey"><b>authKey</b></a> | <a class="codehl codehl_obj" href="../authkey#td.auth.AuthKey"><b>AuthKey</b></a> | The authorization key used to authorize this acocunt. |
| <a class="codehl codehl_name" href="#td.account.Account.UserId"><b>UserId</b></a> | <span class="highlight"><span class="bp">int</span></span> | User ID of this account. |
| <a class="codehl codehl_name" href="#td.account.Account.MainDcId"><b>MainDcId</b></a> | <span class="highlight"><span class="nc">DcId</span></span> | The main Data Center ID this account connects to. |
| <a class="codehl codehl_name" href="#td.account.Account.basePath"><b>basePath</b></a> | <span class="highlight"><span class="bp">str</span></span> | The folder where tdata is stored. |
| <a class="codehl codehl_name" href="#td.account.Account.localKey"><b>localKey</b></a> | <a class="codehl codehl_obj" href="../authkey#td.auth.AuthKey"><b>AuthKey</b></a> | Key used to encrypt and decrypt tdata. |
| <a class="codehl codehl_name" href="#td.account.Account.owner"><b>owner</b></a> | <a class="codehl codehl_obj" href="../tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a> | <span class="highlight"><span class="nn">td</span></span><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_obj" href="../tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a> client owner of this account. |
| <a class="codehl codehl_name" href="#td.account.Account.keyFile"><b>keyFile</b></a> | <span class="highlight"><span class="bp">str</span></span> | See <span class="highlight"><span class="nn">td</span></span><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_obj" href="../tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_name" href="../tdesktop#td.tdesktop.TDesktop.keyFile"><b>keyFile</b></a>. |



<a id="td.account.Account.__init__"></a>


---
### <span class="highlight"><span class="nc">Account</span></span><span class="highlight"><span class="o">()</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L613" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
def __init__(owner: td.TDesktop, basePath: str = None, api: Union[Type[APIData], APIData] = API.TelegramDesktop, keyFile: str = None, index: int = 0) -> None
```

Initialized a <a class="codehl codehl_obj" href="../tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a> account.<br>
You should use <a class="codehl codehl_obj" href="../tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> or <a class="codehl codehl_obj" href="../tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_function" href="../tdesktop#td.tdesktop.TDesktop.FromTelethon"><b>FromTelethon</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> instead.
Manually using <a class="codehl codehl_obj" href="#td.account.Account"><b>Account</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> is not recommended. But this is here for your need anyway.<br>
<h3>Arguments:</h3>

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <a class="codehl codehl_name" href="#td.account.Account.owner"><b>owner</b></a> | <a class="codehl codehl_obj" href="../tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a> |  | <a class="codehl codehl_obj" href="../tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a> client owner of this account. |
| <a class="codehl codehl_name" href="#td.account.Account.basePath"><b>basePath</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | The folder where <span class="highlight"><span class="n">tdata</span></span> is stored. |
| <a class="codehl codehl_name" href="#td.account.Account.api"><b>api</b></a> | <a class="codehl codehl_obj" href="../../authorization/api#api.API"><b>API</b></a> | <a class="codehl codehl_obj" href="../../authorization/api#api.API.TelegramDesktop"><b>TelegramDesktop</b></a> | Which API to use. Read more <a class="codehl codehl_obj" href="../../authorization/api#api.API"><b>here</b></a>. |
| <a class="codehl codehl_name" href="#td.account.Account.keyFile"><b>keyFile</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | See <a class="codehl codehl_obj" href="../tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_name" href="../tdesktop#td.tdesktop.TDesktop.keyFile"><b>keyFile</b></a>. |
| <span class="highlight"><span class="n">index</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">0</span></span> | Index of this account in the <a class="codehl codehl_obj" href="../tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a> client. |

???+ note "TODO"
    <a class="codehl codehl_function" href="#td.account.Account.prepareToStart"><b>prepareToStart</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span> must be call after initalizing the object.



<a id="td.account.Account.api"></a>


---
### <span class="highlight"><span class="n">api</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L669" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
@property
def api() -> APIData
```

The API this acount is using.<br>


<a id="td.account.Account.owner"></a>


---
### <span class="highlight"><span class="n">owner</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L682" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
@property
def owner() -> td.TDesktop
```

TDesktop client owner of this account.<br>


<a id="td.account.Account.basePath"></a>


---
### <span class="highlight"><span class="n">basePath</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L689" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
@property
def basePath() -> str
```

The folder where tdata is stored.<br>


<a id="td.account.Account.keyFile"></a>


---
### <span class="highlight"><span class="n">keyFile</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L696" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
@property
def keyFile() -> str
```

See <a class="codehl codehl_obj" href="../tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_name" href="../tdesktop#td.tdesktop.TDesktop.keyFile"><b>keyFile</b></a><br>


<a id="td.account.Account.localKey"></a>


---
### <span class="highlight"><span class="n">localKey</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L708" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
@property
def localKey() -> Optional[td.AuthKey]
```

Key used to encrypt and decrypt tdata.<br>


<a id="td.account.Account.authKey"></a>


---
### <span class="highlight"><span class="n">authKey</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L720" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
@property
def authKey() -> Optional[td.AuthKey]
```

The authorization key used to authorize this acocunt.<br>


<a id="td.account.Account.UserId"></a>


---
### <span class="highlight"><span class="n">UserId</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L727" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
@property
def UserId() -> int
```

User ID of this account.<br>


<a id="td.account.Account.MainDcId"></a>


---
### <span class="highlight"><span class="n">MainDcId</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L734" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
@property
def MainDcId() -> DcId
```

The main Data Center ID this account connects to.<br>


<a id="td.account.Account.prepareToStart"></a>


---
### <span class="highlight"><span class="nf">prepareToStart</span></span><span class="highlight"><span class="o">()</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L758" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
def prepareToStart(localKey: td.AuthKey) -> td.MTP.Config
```

Prepare the account before starting it<br>
<h3>Arguments:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <a class="codehl codehl_name" href="#td.account.Account.localKey"><b>localKey</b></a> | <a class="codehl codehl_obj" href="../authkey#td.auth.AuthKey"><b>AuthKey</b></a> | <a class="codehl codehl_obj" href="../../authorization/api#api.API"><b>API</b></a> |

<h3>Returns:</h3>

<a class="codehl codehl_obj" href="../mtp#td.mtp.MTP"><b>MTP</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_obj" href="../mtp#td.mtp.MTP.Config"><b>Config</b></a> : [description]



<a id="td.account.Account.SaveTData"></a>


---
### <span class="highlight"><span class="nf">SaveTData</span></span><span class="highlight"><span class="o">()</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/account.py#L889" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
def SaveTData(basePath: str = None, passcode: str = None, keyFile: str = None) -> None
```

Save this account to a folder<br>
<h3>Arguments:</h3>

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <a class="codehl codehl_name" href="#td.account.Account.basePath"><b>basePath</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | The path to the folder. Defaults to None. |
| <a class="codehl codehl_name" href="../tdesktop#td.tdesktop.TDesktop.passcode"><b>passcode</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | Lock the data with a passcode. Defaults to None. |
| <a class="codehl codehl_name" href="#td.account.Account.keyFile"><b>keyFile</b></a> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | See <a class="codehl codehl_obj" href="../tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_name" href="../tdesktop#td.tdesktop.TDesktop.keyFile"><b>keyFile</b></a> |

<h3>Examples</h3>

Add an account to <a class="codehl codehl_obj" href="../tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a> and save it to <span class="highlight"><span class="n">tdata</span></span>:

```python
telethonClient = TelegramClient("sessionFile", API_ID, API_HASH)
td = TDesktop("new_tdata")
account = Account.FromTelethon(telethonClient, owner=td) # add this account to td
td.SaveTData()
```


