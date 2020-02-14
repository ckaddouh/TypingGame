# self.endGame() should give a summary screen. 
from startScreen import Startscreen
from game_Gui import Application
from game_over import Application

class screen_manager(object):
    def __init__(self):
        self.root = Tk()
        self.current_screen = None
        self.wordList = []
        text_file = open("yummywords.txt", r)
        for line in text_file:
            self.wordList.append(line.strip())
        self.wordList.shuffle()

    
    def start_screen(self):
        self.root.title("Welcome!")
        self.current_screen = Startscreen(self.root, self.start_button)
    
    def start_button(self):
        self.current_screen.destroy()
        self.game()

    def game(self):
        self.root.title("Typing Game!")
        self.current_screen = Application(self.root, self.wordList, self.endGame)
    
    def endGame(self):
        self.current_screen.destroy()
        self.root.title("Game Summary")
        self.current_screen = summary(self.root, self.wordList, self.exit_button)
    
    def exit_button(self):
        self.current_screen.destroy()

def main():
    typing = screen_manager
    typing.startScreen
    typing.root.mainloop()