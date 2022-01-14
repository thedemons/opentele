# APIData

## Table of Contents

* [apidata](#apidata)
  * [annotations](#apidata.annotations)
  * [os](#apidata.os)
  * [platform](#apidata.platform)
  * [Any](#apidata.Any)
  * [List](#apidata.List)
  * [Dict](#apidata.Dict)
  * [Type](#apidata.Type)
  * [TypeVar](#apidata.TypeVar)
  * [Union](#apidata.Union)
  * [\*](#apidata.*)
  * [\*](#apidata.*)
  * [\*](#apidata.*)
  * [typing](#apidata.typing)
  * [BaseAPIMetaClass](#apidata.BaseAPIMetaClass)
  * [APIData](#apidata.APIData)
    * [Generate](#apidata.APIData.Generate)
  * [APITemplate](#apidata.APITemplate)
    * [TelegramDesktop](#apidata.APITemplate.TelegramDesktop)
    * [TelegramAndroid](#apidata.APITemplate.TelegramAndroid)
    * [TelegramAndroidX](#apidata.APITemplate.TelegramAndroidX)
    * [TelegramIOS](#apidata.APITemplate.TelegramIOS)
    * [TelegramMacOS](#apidata.APITemplate.TelegramMacOS)
    * [TelegramWeb\_Z](#apidata.APITemplate.TelegramWeb_Z)
    * [TelegramWeb\_K](#apidata.APITemplate.TelegramWeb_K)
    * [Webogram](#apidata.APITemplate.Webogram)

<a id="apidata"></a>

# apidata

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L2)

<a id="apidata.annotations"></a>

## annotations

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L2)

<a id="apidata.os"></a>

## os

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L3)

<a id="apidata.platform"></a>

## platform

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L5)

<a id="apidata.Any"></a>

## Any

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L7)

<a id="apidata.List"></a>

## List

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L7)

<a id="apidata.Dict"></a>

## Dict

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L7)

<a id="apidata.Type"></a>

## Type

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L7)

<a id="apidata.TypeVar"></a>

## TypeVar

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L7)

<a id="apidata.Union"></a>

## Union

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L7)

<a id="apidata.*"></a>

## \*

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L8)

<a id="apidata.*"></a>

## \*

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L9)

<a id="apidata.*"></a>

## \*

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L10)

<a id="apidata.typing"></a>

## typing

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L12)

<a id="apidata.BaseAPIMetaClass"></a>

## BaseAPIMetaClass Objects

```python
class BaseAPIMetaClass(type)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L19)

Super high level tactic metaclass

<a id="apidata.APIData"></a>

## APIData Objects

```python
class APIData(object, metaclass=BaseAPIMetaClass)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L54)

API configuration to connect to `TelegramClient` and `TDesktop`

### Attributes:

| Name | Type | Description |
| :--- | :--: | :---------- |
| api_id  | <span style="color:green">**int**</span> | API_ID |
| api_hash  | <span style="color:green">**str**</span> | API_HASH |
| device_model  | <span style="color:green">**str**</span> | Device model name |
| system_version  | <span style="color:green">**str**</span> | Operating System version |
| app_version  | <span style="color:green">**str**</span> | Current app version |
| lang_code  | <span style="color:green">**str**</span> | Language code of the client |
| system_lang_code  | <span style="color:green">**str**</span> | Language code of operating system |
| lang_pack  | <span style="color:green">**str**</span> | Language pack |

### Methods:

**[Generate()](#apidata.APIData.Generate)** - Generate random device model and system version


<a id="apidata.APIData.Generate"></a>

#### APIData.Generate

```python
@classmethod
def Generate(cls: Type[_T], id: str = None) -> _T
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L198)

Generate random device model and system version

### Arguments:

| Name | Type | Description |
| :--- | :--: | :---------- |
| id  | <span style="color:green">**str**</span> | <span style="color:blue">**None**</span> | description |

### Raises:

`NotImplementedError` - Not supported for web browser yet

### Returns:

**[APIData](#apidata.APIData)** - Return a copy of the api with random data


<a id="apidata.APITemplate"></a>

## APITemplate Objects

```python
class APITemplate(APIData)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L235)

<a id="apidata.APITemplate.TelegramDesktop"></a>

## TelegramDesktop Objects

```python
class TelegramDesktop(APIData)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L237)

Official Telegram for Desktop (Windows, macOS and Linux)\n
[View on GitHub](https://github.com/telegramdesktop/tdesktop)

<a id="apidata.APITemplate.TelegramAndroid"></a>

## TelegramAndroid Objects

```python
class TelegramAndroid(APIData)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L291)

Official Telegram for Android\n
[View on GitHub](https://github.com/DrKLO/Telegram)

<a id="apidata.APITemplate.TelegramAndroidX"></a>

## TelegramAndroidX Objects

```python
class TelegramAndroidX(APIData)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L305)

Official TelegramX for Android\n
[View on GitHub](https://github.com/DrKLO/Telegram)

<a id="apidata.APITemplate.TelegramIOS"></a>

## TelegramIOS Objects

```python
class TelegramIOS(APIData)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L319)

Official Telegram for iOS\n
[View on GitHub](https://github.com/TelegramMessenger/Telegram-iOS)

<a id="apidata.APITemplate.TelegramMacOS"></a>

## TelegramMacOS Objects

```python
class TelegramMacOS(APIData)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L335)

Official Telegram-Swift For MacOS\n
[View on GitHub](https://github.com/overtake/TelegramSwift)

<a id="apidata.APITemplate.TelegramWeb_Z"></a>

## TelegramWeb\_Z Objects

```python
class TelegramWeb_Z(APIData)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L351)

Default Official Telegram Web Z For Browsers\n
[View on GitHub](https://github.com/Ajaxy/telegram-tt) | [Visit on Telegram](https://web.telegram.org/z/)

<a id="apidata.APITemplate.TelegramWeb_K"></a>

## TelegramWeb\_K Objects

```python
class TelegramWeb_K(APIData)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L366)

Official Telegram Web K For Browsers\n
[View on GitHub](https://github.com/morethanwords/tweb) | [Visit on Telegram](https://web.telegram.org/k/)

<a id="apidata.APITemplate.Webogram"></a>

## Webogram Objects

```python
class Webogram(APIData)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\apidata.py#L380)

Old Telegram For Browsers\n
[View on GitHub](https://github.com/zhukov/webogram) | [Vist on Telegram](https://web.telegram.org/?legacy=1#/im)

