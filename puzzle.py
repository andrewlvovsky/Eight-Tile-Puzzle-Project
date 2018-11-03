from random import *

# ============ Puzzle Class ============ #

# class Puzzle:


# ============ Helper Functions ============ #


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


def run_interface():
    print("Welcome to Andrew Lvovsky's Eight-Puzzle Solver!")
    response = ""

    while response != "1" and response != "2":
        print("Type '1' to use a default puzzle, or '2' to enter your own puzzle")
        response = input()

        if response == "1":
            print("Using a default puzzle...")
            # Take a saved puzzle from an array and solve it
        elif response == "2":
            print("Enter your puzzle, use a zero to represent the blank.")
            first_row = input("Enter the first row, using a space between numbers:")
            first_row = [int(s) for s in first_row.split() if s.isdigit()]
            second_row = input("Enter the second row, using a space between numbers:")
            second_row = [int(s) for s in second_row.split() if s.isdigit()]
            third_row = input("Enter the third row, using a space between numbers:")
            third_row = [int(s) for s in third_row.split() if s.isdigit()]

            puzzle_matrix = [first_row, second_row, third_row]
            print(puzzle_matrix)
        else:
            print("'" + response + "' is not a valid response.")


# ============ Main ============ #


# current_matrix = []
# n = 3
#
# init_random_puzzle(current_matrix, n)

run_interface()
