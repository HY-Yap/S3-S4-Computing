colour = {True: "black", False: "white"}
colour_symbol = {True: "●", False: "○"}
player = {True: 1, False: 2}

def get_player(turn):
    return f"Player {player[turn]} ({colour[turn]})"

class GoPiece:
    def __init__(self, turn: bool, row: int, col: int):
        self._turn = turn
        self._row = row
        self._col = col
    
    def get_turn(self) -> bool:
        return self._turn
    
    def get_row(self) -> int:
        return self._row
    
    def get_col(self) -> int:
        return self._col
    
    def __str__(self) -> str:
        return f"{get_player(self.get_turn())} plays at ({self.get_row()}, {self.get_col()})"

# testing_piece = GoPiece(0, 1, 2)
# print(testing_piece)

class Board:
    def __init__(self, board_size: int):
        self._board_size = board_size
        self.reset()
        self._curr_player = True
    
    def reset(self):
        self._board = [[None for _ in range(self._board_size)] for _ in range(self._board_size)]
        self._curr_steps = []
        self._redo_stk = []
        self._turn = True
        self._won = False

    def display_board(self):
        # print top col numbers
        result = "   "
        for c in range(self._board_size):
            result += f"{c:0>2}  "
        result = result[:-2] + "\n"
        # print the actual board with row numbers at the side
        for r in range(self._board_size):
            result += f"{r:0>2}  "
            for c in range(self._board_size):
                if self._board[r][c] == None:
                    result += "+---"
                else:
                    result += f"{colour_symbol[self._board[r][c].get_turn()]}---"
            
            result = result[:-3] # chop off the extre "---"
            if r+1 != self._board_size:
                # not yet last row -> add the border
                result += "\n    |" + "   |" * (self._board_size - 1) + "\n"
        
        print(result)

    def is_valid_move(self, row, col) -> bool:
        return self._board[row][col] is None

    def new_move(self, row, col):
        if not self._won:
            if self.is_valid_move(row, col): # if game not over & valid move
                new_piece = GoPiece(self._curr_player, row, col)
                self._board[row][col] = new_piece
                self._curr_steps.append(new_piece)
                print(new_piece)
                self._redo_stk = []
                self.check_win()
                if not self._won:
                    # continue the game if player hasn't won
                    # next player
                    self._curr_player = not self._curr_player
            else:
                print("Invalid move. Please choose another spot")
        else:
            print(f"Unable to carry out move. Player {player[self._curr_steps[-1].get_turn()]} has already won.")

    def check_win(self) -> bool:
        dir = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
            "down_left": (1, -1),
            "down_right": (1, 1),
            "up-left": (-1, -1),
            "up-right": (-1, 1)
        }
        if self._curr_steps != []:
            latest_piece = self._curr_steps[-1]
            # print("turn", latest_piece.get_turn())
            winning_player = latest_piece.get_turn() # bool
            for key in dir:
                x, y = latest_piece.get_row(), latest_piece.get_col()
                # print(key, dir[key][0], dir[key][1])
                for i in range(4):
                    x, y = x + dir[key][0], y + dir[key][1]
                    if 0 <= x < self._board_size and 0 <= y < self._board_size:
                        # move is within board range
                        if self._board[x][y] is not None:
                            # if this next box has a piece
                            if self._board[x][y].get_turn() == winning_player:
                                # * only continue if this next piece is same as prev
                                # print("correct piece", i)
                                if i == 3:
                                    # * last piece confirmed
                                    self._won = True
                                    return True
                            else:
                                # print("wrong piece", i)
                                break
                        else:
                            break # empty box
                    else:
                        break # move is not in range
        return False

    def undo_move(self):
        if self._curr_steps != []:
            # undo
            obj = self._curr_steps.pop()
            self._redo_stk.append(obj)
            self._board[obj.get_row()][obj.get_col()] = None
            print("Undo successful.")
        else:
            print("No move to undo.")

    def redo_move(self):
        if self._redo_stk != []:
            # redo
            obj = self._redo_stk.pop()
            self._curr_steps.append(obj)
            self._board[obj.get_row()][obj.get_col()] = obj
            print("Redo successful")
        else:
            print("No move to redo")

# testing_board = Board(4)
# print(testing_board._board)
# testing_board._board[1][1] = GoPiece(1, 1, 1)
# testing_board._board[0][2] = GoPiece(0, 0, 2)
# testing_board.display_board()
# print(testing_board.is_valid_move(0, 0)) # empty
# print(testing_board.is_valid_move(1, 1)) # filled
# testing_board.reset()
# testing_board.display_board()

# board = Board(10)
# board.display_board()
# print()
# board.new_move(0,0)
# board.display_board()
# print()
# board.new_move(0,1)
# board.display_board()
# print()
# board.new_move(1,1)
# board.display_board()
# print()
# board.new_move(1,2)
# board.display_board()
# print()
# board.new_move(2,2)
# board.display_board()
# print()
# board.new_move(5,2)
# board.display_board()
# print()
# board.new_move(3,3)
# board.display_board()
# print()
# board.new_move(3,4)
# board.display_board()
# print()
# board.new_move(4,4)
# board.display_board()
# print()
# board.new_move(4,5)

def validate(user_input):
    # returns False if input is invalid, True otherwise
    if len(user_input) == 0:  # Presence check
        print("Presence check failed. Please do not enter an empty input.")
        return False
    elif not user_input.isdigit():  # Type check
        print("Type check failed. Please enter a digit.")
        return False
    elif int(user_input) < 1 or int(user_input) > 5:  # Range check
        print("Range check failed. Please key in a value in between 1 and 5.")
        return False
    else:  # returns True if all checks have been passed
        return True
    
    
def valid_user_input(msg):
    done = False
    while not done:
        user_input = input(msg)
        done = validate(user_input)
    return user_input

def validate_move_input(user_input, board_size):
    # returns False if input is invalid, True otherwise
    if len(user_input) == 0:  # Presence check
        print("Presence check failed. Please do not enter an empty input.")
        return False
    elif not user_input.isdigit():  # Type check
        print("Type check failed. Please enter a digit.")
        return False
    elif int(user_input) < 0 or int(user_input) >= board_size:  # Range check
        print(f"Range check failed. Please key in a value in between 0 and {board_size - 1}.")
        return False
    else:  # returns True if all checks have been passed
        return True

def valid_move_input(msg, board_size):
    done = False
    while not done:
        user_input = input(msg)
        done = validate_move_input(user_input, board_size)
    return user_input

def display_menu():
    menu_opts = """
Choose an option below:
1) New Move
2) Undo Move
3) Redo Move
4) Reset
5) Exit
"""
    print(menu_opts)

    
def menu():
    board = Board(10)  # Initialize a board of size 10
    done = False
    while not done:
        display_menu()
        user_input = int(valid_user_input("Please select an option 1 to 5: "))
        if user_input == 1:
            row = int(valid_move_input("Enter row: ", board._board_size))
            col = int(valid_move_input("Enter column: ", board._board_size))
            board.new_move(row, col)
            board.display_board()
        elif user_input == 2:
            board.undo_move()
            board.display_board()
        elif user_input == 3:
            board.redo_move()
            board.display_board()
        elif user_input == 4:
            print("Resetting game.")
            board.reset()
            board.display_board()
        elif user_input == 5:
            print("Quitting program. Thank you!")
            done = True

menu()