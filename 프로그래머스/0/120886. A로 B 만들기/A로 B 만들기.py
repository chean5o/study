def solution(before, after):
    answer = 0
    before_list = list(before)
    after_list = list(after)
    tmp = 0
    res = []
    for i in range(0, len(before_list)):
        if after_list[i] in before_list:
            tmp = before_list.index(after_list[i])
            del before_list[tmp]
        else:
            res.append(-1)
    if len(res) != 0:
        answer = 0
    else:
        answer = 1
    return answer