# AuthKey

## Table of Contents

* [td.auth](#td.auth)
  * [annotations](#td.auth.annotations)
  * [\*](#td.auth.*)
  * [td](#td.auth.td)
  * [hashlib](#td.auth.hashlib)
  * [AuthKey](#td.auth.AuthKey)

<a id="td.auth"></a>

# td.auth

[[view_source]](https://github.com/thedemons/opentele/blob/dee2df0aaab7f6f44f1259af12b2598a7cd9bcb0/src\td\auth.py#L1)

<a id="td.auth.annotations"></a>

## annotations

[[view_source]](https://github.com/thedemons/opentele/blob/dee2df0aaab7f6f44f1259af12b2598a7cd9bcb0/src\td\auth.py#L1)

<a id="td.auth.*"></a>

## \*

[[view_source]](https://github.com/thedemons/opentele/blob/dee2df0aaab7f6f44f1259af12b2598a7cd9bcb0/src\td\auth.py#L2)

<a id="td.auth.td"></a>

## td

[[view_source]](https://github.com/thedemons/opentele/blob/dee2df0aaab7f6f44f1259af12b2598a7cd9bcb0/src\td\auth.py#L3)

<a id="td.auth.hashlib"></a>

## hashlib

[[view_source]](https://github.com/thedemons/opentele/blob/dee2df0aaab7f6f44f1259af12b2598a7cd9bcb0/src\td\auth.py#L5)

<a id="td.auth.AuthKey"></a>

## AuthKey Objects

```python
class AuthKey(BaseObject)
```

[[view_source]](https://github.com/thedemons/opentele/blob/dee2df0aaab7f6f44f1259af12b2598a7cd9bcb0/src\td\auth.py#L16)

Authorization key
Attributes:
    DcId (DcId): Data Center ID (from 1 to 5)
    type (AuthKeyType): Type of the key
    key (bytes): The actual key, 256 bytes in length


