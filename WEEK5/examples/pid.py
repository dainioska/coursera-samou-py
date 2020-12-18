import os

pid = os.getpid()

for n in range(10):
     print(n, pid)