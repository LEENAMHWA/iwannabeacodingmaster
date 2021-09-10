#Query<->Info 위치 바꿔보기
def solution(info, query):
    q_count = [0] * len(query)
    
    query = list(map(lambda x: x.replace(' and ',' ').split(),query))
    info = list(map(lambda x: x.split(' '), info))
    
    # 하나씩 불러와서 비교, 없으면 바로 넘기기
    for i_idx in range(len(info)):
        match = 0
        for q_idx in range(len(query)):
            
            # Score Filtering
            if int(info[i_idx][-1]) < int(query[q_idx][-1]):
                continue
            
            for item_idx in range(len(info[i_idx]) - 1):
                if (query[q_idx][item_idx] == '-') or (query[q_idx][item_idx] == info[i_idx][item_idx]):
                    # Pass
                    if item_idx == len(info[i_idx]) - 2:
                        q_count[q_idx] += 1
                    continue
                else:
                    # Mismatch
                    break                    
    
    return q_count