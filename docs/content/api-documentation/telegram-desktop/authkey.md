<!-- vim: syntax=Markdown -->

# AuthKey

## Table of Contents

* [AuthKey](#td.auth.AuthKey)

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\auth.py#L2)

<a id="td.auth.AuthKey"></a>

## AuthKey Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\td\auth.py#L17)

```python
class AuthKey(BaseObject)
```

Authorization key
Attributes:
    DcId (DcId): Data Center ID (from 1 to 5)
    type (AuthKeyType): Type of the key
    key (bytes): The actual key, 256 bytes in length


