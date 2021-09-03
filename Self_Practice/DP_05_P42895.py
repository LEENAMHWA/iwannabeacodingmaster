def solution(N, number):
    answer = 0
    
    dp = [[]]
    for idx in range(1,9):
        sub_dp = []
        
        for sub_idx in range(1, idx):
            for idx1 in dp[sub_idx]:
                for idx2 in dp[idx - sub_idx]:
                    sub_dp.append(idx1 + idx2)
                    if idx1 - idx2 >= 0:
                        sub_dp.append(idx1-idx2)
                    if idx1 != 0 and idx2 != 0:
                        sub_dp.append(idx1 / idx2)
                    sub_dp.append(idx1 * idx2)
                    
        sub_dp.append(int(str(N) * idx))
        
        if number in sub_dp:
            return idx
        else:
            dp.append(list(set(sub_dp)))
            
    return -1