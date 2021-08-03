"""
Create a simple calculator app
"""
import tkinter as tk

# TODO Make a calculator app like the one shown in the calculator.png image
#  located in this folder.
#  HINT: you'll need: 2 text fields, 4 buttons, and 1 label

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.text_field_one = tk.Entry(self)
        self.text_field_one.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.1)

        self.text_field_two = tk.Entry(self)
        self.text_field_two.place(relx=0.6, rely=0.1, relwidth=0.3, relheight=0.1)


        self.label = tk.Label(self, bg='white', font=('comic sans', 20, 'normal'))
        self.label.place(relx=0, rely=0.3, relwidth=1, relheight=0.1)


        self.button_plus = tk.Button(self, text="Add", fg='green',
                                    font=('times new roman', 13, 'bold'), command=self.add)
        self.button_plus.place(relx=0, rely=0.5, relwidth=0.25, relheight=0.1)

        self.button_minus = tk.Button(self, text="Subtract", fg='red',
                                     font=('times new roman', 13, 'bold'), command=self.subtract)
        self.button_minus.place(relx=0.25, rely=0.5, relwidth=0.25, relheight=0.1)

        self.button_times = tk.Button(self, text="Multiply", fg='green',
                                     font=('times new roman', 13, 'bold'), command=self.multiply)
        self.button_times.place(relx=0.5, rely=0.5, relwidth=0.25, relheight=0.1)

        self.button_divided = tk.Button(self, text="Divide", fg='red',
                                     font=('times new roman', 13, 'bold'), command=self.divide)
        self.button_divided.place(relx=0.75, rely=0.5, relwidth=0.25, relheight=0.1)


    def add(self):
        self.label.configure(text = str(float(self.text_field_one.get()) + float(self.text_field_two.get())))
    def subtract(self):
        self.label.configure(text = str(float(self.text_field_one.get()) - float(self.text_field_two.get())))
    def multiply(self):
        self.label.configure(text = str(float(self.text_field_one.get())*float(self.text_field_two.get())))
    def divide(self):
        self.label.configure(text = str(float(self.text_field_one.get())/float(self.text_field_two.get())))




if __name__ == "__main__":
    calc = Calculator()
    calc.geometry("400x200")
    calc.mainloop()

