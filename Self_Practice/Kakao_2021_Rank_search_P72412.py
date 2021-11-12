# 효율성 X
# def solution(info, query):
    
#     answer = [0] * len(query)
    
#     i_list = []
#     q_list = []
    
#     for item in info:
#         i_list.append(item.split())
#     for item in query:        
#         q_list.append(item.replace('and',  ' ').split())
    
#     for idx, q_item in enumerate(q_list):
#         cnt_mns = q_item.count('-')
        
#         # 전부 minus인 경우
#         if cnt_mns == len(q_item):
#             answer[idx] += len(i_list)
#             continue
            
#         for i_item in i_list:   
#             len_int = len(set(i_item[:-1]) & set(q_item[:-1]))
        
#             if len_int == len(q_item) - cnt_mns - 1:
#                 if (int(i_item[-1]) >= int(q_item[-1])) or q_item[-1] == '-':
#                     answer[idx] += 1
                    
            
#     return answer

def make_comb(arr):
    from itertools import combinations
    
    combs = []
    for idx in range(5):
        for tmp in list(combinations([0,1,2,3], idx)):
            tmp_comb = []

            for sub_idx in range(4):
                if sub_idx not in tmp:
                    tmp_comb.append('-')
                else:
                    tmp_comb.append(arr[sub_idx])

            combs.append(''.join(tmp_comb))
        
    # 문자열 모두 반환(key로 쓰임)
    return combs

def solution(info, query):
    from bisect import bisect_left
    answer = []
    all_cases = {}
    
    for item in info:
        sp_item = item.split()
        combs = make_comb(sp_item)
        
        for comb in combs:
            # 없다면
            if comb not in all_cases.keys():
                all_cases[comb] = [int(sp_item[-1])]
            # 이미 있으면
            else:
                all_cases[comb].append(int(sp_item[-1]))
                
    for key in all_cases.keys():
        all_cases[key].sort()
    
    for item in query:
        item = item.replace(' and ','').split()
        
        # Dict에 없을 시
        if item[0] not in all_cases.keys():
            answer.append(0)
            continue
            
        scores = all_cases[item[0]]
        
        if item[1] != '-':
            item[1] = int(item[1])
        else:    
            scores.append(len(scores))
            continue
        
        # # lower bound search
        # # 큰쪽으로 가는건 상관없음
        # l = 0
        # r = len(scores) - 1
        # while l <= r:
        #     mid = (r + l) // 2
        #     if item[1] <= scores[mid]:
        #         break
        #     elif item[1] > scores[mid]:
        #         l = mid + 1
        
        # bisect
        answer.append(len(scores) - bisect_left(scores, item[1]))
            
    return answer
