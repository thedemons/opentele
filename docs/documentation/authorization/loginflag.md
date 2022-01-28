<!-- vim: syntax=Markdown -->

# LoginFlag

<a id="api.LoginFlag"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">LoginFlag</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/api.py#L623" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
class LoginFlag(int)
```

Login flag for converting sessions between <a class="codehl codehl_obj" href="../../telegram-desktop/tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a> and <a class="codehl codehl_obj" href="../../telethon/telegramclient#tl.telethon.TelegramClient"><b>TelegramClient</b></a>.<br>
<h3>Attributes:</h3>

| Name | Type | Description |
| :--- | :--: | :---------- |
| <a class="codehl codehl_obj" href="#api.UseCurrentSession"><b>UseCurrentSession</b></a> | <a class="codehl codehl_obj" href="#api.LoginFlag"><b>LoginFlag</b></a> | Use the current session. |
| <a class="codehl codehl_obj" href="#api.CreateNewSession"><b>CreateNewSession</b></a> | <a class="codehl codehl_obj" href="#api.LoginFlag"><b>LoginFlag</b></a> | Create a new session. |

<h3>Related:</h3>


- <a class="codehl codehl_obj" href="../../telegram-desktop/tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_function" href="../../telegram-desktop/tdesktop#td.tdesktop.TDesktop.ToTelethon"><b>ToTelethon</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span>

- <a class="codehl codehl_obj" href="../../telegram-desktop/tdesktop#td.tdesktop.TDesktop"><b>TDesktop</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_function" href="../../telegram-desktop/tdesktop#td.tdesktop.TDesktop.FromTelethon"><b>FromTelethon</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span>

- <a class="codehl codehl_obj" href="../../telethon/telegramclient#tl.telethon.TelegramClient"><b>TelegramClient</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_function" href="../../telethon/telegramclient#tl.telethon.TelegramClient.ToTDesktop"><b>ToTDesktop</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span>

- <a class="codehl codehl_obj" href="../../telethon/telegramclient#tl.telethon.TelegramClient"><b>TelegramClient</b></a><span class="highlight"><span class="o">.</span></span><a class="codehl codehl_function" href="../../telethon/telegramclient#tl.telethon.TelegramClient.FromTDesktop"><b>FromTDesktop</b></a><span class="highlight"><span class="o">(</span></span><span class="highlight"><span class="p">)</span></span>



<a id="api.UseCurrentSession"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">UseCurrentSession</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/api.py#L640" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
class UseCurrentSession(LoginFlag)
```

Use the current session.<br>

- Convert an already-logged in session of <span class="highlight"><span class="n">Telegram</span></span> <span class="highlight"><span class="n">Desktop</span></span> to <span class="highlight"><span class="n">Telethon</span></span> and vice versa.

- The "session" is just an 256-bytes <a class="codehl codehl_obj" href="../../telegram-desktop/authkey#td.auth.AuthKey"><b>AuthKey</b></a> that get stored in <span class="highlight"><span class="n">tdata</span></span> <span class="highlight"><span class="n">folder</span></span> or Telethon <span class="highlight"><span class="n">session</span></span> <span class="highlight"><span class="n">files</span></span> [(under sqlite3 format)](https://docs.telethon.dev/en/latest/concepts/sessions.html?highlight=sqlite3#what-are-sessions).

- <a class="codehl codehl_obj" href="#api.UseCurrentSession"><b>UseCurrentSession</b></a>'s only job is to read this key and convert it to one another.
???+ warning "Use at your own risk!"
    You should only use the same consistant API through out the session.<br/>
    Don't use a same session with multiple different APIs, you might be banned.



<a id="api.CreateNewSession"></a>


---
## <span class="highlight"><span class="k">class </span></span><span class="highlight"><span class="nc">CreateNewSession</span></span><a class="source-link" href="https://github.com/thedemons/opentele/blob/9e18947bea63265404745db4428d49bdf50649e3/src/api.py#L656" title="Source"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H4.75a.75.75 0 0 1 0-1.5H19a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4H5a.5.5 0 0 0-.5.5v6.25a.75.75 0 0 1-1.5 0V3zm12-.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5z"></path><path d="M4.53 12.24a.75.75 0 0 1-.039 1.06l-2.639 2.45 2.64 2.45a.75.75 0 1 1-1.022 1.1l-3.23-3a.75.75 0 0 1 0-1.1l3.23-3a.75.75 0 0 1 1.06.04zm3.979 1.06a.75.75 0 1 1 1.02-1.1l3.231 3a.75.75 0 0 1 0 1.1l-3.23 3a.75.75 0 1 1-1.021-1.1l2.639-2.45-2.64-2.45z"></path></svg></span></a>

```python
class CreateNewSession(LoginFlag)
```

Create a new session.<br>

- Use the <span class="highlight"><span class="n">current</span></span> <span class="highlight"><span class="n">session</span></span> to authorize the <span class="highlight"><span class="n">new</span></span> <span class="highlight"><span class="n">session</span></span> by [Login via QR code](https://core.telegram.org/api/qr-login).

- This works just like when you signing into <span class="highlight"><span class="n">Telegram</span></span> using <span class="highlight"><span class="n">QR</span></span> <span class="highlight"><span class="n">Login</span></span> on mobile devices.

- Although <span class="highlight"><span class="n">Telegram</span></span> <span class="highlight"><span class="n">Desktop</span></span> doesn't let you authorize other sessions via <span class="highlight"><span class="n">QR</span></span> <span class="highlight"><span class="n">Code</span></span> *(or it doesn't have that feature)*, it is still available across all platforms <span class="highlight"><span class="p">(</span></span><a class="codehl codehl_obj" href="../api#api.API"><b>APIs</b></a><span class="highlight"><span class="p">)</span></span>.
???+ done "Safe to use"
    You can always use <span class="highlight"><span class="n">CreateNewSessions</span></span> with any APIs, it can be different from the API that originally created the session.



