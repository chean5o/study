H, W = map(int, input().split())
N = int(input())
sticker = [list(map(int, input().split())) for i in range(N)]
max_area = 0
for i in range(N):
  for j in range(i+1, N):
    r1, c1 = sticker[i]
    r2, c2 = sticker[j]

    # 첫 번째 스티커의 방향 그대로, 두 번째 스티커의 방향 그대로
    if (r1 + r2 <= H and max(c1, c2) <= W) or (c1 + c2 <= W and max(r1, r2) <= H):
        max_area = max(max_area, r1 * c1 + r2 * c2)
    
    # 첫 번째 스티커의 방향 그대로, 두 번째 스티커를 90도 회전
    if (r1 + c2 <= H and max(c1, r2) <= W) or (c1 + r2 <= W and max(r1, c2) <= H):
        max_area = max(max_area, r1 * c1 + r2 * c2)
    
    # 첫 번째 스티커를 90도 회전, 두 번째 스티커의 방향 그대로
    if (c1 + r2 <= H and max(r1, c2) <= W) or (r1 + c2 <= W and max(c1, r2) <= H):
        max_area = max(max_area, r1 * c1 + r2 * c2)
    
    # 첫 번째 스티커를 90도 회전, 두 번째 스티커를 90도 회전
    if (c1 + c2 <= H and max(r1, r2) <= W) or (r1 + r2 <= W and max(c1, c2) <= H):
        max_area = max(max_area, r1 * c1 + r2 * c2)

print(max_area)