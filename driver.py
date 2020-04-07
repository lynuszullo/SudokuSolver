import math

def printBoard(board):
    for i in range(0,9):
        for j in range(0,9):
            print board[i][j],
        print("\n")


def isValidinput(number, rowNum, colNum, board):
    # Checks all the rows/cols
    for i in range(0, 9):
        if(board[rowNum][i] == number):
            return False
        if (board[i][colNum] == number):
            return False

    # Checks the 3x3 block
    topLeftRow = int(math.floor(rowNum / 3)) * 3
    topLeftCol = int(math.floor(colNum / 3)) * 3
    for i in range(topLeftRow, topLeftRow + 3):
        for j in range(topLeftCol, topLeftCol + 3):
            # print(str(i) + "," + str(j))
            if board[i][j] == number:
                return False

    return True

def locationIsEmpty(board):
    for row in range(0,9):
        for col in range(0,9):
            if board[row][col] == 0:
                return row, col
    # There are no empty spaces on the board
    return False

def solvePuzzle(board):

    # No empty spaces on board == we win
    if not locationIsEmpty(board):
        printBoard(board)
        return True
    else:
        row, col = locationIsEmpty(board)

    for val in range(1,10):
        if isValidinput(val, row, col, board):
            board[row][col] = val
            if solvePuzzle(board):
                return True
            board[row][col] = 0

    return False

# 0,1,2 --> 0
# 3,4,5 --> 3
# 6,7,8 --> 6
# floor(rownum / 3) * 3

if __name__ == "__main__":
    # printBoard()
    # assert(isValidinput(5, 0, 4) == (0, 3))
    # assert(isValidinput(5, 3, 3) == (3, 3))

    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    easy = [[0, 3, 0, 0, 0, 2, 5, 0, 0],
            [4, 2, 8, 0, 0, 0, 0, 0, 0],
            [0, 0, 9, 0, 0, 0, 0, 3, 4],
            [8, 7, 0, 2, 9, 5, 4, 0, 0],
            [0, 6, 5, 4, 0, 3, 9, 2, 0],
            [0, 0, 4, 8, 1, 6, 0, 5, 3],
            [9, 5, 0, 0, 0, 0, 8, 0, 0],
            [0, 0, 0, 0, 0, 0, 6, 1, 5],
            [0, 0, 2, 5, 0, 0, 0, 9, 0]]

    evil = [[0, 0, 0, 1, 5, 0, 0, 7, 9],
             [0, 0, 0, 0, 0, 0, 0, 0, 3],
             [0, 5, 0, 0, 0, 0, 0, 8, 6],
             [3, 7, 0, 0, 0, 4, 1, 0, 0],
             [0, 0, 0, 5, 0, 8, 0, 0, 0],
             [0, 0, 5, 7, 0, 0, 0, 3, 8],
             [2, 8, 0, 0, 0, 0, 0, 4, 0],
             [7, 0, 0, 0, 0, 0, 0, 0, 0],
             [5, 9, 0, 0, 7, 6, 0, 0, 0]]
    try:
        solvePuzzle(evil)
    except:
        print("Cannot solve board")
    # print(random.randint(1,9))
    # assert(not isValidinput(5, 8, 8))