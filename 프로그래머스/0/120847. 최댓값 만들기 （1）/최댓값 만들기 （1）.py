def solution(numbers):
    m1 = 0
    m2 = 0
    m1 = max(numbers)
    numbers.remove(m1)
    m2 = max(numbers)
    
    return m1 * m2