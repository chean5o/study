def solution(numbers):
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
    for i, nums in enumerate(num):
        numbers = numbers.replace(nums, str(i))
    return int(numbers)