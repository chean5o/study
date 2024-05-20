def solution(n):
    answer = 0
    tmp = int(n ** 0.5)
    if tmp**2 == n:
        answer = 1
    else:
        answer = 2
    return answer