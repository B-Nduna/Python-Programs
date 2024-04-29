import tkinter as tk
from math import sin, cos, tan, sqrt, pi, log10, log, exp


class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Scientific Calculator")

        self.entry_var = tk.StringVar()
        self.entry_var.set("")

        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display input/output
        entry = tk.Entry(self.master, textvariable=self.entry_var, font=('Arial', 14), bd=5, relief=tk.SUNKEN, justify=tk.RIGHT)
        entry.pack(fill=tk.X)

        # Frame for buttons
        button_frame = tk.Frame(self.master)
        button_frame.pack()

        # Buttons for functions
        func_buttons = [
            ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('sqrt', 1, 3),
            ('log', 2, 0), ('log10', 2, 1), ('exp', 2, 2), ('pi', 2, 3),
            ('(', 3, 0), (')', 3, 1), ('C', 3, 2), ('<-', 3, 3),
        ]

        for (text, row, col) in func_buttons:
            btn = tk.Button(button_frame, text=text, font=('Arial', 14), padx=10, pady=10, command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, sticky='nsew')

        # Buttons for numbers
        num_buttons = [
            ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('/', 4, 3),
            ('4', 5, 0), ('5', 5, 1), ('6', 5, 2), ('*', 5, 3),
            ('1', 6, 0), ('2', 6, 1), ('3', 6, 2), ('-', 6, 3),
            ('0', 7, 0), ('.', 7, 1), ('=', 7, 2), ('+', 7, 3),
        ]

        for (text, row, col) in num_buttons:
            btn = tk.Button(button_frame, text=text, font=('Arial', 14), padx=10, pady=10, command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, sticky='nsew')

    def on_button_click(self, text):
        if text == '=':
            try:
                result = eval(self.entry_var.get())
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set("Error")
        elif text == 'C':
            self.entry_var.set('')
        elif text == '<-':
            current_value = self.entry_var.get()
            self.entry_var.set(current_value[:-1])
        elif text == 'sin':
            self.entry_var.set(sin(float(self.entry_var.get())))
        elif text == 'cos':
            self.entry_var.set(cos(float(self.entry_var.get())))
        elif text == 'tan':
            self.entry_var.set(tan(float(self.entry_var.get())))
        elif text == 'sqrt':
            self.entry_var.set(sqrt(float(self.entry_var.get())))
        elif text == 'log':
            self.entry_var.set(log(float(self.entry_var.get())))
        elif text == 'log10':
            self.entry_var.set(log10(float(self.entry_var.get())))
        elif text == 'exp':
            self.entry_var.set(exp(float(self.entry_var.get())))
        elif text == 'pi':
            self.entry_var.set(pi)
        else:
            self.entry_var.set(self.entry_var.get() + text)


def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
