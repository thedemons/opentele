<a id="src.td.account"></a>

# src.td.account

[[view_source]](https://github.com/thedemons/opentele/blob/ca94141ac7bb35c6a36367d753dfd868ebb5929b/src\td\account.py#L1)

<a id="src.td.account.Account"></a>

## Account Objects

```python
class Account(BaseObject)
```

[[view_source]](https://github.com/thedemons/opentele/blob/ca94141ac7bb35c6a36367d753dfd868ebb5929b/src\td\account.py#L511)

Telegram Desktop account

**Attributes**:

- `api` _APIData_ - The API this acount is using
- `basePath` _str_ - The folder where tdata is stored
- `owner` _TDesktop_ - TDesktop client owner of this account
- `localKey` _AuthKey_ - Key used to encrypt and decrypt tdata
- `authKey` _AuthKey_ - The actual key used to authorize this acocunt
- `UserId` _int_ - User ID of this account
- `MainDcId` _DcId_ - The main Data Center ID this account connects to

<a id="src.td.account.Account.__init__"></a>

#### \_\_init\_\_

```python
def __init__(owner: td.TDesktop, basePath: str = None, api: Union[Type[APIData], APIData] = APITemplate.TelegramDesktop, keyFile: str = None, index: int = 0) -> None
```

[[view_source]](https://github.com/thedemons/opentele/blob/ca94141ac7bb35c6a36367d753dfd868ebb5929b/src\td\account.py#L528)

Setup a tdesktop account

[extended_summary]

**Arguments**:

- `owner` _td.TDesktop_ - TDesktop client owner of this account
- `basePath` _str, optional_ - The folder where tdata is stored. Defaults to None.
- `api` _Union[Type[APIData], APIData], optional_ - [description]. Defaults to APITemplate.TelegramDesktop.
- `keyFile` _str, optional_ - [description]. Defaults to None.
- `index` _int, optional_ - [description]. Defaults to 0.
  
  Remark:
  prepareToStart() must be call after initalizing the object

<a id="src.td.account.Account.SaveTData"></a>

#### SaveTData

```python
def SaveTData(basePath: str = None, passcode: str = None, keyFile: str = None) -> None
```

[[view_source]](https://github.com/thedemons/opentele/blob/ca94141ac7bb35c6a36367d753dfd868ebb5929b/src\td\account.py#L734)

Save this account to a folder

[extended_summary]

**Arguments**:

- `basePath` _str, optional_ - The path to the folder. Defaults to None.
- `passcode` _str, optional_ - Lock the data with a passcode. Defaults to None.
- `keyFile` _str, optional_ - [description]. Defaults to None.

