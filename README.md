# OpenTele

OpenTele is a python library created to make life easier for Telegram API Developers.
It helps you:
- Process [tdesktop](https://github.com/telegramdesktop/tdesktop)'s tdata information
- Convert between tdata and [telethon](https://github.com/LonamiWebs/Telethon) sessions
- Many more features are waiting to be added

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
## Documentation
_to be added_
## License

MIT

