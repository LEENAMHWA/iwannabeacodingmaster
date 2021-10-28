import sys
import copy

move_idx = [[-1,0],[1,0],[0,-1],[0,1]]

# # 단계 L 결정 (2^L 만큼 뭉치)
# # 격자 단위로 회전
# # rotate 90 만들기
# # 얼음 있는 칸 3개 이상과 붙어 있지 않으면 얼음 -1
# #            (move_idx 활용)..?

N, Q = list(map(int, sys.stdin.readline().split()))

# Map
i_map = []
for _ in range(pow(2,N)):
    i_map.append(list(map(int, sys.stdin.readline().split())))

# L arr
L_arr = list(map(int, sys.stdin.readline().split()))

ice_sum = 0
# 얼음 묶기 시작
for L in L_arr:
    pos_r = 0
    pos_c = 0
    L2 = pow(2,L)

    # L 값에 따른 격자별 돌리기
    while True:
        if (pos_r >= len(i_map) - L2) and (pos_c >= len(i_map) - L2):
            break

        print(pos_r, pos_c)
        print(pos_r + L2, pos_c + L2)
        print()

        # Rotate
        tmp_arr = copy.deepcopy(i_map[pos_r:(pos_r + L2)])
        for r_idx in range(L2):
            for c_idx in range(L2):
                i_map[pos_r + c_idx][pos_c + (L2-1-r_idx)] = tmp_arr[r_idx][pos_c + c_idx]

        # 행, 열 바꾸기
        if pos_c == len(i_map) - L2:
                pos_r += L2
                pos_c = 0

        else:
            pos_c += L2
        

    for r_idx in range(len(i_map)):
        for c_idx in range(len(i_map)):
            none_cnt = 0
            for move in move_idx:
                nr = r_idx + move[0]
                nc = c_idx + move[1]
                if nr >= len(i_map) or nr < 0 or nc >= len(i_map) or nc < 0:
                    continue
                elif i_map[nr][nc] <= 0:
                    none_cnt += 1
                if none_cnt >= 3:
                    i_map[r_idx][c_idx] -= 1


    
print(i_map)
                

