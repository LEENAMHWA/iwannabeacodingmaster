# Until 1
import sys

N, K = list(map(int,sys.stdin.readline().split()))

iter_cnt = 0
while N != 1:
    iter_cnt += 1
    if N % K != 0:
        N -= 1
    else:
        N /= K

print(iter_cnt)