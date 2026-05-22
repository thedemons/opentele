<!-- vim: syntax=Markdown -->

# opentele

> Fork of [thedemons/opentele](https://github.com/thedemons/opentele) with Python 3.13 compatibility, updated device spoofing and QR Code login.

<p align="center">
<img src="https://raw.githubusercontent.com/thedemons/opentele/main/opentele.png" alt="logo" width="180"/>
<br><br>
<a href="https://pypi.org/project/opentele/"><img alt="pypi version" src="https://img.shields.io/pypi/v/opentele?logo=pypi&logoColor=%232d93c1"/></a>
<a href="https://pypi.org/project/opentele/"><img alt="pypi status" src="https://img.shields.io/pypi/status/opentele?color=%2331c754&logo=pypi&logoColor=%232d93c1"/></a>
<a href="https://opentele.readthedocs.io/"><img alt="documentation" src="https://img.shields.io/readthedocs/opentele.svg?color=%2331c754&logo=readthedocs"/></a>
<a href="https://codecov.io/gh/thedemons/opentele">
<img src="https://img.shields.io/codecov/c/github/thedemons/opentele?color=%2331c754&label=codecov&logo=codecov&token=H2IWGEJ5LN"/>
</a>
<a href="https://github.com/thedemons/opentele/actions/workflows/package.yml"><img alt="workflow tests" src="https://img.shields.io/github/workflow/status/thedemons/opentele/package?logo=github&color=%2331c754"/></a>
<a href="https://github.com/thedemons/opentele/issues"><img alt="issues" src="https://img.shields.io/github/issues/thedemons/opentele?color=%2331c754&logo=github"/></a>
<a href="https://github.com/thedemons/opentele/commits/main"><img alt="github last commit" src="https://img.shields.io/github/last-commit/thedemons/opentele?color=%2331c754&logo=github"/></a>
<a href="https://github.com/thedemons/opentele/commits/main"><img alt="github commits" src="https://img.shields.io/github/commit-activity/m/thedemons/opentele?logo=github"/></a>
<a href="https://pypi.org/project/opentele/"><img alt="pypi installs" src="https://img.shields.io/pypi/dm/opentele?label=installs&logo=docusign&color=%2331c754"/></a>
<a href="https://en.wikipedia.org/wiki/MIT_License"><img alt="pypi license" src="https://img.shields.io/pypi/l/opentele?color=%2331c754&logo=gitbook&logoColor=white"/></a>
<a href="https://github.com/psf/black"><img alt="code format" src="https://img.shields.io/badge/code%20style-black-000000.svg?logo=python&logoColor=%232d93c1"/></a>
</p>

<br>

A **Python Telegram API Library** for converting between **tdata** and **telethon** sessions, with built-in **official Telegram APIs**. [**Read the documentation**](https://opentele.readthedocs.io/en/latest/documentation/telegram-desktop/tdesktop/).

---

## What's changed from the original

### Python 3.13 compatibility
- Fixed `crossDelete` in `utils.py` to handle new dunder attributes introduced in Python 3.13 (`__firstlineno__`, `__static_attributes__`, `__dict__`, `__weakref__`, `__qualname__`)
- Fixed `_on_login` calls in `tl/telethon.py` that broke under Python 3.13's coroutine handling
- Removed deprecated TDesktop storage keys (`customEmoji`, `searchSuggestions`, `webviewTokens`) that caused parsing errors with recent tdata versions

### QR Code login
- Added a new session creation method via QR Code scan, no need to convert tdata or existing session files
- The app generates a QR code in the terminal, the user scans it from the official Telegram app on their phone, and the session is authorized automatically
- Supports 2FA (two-factor authentication) if enabled on the account

### Updated device spoofing logic
- Replaced the hardcoded device list with a structured system that maps **real Android SDK versions** to **devices that officially support that version**
- Each Android version (Android 13/SDK 33, Android 14/SDK 34, Android 15/SDK 35) is mapped to real devices that were officially released or updated to that version
- Updated app version from `8.4.1` to `12.5.1` to match current official Telegram Android
- Added `DeviceInfo.to_dict()` and `DeviceInfo.from_dict()` methods for serialization
- Added `ResolveDevice()` method that allows passing a specific device instead of always randomizing

### Other changes
- Changed `isinstance` check to `type()` comparison in `APIData.__eq__` to avoid false positives with subclasses

### Platform support

| Platform | Status |
| --- | --- |
| **Linux** | ✅ Tested on Python 3.13 |

---

## Features
- Convert [Telegram Desktop](https://github.com/telegramdesktop/tdesktop) **tdata** sessions to [telethon](https://github.com/LonamiWebs/Telethon) sessions and vice versa.
- Use **telethon** with [official APIs](#authorization) to avoid bot detection.
- Randomize [device info](https://opentele.readthedocs.io/en/latest/documentation/authorization/api/#generate) using real data that recognized by Telegram server.

## Dependencies

- [telethon](https://github.com/LonamiWebs/Telethon) - Widely used Telegram's API library for Python.
- [tgcrypto](https://github.com/pyrogram/tgcrypto) - AES-256-IGE encryption to works with `tdata`.
- [pyQt5](https://www.riverbankcomputing.com/software/pyqt/) - Used by Telegram Desktop to streams data from files.
- [qrcode](https://github.com/lincolnloop/python-qrcode) - QR code generation for terminal-based login.

---

## ⚠️ Warning

This tool uses Telegram's official authentication. It must be properly configured.

The following actions may cause Telegram to freeze your accounts:

- Manually defining `API_ID` and `API_HASH` (the tool already manages these)
- Making rapid or repeated authentication attempts
- Using a different connection method or device than the one used to create the session
- Mixing different Telegram clients or libraries
- Logging in with multiple accounts from the same IP address or device
- Using new virtual numbers or numbers with no prior activity

Notes:
- If you created a session with an official device (e.g., Android), you must continue using that same method for that session
- Using your own `API_ID` and `API_HASH` may cause authentication inconsistencies

## Installation
- Install from [PyPI](https://pypi.org/project/opentele/):
```pip title="pip"
pip install --upgrade opentele
```

## First Run
Load TDesktop from tdata folder and convert it to telethon, with a custom API:
```python
from opentele.td import TDesktop
from opentele.tl import TelegramClient
from opentele.api import API, CreateNewSession, UseCurrentSession
import asyncio

async def main():
    
    # Load TDesktop client from tdata folder
    tdataFolder = r"C:\Users\<username>\AppData\Roaming\Telegram Desktop\tdata"
    tdesk = TDesktop(tdataFolder)

    # Using official iOS API with randomly generated device info
    # print(api) to see more
    api = API.TelegramIOS.Generate()

    # Convert TDesktop session to telethon client
    # CreateNewSession flag will use the current existing session to
    # authorize the new client by `Login via QR code`.
    client = await tdesk.ToTelethon("newSession.session", CreateNewSession, api)

    # Although Telegram Desktop doesn't let you authorize other
    # sessions via QR Code (or it doesn't have that feature),
    # it is still available across all platforms (APIs).

    # Connect and print all logged in devices
    await client.connect()
    await client.PrintSessions()

asyncio.run(main())
```

## QR Code Login (New)
Create a session by scanning a QR code from the official Telegram app. No tdata or session file conversion needed.
```python
from opentele.tl import TelegramClient
from opentele.api import API
from telethon.errors import SessionPasswordNeededError
from getpass import getpass
import qrcode
import asyncio
import os

async def main():
    os.makedirs("sessions", exist_ok=True)
    session_path = "sessions/my_account.session"
    api = API.TelegramAndroid.Generate(unique_id=session_path)
    client = TelegramClient(session_path, api=api)

    await client.connect()

    if await client.is_user_authorized():
        print("Session already authorized.")
        await client.disconnect()
        return

    qr_login = await client.qr_login()

    # Generates a QR code in the terminal
    qr = qrcode.QRCode(border=1)
    qr.add_data(qr_login.url)
    qr.make(fit=True)
    print("\nScan this QR from Telegram on your phone:\n")
    qr.print_ascii(invert=True)

    try:
        await qr_login.wait()
    except SessionPasswordNeededError:
        password = getpass("2FA Password: ")
        await client.sign_in(password=password)

    if await client.is_user_authorized():
        print("Session created successfully.")
        me = await client.get_me()
        if me:
            print(f"User: {me.id} | {me.first_name}")
        await client.PrintSessions()
    else:
        print("Could not authorize the session.")

    await client.disconnect()

asyncio.run(main())
```

> **Note:** Requires `qrcode` package: `pip install qrcode`

## Authorization
**opentele** offers the ability to use **official APIs**, which are used by official apps. You can check that out [here](https://opentele.readthedocs.io/en/latest/documentation/authorization/api/#class-api).
<br>

According to [Telegram TOS](https://core.telegram.org/api/obtaining_api_id#using-the-api-id): *all accounts that sign up or log in using unofficial Telegram API clients are automatically put under observation to avoid violations of the Terms of Service*.
<br>
<br>
It also uses the **[lang_pack](https://core.telegram.org/method/initConnection)** parameter, of which [telethon can't use](https://github.com/LonamiWebs/Telethon/blob/dd51aea4db90fd255a14e27192e221c70b45e105/telethon/_client/telegrambaseclient.py#L197) because it's for official apps only.
<br>
Therefore, **there are no differences** between using opentele and official apps, the server can't tell you apart.

## Incoming Features
- [x] Writing data to tdata for converting telethon sessions to tdesktop.
- [x] Random device information for [initConnection](https://core.telegram.org/method/initConnection) to avoid spam-detection.
- [x] QR Code login without tdata or session conversion.
- [ ] Add support for [pyrogram](https://github.com/pyrogram/pyrogram).
- [ ] Develop opentele-tui using [textual](https://github.com/Textualize/textual) for non-experience user.

## Examples
The best way to learn anything is by looking at the examples. Am I right?

- Example on [readthedocs](https://opentele.readthedocs.io/en/latest/examples/)
- Example on [github](./examples)

## Documentation [![documentation](https://readthedocs.org/projects/opentele/badge/?version=latest&style=flat)](https://opentele.readthedocs.io/)
- Read documentation on [readthedocs](https://opentele.readthedocs.io/en/latest/documentation/telegram-desktop/tdesktop/)
- Read documentation on [github](https://github.com/thedemons/opentele/tree/main/docs-github)



- Usa siempre el cliente proporcionado por esta librería (`opentele`)

Úsala bajo tu propia responsabilidad.

---
