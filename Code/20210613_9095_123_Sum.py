# Dynamic Programming

import sys

t = int(sys.stdin.readline().split()[0])
for test_idx in range(t):
    num = int(sys.stdin.readline().split()[0])
    answer = 0
    s = [1,2,4]

    if num <= 3:
        answer = s[num-1]
    else:
        for l_idx in range(3,num):
            s.append(sum(s[l_idx-3:l_idx]))
        answer = s[num-1]        

    print(answer)
