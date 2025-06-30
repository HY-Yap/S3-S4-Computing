gems = ["down", "s", "t", "right", "e"]

board = [
    ['r', 'r', 'd', 'e', 'd'],
    ['s', 'd', 'r', 'd', 't'],
    ['d', 'd', 'r', 's', 'd'],
    ['e', 'r', 't', 'r', 'r'],
    ['t', 'e', 'e', 's', 'd']]

dirs = {
    "u": (-1, 0),
    "d": (1, 0),
    "l": (0, -1),
    "r": (0, 1)
}

class Board:
    def __init__(self, n: list):
        self._board = [["_" for _ in range(n)] for _ in range(n)]
    
    def new_game(self, new_board: list) -> None:
        self._board = new_board
    
    def check_connection(self, row: int, col: int) -> bool:
        curr_chr = self._board[row][col]
        # check horizontal
        count = 1
        # left
        x, y = row, col - 1
        while y >= 0 and self._board[x][y] == curr_chr:
            count += 1
            y -= 1
        # right
        x, y = row, col + 1
        while y < len(self._board[0]) and self._board[x][y] == curr_chr:
            count += 1
            y += 1
        if count >= 3:
            return True
        
        # check vertical
        count = 1
        # count up
        x, y = row - 1, col
        while x >= 0 and self._board[x][y] == curr_chr:
            count += 1
            x -= 1
        # count down
        x, y = row + 1, col
        while x < len(self._board) and self._board[x][y] == curr_chr:
            count += 1
            x += 1
        if count >= 3:
            return True
            
        return False
    
    def find_valid_moves(self, row: int, col: int) -> list:
        valid_moves = []
        if self._board[row][col] != "_" :
            # try to swap in every dir
            for dir in dirs:
                x, y = row, col
                x2, y2 = x + dirs[dir][0], y + dirs[dir][1]
                # print(dir, dirs[dir][0], dirs[dir][1])
                # print(f"x2={x2}, y2={y2}")
                if 0 <= x2 < len(self._board) and 0 <= y2 < len(self._board) and self._board[x2][y2] != "_":
                    # in range and not empty -> proceed with swap
                    self._board[x][y], self._board[x2][y2] = self._board[x2][y2], self._board[x][y]
                    # print(self._board[x2][y2], self._board[x][y])
                    if self.check_connection(x, y) or self.check_connection(x2, y2):
                        valid_moves.append(dir)
                        # print("valid move found")
                    # SWAP THE BOARD BACK
                    self._board[x][y], self._board[x2][y2] = self._board[x2][y2], self._board[x][y]
        return valid_moves
    
    def display(self, hint:bool=False) -> None:
        # print hint
        if hint == True:
            print()
            highlighted = []
            for i in range(len(self._board)):
                for j in range(len(self._board)):
                    if len(self.find_valid_moves(i, j)) > 0:
                        highlighted.append((i, j))
                        print(f"({i}, {j}) {self.find_valid_moves(i, j)}")
            # print("highlighted", highlighted)
        # print the board
        result = "\n   "
        for i in range(len(self._board)):
            result += f"  {i} "
        border = "   " + "+---" * len(self._board) + "+\n"
        result += '\n' + border
        for i in range(len(self._board)):
            result += f"{i}  |"
            for j in range(len(self._board)):
                if hint == True and (i, j) in highlighted:
                    result += f" {self._board[i][j].upper()} |"
                else:
                    result += f" {self._board[i][j]} |"
            result += '\n'
            result += border
        print(result)


# test_board = Board(2)
# test_board.new_game(board)
# print(test_board._board)
# print(test_board.check_connection(0,0))
# print(test_board.find_valid_moves(1, 3))
# test_board.display()

# initialise game
game = Board(5)
game.new_game(board)

def display_menu(hint):
    game.display(hint)
    print('''Choose an option below:
1) Validate Move
2) Toggle Hint Mode
3) Move the Gem!
4) New Game
5) Exit''')

def validate(user_input):
    if not user_input.isdigit():
        print("\nPlease key in an integer from 1 to 5.")
        return False
    elif not 1 <= int(user_input) <= 5:
        print("\nPlease key in an integer from 1 to 5.")
        return False
    else:
        return True

def get_user_input(msg):
    done = False
    while not done:
        user_input = input(msg)
        done = validate(user_input)
    return int(user_input)

def validate_row_col(user_input):
    if not user_input.isdigit():
        print(f"\nPlease key in an integer from 0 to {len(game._board)-1}.")
        return False
    elif not 0 <= int(user_input) <= len(game._board)-1:
        print(f"\nPlease key in an integer from 0 to {len(game._board)-1}.")
        return False
    else:
        return True

def get_row_col(msg):
    done = False
    while not done:
        user_input = input(msg)
        done = validate_row_col(user_input)
    return int(user_input)

def validate_dir(user_input):
    if not user_input.isalpha():
        print(f"\nPlease key in u/d/l/r.")
        return False
    elif len(user_input) != 1 or user_input not in "udlr":
        print(f"\nPlease key in u/d/l/r.")
        return False
    else:
        return True

def get_dir(msg):
    done = False
    while not done:
        user_input = input(msg)
        done = validate_dir(user_input)
    return user_input

def menu():
    user_playing = True
    hint = False
    while user_playing:
        display_menu(hint)
        user_input = get_user_input("Select an option: ")
        print()
        if user_input == 1:
            print("==Validate Move==")
            row = get_row_col("Row: ")
            col = get_row_col("Col: ")
            dir = get_dir("Direction (u/d/l/r): ")
            print()
            if dir in game.find_valid_moves(row, col):
                print("Valid swap")
            else:
                print("Invalid swap")
        elif user_input == 2:
            print("==Toggle Hint Mode==")
            hint = not hint
            print(f"Hint mode {"on" if hint else "off"}")
        elif user_input == 3:
            print("==Move the Gem!==")
            row = get_row_col("Row: ")
            col = get_row_col("Col: ")
        elif user_input == 4:
            print("==New Game==")
            game.new_game(board)
            hint = False
        else:
            print("==Exit program==")
            user_playing = False

menu()
