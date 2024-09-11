import math
from collections import deque

# 상하좌우 방향 벡터
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    global m, res

    q = deque([(x, y)])  # 큐에 좌표를 튜플로 넣기
    cnt = 1  # 연결된 버섯 칸의 개수
    mushroom_farm[x][y] = 1  # 방문 처리

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and mushroom_farm[nx][ny] == 0:
                mushroom_farm[nx][ny] = 1  # 방문 처리
                cnt += 1  # 연결된 칸의 수 증가
                q.append((nx, ny))  # 다음 탐색할 좌표를 큐에 넣기

    m -= math.ceil(cnt / k)  # 이 구역을 덮는 데 필요한 포자 개수 차감

# 입력 처리
n, m, k = map(int, input().split())
mushroom_farm = [list(map(int, input().split())) for _ in range(n)]
res = 0  # 연결된 구역 수

# 모든 칸에 대해 BFS 실행
for i in range(n):
    for j in range(n):
        if mushroom_farm[i][j] == 0:
            res += 1  # 새로운 구역 발견
            bfs(i, j)  # 해당 구역에 대해 BFS 실행

# 결과 출력
if m >= 0 and res > 0:
    print(f'POSSIBLE\n{m}')  # 남은 포자 수 출력
else:
    print('IMPOSSIBLE')