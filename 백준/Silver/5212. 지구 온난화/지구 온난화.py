r, c = map(int, input().split())
s_map = [list(input()) for _ in range(r)]
n_map = [['.'] * c for _ in range(r)]

def find_sea(land, x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    sea_count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= r or ny >= c or land[nx][ny] == '.':
            sea_count += 1
    return sea_count >= 3

for i in range(r):
    for j in range(c):
        if s_map[i][j] == 'X':
            if not find_sea(s_map, i, j):
                n_map[i][j] = 'X'

min_row, max_row = r, 0
min_col, max_col = c, 0
is_land_found = False

for i in range(r):
    for j in range(c):
        if n_map[i][j] == 'X':
            if not is_land_found:
                min_row = i
                min_col = j
                is_land_found = True
            min_row = min(min_row, i)
            max_row = max(max_row, i)
            min_col = min(min_col, j)
            max_col = max(max_col, j)

for i in range(min_row, max_row + 1):
    print("".join(n_map[i][min_col:max_col + 1]))