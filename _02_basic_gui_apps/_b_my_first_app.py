"""
My first Python app using Tkinter
"""
import tkinter as tk
from PIL import Image, ImageTk


def create_image(filename, width, height):
    image_obj = None

    try:
        image = Image.open(filename)
        image = image.resize((width, height), Image.ANTIALIAS)
        image_obj = ImageTk.PhotoImage(image=image)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)

    return image_obj

# ======================= DO NOT EDIT THE CODE ABOVE =========================

# TODO 1) Make a new class and put tk.Tk in the parenthesis, for example:
#  FirstApp(tk.TK):
class MyApp(tk.Tk):
    # TODO 2) Make a constructor
    def __init__(self):

        # TODO 3) Call the Tk class's constructor
        #  super().__init__()
        super(MyApp, self).__init__()
        # TODO 4) Add a text label and pick a text message to display
        self.label = tk.Label(self, text="Carrots")
        # TODO 5) Place the label somewhere on your app. You can use either
        #  x and y or relx and rely
        self.label.place(x=130, y=50)
        # TODO 6) Create a member variable for the image using the
        #  create_image function. You can use the image provided in this
        #  folder or another image from the internet
        self.img = create_image("carrots.jpg", 150, 150)
        # TODO 7) Create another label and attach to it the image object
        #  from the previous step
        self.label_two = tk.Label(self, image=self.img)

        # TODO 8) Place the label somewhere on your app
        self.label_two.place(x=80, y=80)

# TODO 9) Create an if __name__ == '__main__': block
if __name__ == "__main__":
    # TODO 10) Create an object of your app class
    myApp = MyApp()
    # TODO 11) Use the app object to set a title
    myApp.title("My App")
    # TODO 12) Use the app object to set the window dimensions (width x height)
    myApp.geometry("300x300")
    # TODO 13) Run the app object's mainloop() method
    myApp.mainloop()

