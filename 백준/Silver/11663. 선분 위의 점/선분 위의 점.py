n, m = map(int, input().split())
dot = list(map(int, input().split()))
dot.sort()
res = []


def dot_min(a):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2

        if dot[mid] < a:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1


def dot_max(b):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2

        if b < dot[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return end


for i in range(m):
    a, b = map(int, input().split())
    res.append(dot_max(b) - dot_min(a) + 1)

for i in range(m):
    print(res[i])