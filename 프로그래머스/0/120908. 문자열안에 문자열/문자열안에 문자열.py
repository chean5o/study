def solution(str1, str2):
    answer = 0
    answer = str1.find(str2)
    if answer != -1:
        answer = 1
    else:
        answer += 3
    return answer