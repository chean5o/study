def solution(k, m, score):
    answer = 0
    mini = 0
    score.sort(reverse=True)
    # print(score)
    if len(score) % m == 0:
        # for i in range(0, len(score), (len(score) // m) -1):
        for i in range(0, len(score), m):
            tmp = []
            tmp = score[i:i+m]
            # print(tmp)
            answer += (min(tmp) * m * 1)
    else:
        if len(score) // m < 2:
             for i in range(0, (len(score) // m)):
                    tmp = []
                    tmp = score[i:i+m]
                    # print(tmp)
                    answer += (min(tmp) * m * 1)
        else:
            for i in range(0, len(score), m):
                    tmp = []
                    tmp = score[i:i+m]
                    # print(tmp, i)
                    if len(tmp) == m:
                        # print("더하기~")
                        answer += (min(tmp) * m * 1)
                    else:
                        break
    return answer