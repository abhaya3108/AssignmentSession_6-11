# -*- coding: utf-8 -*-
"""
Created on Sat May 18 18:07:23 2019

@author: panda4
"""

def fib2(n):
    fibonacci = []
    a, b = 0, 1
    while b<n:
        fibonacci.append(b)
        a, b = b, a+b
    print ("The fibonacci sequence till",n,"is", fibonacci)
    