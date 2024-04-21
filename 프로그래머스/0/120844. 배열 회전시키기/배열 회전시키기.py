def solution(numbers, direction):
    answer = []
    tmp = 0
    if direction == "right":
        tmp = numbers[-1]
        numbers.remove(tmp)
        numbers.insert(0,tmp)
    else:
        tmp = numbers[0]
        numbers.remove(tmp)
        numbers.append(tmp)
    return numbers