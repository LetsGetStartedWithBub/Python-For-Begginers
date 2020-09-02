#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_hourglass= -63
    for i in range(1,5):
        for j in range(1,5):
            current_hourglass = 0
            current_hourglass += arr[i-1][j-1]
            current_hourglass += arr[i-1][j]
            current_hourglass += arr[i-1][j+1]
            current_hourglass += arr[i][j]
            current_hourglass += arr[i+1][j-1]
            current_hourglass += arr[i+1][j]
            current_hourglass += arr[i+1][j+1]
            if(current_hourglass>max_hourglass):
                max_hourglass = current_hourglass
    return max_hourglass



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
