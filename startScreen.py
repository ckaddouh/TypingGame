from tkinter import *


class Startscreen(Frame):
    def __init__(self, master, call_on_next):
        super(Startscreen, self).__init__(master)

        self.call_on_selcted = call_on_next

        self.grid()

        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Speed Typing Game", font="Helvetica 20 bold").grid(row=0, column=0, sticky=N)
        Label(self).grid(row=1, column=0)
        Label(self,
              text="Type as fast as you can!").grid(
            row=2, column=0, sticky=N)
        Label(self).grid(row=3, column=0)
        Label(self, text="Username:").grid(row=4, column=0, sticky=N)
        self.username = Entry(self)
        self.username.grid(row=5, column=0)
        start_button = Button(self, text="START GAME", font="Courier 16 bold")
        start_button.grid(row=6, column=0, sticky=N)
    def continue_clicked(self):
        self.call_on_selcted()

    

