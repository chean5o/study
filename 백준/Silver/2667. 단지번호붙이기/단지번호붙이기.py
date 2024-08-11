n = int(input())
house_list = [list(map(int, str(input()))) for _ in range(n)]
cnt = 0
res = []

def dfs(r, c):
    global cnt
    row = [-1, 1, 0, 0] # 상 하 좌 우
    col = [0, 0, -1, 1]
    house_list[r][c] = 0 

    for i in range(4):
        n_r = r + row[i]
        n_c = c + col[i]

        if 0 <= n_r < n and 0 <= n_c < n:
            if house_list[n_r][n_c] == 1: 
                cnt += 1
                dfs(n_r, n_c)
            

for i in range(n):
    for j in range(n):
        if house_list[i][j] == 1:
            cnt = 1
            dfs(i, j)
            res.append(cnt)

res.sort()
print(len(res))
for i in range(len(res)): 
  print(res[i])