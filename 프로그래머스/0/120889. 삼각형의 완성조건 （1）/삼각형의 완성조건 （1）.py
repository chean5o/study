def solution(sides):
    answer = 0
    maxi = max(sides)
    sides.pop(sides.index(maxi))
    if maxi < sum(sides):
        answer = 1
    else:
        answer = 2
    
    return answer