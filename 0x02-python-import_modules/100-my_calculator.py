#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys

    length = len(sys.argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    opr = sys.argv[2]
    b = int(sys.argv[3])

    if opr == '+':
        print("{} {} {} = {}".format(a, opr, b, calculator_1.add(a, b)))
    elif opr == '-':
        print("{} {} {} = {}".format(a, opr, b, calculator_1.sub(a, b)))
    elif opr == '*':
        print("{} {} {} = {}".format(a, opr, b, calculator_1.mul(a, b)))
    elif opr == '/':
        print("{} {} {} = {}".format(a, opr, b, calculator_1.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
