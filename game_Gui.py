# Import tkinter and objects. 
from tkinter import *
import time

# Create a GUI for the word at the top, a timer, and a submission box. 
class Application():
    def __init__(self, master, wordListFile, call_on_next:
        super(Application, self).__init__(master)
        self.wordList = []
        for line in wordListFile:
            self.wordList.append(line.strip())
        self.wordList.shuffle()
        self.points = 0
        self.count = count
        self.call_on_selected = call_on_next
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        self.ready = Label(self, text = "READY...")
        self.ready.grid(row = 2, column = 2)
        time.sleep(2)
        self.ready.destroy()
        self.set = Label(self, text = "SET...")
        self.set.grid(row = 2, column = 2)
        time.sleep(2)
        self.set.destroy()
        self.go = Label(self, text = "GO...")
        self.go.grid(row = 2, column = 2)
        time.sleep(2)
        self.go.destroy()
        self.answer = Entry()
        self.answer.grid(row = 5, column = 2)
        self.showPoints = Label(self, text = "Points: " + self.points)
        self.showPoints.grid(row = 0, column = 5)

    def runGame(self):
        count = self.count
        while count > 0:
            self.word = Label(self, text= i)
            for x in range(0, 4):
                self.word.grid(row = x, column = 2)
            self.word.destroy()
            if self.word == self.answer.get():
                self.points += 1
            time.sleep(1)
            count -= 1
        self.call_on_selected()
        