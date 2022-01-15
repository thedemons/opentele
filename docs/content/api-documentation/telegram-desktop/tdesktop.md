<!-- vim: syntax=Markdown -->

# TDesktop

## Table of Contents

* [TDesktop](#td.tdesktop.TDesktop)
  * [\_\_init\_\_](#td.tdesktop.TDesktop.__init__)
  * [\_\_init\_\_](#td.tdesktop.TDesktop.__init__)
  * [basePath](#td.tdesktop.TDesktop.basePath)
  * [passcode](#td.tdesktop.TDesktop.passcode)
  * [localKey](#td.tdesktop.TDesktop.localKey)
  * [AppVersion](#td.tdesktop.TDesktop.AppVersion)
  * [AppVersionString](#td.tdesktop.TDesktop.AppVersionString)
  * [accountsCount](#td.tdesktop.TDesktop.accountsCount)
  * [accounts](#td.tdesktop.TDesktop.accounts)
  * [mainAccount](#td.tdesktop.TDesktop.mainAccount)
  * [isLoaded](#td.tdesktop.TDesktop.isLoaded)
  * [SaveTData](#td.tdesktop.TDesktop.SaveTData)
  * [FromTelethon](#td.tdesktop.TDesktop.FromTelethon)

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\tdesktop.py#L1)

<a id="td.tdesktop.TDesktop"></a>

## TDesktop Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\tdesktop.py#L16)

```python
class TDesktop(BaseObject)
```

<a id="td.tdesktop.TDesktop.__init__"></a>

#### TDesktop.\_\_init\_\_

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\tdesktop.py#L22)

```python
@typing.overload
def __init__() -> None
```

Create an empty instance

<a id="td.tdesktop.TDesktop.__init__"></a>

#### TDesktop.\_\_init\_\_

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\tdesktop.py#L41)

```python
def __init__(basePath: str = None, api: Union[Type[APIData], APIData] = APITemplate.TelegramDesktop, *, passcode: str = None, keyFile: str = None) -> None
```

### Arguments
    1. basePath (str):\n
        The path to the tdata folder, if the path doesn't exists or its data is corrupted, a new instance is returned

### Optional
    2. passcode (str, default=""):\n
        The passcode for tdata, same as the Local Passcode on Telegram Desktop

    3. keyFile (str, default="data"):\n
        The gKeyFile data name, the same for `Telegram.exe -key gKeyFile`\n
        This argument is rarely used, you should only use this if you understand what it is

### Examples
#### Load from a folder or create new instance at C:\\Telegram\\tdata:
```python
    td = TDesktop("C:\\Telegram\\tdata")
    print( td.isAuthorized() )
```

<a id="td.tdesktop.TDesktop.basePath"></a>

#### TDesktop.basePath

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\tdesktop.py#L95)

```python
@property
def basePath() -> Optional[str]
```

Base folder of TDesktop, this is where data stored\n
Same as tdata folder of Telegram Desktop

<a id="td.tdesktop.TDesktop.passcode"></a>

#### TDesktop.passcode

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\tdesktop.py#L103)

```python
@property
def passcode() -> str
```

Passcode used to encrypt and decrypt data\n
Same as the Local Passcode of Telegram Desktop

<a id="td.tdesktop.TDesktop.localKey"></a>

#### TDesktop.localKey

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\tdesktop.py#L119)

```python
@property
def localKey() -> Optional[td.AuthKey]
```

The key used to encrypt/decrypt data

<a id="td.tdesktop.TDesktop.AppVersion"></a>

#### TDesktop.AppVersion

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\tdesktop.py#L126)

```python
@property
def AppVersion() -> Optional[int]
```

App version of TDesktop client

<a id="td.tdesktop.TDesktop.AppVersionString"></a>

#### TDesktop.AppVersionString

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\tdesktop.py#L133)

```python
@property
def AppVersionString() -> Optional[str]
```

App version of TDesktop client

<a id="td.tdesktop.TDesktop.accountsCount"></a>

#### TDesktop.accountsCount

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\tdesktop.py#L141)

```python
@property
def accountsCount() -> int
```

The number of accounts this client has

<a id="td.tdesktop.TDesktop.accounts"></a>

#### TDesktop.accounts

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\tdesktop.py#L149)

```python
@property
def accounts() -> List[td.Account]
```

List of accounts this client has\n
If you want to get the main account, please use .mainAccount instead

<a id="td.tdesktop.TDesktop.mainAccount"></a>

#### TDesktop.mainAccount

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\tdesktop.py#L157)

```python
@property
def mainAccount() -> Optional[td.Account]
```

The main account of the client

<a id="td.tdesktop.TDesktop.isLoaded"></a>

#### TDesktop.isLoaded

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\tdesktop.py#L163)

```python
def isLoaded() -> bool
```

Return True if the client has loaded tdata

<a id="td.tdesktop.TDesktop.SaveTData"></a>

#### TDesktop.SaveTData

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\tdesktop.py#L197)

```python
def SaveTData(basePath: str = None, passcode: str = None, keyFile: str = None) -> bool
```

Save the login information to a folder
### Optional
    1. basePath (str | None, default=None):\n
        Path to the folder\n
        If None then the data will be saved at the basePath given at creation\n
        If None and no basePath was given at creation, it will raises an OpenTeleException

### Examples
#### Import an account from telethon session and save it as tdata:
```python
    telethon_client = TelegramClient("SessionFile")
    td = TDesktop("NewFolder")
    td.ImportTelethonAccount(telethon_client)
    td.SaveTData()
```

<a id="td.tdesktop.TDesktop.FromTelethon"></a>

#### TDesktop.FromTelethon

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\tdesktop.py#L440)

```python
@staticmethod
async def FromTelethon(telethonClient: tl.TelegramClient, flag: Type[LoginFlag] = CreateNewSession, api: Union[Type[APIData], APIData] = APITemplate.TelegramDesktop, password: str = None) -> TDesktop
```

Create an instance of <a class="md-typeset__a_obj" href="../tdesktop#td.tdesktop.TDesktop">TDesktop</a> from `telethon.TelegramClient`\n

### Arguments
    1. telethonClient (telethon.TelegramClient):\n
        The client need to be authorized (logged in) first.


### Remark
    - If you don't set the basePath, you will have to set it when saving tdata

### Examples
#### Saving a telethon client to tdata:
```python
    telethonClient = TelegramClient("sessionFile", API_ID, API_HASH)
    account = Account.FromTelethon(telethonClient, basePath="new_tdata")
    account.saveTData()
```

