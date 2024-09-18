from itertools import permutations

def calculate_score(guess, answer):
    guess, answer = str(guess), str(answer)
    strike = sum(g == a for g, a in zip(guess, answer))
    ball = len(set(guess) & set(answer)) - strike
    return strike, ball

n = int(input())
questions = [tuple(map(int, input().split())) for _ in range(n)]

possible_answers = [''.join(map(str, p)) for p in permutations(range(1, 10), 3)]

valid_answers = [
    answer for answer in possible_answers
    if all(calculate_score(question, answer) == (strike, ball) for question, strike, ball in questions)
]
print(len(valid_answers))