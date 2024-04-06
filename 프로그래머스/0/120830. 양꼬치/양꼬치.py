def solution(n, k):
    answer = 0
    # tot = n * 12000 + k * 20000
    if n // 10 > 0:
        k = k - (n // 10)
    answer = n * 12000 + k * 2000
    return answer