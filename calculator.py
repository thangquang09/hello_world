"""Simple calculator: +, -, *, /."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


OPS = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculate(a, op, b):
    if op not in OPS:
        raise ValueError(f"unknown operator: {op}")
    return OPS[op](a, b)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument("a", type=float)
    parser.add_argument("op", choices=OPS.keys())
    parser.add_argument("b", type=float)
    args = parser.parse_args()
    print(calculate(args.a, args.op, args.b))


if __name__ == "__main__":
    main()
