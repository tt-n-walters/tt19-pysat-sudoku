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
            n = int(string[j])
            row.append(n)
        puzzle.append(row)
    return puzzle


# Visualisation of the puzzle
def visualise(puzzle):
    output = "+------+-----+------+\n"
    for row in puzzle:
        output += "|"
        for n in row:
            output += " "
            if n > 0:
                output += str(n)
            else:
                output += " "
        output += " |\n"
    output += "+------+-----+------+"
    print(output)



def check_position(puzzle, x, y, n):
    row = puzzle[y]
    column = [row[x] for row in puzzle]
    i = (x // 3) * 3
    j = (y // 3) * 3
    section = [z for row in puzzle[j : j+3] for z in row[i : i+3]]
    
    return not n in row and not n in column and not n in section
    return not n in row + column + section



if __name__ == "__main__":
    puzzles = read_puzzles()
    puzzle = convert_puzzle(puzzles[42])
    visualise(puzzle)

    print(check_position(puzzle, 2, 3, 6))
