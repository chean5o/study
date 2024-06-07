def solution(spell, dic):
    answer = 0
    for i in dic:
        res = 0
        for j in spell:
            if j in i:
                res += 1
            else: res += 0
        if res == len(spell):
            answer = 1
            break
        else:
            answer = 2
    return answer