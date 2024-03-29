def solution(n):
    i = 0
    answer = 0
    while i <= n:
      if i % 2 == 0:
        answer += i
        i += 1
      else:
        i += 1
    return answer