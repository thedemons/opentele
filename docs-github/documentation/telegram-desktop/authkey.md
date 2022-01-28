<!-- vim: syntax=Markdown -->

# AuthKey

<a id="td.auth.AuthKeyType"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">AuthKeyType</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/auth.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class AuthKeyType(IntEnum)
```

Type of <a class="codehl codehl_obj" href="authkey.md#class-authkey"><b>AuthKey</b></a><br>
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">Generated</span></span> | <span class="highlight"><span class="nc">IntEnum</span></span> | Generated key |
| <span class="highlight"><span class="n">Temporary</span></span> | <span class="highlight"><span class="nc">IntEnum</span></span> | Temporary key |
| <span class="highlight"><span class="n">ReadFromFile</span></span> | <span class="highlight"><span class="nc">IntEnum</span></span> | Key red from file |
| <span class="highlight"><span class="n">Local</span></span> | <span class="highlight"><span class="nc">IntEnum</span></span> | Local key |



<a id="td.auth.AuthKey"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">AuthKey</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/auth.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class AuthKey(BaseObject)
```

Authorization key used for [MTProto](https://core.telegram.org/mtproto)
It's also used to encrypt and decrypt local tdata<br>
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="nc">DcId</span></span> | <span class="highlight"><span class="nc">DcId</span></span> | Data Center ID (from 1 to 5). |
| <span class="highlight"><span class="bp">type</span></span> | <a class="codehl codehl_obj" href="authkey.md#class-authkeytype"><b>AuthKeyType</b></a> | Type of the key. |
| <span class="highlight"><span class="n">key</span></span> | <span class="highlight"><span class="bp">bytes</span></span> | The actual key, 256 <span class="highlight"><span class="bp">bytes</span></span> in length. |



