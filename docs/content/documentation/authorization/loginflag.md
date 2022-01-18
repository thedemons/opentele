<!-- vim: syntax=Markdown -->

# LoginFlag

<a id="api.LoginFlag"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/api.py#L561"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">LoginFlag</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">int</span></span><span class="highlight"><span class="o">)</span></span>

```python
class LoginFlag(int)
```

Login flag for converting sessions between <a class="codehl codehl_obj" href="../../documentation/telegram-desktop/tdesktop#tdesktop-objects"><b>TDesktop</b></a> and <a class="codehl codehl_obj" href="../../documentation/telethon/telegramclient#telegramclient-objects"><b>TelegramClient</b></a>.

### Attributes:
| Name | Type | Description |
| :--- | :--: | :---------- |
| <a class="codehl codehl_obj" href="loginflag#usecurrentsession-objects"><b>UseCurrentSession</b></a> | <a class="codehl codehl_obj" href="loginflag#loginflag-objects"><b>LoginFlag</b></a> | Use the current session. |
| <a class="codehl codehl_obj" href="loginflag#createnewsession-objects"><b>CreateNewSession</b></a> | <a class="codehl codehl_obj" href="loginflag#loginflag-objects"><b>LoginFlag</b></a> | Create a new session. |


### Related:

<a class="codehl codehl_obj" href="../../documentation/telegram-desktop/tdesktop#tdesktop-objects"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><span class="highlight"><span class="nf">ToTelethon</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span>

- <a class="codehl codehl_obj" href="../../documentation/telegram-desktop/tdesktop#tdesktop-objects"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_function" href="../../documentation/telegram-desktop/tdesktop#tdesktopfromtelethon"><b>FromTelethon</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span>

- <a class="codehl codehl_obj" href="../../documentation/telethon/telegramclient#telegramclient-objects"><b>TelegramClient</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_function" href="../../documentation/telethon/telegramclient#telegramclienttotdesktop"><b>ToTDesktop</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span>

- <a class="codehl codehl_obj" href="../../documentation/telethon/telegramclient#telegramclient-objects"><b>TelegramClient</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_function" href="../../documentation/telethon/telegramclient#telegramclientfromtdesktop"><b>FromTDesktop</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span>





<a id="api.UseCurrentSession"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/api.py#L577"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">UseCurrentSession</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">LoginFlag</span></span><span class="highlight"><span class="o">)</span></span>

```python
class UseCurrentSession(LoginFlag)
```

Use the current session.

Convert an already-logged in session of <span class="highlight"><span class="n">Telegram</span></span> <span class="highlight"><span class="n">Desktop</span></span> to <span class="highlight"><span class="n">Telethon</span></span> and vice versa.

The "session" is just an 256-bytes <a class="codehl codehl_obj" href="../../documentation/telegram-desktop/authkey#authkey-objects"><b>AuthKey</b></a> that get stored in <span class="highlight"><span class="n">tdata</span></span> <span class="highlight"><span class="n">folder</span></span> or Telethon <span class="highlight"><span class="n">session</span></span> <span class="highlight"><span class="n">files</span></span> [(under sqlite3 format)](https://docs.telethon.dev/en/latest/concepts/sessions.html?highlight=sqlite3#what-are-sessions).

<a class="codehl codehl_obj" href="loginflag#usecurrentsession-objects"><b>UseCurrentSession</b></a>'s only job is to read this key and convert it to one another.



<a id="api.CreateNewSession"></a>

---

## <a href="https://github.com/thedemons/opentele/blob/aa00decd853fe25eba189b66c18d832de5a37ede/src/api.py#L586"><img align="right" style="float:right;" src="https://img.shields.io/badge/view-source-green"></a>

<span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">CreateNewSession</span></span><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="nc">LoginFlag</span></span><span class="highlight"><span class="o">)</span></span>

```python
class CreateNewSession(LoginFlag)
```

Create a new session.

Use the <span class="highlight"><span class="n">current</span></span> <span class="highlight"><span class="n">session</span></span> to authorize the <span class="highlight"><span class="n">new</span></span> <span class="highlight"><span class="n">session</span></span> by [Login via QR code](https://core.telegram.org/api/qr-login).

This works just like when you signing into <span class="highlight"><span class="n">Telegram</span></span> using <span class="highlight"><span class="n">QR</span></span> <span class="highlight"><span class="n">Login</span></span> on mobile devices.

Although <span class="highlight"><span class="n">Telegram</span></span> <span class="highlight"><span class="n">Desktop</span></span> doesn't let you authorize other sessions via <span class="highlight"><span class="n">QR</span></span> <span class="highlight"><span class="n">Code</span></span> *(or it doesn't have that feature)*, it is still available across all platforms <span class="highlight"><span class="p">(</span></span><a class="codehl codehl_obj" href="../authorization/api#api-objects"><b>APIs</b></a><span class="highlight"><span class="p">)</span></span>.



