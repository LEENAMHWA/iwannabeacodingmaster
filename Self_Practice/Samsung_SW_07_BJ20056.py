# 22:15

import sys
from collections import deque

go_dir = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]

N, M, K = list(map(int,sys.stdin.readline().split()))

f_info = deque()
#             홀 - 0, 짝 - 1              
#          수,직전,일괄 여부 - 0(일괄), 1(일치 X), 갯수, 속력
f_map = []
m_sum = 0

for _ in range(N):
    f_row = []
    for _ in range(N):
        f_row.append([0,0,0,0,0])
    f_map.append(f_row)

for r_idx in range(M):
    # 파이어볼 정보 받기
    # row, column, 질량, 속도, 방향
    # r c m s d 
    f_info.append(list(map(int,sys.stdin.readline().split())))

for try_idx in range(K + 1):
    print(f_info)
    while f_info:
        # 하나 꺼냄
        r, c, m, s, d = f_info.popleft()

        if try_idx == K:
            m_sum += m
            continue
        
        # 이동하기
        nr = (r + (go_dir[d][0]*s)) % N
        nc = (c + (go_dir[d][1]*s)) % N
        
        # 첫 접근이면
        if f_map[nr][nc][0] == 0:
            f_map[nr][nc][1] = d # 짝수 홀수 판단
            f_map[nr][nc][2] = 0 # 같은 여부 체크
        else:
            # 직전 방향과 같은지 check
            # 다르면 1
            if f_map[nr][nc][1] % 2 != d % 2:
                f_map[nr][nc][2] = 1

        # 질량, 카운트, 속력(공통)
        f_map[nr][nc][0] += m
        f_map[nr][nc][3] += 1
        f_map[nr][nc][4] += s

    for r_idx in range(N):
        for c_idx in range(N):
            if f_map[r_idx][c_idx][0] == 0:
                continue
                
            # 파이어볼 질량 있을경우
            else:
                m_total = f_map[r_idx][c_idx][0]
                d_total = f_map[r_idx][c_idx][1]
                cnt_total = f_map[r_idx][c_idx][3]
                v_total = f_map[r_idx][c_idx][4]

                # 추가하기
                if f_map[r_idx][c_idx][3] == 1:
                    # 한 개
                    f_info.append(list(map(int,[r_idx, c_idx, m_total, v_total, d_total])))
                else:
                    # 여러 개
                    v_total /= cnt_total
                    m_total /= 5
                    if m_total <= 0:
                        continue

                    d_total = f_map[r_idx][c_idx][1]
                    d_idx_total = f_map[r_idx][c_idx][2]
                    for go_idx in range(len(go_dir)):
                        # 방향 같음
                        if (go_idx % 2) == d_idx_total:
                            f_info.append(list(map(int,[r_idx, c_idx, m_total, v_total, go_idx])))

    
print(m_sum)
