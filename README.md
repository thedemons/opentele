# OpenTele

OpenTele is a python library created to make life easier for Telegram API Developers.
It helps you:
- Process [tdesktop](https://github.com/telegramdesktop/tdesktop)'s tdata information
- Convert between tdata and [telethon](https://github.com/LonamiWebs/Telethon) sessions
- Use [telethon](https://github.com/LonamiWebs/Telethon) with [official API_ID and API_HASH]() to avoid spam detection
- Many more features are [waiting to be added](https://github.com/thedemons/opentele#Incoming%20Features)

## Installation
- This library was created with the help of [telethon](https://github.com/LonamiWebs/Telethon), [tgcrypto](https://github.com/pyrogram/tgcrypto) and [pyQt5](https://www.riverbankcomputing.com/software/pyqt/)
- Just run this command to install it
```
pip install --upgrade opentele
```

## First Run
- This example creates a `telethon.TelegramClient` from `tdata` folder
```python
import opentele
import asyncio

import os

async def main():
    
    tdataFolder = f"{os.getenv('APPDATA')}\\Telegram Desktop\\tdata"

    tdesktop = opentele.TDesktop()
    tdesktop.FromTData(tdataFolder)

    client = tdesktop.ToTelethon()

    await client.connect()
    peer_user = await client.get_me()
    print(f"Logged in as {peer_user.username}")

asyncio.get_event_loop().run_until_complete(main())
```

## Authorization
OpenTele offers the ability to use the **official API_ID and API_HASH**, which are also used by official apps. You can check that out [here](https://github.com/thedemons/opentele/blob/main/opentele/opentele.py#L54).
<br>
According to [Telegram TOS](https://core.telegram.org/api/obtaining_api_id#using-the-api-id): all accounts that sign up or log in using unofficial Telegram API clients are automatically put under observation to avoid violations of the Terms of Service.
<br>
<br>
It also uses the **official [lang_pack](https://core.telegram.org/method/initConnection)** parameter, of which [telethon can't use](https://github.com/LonamiWebs/Telethon/blob/master/telethon/client/telegrambaseclient.py#L375) because it's only for official apps.
<br>
Therefore, **there are no differences** between using OpenTele and official apps, the server can't tell you apart.


## Incoming Features
- Writing data to tdata for converting telethon sessions to tdesktop
- Random device information for [initConnection](https://core.telegram.org/method/initConnection) to perform mass registeration without being detected

## Documentation
_to be added_

## License

MIT

