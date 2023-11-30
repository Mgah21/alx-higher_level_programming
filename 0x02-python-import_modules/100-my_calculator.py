#!/usr/bin/python3

if __name__ == "__main__":

    """Handle basic arithmetic operations."""

    from calculator_1 import add, sub, mul, div  
    import sys   

    if len(sys.argv) - 1 != 3:  # Check if the number 
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

        valid_operators = "+-*/"
        operator = sys.argv[2]
        if operator not in valid_operators:
            print("Unknown operator. Available operators:", valid_operators)
            sys.exit(1)

            a = int(sys.argv[1])
            b = int(sys.argv[3])

            operations = {"+": add, "-": sub, "*": mul, "/": div}
            result = operations[operator](a, b)
            print("{} {} {} = {}".format(a, operator, b, result))
