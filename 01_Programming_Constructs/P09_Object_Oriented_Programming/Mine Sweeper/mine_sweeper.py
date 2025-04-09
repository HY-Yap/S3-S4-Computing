import random
import os


class MineSweeper:
    def __init__(self, size=10, no_of_mines=10):
        self._size = size
        self._no_of_mines = no_of_mines
        self.reset()

    def reset(self):
        self._gstatus = True  # game is ongoing by default
        self._board = [[None for _ in range(self._size)]
                        for _ in range(self._size)]
        self._gboard = [[None for _ in range(self._size)]
                        for _ in range(self._size)]

    def display(self, guess_mode=True):
        # choose the board to be displayed
        if guess_mode:
            board = self._gboard
        else:
            board = self._board

        line = "+" + "---+" * self._size + "\n"
        result = line  # top line
        # display according to the rules
        for i in range(self._size):
            result += "|"  # left
            for j in range(self._size):
                if board[i][j] is None:
                    result += " - |"
                elif board[i][j] == 0:
                    result += "   |"
                else:
                    result += f" {board[i][j]} |"
            result += "\n" + line  # new line and bottom line
        print(result)

    def read_game(self, filename):
        # reset the board and no_of_mines
        self._board = []
        self._no_of_mines = 0

        with open(filename, "r") as f:
            for row in f:
                temp = []  # temp list to hold the row
                for char in row:
                    if char == "@":  # a mine
                        temp.append(char)
                        self._no_of_mines += 1
                    elif char == "\n" or char == "\r":
                        continue
                    else:  # char == " "
                        temp.append(None)
                # add the temp to the board
                self._board.append(temp)

        # update the size and gboard
        self._size = len(self._board[0])
        self._gboard = [[None for _ in range(self._size)]
                        for _ in range(self._size)]

    def save_game(self, filename):
        output = ""
        for row in self._board:
            for char in row:
                if char == "@":  # a mine
                    output += "@"
                else:  # anything else save as a space
                    output += " "
            output += "\n"

        with open(filename, "w") as f:
            f.write(output)

    def generate_mines(self):
        n = 0
        while n < self._no_of_mines:
            row = random.randint(0, self._size - 1)
            col = random.randint(0, self._size - 1)

            if self._board[row][col] != "@":
                # only increase n when a mine is successfully planted
                self._board[row][col] = "@"
                n += 1

    def generate_numbers(self):
        def count_mines(row, col):
            count = 0
            for shift_r in range(-1, 2):
                for shift_c in range(-1, 2):
                    if shift_r == 0 and shift_c == 0:
                        # dont count itself
                        continue

                    new_row = row + shift_r
                    new_col = col + shift_c
                    if 0 <= new_row < self._size and \
                            0 <= new_col < self._size and \
                            self._board[new_row][new_col] == "@":
                        count += 1
            return count

        for row in range(self._size):
            for col in range(self._size):
                if self._board[row][col] != "@":
                    self._board[row][col] = count_mines(row, col)

    def check_win(self):
        for i in range(self._size):
            for j in range(self._size):
                if self._board[i][j] != "@" and \
                        self._gboard[i][j] is None:
                    # field is not mine and yet to be reviewed, return False
                    return False
        return True

    def guess(self, row, col, action, rec=False):
        def double_click(row, col):
            for shift_r in range(-1, 2):
                for shift_c in range(-1, 2):
                    if shift_r == 0 and shift_c == 0:
                        continue  # skip the current cell
                    new_r, new_c = row + shift_r, col + shift_c
                    if 0 <= new_r < self._size and \
                            0 <= new_c < self._size and \
                            self._gboard[new_r][new_c] is None:
                        # perform click only if it is within valid range
                        self.guess(new_r, new_c, "c", rec=True)

        # check gstatus
        if self._gstatus == False:
            print("The game is finished, please restart.")

        if action == "f":  # flag the cell
            self._gboard[row][col] = "⚑"
        elif action == "u":  # unflag the cell
            self._gboard[row][col] = None
        elif action == "c":
            if self._gboard[row][col] == "⚑":
                # already flagged, cannot be clicked
                print("Already flagged.")
            elif self._board[row][col] == "@":
                # if it is a mine, game over
                print("Game over")
                self.display(guess_mode=False)  # display original board
                self._gstatus = False  # set gstatus to false
            elif self._gboard[row][col] is None:
                # copy the number from board to gboard
                self._gboard[row][col] = self._board[row][col]
                # if number is 0, click the 3x3 matrix (double click)
                if self._board[row][col] == 0:
                    double_click(row, col)
                if self.check_win():
                    print("You Win!")
                    self._gstatus = False
        elif action == "d":
            # scan for number of flags vs number of the board
            count = 0
            for shift_x in range(-1, 2):
                for shift_y in range(-1, 2):
                    new_row = row + shift_x
                    new_col = col + shift_y

                    if 0 <= new_row < self._size \
                            and 0 <= new_col < self._size \
                            and self._gboard[new_row][new_col] == "⚑":
                        count += 1

            if self._gboard[row][col] is None or \
                    count != self._board[row][col]:
                print("Cannot double click")
            else:
                double_click(row, col)

        if not rec and self._gstatus:
            # avoid recursive display the board when double click
            self.display()


def validate_opts(user_input):
    if len(user_input) == 0:
        print("Presence check failed. Please enter something")
        return False
    if not user_input.isdigit():
        print("Type check failed. Please make sure to enter a digit.")
        return False
    if int(user_input) < 1 or int(user_input) > 6:
        print("Range check failed. Please make to enter a valid from 1 to 6.")
        return False
    return True


def get_user_input(msg):
    done = False
    while not done:
        user_input = input(msg)
        done = validate_opts(user_input)
    return user_input


def display_options():
    options = """
Choose an option below:
1) User Action
2) Start New Game
3) Save Game
4) Load Game
5) Cheat - Display Mine Field
6) Exit
"""
    print(options)


def menu():
    ms = MineSweeper(10, 10)
    ms.generate_mines()
    ms.generate_numbers()
    print("Welcome to mine sweeper!")
    ms.display()

    done = False
    while not done:
        display_options()
        user_input = int(get_user_input("Your Option: "))
        if user_input == 1:
            restart_input = input("Please key in (row, col, action): ")
            row, col, action = restart_input.split(",")
            row = int(row.strip())  # int
            col = int(col.strip())  # int
            action = action.strip()  # str
            ms.guess(row, col, action)
        elif user_input == 2:
            restart_input = input("Please key in (size, no_of_mines): ")
            size, no_of_mines = restart_input.split(",")
            size = int(size.strip())  # int
            no_of_mines = int(no_of_mines.strip())  # int
            ms = MineSweeper(size, no_of_mines)
            ms.generate_mines()
            ms.generate_numbers()
            print("A new game has been generated")
            ms.display()
        elif user_input == 3:
            filename = input(
                "Please key in the filename to save the current game: ")
            ms.save_game(filename)
        elif user_input == 4:
            filename = input(
                "Please key in the filename to load the current game: ")
            if os.path.exists(filename):
                ms.read_game(filename)
                ms.generate_numbers()
                print("Game loaded.")
                ms.display()
            else:
                print("File is not found.")
        elif user_input == 5:
            ms.display(guess_mode=False)
        elif user_input == 6:
            done = True
            print("Thank you for playing my mine sweeper game.")


menu()