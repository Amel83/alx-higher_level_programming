#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys

    length = len(sys.argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit (1)
    a = int(sys.argv([1]
    opr = sys.argv[2]
    b = int(sys.argv[3])

    if opr == '+':
        print("{} {} {} = {}".format(a, b, add(a, b)))
    elif "a - b":
        print("{}-{} = {}".format(a, b,sub(a, b)))
    elif "a * b":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif a /b:
        print("{} / {} = {}".format(a, b, div(a, b)))
    else
        print("Unknown operator. Available operators: +, -, * and /")
        exit 1
