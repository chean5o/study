def solution(polynomial):
    answer = ''
    tmp = []
    tmp_x = 0
    tmp_s = 0
    tmp = polynomial.split()
    for i in range(0, len(tmp), 2):
        if 'x' in tmp[i]:
            if tmp[i] == 'x':
                tmp_x += 1
            else:
                tmp_x += int(tmp[i].replace('x', ''))
        else:
            tmp_s += int(tmp[i])
            
    if tmp_s != 0 and tmp_x != 0:
        if tmp_x == 1:
            answer = ('x' + ' + ' + str(tmp_s))
        else:
            answer = (str(tmp_x) + 'x' + ' + ' + str(tmp_s))
    elif tmp_x == 0:
        answer = str(tmp_s)
    else:
        if tmp_x == 1:
            answer = 'x'
        else:
            answer = (str(tmp_x) + 'x')
        
    return answer