<!-- vim: syntax=Markdown -->

# APITemplate

## Table of Contents

* [APITemplate](#apidata.APITemplate)
  * [TelegramDesktop](#apidata.APITemplate.TelegramDesktop)
    * [Generate](#apidata.APITemplate.TelegramDesktop.Generate)
  * [TelegramAndroid](#apidata.APITemplate.TelegramAndroid)
  * [TelegramAndroidX](#apidata.APITemplate.TelegramAndroidX)
  * [TelegramIOS](#apidata.APITemplate.TelegramIOS)
  * [TelegramMacOS](#apidata.APITemplate.TelegramMacOS)
  * [TelegramWeb\_Z](#apidata.APITemplate.TelegramWeb_Z)
  * [TelegramWeb\_K](#apidata.APITemplate.TelegramWeb_K)
  * [Webogram](#apidata.APITemplate.Webogram)

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\apidata.py#L2)

<a id="apidata.APITemplate"></a>

## APITemplate Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\apidata.py#L237)

```python
class APITemplate(APIData)
```

Builtin Templates for APIData

#### Attributes:

| Name | Type | Description |
| :--- | :--: | :---------- |
| TelegramDesktop | <a class="md-typeset__a_obj" href="../apidata#apidata.APIData">APIData</a> | Official Telegram for Desktop (Windows, macOS and Linux) [View on GitHub](https://github.com/telegramdesktop/tdesktop) |
| TelegramAndroid | <a class="md-typeset__a_obj" href="../apidata#apidata.APIData">APIData</a> | Official Telegram for Android [View on GitHub](https://github.com/DrKLO/Telegram) |
| TelegramAndroidX | <a class="md-typeset__a_obj" href="../apidata#apidata.APIData">APIData</a> | Official TelegramX for Android [View on GitHub](https://github.com/DrKLO/Telegram) |
| TelegramIOS | <a class="md-typeset__a_obj" href="../apidata#apidata.APIData">APIData</a> | Official Telegram for iOS [View on GitHub](https://github.com/TelegramMessenger/Telegram-iOS) |
| TelegramMacOS | <a class="md-typeset__a_obj" href="../apidata#apidata.APIData">APIData</a> | Official Telegram-Swift For MacOS [View on GitHub](https://github.com/overtake/TelegramSwift) |
| TelegramWeb_Z | <a class="md-typeset__a_obj" href="../apidata#apidata.APIData">APIData</a> | Default Official Telegram Web Z For Browsers [View on GitHub](https://github.com/Ajaxy/telegram-tt) | [Visit on Telegram](https://web.telegram.org/z/) |
| TelegramWeb_K | <a class="md-typeset__a_obj" href="../apidata#apidata.APIData">APIData</a> | Official Telegram Web K For Browsers [View on GitHub](https://github.com/morethanwords/tweb) | [Visit on Telegram](https://web.telegram.org/k/) |
| Webogram | <a class="md-typeset__a_obj" href="../apidata#apidata.APIData">APIData</a> | Old Telegram For Browsers [View on GitHub](https://github.com/zhukov/webogram) | [Vist on Telegram](https://web.telegram.org/?legacy=1#/im) |


<a id="apidata.APITemplate.TelegramDesktop"></a>

## TelegramDesktop Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\apidata.py#L267)

```python
class TelegramDesktop(APIData)
```

Official Telegram for Desktop (Windows, macOS and Linux)
[View on GitHub](https://github.com/telegramdesktop/tdesktop)

#### Attributes:

| Name | Type | Description |
| :--- | :--: | :---------- |
| api_id | <span class="md-typeset__obj">int</span> | 2040 |
| api_hash | <span class="md-typeset__obj">str</span> | b18441a1ff607e10a989891a5462e627 |
| device_model | <span class="md-typeset__obj">str</span> | Desktop |
| system_version | <span class="md-typeset__obj">str</span> | Windows 10 |
| app_version | <span class="md-typeset__obj">str</span> | 3.4.3 x64 |
| lang_code | <span class="md-typeset__obj">str</span> | en |
| system_lang_code | <span class="md-typeset__obj">str</span> | en-US |
| lang_pack | <span class="md-typeset__obj">str</span> | tdesktop <a class="md-typeset__a_obj" href="../apitemplate#apidata.APITemplate.TelegramDesktop.Generate">Generate</a> |

#### Methods:

- `Generate(x)` - Generate Windows device
- `Generate(x)` - Generate macOS device
- `Generate(x)` - Generate Linux device
- `Generate(x)` - Generate random operating system (Windows | macOS | Linux)


<a id="apidata.APITemplate.TelegramDesktop.Generate"></a>

#### TelegramDesktop.Generate

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\apidata.py#L299)

```python
@typing.overload
@classmethod
def Generate(cls: Type[_T], system: str = "windows", id: str = None) -> _T
```

Generate random TelegramDesktop devices

#### Arguments:

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| system | <span class="md-typeset__obj">str</span> | `"windows"` | Which OS to generate, either "windows", "macos", or "linux".<br/>Default is <span class="md-typeset__const">None</span> or "random" which means it will selects randomly between 3 OS |
| id | <span class="md-typeset__obj">str</span> | <span class="md-typeset__const">None</span> | The ID to generate - can be anything.<br/>This will be used to ensure that it will generate the same data everytime.<br/>If not set then it will be randomized every time we runs it. |

#### Returns:

- `_T` - [description]


<a id="apidata.APITemplate.TelegramAndroid"></a>

## TelegramAndroid Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\apidata.py#L351)

```python
class TelegramAndroid(APIData)
```

Official Telegram for Android\n
[View on GitHub](https://github.com/DrKLO/Telegram)

<a id="apidata.APITemplate.TelegramAndroidX"></a>

## TelegramAndroidX Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\apidata.py#L365)

```python
class TelegramAndroidX(APIData)
```

Official TelegramX for Android\n
[View on GitHub](https://github.com/DrKLO/Telegram)

<a id="apidata.APITemplate.TelegramIOS"></a>

## TelegramIOS Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\apidata.py#L379)

```python
class TelegramIOS(APIData)
```

Official Telegram for iOS\n
[View on GitHub](https://github.com/TelegramMessenger/Telegram-iOS)

<a id="apidata.APITemplate.TelegramMacOS"></a>

## TelegramMacOS Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\apidata.py#L395)

```python
class TelegramMacOS(APIData)
```

Official Telegram-Swift For MacOS\n
[View on GitHub](https://github.com/overtake/TelegramSwift)

<a id="apidata.APITemplate.TelegramWeb_Z"></a>

## TelegramWeb\_Z Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\apidata.py#L411)

```python
class TelegramWeb_Z(APIData)
```

Default Official Telegram Web Z For Browsers\n
[View on GitHub](https://github.com/Ajaxy/telegram-tt) | [Visit on Telegram](https://web.telegram.org/z/)

<a id="apidata.APITemplate.TelegramWeb_K"></a>

## TelegramWeb\_K Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\apidata.py#L426)

```python
class TelegramWeb_K(APIData)
```

Official Telegram Web K For Browsers\n
[View on GitHub](https://github.com/morethanwords/tweb) | [Visit on Telegram](https://web.telegram.org/k/)

<a id="apidata.APITemplate.Webogram"></a>

## Webogram Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\apidata.py#L440)

```python
class Webogram(APIData)
```

Old Telegram For Browsers\n
[View on GitHub](https://github.com/zhukov/webogram) | [Vist on Telegram](https://web.telegram.org/?legacy=1#/im)

