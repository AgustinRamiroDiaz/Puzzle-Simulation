# %%
from random import randint
LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3

BORDER = 0


def createPuzzle(widthLength, heightLength):
    width = range(widthLength)
    height = range(heightLength)
    # Each piece is [left, up, right, down]
    puzzle = [[[BORDER] * 4 for column in width] for row in height]

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


def rotatePieceClockwise(piece, numberOfRotations):
    rotations = numberOfRotations % len(piece)
    return piece[rotations:] + piece[:rotations]


# %%
puzzle = createPuzzle(5, 5)
print(puzzleToString(puzzle))


listOfPieces = [tuple(rotatePieceClockwise(piece, randint(0, 15)))
                for row in puzzle for piece in row]


print(listOfPieces)
# %%


def solvePuzzle(pieces):
    # solution is in the form of {piece: (neighbourPiece, pieceSide, neighbourPieceSide)} for all piece pairs
    solution = {}

    unmachedSidesToPiecesAndSide = {}

    for piece in pieces:
        unmachedSides = []
        for side, position in zip(piece, (LEFT, UP, RIGHT, DOWN)):
            if side == BORDER:
                continue

            if side in unmachedSidesToPiecesAndSide:
                matchedPiece, matchedPosition = unmachedSidesToPiecesAndSide[side]
                del unmachedSidesToPiecesAndSide[side]
                solution[piece] = (matchedPiece, position, matchedPosition)
                solution[matchedPiece] = (piece, matchedPosition, position)

            else:
                unmachedSides.append((side, position))

        for unmatchedSide, position in unmachedSides:
            unmachedSidesToPiecesAndSide[unmatchedSide] = (piece, position)

    assert(not unmachedSidesToPiecesAndSide)
    assert(all([piece[position] == matchedPiece[matchedPosition] for piece, (matchedPiece, position, matchedPosition) in solution.items()]))

    return solution


# %%
solution = solvePuzzle(listOfPieces)
print(solution)
# TODO llevar frutillas

# %%
class Polyomino:
    def __init__(self, tile) -> None:
        self.tilePosition = {(0, 0): tile}
        self.tileOutline = {(-1, 0), (0, 1), (1, 0), (0, -1)}

    
# %%
