import random

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_round():
    number = random.randint(1, 100)  # NOSONAR
    correct_answer = "yes" if is_even(number) else "no"
    return str(number), correct_answer
