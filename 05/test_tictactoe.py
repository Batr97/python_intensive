from tictactoe import TicTacGame


def test_wrong_input():
    game = TicTacGame()
    steps = [15, 15, 0, 30, 91]
    for step in steps:
        game.show_board()
        assert game.player_input(step) == 'wrong input'
        break


def test_already_busy_spot():
    game = TicTacGame()
    steps = [1, 1, 2, 3, 9]
    game.player_input(steps[0])
    for step in range(1, len(steps)):
        game.show_board()
        assert game.player_input(steps[step]) == "Oops player is already at that spot"
        break


def test_winner_X_diagonal():
    game = TicTacGame()
    steps = [1, 2, 5, 3, 9]
    for step in steps:
        game.show_board()
        game.player_input(step)
        a = game.win()
        game.switch()
    assert game.winner == "X"
    assert a == 'The winner along the diagonal is X!'


def test_winner_X_row():
    game = TicTacGame()
    steps = [1, 5, 2, 8, 3]
    for step in steps:
        game.show_board()
        game.player_input(step)
        a = game.win()
        game.switch()
    assert game.winner == "X"
    assert a == 'The winner along the row is X!'


def test_winner_X_column():
    game = TicTacGame()
    steps = [1, 2, 4, 3, 7]
    for step in steps:
        game.show_board()
        game.player_input(step)
        a = game.win()
        game.switch()
    assert game.winner == "X"
    assert a == 'The winner along the column is X!'


def test_winner_O_column():
    game = TicTacGame()
    steps = [1, 2, 3, 5, 7, 8]
    for step in steps:
        game.show_board()
        game.player_input(step)
        a = game.win()
        game.switch()
    assert game.winner == "O"
    assert a == 'The winner along the column is O!'


def test_winner_O_row():
    game = TicTacGame()
    steps = [1, 4, 3, 5, 9, 6]
    for step in steps:
        game.show_board()
        game.player_input(step)
        a = game.win()
        game.switch()
    assert game.winner == "O"
    assert a == 'The winner along the row is O!'


def test_winner_O_diagonal():
    game = TicTacGame()
    steps = [1, 3, 2, 5, 9, 7]
    for step in steps:
        game.show_board()
        game.player_input(step)
        a = game.win()
        game.switch()
    assert game.winner == "O"
    assert a == 'The winner along the diagonal is O!'


def test_tie():
    game = TicTacGame()
    steps = [1, 3, 2, 5, 7, 4, 8, 9, 6]
    for step in steps:
        game.show_board()
        game.player_input(step)
        a = game.win()
        game.switch()
    assert game.winner is None
    assert a == 'It is a tie!!'

game = TicTacGame()
print(game.play())