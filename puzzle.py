from random import *

# ============ Puzzle Class ============ #


class Puzzle:
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def __init__(self, puzzle_matrix, size):
        self.puzzle_matrix = puzzle_matrix
        self.size = size
        self.empty_pos_x, self.empty_pos_y = find_empty_tile(puzzle_matrix)

    def move_up(self):
        if 0 not in self.puzzle_matrix[0]:
            self.swap_tiles(self.empty_pos_x, self.empty_pos_y - 1)
            self.empty_pos_y -= 1

    def move_down(self):
        if 0 not in self.puzzle_matrix[self.size - 1]:
            self.swap_tiles(self.empty_pos_x, self.empty_pos_y + 1)
            self.empty_pos_y += 1

    def move_left(self):
        zero_not_in_leftmost_column = True
        for i in range(self.size):
            if self.puzzle_matrix[i][0] == 0:
                zero_not_in_leftmost_column = False
                break
        if zero_not_in_leftmost_column:
            self.swap_tiles(self.empty_pos_x - 1, self.empty_pos_y)
            self.empty_pos_x -= 1

    def move_right(self):
        zero_not_in_leftmost_column = True
        for i in range(self.size):
            if self.puzzle_matrix[i][self.size - 1] == 0:
                zero_not_in_leftmost_column = False
        if zero_not_in_leftmost_column:
            self.swap_tiles(self.empty_pos_x + 1, self.empty_pos_y)
            self.empty_pos_x += 1

    def swap_tiles(self, x_change, y_change):
        temp = self.puzzle_matrix[self.empty_pos_y][self.empty_pos_x]
        self.puzzle_matrix[self.empty_pos_y][self.empty_pos_x] = self.puzzle_matrix[y_change][x_change]
        self.puzzle_matrix[y_change][x_change] = temp

    def print(self):
        print_matrix(self.puzzle_matrix)


# ============ Helper Functions ============ #


def find_empty_tile(puzzle_matrix):
    for column in range(len(puzzle_matrix)):
        for row in range(len(puzzle_matrix[column])):
            if puzzle_matrix[column][row] == 0:
                return row, column


def init_random_puzzle(puzzle_matrix, size_of_matrix):
    used_numbers = []

    while len(puzzle_matrix) < size_of_matrix:
        current_row = []
        while len(current_row) < size_of_matrix:
            rand_num = randint(0, size_of_matrix^2 - 1)
            if rand_num not in used_numbers:
                current_row.append(rand_num)
                used_numbers.append(rand_num)
        puzzle_matrix.append(current_row)

    print(puzzle_matrix)


def print_matrix(matrix):
    for row in matrix:
        print(' '.join([str(elem) for elem in row]))
    print("")


def run_interface():
    print("Welcome to Andrew Lvovsky's Eight-Puzzle Solver!")
    response = ""
    puzzle_loaded = False

    while response != "1" and response != "2":
        print("Type '1' to use a default puzzle, or '2' to enter your own puzzle")
        response = input()

        if response == "1":
            print("Using a default puzzle...")
            # Take a saved puzzle from an array and solve it
            puzzle_loaded = True

        elif response == "2":
            print("Enter your puzzle, use a zero to represent the blank.")
            first_row = input("Enter the first row, using a space between numbers: ")
            first_row = [int(s) for s in first_row.split() if s.isdigit()]
            second_row = input("Enter the second row, using a space between numbers: ")
            second_row = [int(s) for s in second_row.split() if s.isdigit()]
            third_row = input("Enter the third row, using a space between numbers: ")
            third_row = [int(s) for s in third_row.split() if s.isdigit()]

            puzzle_matrix = [first_row, second_row, third_row]
            puzzle_loaded = True
        else:
            print("'" + response + "' is not a valid response.")

    response = ""

    while response != "1" and response != "2" and response != "3":
        print("Enter your choice of algorithm:")
        print("\t1. Uniform Cost Search")
        print("\t2. A* w/ Misplaced Tile Heuristic")
        print("\t3. A* w/ Manhattan Distance Heuristic\n")
        response = input()

        if response == "1":
            print("Running Uniform Cost Search")
            # run UCS
        elif response == "2":
            print("Running A* w/ Misplaced Tile Heuristic")
            # run A* w/ Misplaced Tile Heuristic
        elif response == "3":
            print("Running A* w/ Manhattan Distance Heuristic")
            # run A* w/ Manhattan Distance Heuristic
        else:
            print("'" + response + "' is not a valid response.")


def puzzle_movement_test():
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    p = Puzzle(goal_state, 3)
    response = ""

    print("Move (u)p, (d)own, (l)eft, or (r)ight")

    while response != "q":
        response = input()
        if response == 'w':
            p.move_up()
        elif response == 's':
            p.move_down()
        elif response == 'a':
            p.move_left()
        elif response == 'd':
            p.move_right()
        p.print()


def uniform_cost_search():
    print("placeholder")

# ============ Main ============ #

# run_interface()
# puzzle_movement_test()


