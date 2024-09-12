import sys
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, color, picture, visited, n):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위를 벗어나지 않고, 방문하지 않았으며, 같은 색인 경우에 탐색
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and picture[nx][ny] == color:
            dfs(nx, ny, color, picture, visited, n)

n = int(input())
picture = [list(input().strip()) for _ in range(n)]

# 적록색약이 아닌 경우
visited = [[False] * n for _ in range(n)]
normal_count = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, picture[i][j], picture, visited, n)
            normal_count += 1

# 적록색약인 경우, 'R'을 'G'로 변환한 새로운 그리드를 사용
visited = [[False] * n for _ in range(n)]
picture_b = [['G' if color == 'R' else color for color in row] for row in picture]
b_count = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, picture_b[i][j], picture_b, visited, n)
            b_count += 1

print(normal_count, b_count)