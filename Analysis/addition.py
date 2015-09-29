import sys
from datetime import datetime

"""This is an example for NumPy"""
import numpy as np

def pythonsum(n):
    a = range(n)
    b = range(n)
    c=[]
    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i]+b[i])
    return c

c = pythonsum(10)
print c

def numpysum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a+b
    print c
    return c

numpysum(10)