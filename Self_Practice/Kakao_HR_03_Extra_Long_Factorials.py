#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

result = 1
def extraLongFactorials(n):
    global result
    
    # Write your code here
    if n != 1:
        result *= n
        return extraLongFactorials(n-1)
    else:
        print(result)
        
    
if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
