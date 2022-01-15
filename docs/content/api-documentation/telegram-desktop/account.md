<!-- vim: syntax=Markdown -->

# Account

## Table of Contents

* [Account](#td.account.Account)
  * [\_\_init\_\_](#td.account.Account.__init__)
  * [localKey](#td.account.Account.localKey)
  * [prepareToStart](#td.account.Account.prepareToStart)
  * [SaveTData](#td.account.Account.SaveTData)

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\account.py#L1)

<a id="td.account.Account"></a>

## Account Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\account.py#L511)

```python
class Account(BaseObject)
```

Telegram Desktop account
Pro account
Test New

#### Arguments:

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| api | <a class="md-typeset__a_obj" href="../../authorization/apidata#apidata.APIData">APIData</a> | __required__ | The API this acount is using |
| basePath | <span class="md-typeset__obj">str</span> | __required__ | The folder where tdata is stored |
| owner | `TDesktop` | __required__ | TDesktop client owner of this account |
| localKey | `AuthKey` | __required__ | Key used to encrypt and decrypt tdata |
| authKey | `AuthKey` | __required__ | The actual key used to authorize this acocunt |
| UserId | <span class="md-typeset__obj">int</span> | __required__ | User ID of this account |
| MainDcId | `DcId` | __required__ | The main Data Center ID this account connects to |

#### Raises:

- `OpenTeleException` - Failed


<a id="td.account.Account.__init__"></a>

#### Account.\_\_init\_\_

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\account.py#L545)

```python
def __init__(owner: td.TDesktop, basePath: str = None, api: Union[Type[APIData], APIData] = APITemplate.TelegramDesktop, keyFile: str = None, index: int = 0) -> None
```

Setup a tdesktop account

#### Arguments:

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| owner | <a class="md-typeset__a_obj" href="../tdesktop#td.tdesktop.TDesktop">td.TDesktop</a> | __required__ | TDesktop client owner of this account |
| basePath | <span class="md-typeset__obj">str</span> | None | The folder where tdata is stored |
| api | `Type[APIData]` \| <a class="md-typeset__a_obj" href="../../authorization/apidata#apidata.APIData">APIData</a> \| <a class="md-typeset__a_obj" href="../../authorization/apitemplate#apidata.APITemplate.TelegramDesktop">APITemplate.TelegramDesktop</a> | __required__ | The <a class="md-typeset__a_obj" href="../../authorization/apidata#apidata.APIData">APIData</a> to use |
| keyFile | <span class="md-typeset__obj">str</span> \| <span class="md-typeset__const">None</span> | __required__ | [description] |
| index | <span class="md-typeset__obj">int</span> \| `0` | __required__ | [description] |

#### Remarks:

- - Notes - <a class="md-typeset__a_obj" href="../account#td.account.Account.prepareToStart">prepareToStart()</a> must be call after initalizing the object.
- - Notes - <a class="md-typeset__a_obj" href="../account#td.account.Account.prepareToStart">prepareToStart()</a> must be call after initalizing the object.


<a id="td.account.Account.localKey"></a>

#### Account.localKey

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\account.py#L625)

```python
@localKey.setter
def localKey(value)
```

localKey setter is intended for internal usage

<a id="td.account.Account.prepareToStart"></a>

#### Account.prepareToStart

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\account.py#L662)

```python
def prepareToStart(localKey: td.AuthKey) -> td.MTP.Config
```

Prepare the account before starting it

#### Arguments:

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| localKey | <a class="md-typeset__a_obj" href="../authkey#td.auth.AuthKey">td.AuthKey</a> | __required__ | <a class="md-typeset__a_obj" href="../../authorization/apidata#apidata.APIData">APIData</a> |

#### Returns:

- <a class="md-typeset__a_obj" href="../mtp#td.mtp.MTP.Config">td.MTP.Config</a> - [description]


<a id="td.account.Account.SaveTData"></a>

#### Account.SaveTData

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\account.py#L770)

```python
def SaveTData(basePath: str = None, passcode: str = None, keyFile: str = None) -> None
```

Save this account to a folder
[extended_summary]

Args:
    basePath (str, optional): The path to the folder. Defaults to None.
    passcode (str, optional): Lock the data with a passcode. Defaults to None.
    keyFile (str, optional): [description]. Defaults to None.

Examples:
    Add an account to `tdesktop` and save it to `tdata`:
```python
    telethonClient = TelegramClient("sessionFile", API_ID, API_HASH)
    td = TDesktop("new_tdata")
    account = Account.FromTelethon(telethonClient, owner=td) # add this account to td
    td.SaveTData()
```


