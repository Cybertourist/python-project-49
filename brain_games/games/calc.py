import random
import operator

TASK = "What is the result of the expression?"

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def generate_round():
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)
    op_symbol = random.choice(list(operations.keys()))
    op_func = operations[op_symbol]

    question = f"{number1} {op_symbol} {number2}"
    correct_answer = str(op_func(number1, number2))
    return question, correct_answer
