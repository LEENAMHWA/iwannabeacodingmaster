def solution(s):
    answer = len(s)
    
    for col in range(1, (len(s) // 2) + 1):
        iter = len(s) // col
        
        tmp_len = 0
        tmp_cnt = 1
        for idx in range(0, iter):
            now = s[idx * col:(idx + 1) * col]
            next = s[(idx + 1) * col:(idx + 2) * col]
            if now == next:
                tmp_cnt += 1
            else:
                # n개 반복일 경우
                if tmp_cnt != 1:
                    tmp_len += (col + len(str(tmp_cnt)))
                    tmp_cnt = 1
                else:
                    tmp_len += col
                    
        tmp_len += len(s) % col
        answer = min(tmp_len, answer)
        
    return answer