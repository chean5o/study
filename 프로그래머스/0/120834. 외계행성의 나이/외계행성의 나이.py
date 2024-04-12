def solution(age):
    age = str(age)
    answer=''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for i in age:
        answer += alphabet[int(i)]
    return answer