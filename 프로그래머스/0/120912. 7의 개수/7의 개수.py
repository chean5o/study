def solution(array):
    answer = 0
    tmp = ''
    tmp = str(array)
    for i in tmp:
        if i == '7':
            answer += 1
    return answer