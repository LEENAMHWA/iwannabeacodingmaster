from collections import deque

def bfs(tickets):
    visited = [False for x in tickets]
    queue = deque()
    trav_path = []
    
    # INIT
    for item_idx in range(len(tickets)):
        if tickets[item_idx][0] == "ICN":
            remained = []
            remained.extend(tickets)
            remained.pop(remained.index(tickets[item_idx]))
            queue.append([tickets[item_idx], [tickets[item_idx]], remained])
            
    idx = 0 
    while queue:
        idx += 1
        tmp_path, visited, remained = queue.popleft()
        if len(tickets) == len(visited):
            trav_path.append(visited)
            
        for path_idx in range(len(tickets)):
            visit_tmp = []
            visit_tmp.extend(visited)
            
            remained_tmp = []
            remained_tmp.extend(remained)
            
            if tickets[path_idx][0] == visited[-1][1]:
                if tickets[path_idx] not in remained_tmp:
                    continue
                else:
                    visit_tmp.append(tickets[path_idx])
                    remained_tmp.pop(remained_tmp.index(tickets[path_idx]))
                    queue.append([tickets[path_idx],visit_tmp, remained_tmp])
    return trav_path
    
    
                
def solution(tickets):
    answer = []

    ans_tmp = bfs(tickets)
    ans_tmp.sort()
    
    for data in ans_tmp[0]:
        answer.append(data[0])
        
    answer.append(ans_tmp[0][-1][1])
    
    return answer