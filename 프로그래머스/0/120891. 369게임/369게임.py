def solution(order):
    answer = list(map(int,str(order)))
    tmp = 0
    for i in range(0, len(answer)):
        if answer[i] != 0 and answer[i] % 3 == 0:
            tmp += 1
    return tmp