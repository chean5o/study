def solution(num, total):
    answer = []
    mid = total // num
    if num % 2 == 0:
        for i in range((mid - num//2)+1, (mid + num//2)+1):
             answer.append(i)
    else:
        for i in range(mid- num//2, (mid + num//2) + 1):
            answer.append(i)
    # for i in range(0, 101):
    #     tmp = 0
    #     for j in range(i, num+i):
    #         tmp += j
    #     if tmp == total:
    #         for k in range(i,j+1):
    #             answer.append(k)
    #         break
    return answer