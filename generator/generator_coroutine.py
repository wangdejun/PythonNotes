# def receiver():
#     while True:
#         item = yield
#         print('Got', item)

# recv = receiver()
# next(recv)
# recv.send('Hello')
# recv.send('world')

# def chain(x, y):
#     yield from x
#     yield from y

# a = [1,2,3]
# b = [4,5,6]
# for x in chain(a, b):
#     print(x, end='')

import time
from contextlib import contextmanager

@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print end
        print('%s: %0.3f' %(label, end-start))

with timethis('counting'):
    n=1000000
    while n>0:
        n-=1
