def solution(babbling):
    answer = 0
    say = ["aya", "ye", "woo", "ma"]
    for i in range(0,len(babbling)):
        for j in range(0, len(say)):
            if say[j] in babbling[i]:
                # 옹알이와 같은 부분을 *로 치환시키기
                babbling[i] = babbling[i].replace(say[j], "*")
        if all(char == "*" for char in babbling[i]):
            answer += 1
            
    return answer