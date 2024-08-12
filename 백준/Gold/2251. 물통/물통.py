a, b, c = map(int, input().split())
visited = []
bottle_c = set()
for _ in range(a + 1):
    visited.append([0] * (b + 1))

def dfs(n_a, n_b):
  if visited[n_a][n_b] == 0:
    visited[n_a][n_b] = 1
    n_c = c - n_a - n_b # 현재 세번째 물통에 남아있는 물의 양
    if n_a == 0:
      bottle_c.add(n_c)

    # a -> b
    if n_a + n_b < b : # 첫번째 + 두번째 물통의 물의 양 < 두번째 물통의 최대 용량
      dfs(0, n_a + n_b)
    else: # 첫번째 + 두번째 물통의 물의 양 > 두번째 물통의 최대 용량
      dfs(n_a + n_b - b, b)
    
    # a -> c
    if n_a + n_c <= c:
        dfs(0, n_b)
    else:
        dfs(n_a + n_c - c, n_b)

    # b -> a
    if n_b + n_a <= a:
        dfs(n_b + n_a, 0)
    else:
        dfs(a, n_b + n_a - a)

    # b -> c
    if n_b + n_c <= c:
        dfs(n_a, 0)
    else:
        dfs(n_a, n_b + n_c - c)

    # c -> a
    if n_c + n_a <= a:
        dfs(n_c + n_a, n_b)
    else:
        dfs(a, n_b)

    # c -> a
    if n_c + n_b <= b:
        dfs(n_a, n_c + n_b)
    else:
        dfs(n_a, b)

dfs(0,0) # 초기 값 첫번째와 두번째 물통에는 물이 없는 상태

res = sorted(bottle_c)

for i in res:
    print(i, end=" ")