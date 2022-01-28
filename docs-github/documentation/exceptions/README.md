<!-- vim: syntax=Markdown -->

# Home

<a id="exception.OpenTeleException"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">OpenTeleException</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class OpenTeleException(BaseException)
```

Base exception of the library.<br>


<a id="exception.TFileNotFound"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TFileNotFound</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L69"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class TFileNotFound(OpenTeleException)
```

Could not find or open the file<br>


<a id="exception.TDataInvalidMagic"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDataInvalidMagic</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L75"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class TDataInvalidMagic(OpenTeleException)
```

TData file has an invalid magic data, which is the first 4 bytes of the file\n<br>
This usually mean that the file is corrupted or not in the supported formats<br>


<a id="exception.TDataInvalidCheckSum"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDataInvalidCheckSum</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L82"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class TDataInvalidCheckSum(OpenTeleException)
```

TData file has an invalid checksum\n<br>
This usually mean that the file is corrupted or not in the supported formats<br>


<a id="exception.TDataBadDecryptKey"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDataBadDecryptKey</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L89"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class TDataBadDecryptKey(OpenTeleException)
```

Could not decrypt the data with this key\n<br>
This usually mean that the file is password-encrypted


<a id="exception.TDataWrongPasscode"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDataWrongPasscode</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L96"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class TDataWrongPasscode(OpenTeleException)
```

Wrong passcode to decrypt tdata folder\n<br>


<a id="exception.TDataBadEncryptedDataSize"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDataBadEncryptedDataSize</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L102"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class TDataBadEncryptedDataSize(OpenTeleException)
```

The encrypted data size part of the file is corrupted<br>


<a id="exception.TDataBadDecryptedDataSize"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDataBadDecryptedDataSize</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L108"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class TDataBadDecryptedDataSize(OpenTeleException)
```

The decrypted data size part of the file is corrupted<br>


<a id="exception.TDataBadConfigData"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDataBadConfigData</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L114"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class TDataBadConfigData(OpenTeleException)
```

TData contains bad config data that couldn't be parsed<br>


<a id="exception.QDataStreamFailed"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">QDataStreamFailed</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L120"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class QDataStreamFailed(OpenTeleException)
```

Could not stream data from QDataStream\n<br>
Please check the QDataStream.status() for more information<br>


<a id="exception.AccountAuthKeyNotFound"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">AccountAuthKeyNotFound</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L127"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class AccountAuthKeyNotFound(OpenTeleException)
```

Account.authKey is missing, something went wrong<br>


<a id="exception.TDataReadMapDataFailed"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDataReadMapDataFailed</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L133"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class TDataReadMapDataFailed(OpenTeleException)
```

Could not read map data<br>


<a id="exception.TDataReadMapDataIncorrectPasscode"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDataReadMapDataIncorrectPasscode</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L139"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class TDataReadMapDataIncorrectPasscode(OpenTeleException)
```

Could not read map data because of incorrect passcode<br>


<a id="exception.TDataAuthKeyNotFound"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDataAuthKeyNotFound</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L145"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class TDataAuthKeyNotFound(OpenTeleException)
```

Could not find authKey in TData<br>


<a id="exception.MaxAccountLimit"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">MaxAccountLimit</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L151"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class MaxAccountLimit(OpenTeleException)
```

Maxed out limit for accounts per tdesktop client<br>


<a id="exception.TDesktopUnauthorized"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDesktopUnauthorized</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L157"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class TDesktopUnauthorized(OpenTeleException)
```

TDesktop client is unauthorized<br>


<a id="exception.TelethonUnauthorized"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TelethonUnauthorized</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L163"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class TelethonUnauthorized(OpenTeleException)
```

Telethon client is unauthorized<br>


<a id="exception.TDataSaveFailed"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDataSaveFailed</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L169"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class TDataSaveFailed(OpenTeleException)
```

Could not save TDesktop to tdata folder<br>


<a id="exception.TDesktopNotLoaded"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDesktopNotLoaded</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L175"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class TDesktopNotLoaded(OpenTeleException)
```

TDesktop instance has no account<br>


<a id="exception.TDesktopHasNoAccount"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDesktopHasNoAccount</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L181"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class TDesktopHasNoAccount(OpenTeleException)
```

TDesktop instance has no account<br>


<a id="exception.TDAccountNotLoaded"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">TDAccountNotLoaded</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L187"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class TDAccountNotLoaded(OpenTeleException)
```

TDesktop account hasn't been loaded yet<br>


<a id="exception.NoPasswordProvided"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">NoPasswordProvided</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L193"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class NoPasswordProvided(OpenTeleException)
```

You can't live without a password bro<br>


