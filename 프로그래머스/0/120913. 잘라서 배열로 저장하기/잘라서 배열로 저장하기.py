def solution(my_str, n):
    answer = []
    for i in range (0, len(my_str), n): #0, 3, 6, 9
        answer.append(my_str[i:n+i])
    return answer