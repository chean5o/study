burger = []
side = []

for i in range(3):
  burger.append(int(input()))
for i in range(2):
  side.append(int(input()))
print(min(burger) + min(side)- 50)