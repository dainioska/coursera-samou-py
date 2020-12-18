###start asyncio and show PID
import asyncio
import time
import os

pid = os.getpid()

#@asyncio.coroutine
async def pid_output():
    while True:
       print("PID:" ,pid, "Time:", time.time(), "\n")
       await asyncio.sleep(2.0)
       
###asyncio loop
loop = asyncio.get_event_loop()
loop.run_until_complete(pid_output())
loop.close()

#test on terminal:
#find PID in (>top)
#>ps axu | grep python.py
#>sudo strace -p PID
#>lsof -p PID
#>python3 python.py > log.txt

