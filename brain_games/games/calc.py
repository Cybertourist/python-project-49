import random
import operator

TASK = "What is the result of the expression?"

operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}


def generate_round():
    number1 = random.randint(1, 20)  # NOSONAR
    number2 = random.randint(1, 20)  # NOSONAR
    op_symbol = random.choice(list(operations.keys()))  # NOSONAR
    op_func = operations[op_symbol]

    question = f"{number1} {op_symbol} {number2}"
    correct_answer = str(op_func(number1, number2))
    return question, correct_answer
