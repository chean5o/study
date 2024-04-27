def solution(s):
    answer = s.split(' ')
    sum = 0
    for i in range(0,len(answer)):
        if answer[i] == 'Z' and i != 0:
            sum = sum - int(answer[i-1])
        else:
            sum += int(answer[i])
        
        
    return sum