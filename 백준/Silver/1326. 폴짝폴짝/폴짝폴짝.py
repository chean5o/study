from collections import deque
n = int(input())
step = list(map(int, input().split()))
a, b = map(int, input().split())

def bfs():
    queue = deque([a - 1])
    visited = [-1] * 100000
    visited[a - 1] = 0 
    while queue:
        target = queue.popleft()
        
        for i in range(target, n, step[target]):
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[target] + 1

                if i == b - 1:
                    return visited[i]
                    
        for i in range(target, -1, -step[target]):
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[target] + 1
                if i == b - 1:
                    return visited[i]
    return -1

print(bfs())