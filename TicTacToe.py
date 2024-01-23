from itertools import chain

class TicTacToe:
    __PLAYER_SIGN = 1
    __AI_SIGN = 2
    __EMPTY_SPACE = 0
    BOARD_SIZE = 3

    def __init__(self, is_player_turn):
        self.__board = [[self.__EMPTY_SPACE for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        self.__player_turn = is_player_turn

    def get_player_turn(self) -> bool:
        return self.__player_turn

    def set_player_turn(self, value:bool):
        self.__player_turn = value

    def get_board(self) -> list[list[int]]:
        return self.__board

    def get_empty_space(self):
        return self.__EMPTY_SPACE

    def print_board(self, label="Current position of the board is:"):
        """
        This function prints the board to the console
        :param label: Title of the printing
        """
        print("-------")
        print(label)
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                if self.__board[i][j] == self.__PLAYER_SIGN:
                    print("X", end=" ")
                elif self.__board[i][j] == self.__AI_SIGN:
                    print("O", end=" ")
                elif self.__board[i][j] == self.__EMPTY_SPACE:
                    print("_", end=" ")
            print()
        print("-------")

    def is_valid_move(self, row, col) -> bool:
        """
        This function checks is it valid move
        :param row: row number (between 0-2)
        :param col: col number (between 0-2)
        """
        return self.__board[row][col] == self.__EMPTY_SPACE

    def is_game_ended(self) -> int:
        """
        This function checks is the game ended or not. If the game continues, this function will
        return -1. In the case of draw this function will return 0. When player wins the game this function
        will return 1. When AI wins the game this function will return 2.
        :return: State of the game
        """

        for i in range(self.BOARD_SIZE):
            # Checking rows
            if self.__board[i][0] == self.__board[i][1] == self.__board[i][2] != self.__EMPTY_SPACE:
                return self.__board[i][0]

            # Checking columns
            if self.__board[0][i] == self.__board[1][i] == self.__board[2][i] != self.__EMPTY_SPACE:
                return self.__board[0][i]

        # Checking diagonals
        if self.__board[0][0] == self.__board[1][1] == self.__board[2][2] != self.__EMPTY_SPACE:
            return self.__board[0][0]
        if self.__board[0][2] == self.__board[1][1] == self.__board[2][0] != self.__EMPTY_SPACE:
            return self.__board[0][2]

        # Case of draw
        if self.__EMPTY_SPACE not in list(chain.from_iterable(self.__board)):
            return 0

        # Game continuing
        return -1

    def move(self, row, col):
        """
        Player or AI can move with this function by given row and columns
        :param row: row number (between 0-2)
        :param col: col number (between 0-2)
        """

        if not self.is_valid_move(row, col):
            print("Cell is already occupied")
            return

        if self.__player_turn:
            self.__board[row][col] = self.__PLAYER_SIGN
        else:
            self.__board[row][col] = self.__AI_SIGN

    def undo_move(self, row, col):
        if self.__board[row][col] != self.__EMPTY_SPACE:
            self.__board[row][col] = self.__EMPTY_SPACE

    def score(self, winner, depth) -> int:
        """
        This function calculates the score for the minimax algorithm based on the winner and depth
        :param winner: The winner of the game
        :param depth: The depth of the recursive search
        :return: The score for the current state
        """
        if winner == self.__AI_SIGN:
            return 10 - depth
        elif winner == self.__PLAYER_SIGN:
            return depth - 10
        else:
            return 0

    def get_available_moves(self) -> list[tuple[int, int]]:
        """
        This function returns a list of available moves as tuples (row, col)
        """
        return [(i, j) for i in range(self.BOARD_SIZE) for j in range(self.BOARD_SIZE) if
                self.__board[i][j] == self.__EMPTY_SPACE]