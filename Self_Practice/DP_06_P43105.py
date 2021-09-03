def solution(triangle):
    answer = 0
    
    d = [triangle[0]]
    
    for idx in range(1, len(triangle)):
        d.append([0]*len(triangle[idx]))
        for sub_idx in range(len(d[idx]) - 1):
            d[idx][sub_idx] = max(d[idx-1][sub_idx] + triangle[idx][sub_idx], d[idx][sub_idx])
            d[idx][sub_idx+1] = d[idx-1][sub_idx] + triangle[idx][sub_idx + 1]
        
    return max(d[-1])