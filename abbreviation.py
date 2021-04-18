#!/bin/python

import math
import os
import random
import re
import sys

def abbreviation(a, b):
    onlyUpper = [letter for letter in a if letter.isupper()]
    
    j = 0
    for i in range(len(onlyUpper)):
        while j < len(b) and onlyUpper[i] != b[j]:
            j += 1
        if j == len(b):
            print('NO')
            return
        else:
            j += 1
    
    a = [letter.upper() for letter in a]
    
    j = 0
    for i in range(len(b)):
        while j < len(a) and b[i] != a[j]:
            j += 1
        if j == len(a):
            print('NO')
            return
        else:
            j += 1
            
    print('YES')
    
for _ in range(int(input().strip())):
    a = list(input().strip())
    b = list(input().strip())
    abbreviation(a, b)
