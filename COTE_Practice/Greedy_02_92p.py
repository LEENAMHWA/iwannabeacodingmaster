# 큰 수의 법칙

import sys

N, M, K = list(map(int,sys.stdin.readline().split()))
n_list = sorted(list(map(int,sys.stdin.readline().split())), reverse=True)

n_sum = 0
for iter_idx in range(M):
    if iter_idx != 0 and iter_idx % K == 0:
        n_sum += n_list[1]
    else:
        n_sum += n_list[0]

print(n_sum)