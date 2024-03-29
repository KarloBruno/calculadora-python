import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.screen = tk.Entry(master, width=30, font=('Arial', 16))
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Botões numéricos
        self.create_button(7, 1, 1)
        self.create_button(8, 1, 2)
        self.create_button(9, 1, 3)
        self.create_button(4, 2, 1)
        self.create_button(5, 2, 2)
        self.create_button(6, 2, 3)
        self.create_button(1, 3, 1)
        self.create_button(2, 3, 2)
        self.create_button(3, 3, 3)
        self.create_button(0, 4, 2)

        # Botões de operação
        self.create_button('+', 1, 4)
        self.create_button('-', 2, 4)
        self.create_button('*', 3, 4)
        self.create_button('/', 4, 4)

        # Botão de resultado
        self.create_button('=', 4, 3)

        # Botão de limpar
        self.create_button('C', 4, 1)

        self.equation = ""

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, font=('Arial', 16), command=lambda: self.button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)

    def button_click(self, text):
        if text == 'C':
            self.equation = ""
            self.screen.delete(0, tk.END)
        elif text == '=':
            try:
                self.equation = str(eval(self.equation))
                self.screen.delete(0, tk.END)
                self.screen.insert(0, self.equation)
            except:
                self.screen.delete(0, tk.END)
                self.screen.insert(0, "Erro!")
        else:
            self.equation += str(text)
            self.screen.insert(tk.END, text)

root = tk.Tk()
my_calculator = Calculator(root)
root.mainloop()#   c a l c u l a d o r a - p y t h o n  
 