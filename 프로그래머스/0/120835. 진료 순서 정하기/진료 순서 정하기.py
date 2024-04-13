def solution(emergency):
    answer = []
    sorted_emergency = sorted(emergency, reverse=True)
    for value in emergency:  
        idx = sorted_emergency.index(value) + 1
        answer.append(idx) 
    return answer
