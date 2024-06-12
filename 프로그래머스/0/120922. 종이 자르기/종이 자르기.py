def solution(M, N):
    col = 0
    row = M - 1
    if row > 1:
        col = (N - 1) * M
    elif row == 0:
        col = (N - 1)
    else:
        col = (N - 1) * 2
    return row + col