import sys
from collections import deque
N = int(sys.stdin.readline().split()[0])
pos = list(map(int,sys.stdin.readline().split()))
# N = int(input())
# pos = list(map(int,input().split()))
pan = deque()
pan.append([pos[0],pos[1],0])
tar_r, tar_c = pos[2], pos[3]

visited = []
for n_idx in range(N):
    visited.append([False] * N)
    
ans_arr = []
def bfs():
    r, c, cnt = pan.popleft()
    if r >= N or r < 0 or c < 0 or c >= N:
        return -1

    if visited[r][c] == True:
        return -1
    
    if r == tar_r and c == tar_c:
        return cnt
    
    visited[r][c] = True
    pan.append([r+2,c+1,cnt+1])
    pan.append([r+2,c-1,cnt+1])
    pan.append([r-2,c+1,cnt+1])
    pan.append([r-2,c-1,cnt+1])
    pan.append([r,c+2,cnt+1])
    pan.append([r,c-2,cnt+1])
    
    return -1

answer = 0
while len(pan) != 0:
    answer = bfs()
    if answer != -1:
        break
        
print(answer)