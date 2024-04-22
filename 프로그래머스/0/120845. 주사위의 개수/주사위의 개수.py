def solution(box, n):
    answer = 0
    box_l = 0
    box_w = 0
    box_h = 0
    box_l = box[0] // n
    box_w = box[1] // n
    box_h = box[2] // n
    
    answer = box_l * box_w * box_h
    return answer