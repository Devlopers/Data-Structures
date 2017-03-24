import sys

def factorial(in_int):
    factorial = 1
    while in_int > 0:
        factorial = factorial * in_int
        in_int = in_int - 1
    print(factorial)
    return factorial

if __name__ == "__main__":
    factorial(int(sys.argv[1]))
