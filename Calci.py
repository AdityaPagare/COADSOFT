import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("300x400")

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display the result
        entry = tk.Entry(self, textvariable=self.result_var, font=("Helvetica", 18), bd=10, relief="ridge", justify="right")
        entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, font=("Helvetica", 18), padx=20, pady=20, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

        # Configure row and column weights so that they expand proportionally
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button_text):
        current_text = self.result_var.get()

        if button_text == 'C':
            self.result_var.set('')
        elif button_text == '=':
            try:
                result = str(eval(current_text))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            self.result_var.set(current_text + button_text)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
