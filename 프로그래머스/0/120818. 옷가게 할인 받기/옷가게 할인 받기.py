def solution(price):
    answer = 0
    if price < 100000:
        answer = price
    elif 100000 <= price < 300000:
        answer = price - (price*0.05)
    elif 300000 <= price < 500000:
        answer = price - (price*0.1)
    else:
        answer = price - (price*0.2)
    return int(answer)