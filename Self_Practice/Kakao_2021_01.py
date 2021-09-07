def solution(new_id):
    import re
    
    # rule 1
    new_id = new_id.lower()
    
    # rule 2
    new_id = re.sub('[^0-9a-zA-Zㄱ-힗-_.]', '', new_id)
    
    # rule 3
    new_id = re.sub('(([.])\\2{1,})', '.',new_id)

    # rule 4
    new_id = new_id.strip('.')
        
    # rule 5
    if new_id == '':
        new_id = 'a'
    
    # rule 6, 7
    if len(new_id) > 15:
        new_id = new_id[:15].rstrip('.')
    elif len(new_id) <= 2:
        new_id = new_id + (new_id[-1] * (3-len(new_id)))
    
    return new_id