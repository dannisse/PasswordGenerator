# imports:
# random - this module is used to generate random values
# string - provides different string constants to generate passwords

import random
import string


# generate_password: this takes an optional argument (length), which determines the length of the password. if no
# length is determined, it defaults to "8". but you can change this defines lower and upper case letters, digits,
# and symbols using "string.ascii_lowercase", "string.ascii_uppercase", "string.digits", and "string_puncuation"
# combines all the char sets into "all_chars" generates a random password of specified length by choosing random
# characters from "all_chars" and joins them together finally, returns generated password
def generate_password(length=8):
    """Generate a random password."""
    # Define the character sets for different types of characters
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_chars = lower_case + upper_case + digits + symbols

    # Generate a password with random characters
    password = ''.join(random.choice(all_chars) for _ in range(length))

    print("Generated Password:", password)  # Print the generated password
    return password


def main():
    """Main function to generate a password and display it."""
    # Ask the user for the desired length of the password
    length = int(input("Enter the length of the password: "))

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print("Generated Password:", password)


if __name__ == "__main__":
    main()
