def solution(numbers):
    answer = 0
    tmp =[]
    num1 = 0
    num2 = 0
    maxi = 0
    maxi_2 = 0
    num1 = max(numbers)
    numbers.remove(num1)
    num2 = max(numbers)
    maxi = num1 * num2
    print(maxi)
    for i in numbers:
        if i < 0:
            answer += 1
    if answer % 2 == 0 and answer != 0:
        for i in range(0,len(numbers)):
            if numbers[i] < 0:
                tmp.append(numbers[i] * -1)
        num1 = max(tmp)
        tmp.remove(num1)
        num2 = max(tmp)
        maxi_2 = num1 * num2
        
        if maxi > maxi_2:
            answer = maxi
        else:
            answer = maxi_2
        
    else:
        answer = maxi
        
    
    return answer