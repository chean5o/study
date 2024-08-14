n = int(input())
n_list = list(map(int, input().split()))
m = int(input())

def binary_search(arr, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        tot = 0
        
        for i in arr:
            tot += min(i, mid)
        
        if tot <= m:
            result = mid  # 현재 mid 값이 가능한 상한액이 될 수 있음
            start = mid + 1
        else:
            end = mid - 1
    
    return result

if sum(n_list) <= m:
    res = max(n_list)
else:
    res = binary_search(n_list, 0, max(n_list))

print(res)