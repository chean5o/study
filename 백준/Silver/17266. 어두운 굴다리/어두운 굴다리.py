n = int(input())
m = int(input())
light = list(map(int, input().split()))

start = light[0]
end = n - light[m-1]
mid = 0
if m == 1:
  print(max(start, end))
else:
  for i in range(m):
    mid = max(light[i] - light[i-1], mid)
  
  if mid % 2 != 0:
    mid = (mid//2)+1
  else:
    mid = mid//2

  print(max(start, end, mid))