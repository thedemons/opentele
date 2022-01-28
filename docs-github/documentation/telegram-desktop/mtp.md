<!-- vim: syntax=Markdown -->

# MTP

<a id="td.mtp.MTP"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">MTP</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/mtp.py#L7"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class MTP(BaseObject)
```

[MTProto Protocal](https://core.telegram.org/mtproto)
This class is for further future developments and has no usage for now.<br>
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <a class="codehl codehl_obj" href="mtp.md#class-environment"><b>Environment</b></a> | <span class="highlight"><span class="k">class</span></span> | MTP Enviroment |
| <a class="codehl codehl_obj" href="mtp.md#class-rsapublickey"><b>RSAPublicKey</b></a> | <span class="highlight"><span class="k">class</span></span> | RSAPublicKey |
| <a class="codehl codehl_obj" href="mtp.md#class-dcoptions"><b>DcOptions</b></a> | <span class="highlight"><span class="k">class</span></span> | DcOptions |
| <a class="codehl codehl_obj" href="mtp.md#class-configfields"><b>ConfigFields</b></a> | <span class="highlight"><span class="k">class</span></span> | ConfigFields |
| <a class="codehl codehl_obj" href="mtp.md#class-config"><b>Config</b></a> | <span class="highlight"><span class="k">class</span></span> | Config |



<a id="td.mtp.MTP.Environment"></a>


---
### <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">Environment</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/mtp.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class Environment(IntEnum)
```

Enviroment flag for MTP.Config<br>
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">Production</span></span> | <span class="highlight"><span class="nc">IntEnum</span></span> | Production Enviroment |
| <span class="highlight"><span class="n">Test</span></span> | <span class="highlight"><span class="nc">IntEnum</span></span> | Test Enviroment |



<a id="td.mtp.MTP.RSAPublicKey"></a>


---
### <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">RSAPublicKey</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/mtp.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class RSAPublicKey(BaseObject)
```

To be added<br>


<a id="td.mtp.MTP.DcOptions"></a>


---
### <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">DcOptions</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/mtp.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class DcOptions(BaseObject)
```

Data Center Options, providing information about DC ip, port,.. etc<br>


<a id="td.mtp.MTP.DcOptions.Address"></a>


---
#### <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">Address</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/mtp.py#L183"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class Address(int)
```

Connection flag used for MTP.DcOptions.Endpoint<br>
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">IPv4</span></span> | <span class="highlight"><span class="bp">int</span></span> | IPv4 connection |
| <span class="highlight"><span class="n">IPv6</span></span> | <span class="highlight"><span class="bp">int</span></span> | IPv6 connection |



<a id="td.mtp.MTP.DcOptions.Protocol"></a>


---
#### <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">Protocol</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/mtp.py#L195"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class Protocol(int)
```

Protocal flag used for MTP.DcOptions.Endpoint<br>
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">Tcp</span></span> | <span class="highlight"><span class="bp">int</span></span> | Tcp connection |
| <span class="highlight"><span class="n">Http</span></span> | <span class="highlight"><span class="bp">int</span></span> | Http connection |



<a id="td.mtp.MTP.DcOptions.Flag"></a>


---
#### <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">Flag</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/mtp.py#L207"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class Flag(int)
```

Flag used for MTP.DcOptions.Endpoint<br>
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">f_ipv6</span></span> | <span class="highlight"><span class="bp">int</span></span> | f_ipv6 |
| <span class="highlight"><span class="n">f_media_only</span></span> | <span class="highlight"><span class="bp">int</span></span> | f_media_only |
| <span class="highlight"><span class="n">f_tcpo_only</span></span> | <span class="highlight"><span class="bp">int</span></span> | f_tcpo_only |
| <span class="highlight"><span class="n">f_cdn</span></span> | <span class="highlight"><span class="bp">int</span></span> | f_cdn |
| <span class="highlight"><span class="n">f_static</span></span> | <span class="highlight"><span class="bp">int</span></span> | f_static |
| <span class="highlight"><span class="n">f_secret</span></span> | <span class="highlight"><span class="bp">int</span></span> | f_secret |
| <span class="highlight"><span class="n">MAX_FIELD</span></span> | <span class="highlight"><span class="bp">int</span></span> | MAX_FIELD |



<a id="td.mtp.MTP.DcOptions.Endpoint"></a>


---
#### <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">Endpoint</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/mtp.py#L229"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class Endpoint(BaseObject)
```

