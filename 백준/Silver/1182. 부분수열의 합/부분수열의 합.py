N, S = map(int, input().split())
num_list = list(map(int, input().split()))
count = 0

def subsequences(index, current_sum):
    global count
   
    if index == N:
        return
    
    current_sum += num_list[index]
     
    if current_sum == S:
        count += 1
    
    subsequences(index + 1, current_sum - num_list[index])
    subsequences(index + 1, current_sum)

subsequences(0, 0)

print(count)