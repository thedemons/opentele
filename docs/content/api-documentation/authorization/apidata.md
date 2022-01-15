<!-- vim: syntax=Markdown -->

# APIData

## Table of Contents

* [APIData](#apidata.APIData)
  * [Generate](#apidata.APIData.Generate)

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\apidata.py#L2)

<a id="apidata.APIData"></a>

## APIData Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\apidata.py#L54)

```python
class APIData(object, metaclass=BaseAPIMetaClass)
```

API configuration to connect to `TelegramClient` and `TDesktop`

#### Attributes:

| Name | Type | Description |
| :--- | :--: | :---------- |
| api_id | <span class="md-typeset__obj">int</span> | [API_ID](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id) |
| api_hash | <span class="md-typeset__obj">str</span> | [API_HASH](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id) |
| device_model | <span class="md-typeset__obj">str</span> | Device model name |
| system_version | <span class="md-typeset__obj">str</span> | Operating System version |
| app_version | <span class="md-typeset__obj">str</span> | Current app version |
| lang_code | <span class="md-typeset__obj">str</span> | Language code of the client |
| system_lang_code | <span class="md-typeset__obj">str</span> | Language code of operating system |
| lang_pack | <span class="md-typeset__obj">str</span> | Language pack |

#### Methods:

- <a class="md-typeset__a_obj" href="../apidata#apidata.APIData.Generate">Generate()</a> - Generate random device model and system version


<a id="apidata.APIData.Generate"></a>

#### APIData.Generate

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\apidata.py#L199)

```python
@classmethod
def Generate(cls: Type[_T], id: str = None) -> _T
```

Generate random device model and system version

#### Arguments:

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| id | <span class="md-typeset__obj">str</span> | <span class="md-typeset__const">None</span> [random] | The ID to generate - can be anything.<br/>This will be used to ensure that it will generate the same data everytime.<br/>If not set then it will be randomized every time we runs it. |

#### Raises:

- `NotImplementedError` - Not supported for web browser yet

#### Returns:

- <a class="md-typeset__a_obj" href="../apidata#apidata.APIData">APIData</a> - Return a copy of the api with random data


