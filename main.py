import hangman
import newtictactoe
import numberguess

leave = False

options = """
    (1)  Tic Tac Toe
    (2)  Hangman
    (3)  Number Guess
    (0)  Exit 
"""

while not leave:
    try:
        print(options)
        choice = int(input('> Please pick a game: '))
        if choice == 1:
            tic = newtictactoe.TicTacToe()
            tic.create_board()
            tic.game_loop()
        elif choice == 2:
            h = hangman.Hangman()
            h.new_word()
            h.game()
        elif choice == 3:
            h = numberguess.NumberGuess()
            h.new_number()
            h.game()
        elif choice == 0:
            leave = True
        else:
            print('Please enter a valid choice')
    except ValueError:
        print('Please enter a valid choice')
