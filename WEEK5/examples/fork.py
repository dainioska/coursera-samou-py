#create "parent" and "child" process on python
import time
import os

pid = os.fork()
name = "first"
if pid == 0:
    while True:    
        print("child:", os.getpid(), name)
        if name == "first":
            name = "second"
        else:
            name = "first"
        time.sleep(5)
else:
    print("parent:", os.getpid(), name)
    os.wait()
    
#test on terminal:
#>ps uax | grep fork.py
#>ps axf | grep fork.py
#>sudo strace -p PID


