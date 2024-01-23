from TicTacToe import TicTacToe
import random
import copy


class Ai3T:

    def minimax(self, game, depth):
        """
        Implements the Minimax algorithm to determine the best move for the AI.
        """

        result = game.is_game_ended()

        # Base cases: game ended or maximum depth reached
        if result != -1:
            return result, None  # Return game state and no move
        if depth == 0:
            return 0, None  # Return draw state and no move

        best_score = float('-inf') if game.get_player_turn() else float('inf')
        best_move = None

        # Iterate through all available moves
        for row in range(game.BOARD_SIZE):
            for col in range(game.BOARD_SIZE):
                if game.is_valid_move(row, col):
                    # Make a copy of the game to simulate the move
                    temp_game = copy.deepcopy(game)
                    temp_game.move(row, col)

                    # Change player turn for the next level of recursion
                    temp_game.set_player_turn(not temp_game.get_player_turn())

                    # Recursively call minimax for the opponent's turn
                    score, _ = self.minimax(temp_game, depth - 1)
                    temp_game.undo_move(row, col)

                    # Update best score and move if applicable
                    if game.get_player_turn():
                        if score > best_score:
                            best_score = score
                            best_move = (row, col)
                    else:
                        if score < best_score:
                            best_score = score
                            best_move = (row, col)

        return best_score, best_move

    def get_move(self, game):
        _, best_move = self.minimax(game, 2)
        return best_move

