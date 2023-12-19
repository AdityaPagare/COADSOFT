import random
import string

def generate_password(length):
    # Define character sets for password complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets based on user input
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the length is at least 8 characters
    length = max(8, length)

    # Generate a password using random.choices
    password = ''.join(random.choices(all_characters, k=length))
    return password

def main():
    try:
        # Prompt the user for the desired password length
        password_length = int(input("Enter the desired length for the password: "))

        # Generate and display the password
        generated_password = generate_password(password_length)
        print("Generated Password:", generated_password)

    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
