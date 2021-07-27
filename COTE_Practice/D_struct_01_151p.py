import sys

N, M = list(map(int,sys.stdin.readline().split()))
result = 0

# Graph Input
graph = []
for r_idx in range(N):
    graph.append(list(map(int,list(sys.stdin.readline().rstrip()))))

# 재귀로 주변 노드 탐색
def dfs(x,y):
    # Range Exception
    if x >= N or x < 0 or y >= M or y < 0:
            return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

        return True

    return False     

for r_idx in range(N):
    for c_idx in range(M): 
        if dfs(r_idx, c_idx) == True:
            result += 1

print(result)