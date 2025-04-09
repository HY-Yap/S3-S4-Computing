import random


def get_mapping():
    file_name = "/Users/hanyang/Desktop/HCI Comp Folder Structure/01_Programming_Constructs/P09_Object_Oriented_Programming/Mission: Battleship/ship_class_mapping.txt"

    with open(file_name, "r") as f:
        # method 1
        # data = f.read()
        # # print(data)
        # # print(repr(data))
        # rows = data.split("\n")
        # print(rows)

        # method 2 - while loop
        # rows = []
        # line = f.readline()
        # while line:  # line is not ""
        #     rows.append(line.strip())
        #     line = f.readline()

        # print(rows)

        # method 3 - for loop
        rows = []
        for line in f:
            rows.append(line.strip())

        # print(rows)

    rows = rows[1:]
    ships = {}
    for row in rows:
        class_, abbr, length = row.split(", ")
        # print(ship, abbr, length)
        ships[class_] = (abbr, int(length))

    # print(ships)
    return ships


ships = get_mapping()


class Ship:
    def __init__(self, class_):
        self._class = class_
        self._abbr, self._size = ships[self._class]

    def get_class(self):
        return self._class

    def get_abbr(self):
        return self._abbr

    def get_size(self):
        return self._size

    def __str__(self):
        return f"{self._class} (Size {self._size})"


# ship1 = Ship("Carrier")
# print(ship1.get_class(), ship1.get_abbr(), ship1.get_size())


class Board:
    def __init__(self):
        self.reset()

    def reset(self):
        self._board = [[None for _ in range(10)] for _ in range(10)]
        self._gboard = [[None for _ in range(10)] for _ in range(10)]

    def add_ship(self, ship):
        # TODO: terminate the while loop if board is full
        # TODO: for now we assume sufficient spaces for all ships

        valid_directions = []  # init valid directions list
        while len(valid_directions) == 0:
            # 1. randomly choose a starting point
            start_x, start_y = random.randint(0, 9), random.randint(0, 9)
            # print(start_x, start_y)
            if self._board[start_x][start_y] is not None:
                # starting point is occupied
                # continue to next iteraction to gen a new starting pt
                continue

            # 2. survey 4 diff directions, and save the available directions
            # 4 directions, up/down/left/right
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            # valid_directions = []  # reset valid directions
            for direction in directions:
                shift_x, shift_y = direction
                count = 1
                new_x, new_y = start_x + shift_x, start_y + shift_y
                while 0 <= new_x < 10 and \
                        0 <= new_y < 10 and \
                        self._board[new_x][new_y] is None and \
                        count < ship.get_size():
                    # new position is within the valid range
                    # and available (None)
                    # loop should stop when count == ship size
                    count += 1
                    new_x += shift_x
                    new_y += shift_y

                if count == ship.get_size():
                    # this direction is valid option, add it
                    valid_directions.append(direction)

        # 3. choose one of the available directions
        direction = random.choice(valid_directions)

        # 4. place the ship
        for i in range(ship.get_size()):
            new_x = start_x + direction[0] * i
            new_y = start_y + direction[1] * i
            self._board[new_x][new_y] = ship

    def display_board(self, guess_mode=True):
        # choose the board to be displayed
        if guess_mode:
            board = self._gboard
        else:
            board = self._board

        # top row with numbers
        result = " " * 4
        for i in range(10):
            result += f" {i}  "
        result += "\n"

        # generate the lines in between
        line = "   +"
        for i in range(10):
            line += "---+"
        line += "\n"
        result += line

        # generate the main board
        for i in range(len(board)):
            # left
            result += f"{i}  |"
            # main
            for item in board[i]:
                if item is not None:
                    if isinstance(item, Ship):  # ship obj
                        result += f" {item.get_abbr()} |"
                    else:  # just a string
                        result += f" {item} |"
                else:
                    result += "   |"
            # new line
            result += "\n"
            # line in btw
            result += line

        print(result)

    def generate_new_game(self):
        self.reset()

        message = """
New Game Generated.

The following ships have entered the battlefield:
"""
        for class_ in ships:
            number = random.randint(1, 3)
            # add the ship to the board
            for i in range(number):
                # create a new ship of this class
                ship = Ship(class_)
                self.add_ship(ship)

            message += f"{ship}: {number}\n"

        print(message)

    def guess(self, row, col):
        if self._gboard[row][col] is not None:
            # guessed before
            return False

        if self._board[row][col] is not None:
            # there is a ship
            self._gboard[row][col] = self._board[row][col].get_abbr()
        else:
            # no ship
            self._gboard[row][col] = "X"

        return True

    def power_guess(self, row, col):
        if self._gboard[row][col] is not None:
            # guessed before
            return False

        if self._board[row][col] is None:
            # there is no ship
            self._gboard[row][col] = "X"
            return True

        # ship found
        # 1. mark the current position
        self._gboard[row][col] = self._board[row][col].get_abbr()

        # 2. find 1 direction containing the same ship obj
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for direction in directions:
            shift_x, shift_y = direction
            new_x, new_y = row + shift_x, col + shift_y
            if self._board[new_x][new_y] is self._board[row][col]:
                # ship found in this direction
                break

        oppo_direction = (direction[0] * -1, direction[1] * -1)

        # 3. survey the both directions for the ship obj
        for direction in (direction, oppo_direction):
            shift_x, shift_y = direction
            new_x, new_y = row + shift_x, col + shift_y
            # set the abbr for the new position if it is the same ship
            while 0 <= new_x < 10 and \
                    0 <= new_y < 10 and \
                    self._board[new_x][new_y] is self._board[row][col]:
                # same ship obj is found in this direction
                self._gboard[new_x][new_y] = \
                    self._board[new_x][new_y].get_abbr()

                new_x += shift_x
                new_y += shift_y

        return True

    def check_win(self):
        for i in range(10):
            for j in range(10):
                if isinstance(self._board[i][j], Ship) and \
                        self._board[i][j].get_abbr() != self._gboard[i][j]:
                    return False

        return True


