import sys

N = int(sys.stdin.readline().split()[0])
won = [500, 100, 50, 10]

cnt_won = 0
for list_idx in range(len(won)):
    cnt_won += N // won[list_idx]
    N %= won[list_idx]

print(cnt_won)