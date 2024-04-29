def solution(array, n):
    answer = []
    res = 0
    array.sort()
    for i in range(0, len(array)):
        answer.append(abs(n-array[i]))
    res = answer.index(min(answer))
    print(res)
    return array[res]