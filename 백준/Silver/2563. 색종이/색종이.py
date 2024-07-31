n = int(input())
arr = [[0] * 100 for i in range(100)]

for i in range(n):
  y, x = map(int, input().split())

  for j in range(x, x+10):
    for k in range(y, y+10):
      arr[j][k] = 1

res = 0

for i in range(100):
  res += arr[i].count(1)

print(res)