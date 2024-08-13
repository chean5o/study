t = int(input())

def binary_search(target, arr, low, high):
  while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
  return low

for _ in range(t):
  n, m = map(int, input().split())
  arr_A = list(map(int, input().split()))
  arr_B = list(map(int, input().split()))
  arr_B.sort()
  res = 0

  for i in arr_A:
    idx = binary_search(i, arr_B, 0, m)
    
    # idx가 배열의 끝을 벗어날 경우를 처리
    if idx == m:
        best_val = arr_B[-1]
    else:
        best_val = arr_B[idx]
    
    if idx > 0:
        # 이전 값과 비교
        if abs(arr_B[idx-1] - i) < abs(best_val - i) or \
            (abs(arr_B[idx-1] - i) == abs(best_val - i) and arr_B[idx-1] < best_val):
            best_val = arr_B[idx-1]
    
    res += best_val

  print(res)
