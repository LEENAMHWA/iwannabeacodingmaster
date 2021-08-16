def solution(people, limit):
    answer = 0
    people.sort()
    # Sort 후에 양 끝부터 계산하며 갯수 파악
    l_idx = 0
    r_idx = len(people) - 1
    while l_idx < r_idx:
        if (people[l_idx] + people[r_idx]) <= limit:
            l_idx += 1
            r_idx -= 1
            answer += 1
        else:
            r_idx -= 1
            answer += 1
    if l_idx == r_idx:
        answer += 1
    
    return answer