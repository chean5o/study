import math
def solution(n): # n과 6의 최소 공배수 구하기 // 최소공배수 / 6
    answer = 0
    if n % 6 == 0:
        answer = n // 6
        return answer
    else:
        answer = ((n*6) / math.gcd(n, 6) )// 6
    return answer