a, b, c = map(int, input().split())

visited = [[0 for _ in range(b + 1)] for _ in range(a + 1)]
possible_c = set()  # 세 번째 물통에 담길 수 있는 물의 양 저장

def dfs(n_a, n_b):
    if visited[n_a][n_b] == 0:
        visited[n_a][n_b] = 1
        n_c = c - n_a - n_b  # 현재 세 번째 물통에 남아있는 물의 양
        
        if n_a == 0:  # 첫 번째 물통이 비어있는 경우, 세 번째 물통의 물 양 기록
            possible_c.add(n_c)

        # A -> B
        if n_a + n_b <= b:
            dfs(0, n_a + n_b)
        else:
            dfs(n_a + n_b - b, b)

        # A -> C
        if n_a + n_c <= c:
            dfs(0, n_b)
        else:
            dfs(n_a + n_c - c, n_b)

        # B -> A
        if n_b + n_a <= a:
            dfs(n_b + n_a, 0)
        else:
            dfs(a, n_b + n_a - a)

        # B -> C
        if n_b + n_c <= c:
            dfs(n_a, 0)
        else:
            dfs(n_a, n_b + n_c - c)

        # C -> A
        if n_c + n_a <= a:
            dfs(n_c + n_a, n_b)
        else:
            dfs(a, n_b)

        # C -> B
        if n_c + n_b <= b:
            dfs(n_a, n_c + n_b)
        else:
            dfs(n_a, b)

dfs(0, 0)  # 초기 상태로 DFS 시작

# 가능한 세 번째 물통의 물의 양을 정렬하여 출력
res = sorted(possible_c)
print(*res)