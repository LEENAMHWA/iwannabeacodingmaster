import sys

N, M = list(map(int,(sys.stdin.readline().split()[:2])))
print(N,M)
d = [10001] * M

val_list = []
for _ in range(N):
    tmp = int(sys.stdin.readline().split()[0])
    val_list.append(tmp)

val_list.sort()