def test_board():
    b = Board()
    # ship = Ship("Carrier")
    # b.add_ship(ship)

    b.generate_new_game()
    b.display_board(guess_mode=False)
    b.guess(1, 1)
    b.display_board(guess_mode=True)
    b.power_guess(2, 2)
    b.display_board(guess_mode=True)

    print(b.check_win())


def validate_opts(user_input):
    if len(user_input) == 0:
        print("Presence check failed. Please enter something")
        return False
    if not user_input.isdigit():
        print("Type check failed. Please make sure to enter a digit.")
        return False
    if int(user_input) < 1 or int(user_input) > 5:
        print("Range check failed. Please make to enter a valid from 1 to 5.")
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
1) Normal Guess
2) Power Guess
3) Show Answer
4) Restart Game
5) Exit
"""
    print(options)


def menu():
    b = Board()
    b.generate_new_game()

    done = False
    while not done:
        display_options()
        user_input = int(get_user_input("Your Option: "))
        if user_input == 1:
            guess_done = False
            while not guess_done:
                row_col = input("Please enter (row, col) to guess: ")
                row, col = row_col.split(",")
                row = int(row.strip())
                col = int(col.strip())
                guess_done = b.guess(row, col)

                if not guess_done:
                    print("This position has been guessed before.")

            b.display_board(guess_mode=True)

            # check win
            if b.check_win():
                print("You have won!")
                b.display_board(guess_mode=False)
        elif user_input == 2:
            guess_done = False
            while not guess_done:
                row_col = input("Please enter (row, col) to guess: ")
                row, col = row_col.split(",")
                row = int(row.strip())
                col = int(col.strip())
                guess_done = b.power_guess(row, col)

                if not guess_done:
                    print("This position has been guessed before.")

            b.display_board(guess_mode=True)

            # check win
            if b.check_win():
                print("You have won!")
                b.display_board(guess_mode=False)
        elif user_input == 3:
            b.display_board(guess_mode=False)
        elif user_input == 4:
            b.generate_new_game()
        elif user_input == 5:
            done = True
            print("Thank you.")


menu()