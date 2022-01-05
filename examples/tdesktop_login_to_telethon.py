import opentele
import asyncio

import os

async def main():
    
    tdataFolder = f"{os.getenv('APPDATA')}\\Telegram Desktop\\tdata"
    
    tdesktop = opentele.TDesktop()
    tdesktop.FromTData(tdataFolder)

    client = await tdesktop.ToNewTelethonSession("opentele")
    peer_user = await client.get_me()
    
    print(f"Logged in as {peer_user.username}")

asyncio.get_event_loop().run_until_complete(main())
