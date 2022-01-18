<!-- vim: syntax=Markdown -->

# APITemplate

<a id="api.APITemplate"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/api.py#L276"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">APITemplate</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">API</span></span><span class="highlight"><span class="o">)</span></span>

```python
class APITemplate(API)
```

Builtin Templates for API

### Attributes:
| Name | Type | Description |
| :--- | :--: | :---------- |
| <a class="codehl codehl_obj" href="api.md#telegramdesktop-objects"><b>TelegramDesktop</b></a> | <a class="codehl codehl_obj" href="api.md#api-objects"><b>API</b></a> | Official Telegram for Desktop (Windows, macOS and Linux) [View on GitHub](https://github.com/telegramdesktop/tdesktop) |
| <a class="codehl codehl_obj" href="api.md#telegramandroid-objects"><b>TelegramAndroid</b></a> | <a class="codehl codehl_obj" href="api.md#api-objects"><b>API</b></a> | Official Telegram for Android [View on GitHub](https://github.com/DrKLO/Telegram) |
| <a class="codehl codehl_obj" href="api.md#telegramandroidx-objects"><b>TelegramAndroidX</b></a> | <a class="codehl codehl_obj" href="api.md#api-objects"><b>API</b></a> | Official TelegramX for Android [View on GitHub](https://github.com/DrKLO/Telegram) |
| <a class="codehl codehl_obj" href="api.md#telegramios-objects"><b>TelegramIOS</b></a> | <a class="codehl codehl_obj" href="api.md#api-objects"><b>API</b></a> | Official Telegram for iOS [View on GitHub](https://github.com/TelegramMessenger/Telegram-iOS) |
| <a class="codehl codehl_obj" href="api.md#telegrammacos-objects"><b>TelegramMacOS</b></a> | <a class="codehl codehl_obj" href="api.md#api-objects"><b>API</b></a> | Official Telegram-Swift For MacOS [View on GitHub](https://github.com/overtake/TelegramSwift) |
| <a class="codehl codehl_obj" href="api.md#telegramweb_z-objects"><b>TelegramWeb_Z</b></a> | <a class="codehl codehl_obj" href="api.md#api-objects"><b>API</b></a> | Default Official Telegram Web Z For Browsers [View on GitHub](https://github.com/Ajaxy/telegram-tt) | [Visit on Telegram](https://web.telegram.org/z/) |
| <a class="codehl codehl_obj" href="api.md#telegramweb_k-objects"><b>TelegramWeb_K</b></a> | <a class="codehl codehl_obj" href="api.md#api-objects"><b>API</b></a> | Official Telegram Web K For Browsers [View on GitHub](https://github.com/morethanwords/tweb) | [Visit on Telegram](https://web.telegram.org/k/) |
| <a class="codehl codehl_obj" href="api.md#webogram-objects"><b>Webogram</b></a> | <a class="codehl codehl_obj" href="api.md#api-objects"><b>API</b></a> | Old Telegram For Browsers [View on GitHub](https://github.com/zhukov/webogram) | [Vist on Telegram](https://web.telegram.org/?legacy=1#/im) |




<a id="api.APITemplate.TelegramDesktop"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/api.py#L306"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TelegramDesktop</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">API</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TelegramDesktop(API)
```

Official Telegram for Desktop (Windows, macOS and Linux)

[View on GitHub](https://github.com/telegramdesktop/tdesktop)

### Attributes:
| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">api_id</span></span> | <span class="highlight"><span class="bp">int</span></span> | : <span class="highlight"><span class="mi">2040</span></span> |
| <span class="highlight"><span class="n">api_hash</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">b18441a1ff607e10a989891a5462e627</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">device_model</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">Desktop</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">Windows 10</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">app_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">3.4.3 x64</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en-US</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_pack</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">tdesktop</span></span><span class="highlight"><span class="s2">"</span></span> |


### Methods:

<a class="codehl codehl_function" href="api.md#telegramdesktopgenerate"><b>Generate</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span>: Generate random device data for <span class="highlight"><span class="n">Windows</span></span>, <span class="highlight"><span class="n">macOS</span></span> and <span class="highlight"><span class="n">Linux</span></span>





<a id="api.APITemplate.TelegramDesktop.Generate"></a>

---

#### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/api.py#L335"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nf">Generate</span></span><span class="highlight"><span class="o">()</span></span>

```python
@typing.overload
@classmethod
def Generate(cls: Type[_T], system: str = "windows", id: str = None) -> _T
```

Generate random TelegramDesktop devices

### Arguments:
| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <span class="highlight"><span class="n">system</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">random</span></span><span class="highlight"><span class="s2">"</span></span> | Which OS to generate, either "windows", "macos", or "linux".\\<br/><br/>Default is <span class="highlight"><span class="kc">None</span></span> or "random" which means it will selects randomly |
| <span class="highlight"><span class="nb">id</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | The ID to generate - can be anything.\\<br/><br/>This ID will be used to ensure that it will generate the same data every single time.\\<br/><br/>If not set then it won't generate the same value again. |


### Returns:

<span class="highlight"><span class="n">_T</span></span>: [description]





<a id="api.APITemplate.TelegramAndroid"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/api.py#L387"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TelegramAndroid</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">API</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TelegramAndroid(API)
```

Official Telegram for Android

[View on GitHub](https://github.com/DrKLO/Telegram)

### Attributes:
| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">api_id</span></span> | <span class="highlight"><span class="bp">int</span></span> | : <span class="highlight"><span class="mi">6</span></span> |
| <span class="highlight"><span class="n">api_hash</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">eb06d4abfb49dc3eeb1aeb98ae0f581e</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">device_model</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">Samsung SM-G998B</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">SDK 31</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">app_version</span></span> | str):<span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">8.4.1(2522 | </span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en-US</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_pack</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">android</span></span><span class="highlight"><span class="s2">"</span></span> |




<a id="api.APITemplate.TelegramAndroidX"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/api.py#L411"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TelegramAndroidX</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">API</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TelegramAndroidX(API)
```

Official TelegramX for Android

[View on GitHub](https://github.com/DrKLO/Telegram)

### Attributes:
| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">api_id</span></span> | <span class="highlight"><span class="bp">int</span></span> | : <span class="highlight"><span class="mi">21724</span></span> |
| <span class="highlight"><span class="n">api_hash</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">3e0cb5efcd52300aec5994fdfc5bdc16</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">device_model</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">Samsung SM-G998B</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">SDK 31</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">app_version</span></span> | str):<span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">8.4.1(2522 | </span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en-US</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_pack</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">android</span></span><span class="highlight"><span class="s2">"</span></span> |




<a id="api.APITemplate.TelegramIOS"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/api.py#L435"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TelegramIOS</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">API</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TelegramIOS(API)
```

Official Telegram for iOS

[View on GitHub](https://github.com/TelegramMessenger/Telegram-iOS)

### Attributes:
| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">api_id</span></span> | <span class="highlight"><span class="bp">int</span></span> | : <span class="highlight"><span class="mi">10840</span></span> |
| <span class="highlight"><span class="n">api_hash</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">33c45224029d59cb3ad0c16134215aeb</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">device_model</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">iPhone 13 Pro Max</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">14.8.1</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">app_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">8.4</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en-US</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_pack</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">ios</span></span><span class="highlight"><span class="s2">"</span></span> |




<a id="api.APITemplate.TelegramMacOS"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/api.py#L461"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TelegramMacOS</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">API</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TelegramMacOS(API)
```

Official Telegram-Swift For MacOS

[View on GitHub](https://github.com/overtake/TelegramSwift)

### Attributes:
| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">api_id</span></span> | <span class="highlight"><span class="bp">int</span></span> | : <span class="highlight"><span class="mi">2834</span></span> |
| <span class="highlight"><span class="n">api_hash</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">68875f756c9b437a8b916ca3de215815</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">device_model</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">MacBook Pro</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">macOS 12.0.1</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">app_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">8.4</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en-US</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_pack</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">macos</span></span><span class="highlight"><span class="s2">"</span></span> |




<a id="api.APITemplate.TelegramWeb_Z"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/api.py#L487"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TelegramWeb_Z</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">API</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TelegramWeb_Z(API)
```

Default Official Telegram Web Z For Browsers

[View on GitHub](https://github.com/Ajaxy/telegram-tt) | [Visit on Telegram](https://web.telegram.org/z/)

### Attributes:
| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">api_id</span></span> | <span class="highlight"><span class="bp">int</span></span> | : <span class="highlight"><span class="mi">2496</span></span> |
| <span class="highlight"><span class="n">api_hash</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">8da85b0d5bfe62527e5b244c209159c3</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">device_model</span></span> | str):<span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML, </span></span>likeGecko <span class="highlight"><span class="o">|</span></span> <span class="highlight"><span class="n">Chrome</span></span><span class="highlight"><span class="o">/</span></span><span class="highlight"><span class="mf">96.0</span></span><span class="highlight"><span class="mf">.4664</span></span><span class="highlight"><span class="mf">.110</span></span> <span class="highlight"><span class="n">Safari</span></span><span class="highlight"><span class="o">/</span></span><span class="highlight"><span class="mf">537.36</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">Windows</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">app_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">1.28.3 Z</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en-US</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_pack</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">"</span></span> |




<a id="api.APITemplate.TelegramWeb_K"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/api.py#L512"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TelegramWeb_K</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">API</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TelegramWeb_K(API)
```

Official Telegram Web K For Browsers

[View on GitHub](https://github.com/morethanwords/tweb) | [Visit on Telegram](https://web.telegram.org/k/)

### Attributes:
| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">api_id</span></span> | <span class="highlight"><span class="bp">int</span></span> | : <span class="highlight"><span class="mi">2496</span></span> |
| <span class="highlight"><span class="n">api_hash</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">8da85b0d5bfe62527e5b244c209159c3</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">device_model</span></span> | str):<span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML, </span></span>likeGecko <span class="highlight"><span class="o">|</span></span> <span class="highlight"><span class="n">Chrome</span></span><span class="highlight"><span class="o">/</span></span><span class="highlight"><span class="mf">96.0</span></span><span class="highlight"><span class="mf">.4664</span></span><span class="highlight"><span class="mf">.110</span></span> <span class="highlight"><span class="n">Safari</span></span><span class="highlight"><span class="o">/</span></span><span class="highlight"><span class="mf">537.36</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">Win32</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">app_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">1.0.1 K</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en-US</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_pack</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">macos</span></span><span class="highlight"><span class="s2">"</span></span> |




<a id="api.APITemplate.Webogram"></a>

---

### <a href="https://github.com/thedemons/opentele/blob/73b66dd3aacff5a89e25f30c48d19d105de483f8/src/api.py#L536"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">Webogram</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">API</span></span><span class="highlight"><span class="o">)</span></span>

```python
class Webogram(API)
```

Old Telegram For Browsers

[View on GitHub](https://github.com/zhukov/webogram) | [Vist on Telegram](https://web.telegram.org/?legacy=1#/im)

### Attributes:
| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">api_id</span></span> | <span class="highlight"><span class="bp">int</span></span> | : <span class="highlight"><span class="mi">2496</span></span> |
| <span class="highlight"><span class="n">api_hash</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">8da85b0d5bfe62527e5b244c209159c3</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">device_model</span></span> | str):<span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML, </span></span>likeGecko <span class="highlight"><span class="o">|</span></span> <span class="highlight"><span class="n">Chrome</span></span><span class="highlight"><span class="o">/</span></span><span class="highlight"><span class="mf">96.0</span></span><span class="highlight"><span class="mf">.4664</span></span><span class="highlight"><span class="mf">.110</span></span> <span class="highlight"><span class="n">Safari</span></span><span class="highlight"><span class="o">/</span></span><span class="highlight"><span class="mf">537.36</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">Win32</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">app_version</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">0.7.0</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">system_lang_code</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">en-US</span></span><span class="highlight"><span class="s2">"</span></span> |
| <span class="highlight"><span class="n">lang_pack</span></span> | <span class="highlight"><span class="bp">str</span></span> | : <span class="highlight"><span class="s2">"</span></span><span class="highlight"><span class="s2">"</span></span> |




