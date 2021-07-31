from collections import deque

def how_diff(word_1, word_2):
    n_diff = 0
    
    for x, y in zip(word_1, word_2):
        if x != y:
            n_diff += 1
    
    return n_diff

def bfs(begin, target, words):
    queue = deque()
    idx = 0
    queue.append([begin, idx, []])
    while queue:
        # queue 제일 앞의 단어와 1글자 차이면 모두 append
        w_tmp, idx, visited = queue.popleft()
        
        if w_tmp == target:
            return idx
            
        idx += 1
        for word_idx in range(len(words)):
            # 차이가 1인것 모두 append
            if (how_diff(words[word_idx], w_tmp) == 1) and (words[word_idx] not in visited):
                tmp_visited = visited
                tmp_visited.append(words[word_idx])
                queue.append([words[word_idx], idx, tmp_visited])

                
def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 0

    answer = bfs(begin, target, words)

    return answer
