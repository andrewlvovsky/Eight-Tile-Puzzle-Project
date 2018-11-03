from random import *

# ============ Helper Functions ============ #


def init_random_puzzle(current_matrix, n):
    used_numbers = []

    while len(current_matrix) < n:
        current_row = []
        while len(current_row) < n:
            rand_num = randint(0, n * n - 1)
            if rand_num not in used_numbers:
                current_row.append(rand_num)
                used_numbers.append(rand_num)
        current_matrix.append(current_row)

    print(current_matrix)

# ============ Main ============ #


current_matrix = []
n = 3

init_random_puzzle(current_matrix, n)


