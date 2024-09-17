M, n = map(int, input().split())
x, y = 0, 0
direction = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    command, value = input().split()
    value = int(value)

    if command == "MOVE":
        x += dx[direction] * value
        y += dy[direction] * value
        if not (0 <= x <= M and 0 <= y <= M):
            print(-1)
            exit()

    elif command == "TURN":
        if value == 0:  # 왼쪽으로 90도 회전
            direction = (direction + 1) % 4
        else:           # 오른쪽으로 90도 회전
            direction = (direction - 1) % 4

print(x, y)