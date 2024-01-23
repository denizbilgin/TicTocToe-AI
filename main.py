from Ai3T import Ai3T
from TicTacToe import TicTacToe

if __name__ == '__main__':
    game = TicTacToe(True)
    ai = Ai3T()

    while game.is_game_ended() == -1:
        if game.get_player_turn():
            print("Player's turn")
            game.move(int(input("Row: ")), int(input("Column: ")))
        else:
            # AI hamlesini yapar
            print("AI's turn")
            row, col = ai.get_move(game)
            game.move(row, col)

        game_ended = game.is_game_ended()
        if game_ended == -1:
            game.set_player_turn(not game.get_player_turn())
        elif game_ended == 0:
            print("DRAW!")
        elif game_ended == 1:
            print("PLAYER WINS THE GAME!")
        elif game_ended == 2:
            print("AI WINS THE GAME!")

        game.print_board()