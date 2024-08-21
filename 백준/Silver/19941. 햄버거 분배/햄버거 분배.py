n, k = map(int, input().split())
table = list(input())
cnt = 0
for i in range(n):
  if table[i] == "P":
    for j in range(i-k, i+k+1):
      if 0 <= j < n and table[j] == "H":
        cnt += 1
        table[j] = "E"
        break
  

print(cnt)