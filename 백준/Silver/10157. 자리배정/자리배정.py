c, r = map(int, input().split())
k = int(input())
seat = [[0]*c for _ in range(r)]
dx = [0, 1, 0, -1] # 상 우 하 좌
dy = [1, 0, -1, 0]
x = y = 0
dir = 0

if k > r*c :
  print(0)
  exit()

for i in range(1, c*r+1):
  if i == k:
    print(x+1, y+1)
    break

  else:
    seat[y][x] = i
    x += dx[dir]
    y += dy[dir]

    if x < 0 or y < 0 or x >= c or y >= r or seat[y][x]:
      x -= dx[dir]
      y -= dy[dir]

      dir = (dir+1)%4
      x += dx[dir]
      y += dy[dir]