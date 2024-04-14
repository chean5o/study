def solution(hp): # 5, 3, 1
    answer = 0
    tmp = 0
    tmp2 = 0
    if hp < 3:
        answer = hp // 1
    elif hp < 5:
        tmp = hp // 3
        answer = tmp
        answer += (hp - tmp * 3) // 1
    else:
        tmp = hp // 5
        answer = hp // 5
        if hp % 5 != 0:
            answer += (hp - tmp * 5) // 3
            tmp2 = (hp - tmp * 5) // 3
            if (hp - tmp * 5) % 3 !=  0 :
                answer += ((hp - tmp * 5) - tmp2 * 3) // 1
    return answer