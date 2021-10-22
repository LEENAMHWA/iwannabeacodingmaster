import sys

N = int(sys.stdin.readline().split()[0])

chess = [0] * N
def dfs(chess, N, r):
    n_methods = 0

    # row가 가장 끝일 때
    if r == N:
        return 1

    # 현재 row의 현재 column 에서
    for c_idx in range(N):
        chess[r] = c_idx

        flag = 0
        # 대각 확인과 전에 있는지 확인, 나오지 않았다면 다음 순서로 진행 없으면 dfs 실행 x
        for sub_idx in range(r): 
            if chess[sub_idx] == chess[r]:
                flag = -1

            if abs(sub_idx - r) == abs(chess[sub_idx] - chess[r]):
                flag = -1
                
        if flag == 0:
            n_methods += dfs(chess, N, r + 1)

    return n_methods
result = dfs(chess, N, 0)
print(result)