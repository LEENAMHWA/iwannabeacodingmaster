def solution(n, s, a, b, fares):
    inf = 1000000000
    answer = inf
    
    total = []
    for _ in range(n):
        total.append([inf] * n)
        
    for info in fares:
        total[info[0]-1][info[1]-1] = total[info[1]-1][info[0]-1] = info[2] 
    
    # 자기 자신 체크 안하면 왜 문제됨..?
    for i in range(n):
        total[i][i] = 0
        
    # 최단거리 구하기
    for m in range(n):
        for r in range(n):
            for c in range(r + 1, n):
                    tmp = min(total[r][c], (total[r][m] + total[m][c]))
                    total[r][c] = total[c][r] = tmp
    
    for m in range(n):
        answer = min(answer, total[s-1][m] + total[m][a-1] + total[m][b-1])
                    
    return answer