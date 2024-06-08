def solution(n):
    answer = 0
    tmp = []
    for i in range(0, 186):
        if i % 3 != 0 and '3' not in str(i):
            tmp.append(i)
    print(tmp)
    return tmp[n-1]