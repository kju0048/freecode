def solution(skill, skill_trees):
    answer = 0
    skill_arr = list(skill)
    
    for each_skill_t in skill_trees:
        skill_rank = []
        for single_skill in each_skill_t:
            if single_skill in skill_arr:
                skill_rank.append(skill.index(single_skill))
        length_r = len(skill_rank)
        if skill_rank == sorted(skill_rank) and sum(skill_rank) == length_r * (length_r - 1) // 2:
            answer += 1
        
    return answer