def solution(players, callings):
    dic = {}
    for rank, name in enumerate(players):
        dic[name] = rank
    
    for call in callings:
        winp_index = dic[call]
        losep_name = players[winp_index - 1]
        
        dic[call], dic[losep_name] = dic[losep_name], dic[call]
        players[winp_index], players[winp_index-1] = players[winp_index-1], players[winp_index]
        
    
        
    return players