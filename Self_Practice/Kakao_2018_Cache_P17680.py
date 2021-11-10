def solution(cacheSize, cities):
    answer = 0
    
    cache = []
    for c_item in cities:
        c_item = c_item.lower()
        if c_item not in cache:
            cache.append(c_item)
            if len(cache) > cacheSize:
                cache.pop(0)
            answer += 5
        else:
            cache.pop(cache.index(c_item))
            cache.append(c_item)
            answer += 1
    
    return answer