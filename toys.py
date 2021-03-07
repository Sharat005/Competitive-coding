#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the toys function below.
def toys(w):
    w.sort();
    last = -1;
    count = 0;
    print(w)
    for i in range(len(w)):
        if(w[i]>last):
            count = count + 1;
            last = w[i] + 4;
    print(count)
    return count;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
