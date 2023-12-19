import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Create and set up widgets
        self.label_intro = tk.Label(root, text="Password Generator", font=("Helvetica", 16), pady=10)
        self.label_intro.pack()

        self.label_length = tk.Label(root, text="Enter password length:")
        self.label_length.pack()

        self.entry_length = tk.Entry(root)
        self.entry_length.pack(pady=10)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.result_label = tk.Label(root, text="", font=("Helvetica", 14), pady=10)
        self.result_label.pack()

    def generate_password(self):
        try:
            length = int(self.entry_length.get())
            if length <= 0:
                messagebox.showwarning("Invalid Input", "Please enter a valid password length.")
                return

            password = self._generate_random_password(length)
            self.result_label.config(text=f"Generated Password: {password}")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number for password length.")

    def _generate_random_password(self, length):
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

if __name__ == "__main__":
    root = tk.Tk()
    password_generator = PasswordGenerator(root)
    root.mainloop()
