# Convert Telethon to tdata
This example will show you how to create `tdata` folder from a [TelegramClient][TelegramClient] session. This `tdata` folder can later be used by [Telegram Desktop](https://github.com/telegramdesktop/tdesktop) app.

## Preparing
- We need to import these things:
    ```python
    from opentele.td import TDesktop
    from opentele.tl import TelegramClient
    from opentele.api import API, UseCurrentSession, CreateNewSession
    import asyncio
    ```
- And we need to put the main code inside an async function:
    ```python
    async def main():
        # PUT EXAMPLE CODE HERE

    asyncio.run(main())
    ```


## Initialize [TelegramClient][TelegramClient]
- First we need to load a `TelegramClient`, either by loading an existing session or log in to a new session:
    ```python
    # Load the client from telethon.session file
    # We don't need to specify api, api_id or api_hash, it will use TelegramDesktop API by default.
    client = TelegramClient("telethon.session")
    ```

## Converting [TelegramClient][TelegramClient] to [TDesktop][TDesktop]
There are two ways we can do this, either by using the current session, or create (log in to) a new session.

- Use the current session:
    ```python
    # flag=UseCurrentSession
    #
    # Convert Telethon to TDesktop using the current session.
    tdesk = await client.ToTDesktop(flag=UseCurrentSession)
    ```
- Create a new session:
    ```python
    # flag=CreateNewSession
    #
    # Convert Telethon to TDesktop by creating a new session.
    # CreateNewSession will use the current session (in tdata folder) to authorize a new session using QR Login.
    # If 2FA is enabled for this account, you must specify the password via the password argument.
    # This is of course slower than UseCurrentSession.
    tdesk = await client.ToTDesktop(flag=CreateNewSession)
    ```

## Saving the [TDesktop][TDesktop] session to tdata folder
```python
# Save the session to a folder named "tdata"
tdesk.SaveTData("tdata")
```

## Final result example
```python
from opentele.td import TDesktop
from opentele.tl import TelegramClient
from opentele.api import API, UseCurrentSession
import asyncio

async def main():

    # Load the client from telethon.session file
    # We don't need to specify api, api_id or api_hash, it will use TelegramDesktop API by default.
    client = TelegramClient("telethon.session")
    
    # flag=UseCurrentSession
    #
    # Convert Telethon to TDesktop using the current session.
    tdesk = await client.ToTDesktop(flag=UseCurrentSession)
    
    # Save the session to a folder named "tdata"
    tdesk.SaveTData("tdata")

asyncio.run(main())
```


[TelegramClient]: https://opentele.readthedocs.io/en/latest/documentation/telethon/telegramclient/#class-telegramclient
[TDesktop]: https://opentele.readthedocs.io/en/latest/documentation/telegram-desktop/tdesktop/#class-tdesktop