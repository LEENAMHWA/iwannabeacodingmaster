from collections import deque
import copy
import sys

def rotate_90(arr, rows):
    new_arr = []
    for r_idx in range(rows):
        row_arr = []
        for c_idx in range(rows):
            row_arr.append(arr[(rows-1)-c_idx][r_idx])
        new_arr.append(row_arr)
    
    return new_arr

# baekjoon
N = int(sys.stdin.readline().split()[0])

game = []
for r_idx in range(N):
    # baekjoon
    game.append(list(map(int, sys.stdin.readline().split())))

if N == 1:
    print(game[0][0])
    exit()

# rotate
cnt = 0

scn = deque()
scn.append([game,cnt])
answer = 0

while scn:
    tmp_game, n_try = scn.popleft()
    if n_try == 5:
        continue

    for rot_idx in range(4):
        rot_game = copy.deepcopy(tmp_game)
        for rot_iter in range(rot_idx):
            rot_game = rotate_90(rot_game, N)
        
        for r_idx in range(len(rot_game)):
            visited = [0] * len(rot_game[r_idx])
            for c_idx in range(len(rot_game[r_idx])-1):
                if visited[c_idx] == 1:
                    continue
                if rot_game[r_idx][c_idx+1] != 0:
                    if rot_game[r_idx][c_idx] == rot_game[r_idx][c_idx+1]:

                        rot_game[r_idx][c_idx+1] += rot_game[r_idx][c_idx]
                        visited[c_idx] = visited[c_idx+1] = 1
                        rot_game[r_idx][c_idx] = 0
                    
                else:
                    rot_game[r_idx][c_idx+1] = rot_game[r_idx][c_idx]
                    rot_game[r_idx][c_idx] = 0
                
                if rot_game[r_idx][c_idx+1] > answer:
                    answer = rot_game[r_idx][c_idx+1]

        scn.append([rot_game, n_try+1])
print(answer) 
