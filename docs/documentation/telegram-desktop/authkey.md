<!-- vim: syntax=Markdown -->

# AuthKey

<a id="td.auth.AuthKeyType"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">AuthKeyType</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/auth.py#L11" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
class AuthKeyType(IntEnum)
```

Type of <a class="codehl codehl_obj" href="#td.auth.AuthKey"><b>AuthKey</b></a><br>
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="n">Generated</span></span> | <span class="highlight"><span class="nc">IntEnum</span></span> | Generated key |
| <span class="highlight"><span class="n">Temporary</span></span> | <span class="highlight"><span class="nc">IntEnum</span></span> | Temporary key |
| <span class="highlight"><span class="n">ReadFromFile</span></span> | <span class="highlight"><span class="nc">IntEnum</span></span> | Key red from file |
| <span class="highlight"><span class="n">Local</span></span> | <span class="highlight"><span class="nc">IntEnum</span></span> | Local key |



<a id="td.auth.AuthKey"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">AuthKey</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/td/auth.py#L35" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
class AuthKey(BaseObject)
```

Authorization key used for [MTProto](https://core.telegram.org/mtproto)
It's also used to encrypt and decrypt local tdata<br>
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <span class="highlight"><span class="nc">DcId</span></span> | <span class="highlight"><span class="nc">DcId</span></span> | Data Center ID (from 1 to 5). |
| <span class="highlight"><span class="bp">type</span></span> | <a class="codehl codehl_obj" href="#td.auth.AuthKeyType"><b>AuthKeyType</b></a> | Type of the key. |
| <span class="highlight"><span class="n">key</span></span> | <span class="highlight"><span class="bp">bytes</span></span> | The actual key, 256 <span class="highlight"><span class="bp">bytes</span></span> in length. |



