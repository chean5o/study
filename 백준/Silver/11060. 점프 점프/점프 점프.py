n = int(input())
jump = list(map(int, input().split()))
dp = [-1] * n
dp[0] = 0
for i in range(n):
  if dp[i] == -1:
    continue
  for j in range(jump[i]+1):
    if i + j >= n:
      break
    if dp[i+j] == -1 or dp[i+j] > dp[i] +1:
      dp[i+j] = dp[i] + 1
print(dp[n-1])