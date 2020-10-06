import random


class NumberGuess:
    is_won = False
    number = None
    guesses = 0

    def new_number(self):
        self.guesses = 10
        self.number = random.randint(1, 100)

    def check_win(self, guess):
        if guess > self.number:
            print('Your guess was high')

        elif guess < self.number:
            print('Your guess was low')
        else:
            self.is_won = True
            print('Congratulations, you guessed the number I was thinking!')
        if self.guesses <= 0:
            print('Unlucky! You did manage to guess my number')
        self.guesses -= 1

    def game(self):
        print('I am thinking of a random number between 1 and 100, can you guess it?')

        while not self.is_won:
            print(f"Please guess a number, you have { self.guesses } remaining")
            try:
                guess = int(input('> '))
                self.check_win(guess)
            except ValueError:
                print('Not a valid guess, try again!')
