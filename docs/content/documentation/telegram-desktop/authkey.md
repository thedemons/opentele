<!-- vim: syntax=Markdown -->

# AuthKey

<a id="td.auth.AuthKeyType"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">AuthKeyType</span></span><a href="https://github.com/thedemons/opentele/blob/a4ab2f0e6e9f603b2207d3c82f27c76ecba4f614/src/td/auth.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class AuthKeyType(IntEnum)
```

Type of <a class="codehl codehl_obj" href="authkey.md#authkey-objects"><b>AuthKey</b></a><br>
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">Generated</span></span> | <span class="highlight"><span class="nc">IntEnum</span></span> | Generated key |
| <span class="highlight"><span class="n">Temporary</span></span> | <span class="highlight"><span class="nc">IntEnum</span></span> | Temporary key |
| <span class="highlight"><span class="n">ReadFromFile</span></span> | <span class="highlight"><span class="nc">IntEnum</span></span> | Key red from file |
| <span class="highlight"><span class="n">Local</span></span> | <span class="highlight"><span class="nc">IntEnum</span></span> | Local key |



<a id="td.auth.AuthKey"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">AuthKey</span></span><a href="https://github.com/thedemons/opentele/blob/a4ab2f0e6e9f603b2207d3c82f27c76ecba4f614/src/td/auth.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class AuthKey(BaseObject)
```

Authorization key used for [MTProto](https://core.telegram.org/mtproto)
It's also used to encrypt and decrypt local tdata<br>
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="nc">DcId</span></span> | <span class="highlight"><span class="nc">DcId</span></span><span class="highlight"><span class="p">)</span></span><span class="highlight"><span class="p">:</span></span><span class="highlight"><span class="nf">DataCenterID</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="n">from1to5</span></span> | . |
| <span class="highlight"><span class="bp">type</span></span> | <a class="codehl codehl_obj" href="authkey.md#authkeytype-objects"><b>AuthKeyType</b></a> | Type of the key. |
| <span class="highlight"><span class="n">key</span></span> | <span class="highlight"><span class="bp">bytes</span></span> | The actual key, 256 <span class="highlight"><span class="bp">bytes</span></span> in length. |



