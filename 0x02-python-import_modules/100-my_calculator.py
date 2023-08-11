def main():
    """Handle basic arithmetic operations."""
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}

    try:
        a = int(argv[1])
        b = int(argv[3])
    except ValueError as e:
        print(e)
        sys.exit(1)

    print("{} {} {} = {}".format(a, argv[2], b, ops[argv[2]](a, b)))

if __name__ == "__main__":
    main()
