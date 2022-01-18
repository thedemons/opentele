<!-- vim: syntax=Markdown -->

# Exceptions

<a id="exception.OpenTeleException"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">BaseException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class OpenTeleException(BaseException)
```

Base exception of the library.



<a id="exception.TFileNotFound"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L63"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TFileNotFound</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TFileNotFound(OpenTeleException)
```

Could not find or open the file



<a id="exception.TDataInvalidMagic"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L68"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDataInvalidMagic</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TDataInvalidMagic(OpenTeleException)
```

TData file has an invalid magic data, which is the first 4 bytes of the file\n

This usually mean that the file is corrupted or not in the supported formats



<a id="exception.TDataInvalidCheckSum"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L74"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDataInvalidCheckSum</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TDataInvalidCheckSum(OpenTeleException)
```

TData file has an invalid checksum\n

This usually mean that the file is corrupted or not in the supported formats



<a id="exception.TDataBadDecryptKey"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L80"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDataBadDecryptKey</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TDataBadDecryptKey(OpenTeleException)
```

Could not decrypt the data with this key\n

This usually mean that the file is password-encrypted



<a id="exception.TDataWrongPasscode"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L86"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDataWrongPasscode</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TDataWrongPasscode(OpenTeleException)
```

Wrong passcode to decrypt tdata folder\n



<a id="exception.TDataBadEncryptedDataSize"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L91"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDataBadEncryptedDataSize</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TDataBadEncryptedDataSize(OpenTeleException)
```

The encrypted data size part of the file is corrupted



<a id="exception.TDataBadDecryptedDataSize"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L95"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDataBadDecryptedDataSize</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TDataBadDecryptedDataSize(OpenTeleException)
```

The decrypted data size part of the file is corrupted



<a id="exception.TDataBadConfigData"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L99"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDataBadConfigData</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TDataBadConfigData(OpenTeleException)
```

TData contains bad config data that couldn't be parsed



<a id="exception.QDataStreamFailed"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L104"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">QDataStreamFailed</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class QDataStreamFailed(OpenTeleException)
```

Could not stream data from QDataStream\n

Please check the QDataStream.status() for more information



<a id="exception.AccountAuthKeyNotFound"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L110"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">AccountAuthKeyNotFound</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class AccountAuthKeyNotFound(OpenTeleException)
```

Account.authKey is missing, something went wrong



<a id="exception.TDataReadMapDataFailed"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L115"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDataReadMapDataFailed</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TDataReadMapDataFailed(OpenTeleException)
```

Could not read map data



<a id="exception.TDataReadMapDataIncorrectPasscode"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L119"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDataReadMapDataIncorrectPasscode</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TDataReadMapDataIncorrectPasscode(OpenTeleException)
```

Could not read map data because of incorrect passcode



<a id="exception.TDataAuthKeyNotFound"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L123"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDataAuthKeyNotFound</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TDataAuthKeyNotFound(OpenTeleException)
```

Could not find authKey in TData



<a id="exception.MaxAccountLimit"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L127"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">MaxAccountLimit</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class MaxAccountLimit(OpenTeleException)
```

Maxed out limit for accounts per tdesktop client



<a id="exception.TDesktopUnauthorized"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L132"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDesktopUnauthorized</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TDesktopUnauthorized(OpenTeleException)
```

TDesktop client is unauthorized



<a id="exception.TelethonUnauthorized"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L137"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TelethonUnauthorized</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TelethonUnauthorized(OpenTeleException)
```

Telethon client is unauthorized



<a id="exception.TDataSaveFailed"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L142"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDataSaveFailed</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TDataSaveFailed(OpenTeleException)
```

Could not save TDesktop to tdata folder



<a id="exception.TDesktopNotLoaded"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L147"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDesktopNotLoaded</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TDesktopNotLoaded(OpenTeleException)
```

TDesktop instance has no account



<a id="exception.TDesktopHasNoAccount"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L151"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDesktopHasNoAccount</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TDesktopHasNoAccount(OpenTeleException)
```

TDesktop instance has no account



<a id="exception.TDAccountNotLoaded"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L156"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDAccountNotLoaded</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class TDAccountNotLoaded(OpenTeleException)
```

TDesktop account hasn't been loaded yet



<a id="exception.NoPasswordProvided"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L160"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">NoPasswordProvided</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class NoPasswordProvided(OpenTeleException)
```

