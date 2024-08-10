from collections import deque

n, m = map(int, input().split())
shark = [list(map(int, input().split())) for _ in range(n)]

row = [-1, -1, -1, 0, 0, 1, 1, 1]# 방향 벡터 정의 (8방향: 상, 하, 좌, 우, 대각선 4개)
col = [-1, 0, 1, -1, 1, -1, 0, 1]

queue = deque()# 모든 아기 상어 위치를 큐에 추가
visited = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if shark[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = 0  # 아기 상어 위치는 거리가 0

# BFS 실행
while queue:
    curr_r, curr_c = queue.popleft()

    for i in range(8):
        n_r = curr_r + row[i]
        n_c = curr_c + col[i]

        if 0 <= n_r < n and 0 <= n_c < m and visited[n_r][n_c] == -1:
            visited[n_r][n_c] = visited[curr_r][curr_c] + 1
            queue.append((n_r, n_c))

# 방문 배열에서 가장 큰 값을 찾기
res = max(max(dis) for dis in visited)
print(res)