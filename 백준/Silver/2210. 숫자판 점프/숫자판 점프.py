num_plate = [list(map(int, input().split())) for _ in range(5)]
res = [] #나올 수 있는 모든 경우의 수 저장
def dfs(r, c, num):
  row = [-1, 1, 0, 0] # 상 하 좌 우
  col = [0, 0, -1, 1]
  
  num += str(num_plate[r][c])

  if len(num) == 6:
    res.append(num)
    #print(num)
    return

  for i in range(4):
    current_r = r + row[i]
    current_c = c + col[i]
    
    if 0 <= current_r < 5 and 0 <= current_c < 5:
        dfs(current_r, current_c, num)

for i in range(0, 5):
  for j in range(0, 5):
    dfs(i, j, "")

# print(set(res))
print(len(set(res)))