You can't live without a password bro



<a id="exception.PasswordIncorrect"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L165"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">PasswordIncorrect</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class PasswordIncorrect(OpenTeleException)
```

incorrect passwrd



<a id="exception.LoginFlagInvalid"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L170"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">LoginFlagInvalid</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class LoginFlagInvalid(OpenTeleException)
```

Invalid login flag



<a id="exception.NoInstanceMatched"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L175"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">NoInstanceMatched</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><span class="highlight"><span class="o">)</span></span>

```python
class NoInstanceMatched(OpenTeleException)
```

Invalid login flag



<a id="exception.Expects"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L181"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nf">Expects</span></span><span class="highlight"><span class="o">()</span></span>

```python
@typing.overload
def Expects(condition: bool, message: str = None, done: typing.Callable[[],None] = None, fail: typing.Callable[[OpenTeleException],None] = None, silent: bool = False, stack_index: int = 1) -> bool
```

Expect a condition to be <span class="highlight"><span class="kc">True</span></span>, raise an <a class="codehl codehl_obj" href="exceptions#openteleexception-objects"><b>OpenTeleException</b></a> if it's not.

### Arguments:
| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <span class="highlight"><span class="n">condition</span></span> | <span class="highlight"><span class="bp">bool</span></span> |  | Condition that you're expecting. |
| <span class="highlight"><span class="n">message</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | Custom exception message |
| <span class="highlight"><span class="n">done</span></span> | <span class="highlight"><span class="kc">lambda</span></span> | <span class="highlight"><span class="kc">None</span></span> | lambda to execute when done without error |
| <span class="highlight"><span class="n">fail</span></span> | <span class="highlight"><span class="kc">lambda</span></span> | <span class="highlight"><span class="kc">None</span></span> | lambda to execute when the condition is False, the lambda will be execute before raising the exception. |
| <span class="highlight"><span class="n">silent</span></span> | <span class="highlight"><span class="bp">bool</span></span> | <span class="highlight"><span class="kc">False</span></span> | if True then it won't raise the exception, only execute fail lambda. |
| <span class="highlight"><span class="n">stack_index</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">1</span></span> | stack index to raise the exception with trace back to where it happens, intended for internal usage. |


### Raises:

<a class="codehl codehl_obj" href="exceptions#openteleexception-objects"><b>OpenTeleException</b></a>: exception





<a id="exception.Expects"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/exception.py#L215"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="nf">Expects</span></span><span class="highlight"><span class="o">()</span></span>

```python
@typing.overload
def Expects(condition: bool, exception: OpenTeleException = None, done: typing.Callable[[],None] = None, fail: typing.Callable[[OpenTeleException],None] = None, silent: bool = False, stack_index: int = 1) -> bool
```

Expect a condition to be <span class="highlight"><span class="kc">True</span></span>, raise an <a class="codehl codehl_obj" href="exceptions#openteleexception-objects"><b>OpenTeleException</b></a> if it's not.

### Arguments:
| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <span class="highlight"><span class="n">condition</span></span> | <span class="highlight"><span class="bp">bool</span></span> |  | Condition that you're expecting. |
| <span class="highlight"><span class="n">message</span></span> | <a class="codehl codehl_obj" href="exceptions#openteleexception-objects"><b>OpenTeleException</b></a> | <span class="highlight"><span class="kc">None</span></span> | Custom exception. |
| <span class="highlight"><span class="n">done</span></span> | <span class="highlight"><span class="kc">lambda</span></span> | <span class="highlight"><span class="kc">None</span></span> | lambda to execute when done without error. |
| <span class="highlight"><span class="n">fail</span></span> | <span class="highlight"><span class="kc">lambda</span></span> | <span class="highlight"><span class="kc">None</span></span> | lambda to execute when the condition is False, the lambda will be execute before raising the exception. |
| <span class="highlight"><span class="n">silent</span></span> | <span class="highlight"><span class="bp">bool</span></span> | <span class="highlight"><span class="kc">False</span></span> | if True then it won't raise the exception, only execute fail lambda. |
| <span class="highlight"><span class="n">stack_index</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">1</span></span> | stack index to raise the exception with trace back to where it happens, intended for internal usage. |


### Raises:

<a class="codehl codehl_obj" href="exceptions#openteleexception-objects"><b>OpenTeleException</b></a>: exception





