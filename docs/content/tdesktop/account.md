
# Account

## Table of Contents

* [td.account](#td.account)
  * [Account](#td.account.Account)
    * [\_\_init\_\_](#td.account.Account.__init__)
    * [localKey](#td.account.Account.localKey)
    * [prepareToStart](#td.account.Account.prepareToStart)
    * [SaveTData](#td.account.Account.SaveTData)

<a id="td.account"></a>

# td.account

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\td\account.py#L1)

<a id="td.account.Account"></a>

## Account Objects

```python
class Account(BaseObject)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\td\account.py#L511)

Telegram Desktop account
Pro account
Test New

### Arguments:

| Name | Type | Description |
| :--- | :--: | :---------- |
| api  | **[APIData](../../APIData#apidata.APIData)** | The API this acount is using |
| basePath  | <span style="color:green">**str**</span> | The folder where tdata is stored |
| owner  | `TDesktop` | TDesktop client owner of this account |
| localKey  | `AuthKey` | Key used to encrypt and decrypt tdata |
| authKey  | `AuthKey` | The actual key used to authorize this acocunt |
| UserId  | <span style="color:green">**int**</span> | User ID of this account |
| MainDcId  | `DcId` | The main Data Center ID this account connects to |

### Raises:

`OpenTeleException` - Failed


<a id="td.account.Account.__init__"></a>

#### Account.\_\_init\_\_

```python
def __init__(owner: td.TDesktop, basePath: str = None, api: Union[Type[APIData], APIData] = APITemplate.TelegramDesktop, keyFile: str = None, index: int = 0) -> None
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\td\account.py#L545)

Setup a tdesktop account

### Arguments:

| Name | Type | Description |
| :--- | :--: | :---------- |
| owner  | `td.TDesktop` | TDesktop client owner of this account |
| basePath  | <span style="color:green">**str**</span> | <span style="color:blue">**None**</span> | The folder where tdata is stored |
| api  | `Type[APIData]` | **[APIData](../../APIData#apidata.APIData)** | **[APITemplate.TelegramDesktop](../../APIData#apidata.APITemplate.TelegramDesktop)** | The **[APIData](../../APIData#apidata.APIData)** to use |
| keyFile  | <span style="color:green">**str**</span> | <span style="color:blue">**None**</span> | [description] |
| index  | <span style="color:green">**int**</span> | `0` | [description] |

### Remarks:

- Notes - **[prepareToStart()](#td.account.Account.prepareToStart)** must be call after initalizing the object.
- Notes - **[prepareToStart()](#td.account.Account.prepareToStart)** must be call after initalizing the object.


<a id="td.account.Account.localKey"></a>

#### Account.localKey

```python
@localKey.setter
def localKey(value)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\td\account.py#L626)

localKey setter is intended for internal usage

<a id="td.account.Account.prepareToStart"></a>

#### Account.prepareToStart

```python
def prepareToStart(localKey: td.AuthKey) -> td.MTP.Config
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\td\account.py#L663)

Prepare the account before starting it

### Arguments:

| Name | Type | Description |
| :--- | :--: | :---------- |
| localKey  | **[td.AuthKey](../AuthKey#td.auth.AuthKey)** | **[APIData](../../APIData#apidata.APIData)** |

### Returns:

**[td.MTP.Config](../MTP#td.mtp.MTP.Config)** - [description]


<a id="td.account.Account.SaveTData"></a>

#### Account.SaveTData

```python
def SaveTData(basePath: str = None, passcode: str = None, keyFile: str = None) -> None
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\td\account.py#L771)

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


