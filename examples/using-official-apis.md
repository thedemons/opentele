# Using official APIs
This example will show you how to use Telethon with official APIs.

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

## Creating an [official API][APIDATA]
- Using the default built-in template for [Telegram Android API][AndroidAPI]:
    ```python
    api = API.TelegramAndroid
    ```
- [Randomize][APIGenerate] the API's device data:
    ```python
    # Randomize the device data
    api = API.TelegramAndroid.Generate()
    ```
- [Randomize][APIGenerate] the API's device data with a `unique_id`:
    ```python
    # unique_id can be anything
    # This will be used to ensure that it will generate the same data everytime.
    # If not set then the data will be randomized each time we runs it.
    api = API.TelegramAndroid.Generate(unique_id="telethon.session")
    ```
- All the built-in [API templates][APITemplates] available:
    ```python
    api = API.TelegramDesktop
    api = API.TelegramAndroid
    api = API.TelegramAndroidX	
    api = API.TelegramIOS
    api = API.TelegramMacOS
    api = API.TelegramWeb_Z
    api = API.TelegramWeb_K
    api = API.Webogram
    ```

## Creating a [TelegramClient][TelegramClient] using the API
- From an existing session:
    ```python
    client = TelegramClient("telethon.session", api=api)
    await client.connect()
    ```
- From a `tdata` folder:
    ```python
    tdataFolder = r"C:\Users\<username>\AppData\Roaming\Telegram Desktop\tdata"
    tdesk = TDesktop(tdataFolder)
    assert tdesk.isLoaded()

    client = TelegramClient.FromTDesktop(tdesk, session="telethon.session", flag=UseCurrentSession, api=api)

    await client.connect()
    ```

## Final result example
```python
from opentele.td import TDesktop
from opentele.tl import TelegramClient
from opentele.api import API, UseCurrentSession
import asyncio

async def main():

    # Randomize the device data
    api = API.TelegramAndroid.Generate()

    client = TelegramClient("telethon.session", api=api)
    await client.connect()

asyncio.run(main())
```

## Extra: Demonstrate the behavior of unique_id
```python
def PrintAPI(api):
    print("\t", {"device_model": api.device_model, "system_version": api.system_version})

# Randomize using ["opentele", "library", "by", "thedemons"] as unique_ids
unique_string = "opentele library by thedemons"

for unique_id in unique_string.split(" "):
    print(f"Using {unique_id} as unique_id")

    for x in range(5):
        PrintAPI(API.TelegramAndroid.Generate(unique_id))

# Randomize without unique_id
print("Not using unique_id")
for x in range(5):
    PrintAPI(API.TelegramAndroid.Generate())
```

The result should look like this:
```python
Using opentele as unique_id
         {'device_model': 'Samsung SM-A750FN', 'system_version': 'SDK 24'}
         {'device_model': 'Samsung SM-A750FN', 'system_version': 'SDK 24'}
         {'device_model': 'Samsung SM-A750FN', 'system_version': 'SDK 24'}
         {'device_model': 'Samsung SM-A750FN', 'system_version': 'SDK 24'}
         {'device_model': 'Samsung SM-A750FN', 'system_version': 'SDK 24'}
Using library as unique_id
         {'device_model': 'Samsung SM-J100G', 'system_version': 'SDK 30'}
         {'device_model': 'Samsung SM-J100G', 'system_version': 'SDK 30'}
         {'device_model': 'Samsung SM-J100G', 'system_version': 'SDK 30'}
         {'device_model': 'Samsung SM-J100G', 'system_version': 'SDK 30'}
         {'device_model': 'Samsung SM-J100G', 'system_version': 'SDK 30'}
Using by as unique_id
         {'device_model': 'Samsung GT-S6800', 'system_version': 'SDK 26'}
         {'device_model': 'Samsung GT-S6800', 'system_version': 'SDK 26'}
         {'device_model': 'Samsung GT-S6800', 'system_version': 'SDK 26'}
         {'device_model': 'Samsung GT-S6800', 'system_version': 'SDK 26'}
         {'device_model': 'Samsung GT-S6800', 'system_version': 'SDK 26'}
Using thedemons as unique_id
         {'device_model': 'Samsung SM-N930VL', 'system_version': 'SDK 29'}
         {'device_model': 'Samsung SM-N930VL', 'system_version': 'SDK 29'}
         {'device_model': 'Samsung SM-N930VL', 'system_version': 'SDK 29'}
         {'device_model': 'Samsung SM-N930VL', 'system_version': 'SDK 29'}
         {'device_model': 'Samsung SM-N930VL', 'system_version': 'SDK 29'}
Not using unique_id
         {'device_model': 'Samsung SC-02B', 'system_version': 'SDK 24'}
         {'device_model': 'Samsung SPH-D700', 'system_version': 'SDK 26'}
         {'device_model': 'Huawei HUAWEI Y600-U151', 'system_version': 'SDK 23'}
         {'device_model': 'Samsung SCV41', 'system_version': 'SDK 28'}
         {'device_model': 'Samsung SM-G920F', 'system_version': 'SDK 27'}
```

[APIDATA]: https://opentele.readthedocs.io/en/latest/documentation/authorization/api/#class-apidata
[AndroidAPI]: https://opentele.readthedocs.io/en/latest/documentation/authorization/api/#class-telegramandroid
[DesktopdAPI]: https://opentele.readthedocs.io/en/latest/documentation/authorization/api/#class-telegramdesktop
[APITemplates]: https://opentele.readthedocs.io/en/latest/documentation/authorization/api/#class-api
[APIGenerate]: https://opentele.readthedocs.io/en/latest/documentation/authorization/api/#generate
[TelegramClient]: https://opentele.readthedocs.io/en/latest/documentation/telethon/telegramclient/
[TDesktop]: https://opentele.readthedocs.io/en/latest/documentation/telethon/telegramclient/