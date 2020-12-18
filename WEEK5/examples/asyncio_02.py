#asyncio version
import asyncio

async def  hello_world():
    while True:
        print ("Hello hello")
        await asyncio.sleep(2.0)

loop = asyncio.get_event_loop()
loop.run_until_complete(hello_world())
loop.close()

