import sys
from collections import deque
    
def bfs(me, you):
    visited = [0] * 100001
    
    queue = deque()
    queue.append([me, 0])
    
    while queue:
        pos, cnt = queue.popleft()
        
        if pos > 100000 or pos < 0:
            continue
        
        if visited[pos] == 1:
            continue
        else:
            visited[pos] = 1
        
        if pos == you:
            print(cnt)
            break
        
        queue.append([2*pos, cnt+1])
        queue.append([pos-1, cnt+1])
        queue.append([pos+1, cnt+1])    

# For BJ
pos_i, pos_u = list(map(int,sys.stdin.readline().split()))

bfs(pos_i, pos_u)