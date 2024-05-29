def solution(dots):
    answer = 0
    row = 0
    col = 0
    for i in range(0, len(dots)):
        for j in range(i+1, len(dots)):
            if dots[i][1] == dots[j][1]:
                row = dots[i][0] - dots[j][0]
            elif dots[i][0] == dots[j][0]:
                col = dots[i][1] - dots[j][1]
    answer = abs(row*col)
    return answer