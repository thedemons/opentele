# MTP

## Table of Contents

* [td.mtp](#td.mtp)
  * [annotations](#td.mtp.annotations)
  * [\*](#td.mtp.*)
  * [td](#td.mtp.td)
  * [MTP](#td.mtp.MTP)
    * [Environment](#td.mtp.MTP.Environment)
    * [RSAPublicKey](#td.mtp.MTP.RSAPublicKey)
    * [DcOptions](#td.mtp.MTP.DcOptions)
    * [ConfigFields](#td.mtp.MTP.ConfigFields)
    * [Config](#td.mtp.MTP.Config)

<a id="td.mtp"></a>

# td.mtp

[[view_source]](https://github.com/thedemons/opentele/blob/e63c9bb552f72354268d8f1b58db18df5ab4e0ea/src\td\mtp.py#L1)

<a id="td.mtp.annotations"></a>

## annotations

[[view_source]](https://github.com/thedemons/opentele/blob/e63c9bb552f72354268d8f1b58db18df5ab4e0ea/src\td\mtp.py#L1)

<a id="td.mtp.*"></a>

## \*

[[view_source]](https://github.com/thedemons/opentele/blob/e63c9bb552f72354268d8f1b58db18df5ab4e0ea/src\td\mtp.py#L3)

<a id="td.mtp.td"></a>

## td

[[view_source]](https://github.com/thedemons/opentele/blob/e63c9bb552f72354268d8f1b58db18df5ab4e0ea/src\td\mtp.py#L4)

<a id="td.mtp.MTP"></a>

## MTP Objects

```python
class MTP(BaseObject)
```

[[view_source]](https://github.com/thedemons/opentele/blob/e63c9bb552f72354268d8f1b58db18df5ab4e0ea/src\td\mtp.py#L9)

MTProto Protocal
https://core.telegram.org/mtproto

<a id="td.mtp.MTP.Environment"></a>

## Environment Objects

```python
class Environment(int)
```

[[view_source]](https://github.com/thedemons/opentele/blob/e63c9bb552f72354268d8f1b58db18df5ab4e0ea/src\td\mtp.py#L16)

Enviroment flag for MTP.Config

<a id="td.mtp.MTP.RSAPublicKey"></a>

## RSAPublicKey Objects

```python
class RSAPublicKey(BaseObject)
```

[[view_source]](https://github.com/thedemons/opentele/blob/e63c9bb552f72354268d8f1b58db18df5ab4e0ea/src\td\mtp.py#L23)

To be added

<a id="td.mtp.MTP.DcOptions"></a>

## DcOptions Objects

```python
class DcOptions(BaseObject)
```

[[view_source]](https://github.com/thedemons/opentele/blob/e63c9bb552f72354268d8f1b58db18df5ab4e0ea/src\td\mtp.py#L28)

Data Center Options, providing information about DC ip, port,.. etc

<a id="td.mtp.MTP.DcOptions.Address"></a>

## Address Objects

```python
class Address(int)
```

[[view_source]](https://github.com/thedemons/opentele/blob/e63c9bb552f72354268d8f1b58db18df5ab4e0ea/src\td\mtp.py#L167)

Flag used for MTP.DcOptions.Endpoint

<a id="td.mtp.MTP.DcOptions.Protocol"></a>

## Protocol Objects

```python
class Protocol(int)
```

[[view_source]](https://github.com/thedemons/opentele/blob/e63c9bb552f72354268d8f1b58db18df5ab4e0ea/src\td\mtp.py#L174)

Flag used for MTP.DcOptions.Endpoint

<a id="td.mtp.MTP.DcOptions.Flag"></a>

## Flag Objects

```python
class Flag(int)
```

[[view_source]](https://github.com/thedemons/opentele/blob/e63c9bb552f72354268d8f1b58db18df5ab4e0ea/src\td\mtp.py#L181)

Flag used for MTP.DcOptions.Endpoint

<a id="td.mtp.MTP.DcOptions.Endpoint"></a>

## Endpoint Objects

```python
class Endpoint(BaseObject)
```

[[view_source]](https://github.com/thedemons/opentele/blob/e63c9bb552f72354268d8f1b58db18df5ab4e0ea/src\td\mtp.py#L193)

Data center endpoint information

<a id="td.mtp.MTP.ConfigFields"></a>

## ConfigFields Objects

```python
class ConfigFields(BaseObject)
```

[[view_source]](https://github.com/thedemons/opentele/blob/e63c9bb552f72354268d8f1b58db18df5ab4e0ea/src\td\mtp.py#L205)

Configuration data for MTP.Config

<a id="td.mtp.MTP.Config"></a>

## Config Objects

```python
class Config(BaseObject)
```

[[view_source]](https://github.com/thedemons/opentele/blob/e63c9bb552f72354268d8f1b58db18df5ab4e0ea/src\td\mtp.py#L241)

Configuration of MTProto

