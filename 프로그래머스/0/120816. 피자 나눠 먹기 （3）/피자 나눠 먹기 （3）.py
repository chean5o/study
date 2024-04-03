def solution(slice, n):
    answer = 0
    # if slice >= n:
    #         answer = n // slice + 1
    # else: 
    if n % slice != 0:
        answer = (n // slice) + 1
    else:
        answer = n // slice
    return answer