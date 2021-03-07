#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    #sort calorie array in descending order
    calorie.sort(reverse=True)
    sum = 0
    
    #run a for loop on calorie multiplying it with 2 power j and adding to the result
    for i in range(len(calorie)):
        sum = sum + 2**i*calorie[i];
        
    return sum
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
