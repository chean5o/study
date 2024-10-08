n, m = map(int, input().split())
found_map = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = found_map[0][0]

for i in range(n):
  for j in range(m):
    if i == 0 and j == 0:
      continue
    elif i > 0 and j == 0:
      dp[i][j] = dp[i-1][j]
    elif i == 0 and j > 0:
      dp[i][j] = dp[i][j-1]
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    if found_map[i][j] == 1:
      dp[i][j] += 1
print(max(map(max, dp)))