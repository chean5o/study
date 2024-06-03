def solution(i, j, k):
    answer = 0
    res = 0
    # str(k)
    for o in range(i, j+1):
        answer = str(o)
        answer = list(answer)
        # print(answer)
        for e in range(0, len(answer)):
            if int(answer[e]) == k:
                # print(answer)
                res += 1
            else:
                # print(answer)
                res += 0
        # print('next')
    return res