Data center endpoint<br>
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="nb">id</span></span> | <span class="highlight"><span class="nc">DcId</span></span> | Data Center ID |
| <span class="highlight"><span class="n">flags</span></span> | <a class="codehl codehl_obj" href="mtp.md#class-flag"><b>Flag</b></a> | <a class="codehl codehl_obj" href="mtp.md#class-flag"><b>Flag</b></a> |
| <span class="highlight"><span class="n">ip</span></span> | <span class="highlight"><span class="bp">str</span></span> | IP address of the data center |
| <span class="highlight"><span class="n">port</span></span> | <span class="highlight"><span class="bp">int</span></span> | Port to connect to |
| <span class="highlight"><span class="n">secret</span></span> | <span class="highlight"><span class="bp">bytes</span></span> | secret |



<a id="td.mtp.MTP.ConfigFields"></a>


---
### <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">ConfigFields</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/mtp.py#L255"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class ConfigFields(BaseObject)
```

Configuration data for <a class="codehl codehl_obj" href="mtp.md#class-mtp"><b>MTP</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_obj" href="mtp.md#class-config"><b>Config</b></a><br>
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">chatSizeMax</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">200</span></span> |
| <span class="highlight"><span class="n">megagroupSizeMax</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">10000</span></span> |
| <span class="highlight"><span class="n">forwardedCountMax</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">100</span></span> |
| <span class="highlight"><span class="n">onlineUpdatePeriod</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">120000</span></span> |
| <span class="highlight"><span class="n">offlineBlurTimeout</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">5000</span></span> |
| <span class="highlight"><span class="n">offlineIdleTimeout</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">30000</span></span> |
| <span class="highlight"><span class="n">onlineFocusTimeout</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">1000</span></span> <span class="highlight"><span class="c1"># Not from the server config.</span></span> |
| <span class="highlight"><span class="n">onlineCloudTimeout</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">300000</span></span> |
| <span class="highlight"><span class="n">notifyCloudDelay</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">30000</span></span> |
| <span class="highlight"><span class="n">notifyDefaultDelay</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">1500</span></span> |
| <span class="highlight"><span class="n">savedGifsLimit</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">200</span></span> |
| <span class="highlight"><span class="n">editTimeLimit</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">172800</span></span> |
| <span class="highlight"><span class="n">revokeTimeLimit</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">172800</span></span> |
| <span class="highlight"><span class="n">revokePrivateTimeLimit</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">172800</span></span> |
| <span class="highlight"><span class="n">revokePrivateInbox</span></span> | <span class="highlight"><span class="bp">bool</span></span> | <span class="highlight"><span class="kc">False</span></span> |
| <span class="highlight"><span class="n">stickersRecentLimit</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">30</span></span> |
| <span class="highlight"><span class="n">stickersFavedLimit</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">5</span></span> |
| <span class="highlight"><span class="n">pinnedDialogsCountMax</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">5</span></span> |
| <span class="highlight"><span class="n">pinnedDialogsInFolderMax</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">100</span></span> |
| <span class="highlight"><span class="n">internalLinksDomain</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">https://t.me/</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">channelsReadMediaPeriod</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">86400</span></span> <span class="highlight"><span class="o">*</span></span> <span class="highlight"><span class="mi">7</span></span> |
| <span class="highlight"><span class="n">callReceiveTimeoutMs</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">20000</span></span> |
| <span class="highlight"><span class="n">callRingTimeoutMs</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">90000</span></span> |
| <span class="highlight"><span class="n">callConnectTimeoutMs</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">30000</span></span> |
| <span class="highlight"><span class="n">callPacketTimeoutMs</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">10000</span></span> |
| <span class="highlight"><span class="n">webFileDcId</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">4</span></span> |
| <span class="highlight"><span class="n">txtDomainString</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="bp">str</span></span><span class="highlight"><span class="p">(</span></span><span class="highlight"><span class="p">)</span></span> |
| <span class="highlight"><span class="n">phoneCallsEnabled</span></span> | <span class="highlight"><span class="bp">bool</span></span> | <span class="highlight"><span class="kc">True</span></span> |
| <span class="highlight"><span class="n">blockedMode</span></span> | <span class="highlight"><span class="bp">bool</span></span> | <span class="highlight"><span class="kc">False</span></span> |
| <span class="highlight"><span class="n">captionLengthMax</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">1024</span></span> |



<a id="td.mtp.MTP.Config"></a>


---
### <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">Config</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/mtp.py#L324"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class Config(BaseObject)
```

Configuration of MTProto<br>
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">kVersion</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">1</span></span> |



