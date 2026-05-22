# QR Code Login
This example will show you how to create a session by scanning a QR code from the official Telegram app. No tdata or session file conversion needed.

## Preparing
- You need to have the official Telegram app installed on your phone with a logged-in account.
- We need to import these things:
```python
    from opentele.tl import TelegramClient
    from opentele.api import API
    from telethon.errors import SessionPasswordNeededError
    from getpass import getpass
    import qrcode
    import asyncio
    import os
```
- And we need to put the main code inside an async function:
```python
    async def main():
        # PUT EXAMPLE CODE HERE

    asyncio.run(main())
```

## Initialize [TelegramClient][TelegramClient]
- Create a new client using the official Android API with randomized device info:
```python
    os.makedirs("sessions", exist_ok=True)
    session_path = "sessions/my_account.session"
    api = API.TelegramAndroid.Generate(unique_id=session_path)
    client = TelegramClient(session_path, api=api)

    await client.connect()
```

## Check if already authorized
- If the session already exists and is authorized, no need to log in again:
```python
    if await client.is_user_authorized():
        print("Session already authorized.")
        await client.disconnect()
        return
```

## Generate and scan QR Code
- Request a QR login and display it in the terminal:
```python
    qr_login = await client.qr_login()

    qr = qrcode.QRCode(border=1)
    qr.add_data(qr_login.url)
    qr.make(fit=True)
    print("\nScan this QR from Telegram on your phone:\n")
    qr.print_ascii(invert=True)
```

## Wait for authorization
- Wait for the user to scan the QR code. If 2FA is enabled, it will ask for the password:
```python
    try:
        await qr_login.wait()
    except SessionPasswordNeededError:
        password = getpass("2FA Password: ")
        await client.sign_in(password=password)
```

## Final result example
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

[TelegramClient]: https://opentele.readthedocs.io/en/latest/documentation/telethon/telegramclient/#class-telegramclient
