def solution(my_string):
    answer = ''
    for i in my_string:
        if i == "e" or i == "a" or i == "i" or i == "o" or i == "u":
            my_string = my_string.replace(i, "")
    return my_string