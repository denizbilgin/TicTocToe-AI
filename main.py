from TicTacToe import TicTacToe

if __name__ == '__main__':
    game = TicTacToe(isPlayerTurn=True)
    game.print_board()
    while game.is_game_ended() == -1:
        row_to_play = int(input("Type row:"))
        col_to_play = int(input("Type column:"))
        game.move(row_to_play, col_to_play)
        game.print_board()
