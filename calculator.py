from tkinter import *

class Calculator(Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.geometry('440x425')
        self.resizable(0, 0)
        self.result = Entry(self, font=("Arial", 23), justify=LEFT)
        self.result.grid(row=0, column=0, columnspan=4, ipadx=40, ipady=20, padx=10, pady=10, sticky=W+E)
        self.button_frame = Frame(self)
        self.button_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
        self.create_button('1', self.button_frame, 0, 0, lambda: self.add_number(1))
        self.create_button('2', self.button_frame, 0, 1, lambda: self.add_number(2))
        self.create_button('3', self.button_frame, 0, 2, lambda: self.add_number(3))
        self.create_button('4', self.button_frame, 1, 0, lambda: self.add_number(4))
        self.create_button('5', self.button_frame, 1, 1, lambda: self.add_number(5))
        self.create_button('6', self.button_frame, 1, 2, lambda: self.add_number(6))
        self.create_button('7', self.button_frame, 2, 0, lambda: self.add_number(7))
        self.create_button('8', self.button_frame, 2, 1, lambda: self.add_number(8))
        self.create_button('9', self.button_frame, 2, 2, lambda: self.add_number(9))
        self.create_button('+', self.button_frame, 0, 3, lambda: self.add_operation("+"))
        self.create_button('-', self.button_frame, 1, 3, lambda: self.add_operation("-"))
        self.create_button('*', self.button_frame, 2, 3, lambda: self.add_operation("*"))
        self.create_button('/', self.button_frame, 3, 3, lambda: self.add_operation("/"))
        self.create_button('0', self.button_frame, 3, 0, lambda: self.add_number(0))
        self.create_button('C', self.button_frame, 3, 1, lambda: self.clear())
        self.create_button('=', self.button_frame, 3, 2, lambda: self.calculate())
    def create_button(self, text, frame, row, column, command=None, bg="white"):
        button = Button(frame, text=text, width=8, height=3, command=command, bg=bg)
        button.grid(row=row, column=column, padx=20, pady=10)
    def add_number(self, number):
        current = self.result.get()
        current += str(number)
        self.result.delete(0, END)
        self.result.insert(END, current)
    def add_operation(self, operator):
        current = self.result.get()
        current += operator
        self.result.delete(0, END)
        self.result.insert(END, current)
    def clear(self):
        self.result.delete(0, END)
    def calculate(self):
        try:
            current = self.result.get()
            self.result.delete(0, END)
            self.result.insert(END, eval(current))
        except:
            self.result.insert(END, 'Error!')

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()