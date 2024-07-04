def solution(arr, k):
    answer = []
    if k % 2 == 0:
        for i in range(0, len(arr)):
            answer.append(arr[i] + k)
    else:
        for i in range(0, len(arr)):
            answer.append(arr[i] * k)       
    return answer