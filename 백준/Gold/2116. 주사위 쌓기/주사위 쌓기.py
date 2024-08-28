n = int(input())
dice_list = [list(map(int, input().split())) for _ in range(n)]
dice_pair = [5,3,4,1,2,0]
res = 0

for i in range(6):
  tot = 0
  top = i
  bottom = dice_pair[top]

  for j in range(n):
    side_max = 0
    for k in range(6):
      if k != top and k != bottom:
        side_max = max(side_max, dice_list[j][k])
    
    tot += side_max

    if j < n - 1:
      next_dice = dice_list[j][top]
      bottom = dice_list[j+1].index(next_dice)
      top = dice_pair[bottom]
    
    res = max(res, tot)

print(res)