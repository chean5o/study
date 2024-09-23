n, m = map(int, input().split())
trees = list(map(int, input().split()))
start = 1
end = max(trees)
while start <= end:
  mid = (start + end) // 2

  tot = 0
  for i in trees:
    if i >= mid:
      tot += i - mid

  if tot >= m:
    start = mid + 1
  else:
    end = mid -1

print(end)