#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    min_candies = [0] * n
    min_candies[0] = 1
    total_candies = 0;
    for i in range(1,n):
        if(arr[i] > arr[i-1]):
            min_candies[i] = min_candies[i-1] + 1;
        else:
            min_candies[i] = 1;
    # backward loop to update min_candies
    for i in range(n-2,-1,-1):
        print(i)
        if(arr[i] > arr[i+1] and min_candies[i] <= min_candies[i+1]):
            min_candies[i] = min_candies[i+1] + 1;
    for i in range(n):
        total_candies+= min_candies[i];
        
    return total_candies;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
  
