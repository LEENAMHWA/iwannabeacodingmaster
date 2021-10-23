import sys
from collections import deque
import math

N, M, K = list(map(int, sys.stdin.readline().split()))
move_dir = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]

# MAP 지나갈때 초기화 제발 ㅠ

# 질량합
m_sum = 0

# 파이어볼 정보
fb_info = deque()

# 파이어볼 맵
fb_map = []
for _ in range(N):
    fb_tmp = []
    for _ in range(N):
        # 질량, 속도합, 방향, 방향 변화, 카운트
        fb_tmp.append([0,0,0,0,0])
    fb_map.append(fb_tmp)

# 파이어볼 붙이기
for m_idx in range(M):
    tmp_info = list(map(int, sys.stdin.readline().split()))
    tmp_info[0] -= 1
    tmp_info[1] -= 1
    fb_info.append(tmp_info)
    
# Index 니까 -1 씩, input 과 index의 관계 잘 파악할 것

for try_idx in range(K + 1):
    
    # 파이어볼 맵
    fb_map = []
    for _ in range(N):
        fb_tmp = []
        for _ in range(N):
            # 질량, 속도합, 방향, 방향 변화, 카운트
            fb_tmp.append([0,0,0,0,0])
        fb_map.append(fb_tmp)

    while fb_info:
        r, c, m, s, d = fb_info.popleft()
        if try_idx >= K:
            m_sum += m
            continue
        
        # 1 Fireball move
        nr = (r + (move_dir[d][0] * s)) % N
        nc = (c + (move_dir[d][1] * s)) % N
        
        # Count
        fb_map[nr][nc][4] += 1

        # Speed
        fb_map[nr][nc][1] += s

        # mass
        fb_map[nr][nc][0] += m
        
        # 처음 접근이 아닐 떄
        if fb_map[nr][nc][4] >= 2:
            # 직전 방향과 짝수 홀수 다른지 여부 판단
            if (fb_map[nr][nc][2] % 2) != (d % 2):
                # 다르면 1 넣기
                fb_map[nr][nc][3] = 1
        
        fb_map[nr][nc][2] = d
        # if nr == 1 and nc == 0:

    if try_idx >= K:
        break


    # 추가 cycle
    for r_idx in range(N):
        for c_idx in range(N):
            # 파이어볼이 존재하지 않는 경우
            if fb_map[r_idx][c_idx][0] == 0:
                continue

            # 존재하는 경우
            else:
                # 한개인 경우
                nm = fb_map[r_idx][c_idx][0]
                ns = fb_map[r_idx][c_idx][1]
                nd = fb_map[r_idx][c_idx][2]
                nd_true = fb_map[r_idx][c_idx][3]
                ncnt = fb_map[r_idx][c_idx][4]

                if ncnt <= 1:
                    fb_info.append([r_idx, c_idx, nm, ns, nd])
                    continue
                
                # 여러개인 경우
                nm = math.floor(nm / 5)

                # 질량 0이면 버린다, append를 하지 않는다
                if nm <= 0:
                    continue
    
                ns = math.floor(ns / ncnt)
                for dir_idx in range(len(move_dir)):
                    if (dir_idx % 2) == nd_true:
                        fb_info.append([r_idx, c_idx, nm, ns, dir_idx])

print(m_sum)