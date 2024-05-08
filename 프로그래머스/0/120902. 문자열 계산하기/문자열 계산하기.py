def solution(my_string):
    answer = 0
    list_str = my_string.split()
    if list_str[1] == '+':
        answer += int(list_str[0]) + int(list_str[2])
    elif list_str[1] == '-':
        answer = int(list_str[0]) - int(list_str[2])
    for i in range(2, len(list_str)):
        if list_str[i] == '+':
            answer += int(list_str[i+1])
        elif list_str[i] == '-':
            answer -= int(list_str[i+1])
    return answer