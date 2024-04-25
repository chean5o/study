def solution(n):
    answer = []
    tmp = []
    for i in range(1, n+1):
        if n % i == 0:
            tmp.append(i)
    for i in range(1, len(tmp)):
        tmp_v = 0
        for j in range(1, tmp[i]+1):
            if tmp[i] % j == 0:
                tmp_v += 1
        if tmp_v != 2:
            tmp[i] = 0
    answer = [x for x in tmp if x not in (0, 1)]
    return answer