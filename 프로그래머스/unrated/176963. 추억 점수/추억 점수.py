def solution(name, yearning, photo):
    answer = []
    for i in photo:
        num = 0
        for j in i:
            if j in name:
                num += yearning[name.index(j)]
        
        answer.append(num)
            
    
    
    return answer

    