<a id="exception.PasswordIncorrect"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">PasswordIncorrect</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L199"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class PasswordIncorrect(OpenTeleException)
```

incorrect passwrd<br>


<a id="exception.LoginFlagInvalid"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">LoginFlagInvalid</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L205"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class LoginFlagInvalid(OpenTeleException)
```

Invalid login flag<br>


<a id="exception.NoInstanceMatched"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">NoInstanceMatched</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L211"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class NoInstanceMatched(OpenTeleException)
```

Invalid login flag<br>


<a id="exception.Expects"></a>


---
## <span class="highlight"><span class="nf">Expects</span></span><span class="highlight"><span class="o">()</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L218"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
@typing.overload
def Expects(condition: bool, message: str = None, done: typing.Callable[[], None] = None, fail: typing.Callable[[OpenTeleException], None] = None, silent: bool = False, stack_index: int = 1) -> bool
```

Expect a condition to be <span class="highlight"><span class="kc">True</span></span>, raise an <a class="codehl codehl_obj" href="home.md#class-openteleexception"><b>OpenTeleException</b></a> if it's not.<br>
<h3>Arguments:</h3>

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <span class="highlight"><span class="n">condition</span></span> | <span class="highlight"><span class="bp">bool</span></span> |  | Condition that you're expecting. |
| <span class="highlight"><span class="n">message</span></span> | <span class="highlight"><span class="bp">str</span></span> | <span class="highlight"><span class="kc">None</span></span> | Custom exception message |
| <span class="highlight"><span class="n">done</span></span> | <span class="highlight"><span class="kc">lambda</span></span> | <span class="highlight"><span class="kc">None</span></span> | lambda to execute when done without error |
| <span class="highlight"><span class="n">fail</span></span> | <span class="highlight"><span class="kc">lambda</span></span> | <span class="highlight"><span class="kc">None</span></span> | lambda to execute when the condition is False, the lambda will be execute before raising the exception. |
| <span class="highlight"><span class="n">silent</span></span> | <span class="highlight"><span class="bp">bool</span></span> | <span class="highlight"><span class="kc">False</span></span> | if True then it won't raise the exception, only execute fail lambda. |
| <span class="highlight"><span class="n">stack_index</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">1</span></span> | stack index to raise the exception with trace back to where it happens, intended for internal usage. |

<h3>Raises:</h3>

<a class="codehl codehl_obj" href="home.md#class-openteleexception"><b>OpenTeleException</b></a> : exception



<a id="exception.Expects"></a>


---
## <span class="highlight"><span class="nf">Expects</span></span><span class="highlight"><span class="o">()</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/exception.py#L253"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
@typing.overload
def Expects(condition: bool, exception: OpenTeleException = None, done: typing.Callable[[], None] = None, fail: typing.Callable[[OpenTeleException], None] = None, silent: bool = False, stack_index: int = 1) -> bool
```

Expect a condition to be <span class="highlight"><span class="kc">True</span></span>, raise an <a class="codehl codehl_obj" href="home.md#class-openteleexception"><b>OpenTeleException</b></a> if it's not.<br>
<h3>Arguments:</h3>

| Name | Type | Default | Description |
| :--- | :--: | :-----: | :---------- |
| <span class="highlight"><span class="n">condition</span></span> | <span class="highlight"><span class="bp">bool</span></span> |  | Condition that you're expecting. |
| <span class="highlight"><span class="n">message</span></span> | <a class="codehl codehl_obj" href="home.md#class-openteleexception"><b>OpenTeleException</b></a> | <span class="highlight"><span class="kc">None</span></span> | Custom exception. |
| <span class="highlight"><span class="n">done</span></span> | <span class="highlight"><span class="kc">lambda</span></span> | <span class="highlight"><span class="kc">None</span></span> | lambda to execute when done without error. |
| <span class="highlight"><span class="n">fail</span></span> | <span class="highlight"><span class="kc">lambda</span></span> | <span class="highlight"><span class="kc">None</span></span> | lambda to execute when the condition is False, the lambda will be execute before raising the exception. |
| <span class="highlight"><span class="n">silent</span></span> | <span class="highlight"><span class="bp">bool</span></span> | <span class="highlight"><span class="kc">False</span></span> | if True then it won't raise the exception, only execute fail lambda. |
| <span class="highlight"><span class="n">stack_index</span></span> | <span class="highlight"><span class="bp">int</span></span> | <span class="highlight"><span class="mi">1</span></span> | stack index to raise the exception with trace back to where it happens, intended for internal usage. |

<h3>Raises:</h3>

<a class="codehl codehl_obj" href="home.md#class-openteleexception"><b>OpenTeleException</b></a> : exception



