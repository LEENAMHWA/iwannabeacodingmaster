def solution(name):
    num = sum([1 if x != 'A' else 0 for x in name])
    
    if not num:
        return 0

    answer = cursor = next_ch = 0
    base_ch = 'A'
    
    # 정방향 돌기 vs 역방향 돌기 (Alphabet(상-하) 먼저 확인)
    answer = sum([min(ord(ch)-ord('A'), ord('Z')-ord(ch)+1) for ch in name])
    
    name = list(name)
    if name[0] != "A":
        num -= 1
        name[0] = "A"
    
    # 좌-우 확인(A의 존재에 따라 다름)
    cursor = 0    
    for i in range(num):
        for idx in range(1, len(name)):    
            r_idx = (cursor + idx)%len(name)
            l_idx = (cursor - idx)%len(name)
            
            if name[r_idx] != 'A':
                answer += idx
                cursor = r_idx
                name[cursor] = 'A'
                break

            if name[l_idx] != 'A':
                answer += idx
                cursor = l_idx
                name[l_idx] = 'A'
                break
                
    return answer
