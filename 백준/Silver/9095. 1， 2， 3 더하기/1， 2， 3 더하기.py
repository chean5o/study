dp = [0] * 11  
dp[0] = 1 

for i in range(1, 11):
    if i >= 1:
        dp[i] += dp[i-1]
    if i >= 2:
        dp[i] += dp[i-2]
    if i >= 3:
        dp[i] += dp[i-3]

T = int(input())  
for _ in range(T):
    n = int(input()) 
    print(dp[n]) 