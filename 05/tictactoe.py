class TicTacGame:
    def __init__(self):
        self.board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        self.player = "X"
        self.winner = None
        self.run = True

    def show_board(self):
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("---------")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("---------")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def player_input(self, val):
        inp = val
        if inp < 0 or inp > 9:
            return 'wrong input'
        elif self.board[inp-1] != "-":
            return "Oops player is already at that spot"
        else:
            self.board[inp-1] = self.player

    def switch(self):
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"

    def horizont(self):
        if self.board[0] == self.board[1] == self.board[2] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        elif self.board[3] == self.board[4] == self.board[5] and self.board[3] != "-":
            self.winner = self.board[3]
            return True
        elif self.board[6] == self.board[7] == self.board[8] and self.board[6] != "-":
            self.winner = self.board[6]
            return True

    def vertical(self):
        if self.board[0] == self.board[3] == self.board[6] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        elif self.board[1] == self.board[4] == self.board[7] and self.board[1] != "-":
            self.winner = self.board[1]
            return True
        elif self.board[2] == self.board[5] == self.board[8] and self.board[2] != "-":
            self.winner = self.board[3]
            return True

    def diagonal(self):
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        elif self.board[2] == self.board[4] == self.board[6] and self.board[4] != "-":
            self.winner = self.board[2]
            return True

    def win(self,):
        if self.horizont():
            self.show_board()
            self.run = False
            return f'The winner along the row is {self.winner}!'

        elif self.vertical():
            self.show_board()
            self.run = False
            return f'The winner along the column is {self.winner}!'

        elif self.diagonal():
            self.show_board()
            self.run = False
            return f'The winner along the diagonal is {self.winner}!'

        elif "-" not in self.board:
            self.show_board()
            self.run = False
            return 'It is a tie!!'

    def play(self):
        self.run = True
        while self.run:
            self.show_board()
            step = int(input())
            turn = self.player_input(step)
            while (turn == 'wrong input') or turn == ('Oops player is already at that spot'):
                step = int(input())
                turn = self.player_input(step)
            win = self.win()
            self.switch()
        return win

