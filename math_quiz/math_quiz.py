import random


def function_int(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def choice():
    return random.choice(['+', '-', '*'])


def question(n1, n2, o):
    p = f"{n1} {o} {n2}"
    if o == '+':
        a = n1 + n2
    elif o == '-':
        a = n1 - n2
    else:
        a = n1 * n2
    return p, a


def math_quiznew():
    s = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(int(t_q)):
        n1 = function_int(1, 10)
        n2 = function_int(1, 5)
        o = choice()

        PROBLEM, ANSWER = question(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")

        try:
            useranswer = int(input("Your answer: "))
            if o == '/' and useranswer == 0:
                raise ValueError("Cannot divide by zero.")
        except ValueError as ve:
            print(f"Invalid input: {ve}")
            useranswer = 0  # Assigning a default value for an invalid input

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{int(t_q)}")


if __name__ == "__main__":
    math_quiznew()
