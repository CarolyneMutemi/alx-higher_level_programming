#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        sys.stderr.write("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        exit(1)

    operator = {"+": add, "-": sub, "*": mul, "/": div}
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] not in list(operator.keys()):
        sys.stderr.write("Unknown operator. Available operators: +, -, * and /\n")

    print("{} {} {} = {}".format(a, sys.argv[2], b, operator[sys.argv[2]](a, b)))
