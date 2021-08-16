def solution(n, lost, reserve):
    answer = n
 
    common_list = list(set(lost) & set(reserve))
    lost = list(set(lost) - set(common_list))
    reserve = list(set(reserve) - set(common_list))
    
    for item_idx in range(len(lost)):
        for res_idx in range(len(reserve)):
            if abs(lost[item_idx] - reserve[res_idx]) == 1:
                lost[item_idx] = 0
                reserve.pop(res_idx)
                break
    for item in lost:
        if item != 0:
            answer -= 1
    
    return answer