import sys
import os


f = open('test.txt', 'r')


def get_value(f):
    try:
        x = f.read(1)
        if not x:
            return '\f'
    except Exception:
        return '\f'
    return x


a = get_value(f)
b = get_value(f)
c = get_value(f)
while a != '\f' or b != '\f' or c != '\f':
    print a
    print b
    print c
    a = get_value(f)
    b = get_value(f)
    c = get_value(f)

print ord(a)
print ord(b)
print ord(c)