from concurrent.futures import ThreadPoolExecutor

def func(x,y):
    'Some function. Nothing too interesting'
    import time
    time.sleep(5)
    return x+y

pool = ThreadPoolExecutor(max_workers=8)
fut = pool.submit(func, 2, 3)
r = fut.result()
print('Got:', r)

