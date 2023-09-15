def solution(n, m, section):
    answer = 0
    save = 0
    for i in section:
        if not i <= save:
            answer += 1
            save = i + m - 1
    
    return answer