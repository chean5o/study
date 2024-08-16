n, m = map(int, input().split())
time = [int(input()) for _ in range(n)]

def binary_search(arr, start, end):
  result = end
  while start <= end:
    mid = (start + end) // 2
    tot = 0

    for i in time:
      tot += mid // i

    if tot >= m:
      result = mid
      end = mid - 1
    else:
      start = mid + 1

  return result

# 결과 출력
print(binary_search(time, min(time), max(time) * m))