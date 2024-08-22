n = int(input())
tree_h = list(map(int, input().split()))
grow = list(map(int, input().split()))
res = 0
tot_tree = list(zip(grow, tree_h))
tot_tree.sort()

for i in range(n):
  growth_rate, initial_height = tot_tree[i]
    
  wood_length = initial_height + (i * growth_rate)
  res += wood_length

print(res)