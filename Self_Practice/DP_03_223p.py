import sys

N = int(sys.stdin.readline().split()[0])

d = [0] * 1001

d[1] = 1
d[2] = 3
for idx in range(3, N+1):
    d[idx] = (d[idx - 2] * 2) + d[idx - 1] % 796796

print(d[N])

