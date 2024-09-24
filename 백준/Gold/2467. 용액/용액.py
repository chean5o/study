n = int(input())
liquid = list(map(int, input().split()))
start = 0
end = n - 1
res = abs(liquid[start] + liquid[end])
left_res = 0
right_res = 0
while start < end:
  tot = liquid[start] + liquid[end]

  if abs(tot) <= res:
    left_res = start
    right_res = end
    res = abs(tot)

    if res == 0:
      break
  if tot < 0:
    start += 1
  else:
    end -= 1
print(liquid[left_res], liquid[right_res])