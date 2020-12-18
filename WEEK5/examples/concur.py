#python thread pool example
from concurrent.futures import ThreadPoolExecutor, as_completed

def  fcn(a):
    return a*a

with ThreadPoolExecutor(max_workers=3) as pool:
    results = [pool.submit(fcn, i) for i in range(10)]

    for future in as_completed(results):
        print(future.result())

    

    