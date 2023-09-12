#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    a_points = 0
    b_points = 0
    for i in range(len(b)):
        if a[i] > b[i]:
            a_points +=1
        elif a[i] < b[i] :
            b_points +=1      
            
        else:
            continue
            
    return[a_points,b_points] 
    #Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = [3,5,6,6]

    b = [4,6,2,6,2]

    result = compareTriplets(a, b)
    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
