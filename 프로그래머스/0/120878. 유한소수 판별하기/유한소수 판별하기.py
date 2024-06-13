from fractions import Fraction

def solution(a, b):
    answer = Fraction(a, b)
    print(answer)
    res = 0
    mo = answer.denominator
    tmp = []
    i = 2
    if mo == 1:
        res = 1
    else:
        while i <= mo:
            if mo % i == 0:
                tmp.append(i)
                mo = mo / i
                print(tmp)
            else:
                i += 1
                print("else:", tmp)
        tmp_2 = set(tmp)
        print("set tmp: ", tmp_2)
        if len(tmp_2) < 3 and 2 in tmp_2 and 5 in tmp_2:
            res = 1
        elif len(tmp_2) < 2 and 2 in tmp_2:
            res = 1
        elif len(tmp_2) < 2 and 5 in tmp_2:
            res = 1
        else:
            res = 2
        print(res)
    return res

# 반례 : 3500, 500
# 기대값 : 1
# 리턴값 : 2