# heuristics
# backtracking


# Read the file of puzzles
def read_puzzles():
    with open("puzzles") as file:
        content = file.read().splitlines()
        return content


# Parse/convert a puzzle string into a useable data-structure
def convert_puzzle(string):
    puzzle = []
    for i in range(9):
        row = []
        for j in range(i * 9, (i + 1) * 9):
            n = string[j]
            row.append(n)
        puzzle.append(row)
    return puzzle


# Visualisation of the puzzle




if __name__ == "__main__":
    puzzles = read_puzzles()
    puzzle = puzzles[42]

    print(puzzle)
    print(convert_puzzle(puzzle))