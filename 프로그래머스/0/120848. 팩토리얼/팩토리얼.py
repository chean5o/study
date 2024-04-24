def solution(n):
    answer = []
    fac = []
    for i in range(1, 11):
        tmp = 1
        for j in range(1,i+1):
            tmp *= j
        fac.append(tmp)
            
    for k in range(0, 10):
        if n >= fac[k]:
            answer.append(fac[k])
        
    return answer.index(answer[-1]) + 1