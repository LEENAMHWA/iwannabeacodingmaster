# 숫자 카드 게임
import sys

N, M = list(map(int,sys.stdin.readline().split()))
min_list = []

for r_idx in range(N):
    min_list.append(min(list(map(int,sys.stdin.readline().split()))))

print(max(min_list))