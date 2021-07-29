from collections import deque
    
def solution(n, computers):
    answer = 0
    vist = [False for idx in range(n)]
    
    for c_idx in range(n):
        # Visit array가 False = 아직 인접노드로 방문 되지 않은것 (이어져 있지 않음)
        if vist[c_idx] == False:
            bfs(vist, computers, c_idx, n)
            answer += 1

    return answer


def bfs(vist, computers, n_idx, n):
    vist[n_idx] = True
    queue = deque()
    queue.append(n_idx)
    while queue:
        n_idx = queue.popleft()
        vist[n_idx] = True
        # 방문 하지 않은 인접 노드 큐에 넣기 
        for conn_idx in range(n):
            if (conn_idx != n_idx) and computers[n_idx][conn_idx] == 1:
                if vist[conn_idx] == False:
                    queue.append(conn_idx)

