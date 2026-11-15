import sys


def validate_number(user_input_str: str) -> float | None:
    if user_input_str == "/q":
        print("Goodbye!")
        sys.exit()

    try:
        return float(user_input_str)
    except ValueError:
        print("Please enter a number\n")


def validate_integer(user_input_str: str) -> int | None:
    if user_input_str == "/q":
        print("Goodbye!")
        sys.exit()

    try:
        return int(user_input_str)
    except ValueError:
        print("Please enter a number\n")
