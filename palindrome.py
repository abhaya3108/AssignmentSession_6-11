# -*- coding: utf-8 -*-
"""
Created on Sat May 18 18:29:24 2019

@author: panda4
"""

def ispalindrome(inputString):
    reverse = inputString[::-1]
    if reverse == inputString:
        print(inputString, "is palindrome")
    else:
        print(inputString, "is not a palindrome")

    