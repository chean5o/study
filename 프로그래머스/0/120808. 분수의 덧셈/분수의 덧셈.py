import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom = 0
    numer = 0
    denom = denom1 * denom2
    numer = numer1 * denom2 + numer2 * denom1
    answer= [numer/math.gcd(numer, denom), denom/math.gcd(numer, denom)]
    return answer