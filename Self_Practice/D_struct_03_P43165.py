from collections import deque

# BFS
def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([numbers[0], 0])
    queue.append([numbers[0] * (-1), 0])

    num_len = len(numbers)    
    while queue:
        tmp, idx = queue.popleft()
        
        idx += 1
        if idx < num_len:
            queue.append([tmp + numbers[idx], idx])
            queue.append([tmp - numbers[idx], idx])
        else:
            if tmp == target:
                answer += 1
                
    return answer

