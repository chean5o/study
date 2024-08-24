n, k = map(int, input().split())
kid_h = list(map(int, input().split()))
arr = []
res = 0
for i in range(n-1):
  arr.append(kid_h[i+1] - kid_h[i])
arr.sort()
for i in range(n-k):
  res += arr[i]

print(res)