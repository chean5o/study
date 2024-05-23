def solution(quiz):
    answer = []
    res = []
    tmp= 0
    for i in range(0, len(quiz)):
        answer = quiz[i].split()
        if answer[1] == '-':
            tmp = int(answer[0]) - int(answer[2])
            if tmp == int(answer[4]):
                res.append('O')
            else:
                res.append('X')
        elif answer[1] == '+':
            tmp = int(answer[0]) + int(answer[2])
            if tmp == int(answer[4]):
                res.append('O')
            else:
                res.append('X')
    return res