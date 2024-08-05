H, W = map(int, input().split())
N = int(input())
sticker = [list(map(int, input().split())) for i in range(N)]


def can_place(r1, c1, r2, c2):
    if (r1 + r2 <= H and max(c1, c2) <= W) or (c1 + c2 <= W and max(r1, r2) <= H):
        return True
    if (r1 + c2 <= H and max(c1, r2) <= W) or (c1 + r2 <= W and max(r1, c2) <= H):
        return True
    return False

max_area = 0

for i in range(N):
    for j in range(i+1, N):
        r1, c1 = sticker[i]
        r2, c2 = sticker[j]
        
        if can_place(r1, c1, r2, c2):
            max_area = max(max_area, r1*c1 + r2*c2)
        if can_place(r1, c1, c2, r2):
            max_area = max(max_area, r1*c1 + r2*c2)
        if can_place(c1, r1, r2, c2):
            max_area = max(max_area, r1*c1 + r2*c2)
        if can_place(c1, r1, c2, r2):
            max_area = max(max_area, r1*c1 + r2*c2)

print(max_area)