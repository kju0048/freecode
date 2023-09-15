import sys

def five_pow(i):
    ret = 0
    for i in range (0, 5-i):
        ret = ret + 5**i
    return ret

def solution(word):
    word_turn = ['A', 'E', 'I', 'O', 'U']
    answer = 1
    
    wordL = word.strip()
    word_length = len(wordL)
    
    for i in range(0, len(wordL)):
        answer = answer + word_turn.index(wordL[i]) * five_pow(i)
        if word_length == i + 1:
            return answer + i
    
    # answer = answer + word_turn.index(wordL[0]) * 781 # 5^4 + 5^3 + 5^2 + 5^1 + 5^0
    # if word_length == 1:
    #     return answer
    # answer = answer + word_turn.index(wordL[1]) * 156 # 5^3 + 5^2 + 5^1 + 5^0
    # if word_length == 2:
    #     return answer + 1
    # answer = answer + word_turn.index(wordL[2]) * 31 # 5^2 + 5^1 + 5^0
    # if word_length == 3:
    #     return answer + 2
    # answer = answer + word_turn.index(wordL[3]) * 6 # 5^1 + 5^0
    # if word_length == 4:
    #     return answer + 3
    # answer = answer + word_turn.index(wordL[4]) * 1 # 5^0
    # if word_length == 5:
    #     return answer + 4
        
    
    
    