#!/bin/python3

import math
import os
import random
import re
import sys

MOD = 10**9 + 7

def summingPieces(arr):
    pow2 = 1
    value = 0
    sumlast = 0
    for elt in arr:
        value = (2*value + sumlast + (2*pow2-1)*elt) % MOD
        sumlast = (sumlast + pow2 * elt) % MOD
        pow2 = (2 * pow2) % MOD
    return value

n = int(input())
arr = [int(fld) for fld in input().strip().split()]
print(summingPieces(arr))