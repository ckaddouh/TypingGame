from tkinter import *


class Application():
    def __init__(self, master, wordListFile, count):
        super(Application, self).__init__(master)
        self.call_on_selected = call_on_next
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        Label(self, text = "GAME OVER").grid(row = 0, column = 2)
        Label(self, text = self.points + " WPM").grid(row = 2, column = 2)
        self.exitbutton = Button(self, text = "Exit", command = self.exit)
        self.exitbutton.grid(row = 3, column = 2, sticky = E)

    def exit(self):
        self.call_on_selected()
