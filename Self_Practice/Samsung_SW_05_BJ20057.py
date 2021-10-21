import sys
import math

def rotate_m(x, y, idx):
    rotate_add = [[x, y], [-1*y, -1*x], [x, -1*y], [y, x]]

    return rotate_add[idx]

N = int(sys.stdin.readline().split()[0])

m_map = []
per_map = [[-2, 0, 0.02],\
 [-1, -1, 0.1], [-1, 0, 0.07], [-1, 1, 0.01],\
 [0, -2, 0.05],\
 [1, -1, 0.1], [1, 0, 0.07], [1, 1, 0.01],\
 [2, 0, 0.02], [0, -1, 1]] 

sand_sum = 0

for r_idx in range(N):
    m_map.append(list(map(int,sys.stdin.readline().split())))

pos = [N//2, N//2]

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

sub_try = 0
try_n = 0
go_n = 1
dir_idx = 0

while True:
    if pos[0] <= 0 and pos[1] <= 0:
        break

    # 이동
    pos[0] += dr[dir_idx]
    pos[1] += dc[dir_idx]

    # 휘날릴 모래가 있을 때
    if m_map[pos[0]][pos[1]] != 0:
        # 휘날리기
        remain_sand = m_map[pos[0]][pos[1]]
        for per_r, per_c, per in per_map:

            # 해당 인덱스에 따라 90도씩 회전하기
            sand_r, sand_c = rotate_m(per_r, per_c, dir_idx)
            amount_sand = math.floor(m_map[pos[0]][pos[1]] * per)

            if amount_sand == 0:
                continue

            sand_r += pos[0]
            sand_c += pos[1]

            # 범위에 벗어나면 날린 모래
            if sand_r < 0 or sand_r >= N or sand_c < 0 or sand_c >= N:
                if per == 1:
                    sand_sum += remain_sand
                else:
                    sand_sum += amount_sand
                    remain_sand -= amount_sand
            else:
                if per == 1:
                    m_map[sand_r][sand_c] += remain_sand
                else:
                    m_map[sand_r][sand_c] += amount_sand
                    remain_sand -= amount_sand

        m_map[pos[0]][pos[1]] = 0

    # 방향 및 숫자 칸수 조정
    sub_try += 1
    
    if sub_try == go_n:
        try_n += 1
        dir_idx = (dir_idx + 1) % 4
        sub_try = 0

    if try_n == 2:
        go_n += 1
        try_n = 0
        

print(sand_sum)