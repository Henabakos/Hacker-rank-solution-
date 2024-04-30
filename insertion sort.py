#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    sortd = sorted(arr)
    for i in range(-1, -n-1, -1):
        x = i
        while arr[i] != sortd[i]:
            if sortd[x] == sortd[i]:
                arr[x] = sortd[i]
            arr[i] = arr[x]
            [print(str(arr[y]), end=" ") for y in range(n)]
            print("")
            x = x - 1
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
