def solution(rsp):
    list_rsp = list(rsp)
    print(list_rsp)
    answer = ''
    for i in range (0,len(list_rsp)):
        if list_rsp[i] == '2':
            answer += '0'
        elif list_rsp[i] == '0':
            answer += '5'
        elif list_rsp[i] == '5':
            answer += '2'
    return answer