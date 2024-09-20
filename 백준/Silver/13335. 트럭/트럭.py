n, w, l = map(int, input().split())
truck_w = list(map(int, input().split()))

bridge = [0]*w
res = 0

while bridge:
  res += 1
  bridge.pop(0)
  if truck_w:
    if sum(bridge) + truck_w[0] <= l:
      bridge.append(truck_w.pop(0))
    else:
      bridge.append(0)

print(res)