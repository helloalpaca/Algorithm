def skill_tree(skill, skill_tree):
    skill_list = list(skill)
    temp = []
    flag = True
    for i in range(len(skill_tree)):
        if skill_tree[i] in skill_list:
            temp.append(skill_tree[i])

    for i in range(len(temp)):
        if(skill_list[i]!=temp[i]):
            flag = False

    return flag

def solution(skill, skill_trees):
    answer = 0
    for temp in skill_trees:
        flag = skill_tree(skill, temp)
        if(flag):
            answer+=1
    return answer