def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        tmp = 0
        for j in range(1, i+1):
            if i % j == 0:
                tmp += 1
                print(i, tmp)
        if tmp >= 3:
            answer += 1
    return answer