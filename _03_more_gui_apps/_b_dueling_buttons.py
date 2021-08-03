"""
Press one button and the other button changes its size!
"""
import tkinter as tk

LEFT_BIG = {'relwidth' : 0.8}
LEFT_SMALL = {'relwidth' : 0.2}
RIGHT_BIG = {'relx' : 0.2, 'relwidth' : 0.8}
RIGHT_SMALL = {'relx' : 0.8, 'relwidth' : 0.2}

# ======================= DO NOT EDIT THE CODE ABOVE =========================

# TODO 1) Create a new tkinter class
class DuelingButtons(tk.Tk):

    # TODO 2) Create a constructor
    def __init__(self):
    # TODO 3) call Tk's constructor,
        super().__init__()

    # TODO 4) Create 2 buttons next to each other, side by side, with the
    #  text "Click me!". Make sure the buttons are member variables and
    #  look at the example photo for reference.
        self.button_one = tk.Button(self, text="Click me!", fg='blue',
                                    font=('times new roman', 13, 'bold'), command=self.button_one_pressed)

        self.button_one.place(relx=0, rely=0, relwidth=0.5, relheight=1)

        self.button_two = tk.Button(self, text="Click me!", fg='blue',
                                font=('times new roman', 13, 'bold'), command=self.button_two_pressed)

        self.button_two.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)
    # TODO 5) For the left button, add: command=self.left_button_pressed
    #  For the right button, add: command=self.right_button_pressed

    # TODO 6) Create a method called left_button_pressed that places the left
    #  button to small and the right button to big. For example,
    #  self.button_left.place(LEFT_SMALL)
    #  self.button_right.place(RIGHT_BIG)
    def button_one_pressed(self):
        self.button_one.place(LEFT_SMALL)
        self.button_two.place(RIGHT_BIG)

    # TODO 7) Create a method called right_button_pressed and place the left
    #  button to big and the right button to small
    def button_two_pressed(self):
        self.button_one.place(LEFT_BIG)
        self.button_two.place(RIGHT_SMALL)

# TODO 8) Create an if __name__ == '__main__': block
if __name__ == '__main__':
    # TODO 9) Create an object of the dueling buttons class
    duel = DuelingButtons()
    # TODO 10) Set the object's width and size using the geometry method
    duel.geometry("500x300")
    # TODO 11) Call the object's mainloop method
    duel.mainloop()
