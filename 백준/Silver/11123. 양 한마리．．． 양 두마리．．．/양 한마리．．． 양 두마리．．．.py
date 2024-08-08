import sys
sys.setrecursionlimit(100000)
t = int(input())
res = []
def dfs(r, c):
    row = [-1, 1, 0, 0] # 상 하 좌 우
    col = [0, 0, -1, 1]
    sheep[r][c] = "." # 돌았던 부분은 풀로 바꿔주기

    for i in range(4):
        n_r = r + row[i]
        n_c = c + col[i]

        if 0 <= n_r < h and 0 <= n_c < s:
            if sheep[n_r][n_c] == "#": # 상 하 좌 우에 양이 또 있을경우 재귀사용
                dfs(n_r, n_c)
            
for _ in range(t):
    cnt = 0
    h, s = map(int, input().split())
    sheep = [list(input()) for _ in range(h)]
    for i in range(h):
        for j in range(s):
            if sheep[i][j] == "#":
                dfs(i, j)
                cnt +=1 # 양의 무리가 발견 될 때마다 +1
    res.append(cnt)
for x in range(t):
    print(res[x])