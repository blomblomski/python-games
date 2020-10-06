import random


class Hangman:
    is_won = False
    player_turn = False
    word_list = [
        'cheese', 'monkey', 'snake', 'pants', 'transfer',
        'fuchsia', 'sacrilegious', 'dilate', 'paraphernalia',
        'misspell', 'pharaoh', 'weird', 'intelligence', 'pronunciation',
        'handkerchief', 'gobbledegook'
    ]
    word = None
    current_word = []
    guesses = 10

    def new_word(self):
        self.word = random.choice(self.word_list)
        self.guesses = 10
        for x in range(len(self.word)):
            self.current_word.append(str(' '))

    def print(self):
        print('Guesses left: ', self.guesses)
        print(self.current_word)

    def check_win(self):
        if ' ' not in self.current_word:
            print('Congratulations! You win.')
            self.is_won = True
        elif self.guesses <= 0:
            print('Unlucky! You did not mange to guess the correct word.')
            self.is_won = True

    def game(self):
        while not self.is_won:
            self.print()
            try:
                selection = input('> ')
                if selection in self.word:
                    for i, x in enumerate(self.word):
                        if selection == x:
                            self.current_word[i] = selection
                else:
                    self.guesses -= 1
                self.check_win()
            except ValueError:
                print('Please enter valid choice')
