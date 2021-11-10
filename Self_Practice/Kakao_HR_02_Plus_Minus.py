#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    
    num_len = len(arr)
    pro_arr = [0,0,0]
    # Write your code here
    for item in arr:
        if item < 0:
            pro_arr[1] += 1
        elif item > 0:
            pro_arr[0] += 1
        else:
            pro_arr[2] += 1
    
    for p_item in pro_arr:
        print(p_item/num_len)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
