__author__ = 'galvin'
#-*-coding:utf-8-*-

from random import randrange
seq = [randrange(100) for i in range(10)]
print(seq)
dd = float('inf')
print(dd)

for x in seq:
    for y in seq:
        if x==y:
            continue
        d = abs(x-y)
        if d < dd:
            xx,yy,dd = x,y,d
print(xx,yy)