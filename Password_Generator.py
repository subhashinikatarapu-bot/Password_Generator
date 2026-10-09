import random
import string


def generate_password(length, use_digits, use_symbols):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


print("=" * 45)
print("        PASSWORD GENERATOR")
print("=" * 45)

while True:

    try:
        length = int(input("\nEnter password length: "))

        if length < 4:
            print("Password length should be at least 4.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")


print("\nChoose password options:")

digits_choice = input("Include numbers? (y/n): ").lower()
symbols_choice = input("Include special characters? (y/n): ").lower()

use_digits = digits_choice == "y"
use_symbols = symbols_choice == "y"

password = generate_password(
    length,
    use_digits,
    use_symbols
)

print("\n" + "=" * 45)
print("Generated Password:", password)
print("=" * 45)

print("\nPassword generated successfully!")