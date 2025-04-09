# use 3 rows to print the current arrangement of the towers
# use numbers to represent the disks, such as 3, 2, 1

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def __str__(self):
        return str(self.items)


class TowerOfHanoi:
    def __init__(self, n):
        # init n disks
        self._n = n
        self._step = 1
        self.reset_towers()
        self._past_moves = Stack()
        self._undone_moves = Stack()

    def get_n(self):
        return self._n

    def reset_step(self):
        self._step = 1

    def get_tower(self, tower):
        return self._towers[tower]

    def get_step(self):
        return self._step

    def reset_towers(self):
        # init 3 towers
        self._towers = {"A": Stack(), "B": Stack(), "C": Stack()}
        for n in range(self._n, 0, -1):
            self._towers["A"].push(n)

    def __str__(self):
        result = ""
        result += f"Tower A: {self._towers['A']}\n"
        result += f"Tower B: {self._towers['B']}\n"
        result += f"Tower C: {self._towers['C']}\n"
        return result

    def __repr__(self):
        result = f"TowerOfHanoi({self._n})\n"
        result += f"Step: {self._step}\n"
        result += f"Past moves: {repr(self._past_moves)}\n"
        result += f"Undone moves: {repr(self._undone_moves)}\n"
        result += f"Towers:\n"
        result += f"Tower A: {self._towers['A']}\n"
        result += f"Tower B: {self._towers['B']}\n"
        result += f"Tower C: {self._towers['C']}\n"
        return result

    def check_win(self):
        return self._towers["C"].size() == self._n

    def move_disk(self, src, dst, increment_step=1):
        src_tower = self.get_tower(src)
        dst_tower = self.get_tower(dst)

        # check if the move is valid
        # 1. source tower must not be empty
        if src_tower.is_empty():
            print("Invalid move: source tower is empty")
            return
        # 2. disk from source tower must be smaller than disk from dest tower
        if dst_tower.size() > 0 and \
                src_tower.peek() > dst_tower.peek():
            print(
                "Invalid move: disk from source \
                    is larger than top disk in dest tower")
            return

        # move disk from source to dest
        dst_tower.push(src_tower.pop())

        # print step and movement after successful move
        print("Step", self._step)
        print("Moving disk from", src, "to", dst)

        # print new arrangement of the towers
        print(self)

        # check if the game is won
        if self.check_win():
            print("You win!")
            print("Total steps taken:", self._step)
            print(
                f"Optimal steps expected (2^{self._n} - 1): {(2 ** self._n - 1)}\n")
            if self._step == 2 ** self._n - 1:
                print("You have completed the game in the optimal number of steps!")

        # increment step
        self._step += increment_step
        if increment_step == 1:
            self._past_moves.push((src, dst))
        else:
            self._undone_moves.push((dst, src))

    def undo_move(self):
        if self._past_moves.is_empty():
            print("No moves to undo")
            return

        src, dst = self._past_moves.pop()
        self.move_disk(dst, src, increment_step=-1)

    def redo_move(self):
        if self._undone_moves.is_empty():
            print("No moves to redo")
            return

        src, dst = self._undone_moves.pop()
        self.move_disk(src, dst, increment_step=1)

    def solve(self):
        def toh_solver(n, src, dst, aux):
            # base case: when no disk left, do nothing

            # if more than 0 disks left
            if n > 0:
                # move n-1 disks from source to aux
                toh_solver(n-1, src, aux, dst)

                # base case
                # move the last disk from source to dest
                self.move_disk(src, dst)

                # move n-1 disks from aux to dest
                toh_solver(n-1, aux, dst, src)

        # reset towers
        print("Solving for", self._n, "disks")
        self.reset_step()
        self.reset_towers()
        print("Starting arrangement:")
        print(self)

        # start solving
        toh_solver(self._n, "A", "C", "B")


def test_game():
    game = TowerOfHanoi(3)
    game.solve()


# test_game()


def print_menu():
    print("""
Please choose one of the following options:
1. Start/Reset a new game
2. Move a disk
3. Undo move
4. Redo move
5. Auto-solve game
6. Quit
""")


def menu():
    done = False

    # init with a new game
    print("Welcome to Tower of Hanoi!")
    print("Starting a new game...")
    n = int(input("How many disks? "))
    game = TowerOfHanoi(n)

    print("starting a new game with {n} disks:")
    print(game)

    while not done:
        print_menu()
        choice = input("Your choice: ")

        if choice == "1":
            n = int(input("How many disks? "))
            game = TowerOfHanoi(n)

            print("starting a new game with {n} disks:")
            print(game)
        elif choice == "2":
            source = input("Source tower: ")
            dest = input("Destination tower: ")
            game.move_disk(source, dest)
        elif choice == "3":
            game.undo_move()
            # print(repr(game))
        elif choice == "4":
            game.redo_move()
            # print(repr(game))
        elif choice == "5":
            game.solve()
        elif choice == "6":
            done = True
        else:
            print("Invalid choice. Please try again.")


menu()
