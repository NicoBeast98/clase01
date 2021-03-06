import random

class Game():
    def __init__(self):
        self.is_playing = True
    def end(self):
        self.is_playing = False


class HumanAgainstComputerGame(Game):

    def __init__(self):
        self.is_playing = True
        self.secret_number = random.randrange(101)
        
    def play(self,inputx):
        
        if inputx == self.secret_number:
            self.end()
            return 'You win'
        if inputx < self.secret_number:
            return 'My number is bigger'
        if inputx > self.secret_number:
            return 'My number is smaller'

class ComputerAgainstHumanGame(Game):

    def __init__(self):
        self.is_playing = True
        self.guest = 50
        self.top = 100
        self.bottom = 0

    def input_text(self):
        n = str(self.guest)
        ans = ('Is it your number '+n+'?')
        return ans

    def play(self,inputx):
        try:
            inputx = int(inputx)
        except:
            if inputx == '+':
                self.bottom = self.guest
                self.guest += int((self.top - self.bottom)/2)
                return
            if inputx == '-':
                self.top = self.guest
                self.guest -= int((self.top - self.bottom)/2)
                return
            if inputx == '=':
                self.is_playing = False
                return

