def solution(score):
    # answer = []
    # tmp = []
    # res = 0
    # for i in range(0, len(score)):
    #     tmp.append((score[i][0] + score[i][1]) / 2)
    #     answer.append(0)
    # print(tmp)
    # for j in range(0, len(tmp)):
    #     tmp[tmp.index(max(tmp))] = res+1
    #     print(res)
    #     print('최대지우고',tmp)
    #     res += 1
    avg = [sum(i)/2 for i in score]
    s_avg = sorted(avg, reverse=True)

    answer =[] 
    for i in avg:
        answer.append(s_avg.index(i)+1)
    return answer