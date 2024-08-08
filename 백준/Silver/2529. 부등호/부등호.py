k = int(input())
sign = input().split()

res = []

def dfs(num_list, idx):
    if len(num_list) == k + 1:  # k+1 자리 숫자가 완성되었을 때
        res.append(''.join(map(str, num_list)))  # 리스트를 문자열로 변환해 결과에 추가
        return
    
    for i in range(10):
        if i in num_list:  # 이미 사용된 숫자는 건너뜀
            continue
        
        if idx == 0 or (sign[idx-1] == "<" and num_list[idx-1] < i) or (sign[idx-1] == ">" and num_list[idx-1] > i):
            dfs(num_list + [i], idx + 1)  # 숫자를 추가하고 다음 단계로 이동

dfs([], 0)  # 초기 num_list는 빈 리스트로 시작
print(max(res))
print(min(res))