import sys

N = int(sys.stdin.readline().split()[0])
move = [[-1,0], [1,0], [0,-1], [0,1]]

arr = []
for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))

cnt = 0
def dfs(r,c):
    
    if r >= N or r < 0 or c >= N or c < 0:
        return False
    
    if arr[r][c] != 0:
        global cnt 
        cnt += arr[r][c]
        arr[r][c] = 0
        for m_item in move:
            dfs(r + m_item[0],c + m_item[1])
        return True

    else:
        return False

result = 0
for r_idx in range(N):
    for c_idx in range(N):
        if dfs(r_idx,c_idx) == True:
            result += 1
            print(cnt)
            cnt = 0

print(result)