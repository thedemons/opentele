<!-- vim: syntax=Markdown -->

# LoginFlag

<a id="api.LoginFlag"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">LoginFlag</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/api.py#L623"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class LoginFlag(int)
```

Login flag for converting sessions between <a class="codehl codehl_obj" href="../../documentation/telegram-desktop/tdesktop.md#class-tdesktop"><b>TDesktop</b></a> and <a class="codehl codehl_obj" href="../../documentation/telethon/telegramclient.md#class-telegramclient"><b>TelegramClient</b></a>.<br>
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <a class="codehl codehl_obj" href="loginflag.md#class-usecurrentsession"><b>UseCurrentSession</b></a> | <a class="codehl codehl_obj" href="loginflag.md#class-loginflag"><b>LoginFlag</b></a> | Use the current session. |
| <a class="codehl codehl_obj" href="loginflag.md#class-createnewsession"><b>CreateNewSession</b></a> | <a class="codehl codehl_obj" href="loginflag.md#class-loginflag"><b>LoginFlag</b></a> | Create a new session. |

<h3>Related:</h3>


- <a class="codehl codehl_obj" href="../../documentation/telegram-desktop/tdesktop.md#class-tdesktop"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_function" href="../../documentation/telegram-desktop/tdesktop.md#totelethon"><b>ToTelethon</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span>

- <a class="codehl codehl_obj" href="../../documentation/telegram-desktop/tdesktop.md#class-tdesktop"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_function" href="../../documentation/telegram-desktop/tdesktop.md#fromtelethon"><b>FromTelethon</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span>

- <a class="codehl codehl_obj" href="../../documentation/telethon/telegramclient.md#class-telegramclient"><b>TelegramClient</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_function" href="../../documentation/telethon/telegramclient.md#totdesktop"><b>ToTDesktop</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span>

- <a class="codehl codehl_obj" href="../../documentation/telethon/telegramclient.md#class-telegramclient"><b>TelegramClient</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_function" href="../../documentation/telethon/telegramclient.md#fromtdesktop"><b>FromTDesktop</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span>



<a id="api.UseCurrentSession"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">UseCurrentSession</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/api.py#L640"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class UseCurrentSession(LoginFlag)
```

Use the current session.<br>

- Convert an already-logged in session of <span class="highlight"><span class="n">Telegram</span></span> <span class="highlight"><span class="n">Desktop</span></span> to <span class="highlight"><span class="n">Telethon</span></span> and vice versa.

- The "session" is just an 256-bytes <a class="codehl codehl_obj" href="../../documentation/telegram-desktop/authkey.md#class-authkey"><b>AuthKey</b></a> that get stored in <span class="highlight"><span class="n">tdata</span></span> <span class="highlight"><span class="n">folder</span></span> or Telethon <span class="highlight"><span class="n">session</span></span> <span class="highlight"><span class="n">files</span></span> [(under sqlite3 format)](https://docs.telethon.dev/en/latest/concepts/sessions.html?highlight=sqlite3#what-are-sessions).

- <a class="codehl codehl_obj" href="loginflag.md#class-usecurrentsession"><b>UseCurrentSession</b></a>'s only job is to read this key and convert it to one another.

| :warning: Use at your own risk! |
| :--- |
|     You should only use the same consistant API through out the session.<br/>    Don't use a same session with multiple different APIs, you might be banned. |



<a id="api.CreateNewSession"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">CreateNewSession</span></span><a href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/api.py#L656"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

```python
class CreateNewSession(LoginFlag)
```

Create a new session.<br>

- Use the <span class="highlight"><span class="n">current</span></span> <span class="highlight"><span class="n">session</span></span> to authorize the <span class="highlight"><span class="n">new</span></span> <span class="highlight"><span class="n">session</span></span> by [Login via QR code](https://core.telegram.org/api/qr-login).

- This works just like when you signing into <span class="highlight"><span class="n">Telegram</span></span> using <span class="highlight"><span class="n">QR</span></span> <span class="highlight"><span class="n">Login</span></span> on mobile devices.

- Although <span class="highlight"><span class="n">Telegram</span></span> <span class="highlight"><span class="n">Desktop</span></span> doesn't let you authorize other sessions via <span class="highlight"><span class="n">QR</span></span> <span class="highlight"><span class="n">Code</span></span> *(or it doesn't have that feature)*, it is still available across all platforms <span class="highlight"><span class="p">(</span></span><a class="codehl codehl_obj" href="../authorization/api.md#class-api"><b>APIs</b></a><span class="highlight"><span class="p">)</span></span>.

| :heavy_check_mark: Safe to use |
| :--- |
|     You can always use <span class="highlight"><span class="n">CreateNewSessions</span></span> with any APIs, it can be different from the API that originally created the session. |



