import sys
from collections import deque

N, M = list(map(int,sys.stdin.readline().split()))
result = 0

# 동서남북 방향
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# Graph Input
graph = []
for r_idx in range(N):
    graph.append(list(map(int,list(sys.stdin.readline().rstrip()))))

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        
        for d_idx in range(4):
            nx = x + dx[d_idx]
            ny = y + dy[d_idx]

            if nx < 0  or nx >= N or ny < 0 or ny >= M:
                continue
            elif graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
        print(graph)

    return graph[N-1][M-1]

print(bfs(0,0))
