class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
        self.remianing_guess = lives

    def guess(self,n):
        if self.remianing_guess <= 0:
            raise ValueError("Out of guesses! You lost the game.")

        if n == self.number:
            return True
        else:
            self.remianing_guess -= 1
            return False
