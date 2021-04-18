#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the powerSum function below.
def powerSum(X, N, num):
    nextVal = X - pow(num, N);
    
    if(nextVal < 0): 
      return 0;
    elif(nextVal == 0):
      return 1;
    else: 
      return powerSum(nextVal , N, num + 1) + powerSum(X, N, num+1);

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N, 1)

    fptr.write(str(result) + '\n')

    fptr.close()
