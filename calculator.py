import sys
from __init__ import add, subtract, multiply, divide, add_then_multiply, multiply_then_subtract

def get_args():
    try:
        return (sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

    except IndexError:
        print("Not all arguments have been provided!")
        print("USAGE: [operation] [start_number] [operation_number]")
        raise
    except :
        print("Unknown error! See the details and usage reminder below")
        print("USAGE: [operation] [start_number] [operation_number]")
        raise


def main():
    operation, start_number, operation_number = get_args()
    print(operation)
    print(start_number)
    print(operation_number)

    if operation == 'add':
        result = add(start_number, operation_number)
    elif operation == 'subtract':
        result = subtract(start_number, operation_number)
    elif operation == 'multiply':
        result = multiply(start_number, operation_number)
    elif operation == 'divide':
        result = divide(start_number, operation_number)
    elif operation == "add_then_multiply":
        result = add_then_multiply(start_number, operation_number)
    elif operation == "multiply_then_subtract":
        result = multiply_then_subtract(start_number, operation_number)
        calc_output = "*-"
    print(result, calc_output)
    return 0


if __name__ == '__main__':
    sys.exit(main())



# Take 3 positional arguments from command line
# Must support (add, subtract, multiply, divide)
# Numerical arguments must be whole numbers or integers
# Result must be printed out on command line
# Basic error handling must be used for the arguments
# Custom module for calculator operations
