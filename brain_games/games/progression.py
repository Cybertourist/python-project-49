import random

TASK = "What number is missing in the progression?"


def generate_progression(start, step, length):
    return [start + i * step for i in range(length)]


def generate_round():
    length = random.randint(5, 10) # NOSONAR
    start = random.randint(1, 20) # NOSONAR
    step = random.randint(2, 10) # NOSONAR

    progression = generate_progression(start, step, length)

    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])

    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))

    return question, correct_answer
