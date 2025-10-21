# Function to check if two queens threaten each other or not
def isSafe(mat, r, c):
    # return false if two queens share the same column
    for i in range(r):
        if mat[i][c] == 'Q':
            return False

    # return false if two queens share the same `\` diagonal
    i, j = r, c
    while i >= 0 and j >= 0:
        if mat[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # return false if two queens share the same `/` diagonal
    i, j = r, c
    while i >= 0 and j < len(mat):
        if mat[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def printSolution(mat):
    for r in mat:
        print(' '.join(r))
    print()


def nQueen(mat, r):
    # if `N` queens are placed successfully, print the solution
    if r == len(mat):
        printSolution(mat)
        return

    # place queen at every square in the current row `r`
    for i in range(len(mat)):
        # if no two queens threaten each other
        if isSafe(mat, r, i):
            mat[r][i] = 'Q'  # place queen
            nQueen(mat, r + 1)  # recur
            mat[r][i] = '–'  # backtrack


if __name__ == '__main__':
    N = 4  # `N × N` chessboard
    mat = [['–' for x in range(N)] for y in range(N)]
    nQueen(mat, 0)
