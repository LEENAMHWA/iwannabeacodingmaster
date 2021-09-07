def solution(orders, course):
    # 조합 직접 하지 말고 combinations 사용할 것!
    from itertools import combinations as comb
    answer = []
    
    for c_size in course:
        order_dict = {}
        order_comb = []
        for order in orders:
            order_comb.extend(list(comb(sorted(order), c_size)))
            
        for order_item in order_comb:
            order_str = ''.join(order_item)
            
            if order_str in order_dict:
                order_dict[order_str] += 1
            else:
                order_dict[order_str] = 1
        
        for order_d_item in order_dict:
            if order_dict[order_d_item] == max(order_dict.values()) and order_dict[order_d_item] > 1:
                answer.append(order_d_item)
            
    return sorted(answer)