from datetime import datetime
from config import DATE_FORMAT


def get_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")


def get_optional_text(prompt):
    return input(prompt).strip()


def get_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt).strip())

            if number >= 0:
                return number

            print("Enter zero or a positive number.")

        except ValueError:
            print("Enter a valid whole number.")


def get_date(prompt):
    while True:
        value = input(prompt).strip()

        try:
            parsed = datetime.strptime(value, DATE_FORMAT)

            if parsed.strftime(DATE_FORMAT) != value:
                raise ValueError

            return value

        except ValueError:
            print("Enter a valid date in YYYY-MM-DD format.")


def get_optional_date(prompt):
    while True:
        value = input(prompt).strip()

        if not value:
            return None

        try:
            parsed = datetime.strptime(value, DATE_FORMAT)

            if parsed.strftime(DATE_FORMAT) != value:
                raise ValueError

            return value

        except ValueError:
            print("Enter a valid date or leave it blank.")


def get_choice(prompt, options):
    print("\nAvailable options:")

    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    while True:
        value = input(prompt).strip()

        if value.isdigit():
            number = int(value)

            if 1 <= number <= len(options):
                return options[number - 1]

        print(f"Choose a number between 1 and {len(options)}.")


def current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def pause():
    input("\nPress Enter to continue...")
