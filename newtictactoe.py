class TicTacToe:
    is_won = False
    player_turn = True
    board = []

    def create_board(self):
        self.board = []
        self.is_won = False
        for x in range(10):
            self.board.append(str(x + 1))

    def print_board(self):
        b = self.board
        print('|' + b[0] + '|' + b[1] + '|' + b[2] + '|')
        print('|' + b[3] + '|' + b[4] + '|' + b[5] + '|')
        print('|' + b[6] + '|' + b[7] + '|' + b[8] + '|')

    def check_win(self):
        b = self.board
        for x in range(3):
            if b[0 + (x * 3)] == b[1 + (x * 3)] == b[2 + (x * 3)] \
                    and (b[0 + (x * 3)] is 'x' or 'o'):
                self.is_won = True

        for y in range(3):
            if b[0 + (y * 3)] == b[3 + (y * 3)] == b[6 + (y * 3)] \
                    and (b[0 + (y * 3)] is 'x' or 'o'):
                self.is_won = True

        if (b[0] == b[4] == b[8] and (b[0] is 'x' or 'o')) or \
                (b[2] == b[4] == b[6] and (b[2] is 'x' or 'o')):
            self.is_won = True

        if self.is_won:
            print('Well done {}, you win!'.format(('Player one', 'Player two')[self.player_turn - 1]))

        self.player_turn = not self.player_turn

    def game_loop(self):
        while not self.is_won:
            self.print_board()
            try:
                a = 'one' if self.player_turn else 'two'
                p = 'Player {} pick a tile > '.format(a)
                choice = int(input(p)) - 1
                if 0 <= choice <= 8:
                    if self.board[choice] is not ('x' or 'o'):
                        if self.player_turn:
                            self.board[choice] = 'x'
                        else:
                            self.board[choice] = 'o'
                        self.check_win()
                    else:
                        print('Please pick blank tile')
                else:
                    print('Please enter a valid choice')
            except ValueError:
                print('Please enter a valid choice')
