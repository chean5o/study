def calc_dis(dir, dis):
  if dir == 1:
    return dis
  elif dir == 2:
    return w + h + w - dis
  elif dir == 3:
    return w + h + w + h - dis
  else:
    return w + dis

w, h = map(int, input().split())
n = int(input())
store_pos = []

for _ in range(n):
  store_pos.append(list(map(int, input().split())))

guard_dir, guard_dis = map(int, input().split())

tot = 0
guard_pos = calc_dis(guard_dir, guard_dis)

for store_dir, store_dis in store_pos:
  n_store_pos = calc_dis(store_dir, store_dis)

  dir_dis = abs(guard_pos - n_store_pos)
  opp_dis = 2 * (w + h) - dir_dis

  tot += min(dir_dis, opp_dis)

print(tot)