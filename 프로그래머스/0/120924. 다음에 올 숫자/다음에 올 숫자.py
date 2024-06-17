def solution(common):
    answer = 0
    d = common[2] - common[1]
    if common[0] != 0 :
        r = common[1] // common[0]
    # else:
    #     print("0으로 못나눔")
    #     return 0
    # print(d, r)
    for i in range(0, len(common)-1):
        if common[i] + d == common[i+1]:
            if d == 0:
                return common[len(common)-1]
            else:
                return common[len(common)-1] + d
        else:
            if common[0] == 0:
                return 0
            else:
                # print("등비",common[len(common)-1])
                return common[len(common)-1] * r