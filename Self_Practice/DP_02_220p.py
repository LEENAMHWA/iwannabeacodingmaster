import sys

n = int(sys.stdin.readline().split()[0])
x = list(map(int,sys.stdin.readline().strip().split()))

d = [0] * 100

d[0] = x[0]
d[1] = max(x[0], x[1])

for idx in range(2, n):
    d[idx] = max(d[idx-1], d[idx-2] + x[idx])

print(d[n-1])

