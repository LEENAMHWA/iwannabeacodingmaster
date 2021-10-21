import sys
import copy
from collections import deque
from queue import PriorityQueue

# row, columns
dr = [-1,1,0,0]
dc = [0,0,-1,1]
visited = []

N, M, fuel = list(map(int,sys.stdin.readline().split()))
for _ in range(N):
    visited.append([0]* N)

def get_shortest_son(pos_r, pos_c, son_arr, fuel):
    queue = deque()
    queue.append([pos_r, pos_c, 0])
    path_visited = copy.deepcopy(visited)

    min_dist = N * N
    min_idx = -1
    while queue:
        pos_r, pos_c, dist = queue.popleft()        
        if fuel < dist:
            continue

        if pos_r >= N or pos_r < 0 or pos_c < 0 or pos_c >= N:
            continue

        if t_map[pos_r][pos_c] == 1:
            continue
        
        if path_visited[pos_r][pos_c] == 1:
            continue
        else:
            path_visited[pos_r][pos_c] = 1

        # 가장 가까운 손님이 있는 경우
        for son_idx in range(len(son_arr)):
            # 일치할 경우
            if son_arr[son_idx][0] == pos_r and son_arr[son_idx][1] == pos_c:
                if dist < min_dist:
                    min_dist = dist
                    min_idx = son_idx
                elif dist == min_dist:
                    if son_arr[son_idx][0] < son_arr[min_idx][0]:
                        min_idx = son_idx
                    elif son_arr[son_idx][0] == son_arr[min_idx][0]:
                        if son_arr[son_idx][1] < son_arr[min_idx][1]:
                            min_idx = son_idx

        for d_idx in range(4):
            nr = pos_r + dr[d_idx]
            nc = pos_c + dc[d_idx]
            queue.append([nr, nc, dist + 1])

    return min_idx, min_dist

def get_shortest_path(pos_r, pos_c, arr_r, arr_c, fuel):
    queue = deque()
    queue.append([pos_r, pos_c, 0])
    path_visited = copy.deepcopy(visited)
    while queue:
        pos_r, pos_c, dist = queue.popleft()
        if dist > fuel:
            continue

        if pos_r >= N or pos_r < 0 or pos_c < 0 or pos_c >= N:
            continue

        if t_map[pos_r][pos_c] == 1:
            continue
        
        if path_visited[pos_r][pos_c] == 1:
            continue
        else:
            path_visited[pos_r][pos_c] = 1

        if pos_r == arr_r and pos_c == arr_c:
            return dist

        for d_idx in range(4):
            nr = pos_r + dr[d_idx]
            nc = pos_c + dc[d_idx]
            queue.append([nr, nc, dist + 1])

    return -1

t_map = []
for _ in range(N):
    t_map.append(list(map(int, sys.stdin.readline().split())))

pos_r, pos_c = list(map(int,sys.stdin.readline().split()))
pos_r -= 1
pos_c -= 1

son_arr = []
for _ in range(M):
    tmp_son = list(map(int, sys.stdin.readline().split()))
    tmp_son = list(map(lambda x: x - 1, tmp_son))

    son_arr.append(tmp_son)

try_n = 0
while son_arr:
    
    min_dist = N*N
    short_idx = -1

    # 손 찾기
    short_idx, min_dist = get_shortest_son(pos_r, pos_c, son_arr, fuel)

    if short_idx == -1:
        fuel = -1
        break 

    if fuel < min_dist:
        fuel = -1
        break
    else:
        fuel -= min_dist

    sd_r, sd_c, sa_r, sa_c = son_arr.pop(short_idx)
    pos_r = sd_r
    pos_c = sd_c

    taxi_path = get_shortest_path(sd_r, sd_c, sa_r, sa_c, fuel)
    if taxi_path == -1:
        fuel = -1
        break

    if fuel < taxi_path:
        fuel = -1
        break

    else:
        # 소모한 만큼 x2 되니까 결국 한번 더하는것과 같음
        fuel += taxi_path

    pos_r = sa_r
    pos_c = sa_c

    try_n += 1


print(fuel)