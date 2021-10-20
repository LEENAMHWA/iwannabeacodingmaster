# import sys
from collections import deque
import copy
import sys

# for BJ
N = int(sys.stdin.readline().split()[0])

# for jupyter
# N = int(input())
area = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

eaten_cnt = 0
sum_dist = 0
queue = deque()
q_visited = []

shark_size = 2
for r_idx in range(N): 
#     # for bj
    tmp_area = list(map(int,sys.stdin.readline().split()))
    # tmp_area = list(map(int,input().split()))
    
    if 9 in tmp_area:
        queue.append([r_idx,tmp_area.index(9), 0])
        
    area.append(tmp_area)
    q_visited.append([0]*N)
    
def bfs(s_size):
    min_x = min_y = N
    min_dist = N*N
    tmp_visited = copy.deepcopy(q_visited)
    
    while queue:
        pos_x, pos_y, dist = queue.popleft()
        
        # 범위 check
        if pos_x >= N or pos_x < 0 or pos_y >= N or pos_y < 0:
            continue
        
        # 방문 check
        if tmp_visited[pos_x][pos_y] == 0:
            tmp_visited[pos_x][pos_y] = 1
        else:
            continue
        
        if area[pos_x][pos_y] != 9 and area[pos_x][pos_y] != 0:
        
            if s_size < area[pos_x][pos_y]:
                continue
                
            # 상어 사이즈가 더 클때
            elif s_size > area[pos_x][pos_y]:
                # 최소 거리가 더 멀 때
                if min_dist > dist:
                    min_dist = dist
                    min_x = pos_x
                    min_y = pos_y
                    continue 
                    
                # 같을 때
                elif min_dist == dist:
                    # 위 아래 비교
                    if pos_x < min_x:
                        min_x = pos_x
                        min_y = pos_y
                        
                    # 왼오 비교
                    elif pos_x == min_x:
                        if pos_y < min_y:
                            min_x = pos_x
                            min_y = pos_y
                    continue
            
                
        for d_idx in range(len(dx)):
            queue.append([pos_x + dx[d_idx], pos_y + dy[d_idx], dist + 1])
    
    return [min_x, min_y, min_dist]

while True:
    res_x, res_y, res_dist = bfs(shark_size)
    if res_x != N:
        eaten_cnt += 1
        area[res_x][res_y] = 0
        
        sum_dist += res_dist
        queue.append([res_x, res_y, 0])
        
        if eaten_cnt == shark_size:
            shark_size += 1
            eaten_cnt = 0
    else:
        break
    
print(sum_dist)