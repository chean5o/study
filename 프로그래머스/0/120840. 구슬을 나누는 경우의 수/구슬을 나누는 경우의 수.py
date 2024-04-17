def solution(balls, share):
    answer = 0
    fac_balls = 1
    fac_share = 1
    mid = 1
    for i in range(1, balls+1):
        fac_balls *= i
    for j in range(1, share+1):
        fac_share *= j
    for k in range(1, balls-share+1):
        mid *= k
        
    answer = fac_balls // (mid * fac_share) 
    return answer