# Import tkinter and objects. 
from tkinter import *
import time

# Create a GUI for the word at the top, a timer, and a submission box. 
class Application(Frame):
    def __init__(self, master, wordList, call_on_next):
        super(Application, self).__init__(master)
        self.grid()

        self.points = 0
        self.count = 60
        self.call_on_selected = call_on_next
        self.wordList = wordList


        self.create_widgets()
    
    def create_widgets(self):
        Label(self, text = "").grid(row=1, column = 0)
        Label(self, text = "").grid(row = 2, column = 0)
        Label(self, text = "").grid(row = 3, column = 0)
        Label(self, text = "").grid(row = 4, column = 0)

        # self.ready = Label(self, text = "READY...")
        # self.ready.grid(row = 2, column = 2)
        # time.sleep(2)
        # self.ready.destroy()
        # self.set = Label(self, text = "SET...")
        # self.set.grid(row = 2, column = 2)
        # time.sleep(2)
        # self.set.destroy()
        # self.go = Label(self, text = "GO...")
        # self.go.grid(row = 2, column = 2)
        # time.sleep(2)
        # self.go.destroy()
        self.answer = Entry()
        self.answer.grid(row = 5, column = 2)
        self.showPoints = Label(self, text = "Points: " + str(self.points))
        self.showPoints.grid(row = 0, column = 5)
        while self.count > 0:
            for i in self.wordList:
                self.word = Label(self, text=i)
                self.word.grid(row=0, column=1)
            if self.word == self.answer.get():
                self.points += 1
            time.sleep(3)
            self.count -= 1

    def runGame(self):

        self.call_on_selected()