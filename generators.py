# https://www.python-course.eu/python3_generators.php
import random
from datetime import timedelta
from nptime import nptime

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def permutations(items):
    if len(items) == 0: yield []
    else:
        for i in range(len(items)):
            for cc in permutations(items[:i] + items[i + 1:]):
                yield [items[i]] + cc

def k_permutations(items, n):
    if n == 0:
        yield []
    else:
        for item in items:
            for kp in k_permutations(items, n - 1):
                if item not in kp:
                    yield [item] + kp

def firstn(generator, n):
    g = generator()
    for _ in range(n):
        yield next(g)


# excercies
# write a generator which computes the running average
def average(items):
    total, count = 0, 0
    for n in items:
        total += n
        count += 1
        yield (total/count)

# write a generator frange, which behaves like range but accepts float values
def frange(start, stop=None, step=1):
    if stop == None: return
    while start < stop:
        yield ('%g' % start)
        start += step
    return

# 3
def trange(start=nptime, stop=None, step=None):
    if stop == None or step == None: return
    while str(start) < str(stop):
        yield str(start)
        start += step
    return

# 4
def rtrange(start=tuple, stop=None, step=None):
    if stop == None or step == None: return
    s = start
    while start < stop:
        counter = yield start
        if counter == 'r':
            start = s
        else:
            h1, m1, s1 = start
            h2, m2, s2 = step
            start = (h1 + h2, m1 + m2, s1 + s2)

# 5 
with open('times_and_temperatures.txt', 'w') as f:
    for time in trange(nptime(6, 0, 0), nptime(6, 15, 0), timedelta(0, 90)):
        s = '%s %.1f\n' % (time, round(random.uniform(10.0, 25.0), 1))
        f.write(s)

# 6
def random_ones_and_zeroes(p=0.5):
    while True:
        x = random.random()
        message = yield 1 if x < p else 0
        if message != None:
            p = message

x = random_ones_and_zeroes()
next(x)
for p in [0.2, .8]:
    x.send(p)
    for i in range(20):
            print(next(x), end=' ')
    print()