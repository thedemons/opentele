# Exceptions

## Table of Contents

* [exception](#exception)
  * [annotations](#exception.annotations)
  * [inspect](#exception.inspect)
  * [types](#exception.types)
  * [typing](#exception.typing)
  * [QDataStream](#exception.QDataStream)
  * [FileNotFound](#exception.FileNotFound)
  * [TDataInvalidMagic](#exception.TDataInvalidMagic)
  * [TDataInvalidCheckSum](#exception.TDataInvalidCheckSum)
  * [TDataBadDecryptKey](#exception.TDataBadDecryptKey)
  * [TDataWrongPasscode](#exception.TDataWrongPasscode)
  * [TDataBadEncryptedDataSize](#exception.TDataBadEncryptedDataSize)
  * [TDataBadDecryptedDataSize](#exception.TDataBadDecryptedDataSize)
  * [TDataBadConfigData](#exception.TDataBadConfigData)
  * [QDataStreamFailed](#exception.QDataStreamFailed)
  * [AccountAuthKeyNotFound](#exception.AccountAuthKeyNotFound)
  * [TDataReadMapDataFailed](#exception.TDataReadMapDataFailed)
  * [TDataReadMapDataIncorrectPasscode](#exception.TDataReadMapDataIncorrectPasscode)
  * [TDataAuthKeyNotFound](#exception.TDataAuthKeyNotFound)
  * [MaxAccountLimit](#exception.MaxAccountLimit)
  * [TDesktopUnauthorized](#exception.TDesktopUnauthorized)
  * [TelethonUnauthorized](#exception.TelethonUnauthorized)
  * [TDataSaveFailed](#exception.TDataSaveFailed)
  * [TDesktopNotLoaded](#exception.TDesktopNotLoaded)
  * [TDesktopHasNoAccount](#exception.TDesktopHasNoAccount)
  * [TDAccountNotLoaded](#exception.TDAccountNotLoaded)
  * [NoPasswordProvided](#exception.NoPasswordProvided)
  * [Passwordincorrect](#exception.Passwordincorrect)
  * [LoginFlagInvalid](#exception.LoginFlagInvalid)
  * [NoInstanceMatched](#exception.NoInstanceMatched)
  * [Expects](#exception.Expects)
  * [Expects](#exception.Expects)

<a id="exception"></a>

# exception

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L1)

<a id="exception.annotations"></a>

## annotations

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L1)

<a id="exception.inspect"></a>

## inspect

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L2)

<a id="exception.types"></a>

## types

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L3)

<a id="exception.typing"></a>

## typing

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L4)

<a id="exception.QDataStream"></a>

## QDataStream

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L5)

<a id="exception.FileNotFound"></a>

## FileNotFound Objects

```python
class FileNotFound(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L60)

Could not find or open the file

<a id="exception.TDataInvalidMagic"></a>

## TDataInvalidMagic Objects

```python
class TDataInvalidMagic(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L65)

TData file has an invalid magic data, which is the first 4 bytes of the file\n
This usually mean that the file is corrupted or not in the supported formats

<a id="exception.TDataInvalidCheckSum"></a>

## TDataInvalidCheckSum Objects

```python
class TDataInvalidCheckSum(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L71)

TData file has an invalid checksum\n
This usually mean that the file is corrupted or not in the supported formats

<a id="exception.TDataBadDecryptKey"></a>

## TDataBadDecryptKey Objects

```python
class TDataBadDecryptKey(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L77)

Could not decrypt the data with this key\n
This usually mean that the file is password-encrypted

<a id="exception.TDataWrongPasscode"></a>

## TDataWrongPasscode Objects

```python
class TDataWrongPasscode(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L83)

Wrong passcode to decrypt tdata folder\n

<a id="exception.TDataBadEncryptedDataSize"></a>

## TDataBadEncryptedDataSize Objects

```python
class TDataBadEncryptedDataSize(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L88)

The encrypted data size part of the file is corrupted

<a id="exception.TDataBadDecryptedDataSize"></a>

## TDataBadDecryptedDataSize Objects

```python
class TDataBadDecryptedDataSize(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L92)

The decrypted data size part of the file is corrupted

<a id="exception.TDataBadConfigData"></a>

## TDataBadConfigData Objects

```python
class TDataBadConfigData(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L96)

TData contains bad config data that couldn't be parsed

<a id="exception.QDataStreamFailed"></a>

## QDataStreamFailed Objects

```python
class QDataStreamFailed(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L101)

Could not stream data from QDataStream\n
Please check the QDataStream.status() for more information

<a id="exception.AccountAuthKeyNotFound"></a>

## AccountAuthKeyNotFound Objects

```python
class AccountAuthKeyNotFound(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L107)

Account.authKey is missing, something went wrong

<a id="exception.TDataReadMapDataFailed"></a>

## TDataReadMapDataFailed Objects

```python
class TDataReadMapDataFailed(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L112)

Could not read map data

<a id="exception.TDataReadMapDataIncorrectPasscode"></a>

## TDataReadMapDataIncorrectPasscode Objects

```python
class TDataReadMapDataIncorrectPasscode(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L116)

Could not read map data because of incorrect passcode

<a id="exception.TDataAuthKeyNotFound"></a>

## TDataAuthKeyNotFound Objects

```python
class TDataAuthKeyNotFound(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L120)

Could not find authKey in TData

<a id="exception.MaxAccountLimit"></a>

## MaxAccountLimit Objects

```python
class MaxAccountLimit(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L124)

Maxed out limit for accounts per tdesktop client

<a id="exception.TDesktopUnauthorized"></a>

## TDesktopUnauthorized Objects

```python
class TDesktopUnauthorized(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L129)

TDesktop client is unauthorized

<a id="exception.TelethonUnauthorized"></a>

## TelethonUnauthorized Objects

```python
class TelethonUnauthorized(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L134)

Telethon client is unauthorized

<a id="exception.TDataSaveFailed"></a>

## TDataSaveFailed Objects

```python
class TDataSaveFailed(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L139)

Could not save TDesktop to tdata folder

<a id="exception.TDesktopNotLoaded"></a>

## TDesktopNotLoaded Objects

```python
class TDesktopNotLoaded(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L144)

TDesktop instance has no account

<a id="exception.TDesktopHasNoAccount"></a>

## TDesktopHasNoAccount Objects

```python
class TDesktopHasNoAccount(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L148)

TDesktop instance has no account

<a id="exception.TDAccountNotLoaded"></a>

## TDAccountNotLoaded Objects

```python
class TDAccountNotLoaded(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L153)

TDesktop account hasn't been loaded yet

<a id="exception.NoPasswordProvided"></a>

## NoPasswordProvided Objects

```python
class NoPasswordProvided(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L157)

You can't live without a password bro

<a id="exception.Passwordincorrect"></a>

## Passwordincorrect Objects

```python
class Passwordincorrect(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L162)

incorrect passwrd

<a id="exception.LoginFlagInvalid"></a>

## LoginFlagInvalid Objects

```python
class LoginFlagInvalid(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L167)

Invalid login flag

<a id="exception.NoInstanceMatched"></a>

## NoInstanceMatched Objects

```python
class NoInstanceMatched(OpenTeleException)
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L172)

Invalid login flag

<a id="exception.Expects"></a>

#### Expects

```python
@typing.overload
def Expects(condition: bool, exception: str = None, done: typing.Callable[[],None] = None, fail: typing.Callable[[OpenTeleException],None] = None, silent: bool = False, stack_index: int = 1) -> bool
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L178)

Expect a condition to be true, raise an OpenTeleException exception if it's not.
### Arguments
    1. condition (bool):\n
        Condition that you're expecting

### Optional
    2. message (OpenTeleException, default=None):\n
        custom exception message

    3. done (`typing.Callable[[],None]`, default=None):\n
        lambda to execute when done without error

    4. fail (`typing.Callable[[OpenTeleException],None]`, default=None):\n
        lambda to execute when the condition is False, the lambda will be execute before raising the exception

    5. silent (bool, default=False):\n
        if True then it won't raise the exception, only execute fail() lambda

    6. `stack_index` (int, default=1):\n
        stack index to raise the exception with trace back to where it happens, intended for internal usage

### Raises:

`exception` - OpenTeleException


<a id="exception.Expects"></a>

#### Expects

```python
@typing.overload
def Expects(condition: bool, exception: OpenTeleException = None, done: typing.Callable[[],None] = None, fail: typing.Callable[[OpenTeleException],None] = None, silent: bool = False, stack_index: int = 1) -> bool
```

[[view_source]](https://github.com/thedemons/opentele/blob/f517ab58fde29562675ce88704334ce45d5842c5/src\exception.py#L213)

Expect a condition to be true, raise an OpenTeleException exception if it's not.
### Arguments
    1. condition (bool):\n
        Condition that you're expecting

### Optional
    2. exception (OpenTeleException, default=None):\n
        custom exception to raise if False

    3. done (`typing.Callable[[],None]`, default=None):\n
        lambda to execute when done without error

    4. fail (`typing.Callable[[OpenTeleException],None]`, default=None):\n
        lambda to execute when the condition is False, the lambda will be execute before raising the exception

    5. silent (bool, default=False):\n
        if True then it won't raise the exception, only execute fail() lambda

    6. `stack_index` (int, default=1):\n
        stack index to raise the exception with trace back to where it happens, intended for internal usage

### Raises:

`exception` - OpenTeleException


