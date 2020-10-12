#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n,ar):
    set_ar=set(ar)
    count = 0
    for a in set_ar:
        if ar.count(a)%2==0 and ar.count(a)>=2 :
            add_a = ar.count(a)//2
            count += add_a
        else:
            if ar.count(a) >= 2:
                add_a = (ar.count(a)-1)//2
                count+=add_a
    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n,ar)

    fptr.write(str(result) + '\n')

    fptr.close()
