n = int(input()) # 사진 틀 개수
tot_recom = int(input())
recom = list(map(int, input().split()))
pic = {}
order = []
for i in range(len(recom)):
  if recom[i] in pic:
    pic[recom[i]] += 1
  else:
    if len(pic) < n:
      pic[recom[i]] = 1
      order.append(recom[i])
    else:
      min_key = min(order, key=lambda x: (pic[x], order.index(x)))
      del pic[min_key]
      order.remove(min_key)
      
      pic[recom[i]] = 1
      order.append(recom[i])

print(" ".join(map(str, sorted(pic.keys()))))