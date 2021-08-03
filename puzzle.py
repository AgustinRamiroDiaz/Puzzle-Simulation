# %%
LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3


def createPuzzle(widthLength, heightLength):
    width = range(widthLength)
    height = range(heightLength)
    # Each piece is [left, up, right, down]
    puzzle = [[[0, 0, 0, 0] for column in width] for row in height]

    cutValue = 32
    for row in height[:-1]:
        for column in width[:-1]:
            puzzle[row][column][RIGHT] = chr(cutValue)
            puzzle[row][column + 1][LEFT] = chr(cutValue)
            cutValue += 1

            puzzle[row][column][DOWN] = chr(cutValue)
            puzzle[row + 1][column][UP] = chr(cutValue)
            cutValue += 1

    # Last row
    for column in width[:-1]:
        puzzle[-1][column][RIGHT] = chr(cutValue)
        puzzle[-1][column + 1][LEFT] = chr(cutValue)
        cutValue += 1

    # Last column
    for row in height[:-1]:
        puzzle[row][-1][DOWN] = chr(cutValue)
        puzzle[row + 1][-1][UP] = chr(cutValue)
        cutValue += 1

    return puzzle


def puzzleToString(puzzle):
    rowDivisor = '-' * ((len(puzzle[0]) * 6) + 1)
    puzzleString = rowDivisor + '\n'

    for row in puzzle:
        topRow = '|'
        middleRow = '|'
        bottomRow = '|'
        for value in row:
            topRow += f'  {value[UP]}  |'
            middleRow += f'{value[LEFT]}   {value[RIGHT]}|'
            bottomRow += f'  {value[DOWN]}  |'

        puzzleString += topRow + '\n'
        puzzleString += middleRow + '\n'
        puzzleString += bottomRow + '\n'
        puzzleString += rowDivisor + '\n'

    return puzzleString

# %%


puzzle = createPuzzle(5, 5)
print(puzzleToString(puzzle))

listOfPieces = [piece for row in puzzle for piece in row]

# %%
