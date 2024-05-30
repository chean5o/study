def solution(keyinput, board):
    answer = [0, 0]
    tmp_x = board[0] // 2
    tmp_y = board[1] // 2
    print("tmp_x:", tmp_x)
    print("tmp_y:", tmp_y)
    for i in keyinput:
        if i == "left":
            if tmp_x * -1 < answer[0]:
                answer[0] -= 1
            else:
                answer[0] = tmp_x * -1
        elif i == "right":
            if tmp_x > answer[0]:
                answer[0] += 1
            else:
                answer[0] = tmp_x
        elif i == "up":
            if tmp_y > answer[1]:
                answer[1] += 1
            else:
                answer[1] = tmp_y
        else:
            if tmp_y * -1 < answer[1]:
                answer[1] -= 1
            else:
                answer[1] = tmp_y * -1
            
    print("비교전",answer)
    return answer