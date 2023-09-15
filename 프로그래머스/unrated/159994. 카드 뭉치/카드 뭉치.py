def solution(cards1, cards2, goal):
    answer = "Yes"

    for ans in goal:
        if len(cards1) > 0 and cards1[0] == ans:
            del cards1[0]
        elif len(cards2) > 0 and cards2[0] == ans:
            del cards2[0]
        else:
            return "No"
            
    return answer