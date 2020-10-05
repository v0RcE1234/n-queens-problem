from itertools import permutations

K = int(input('Input the board size: '))

def printRow(idx):
    row_str = ['@' if i==idx else '-' for i in range(0, K)]
    print('      '.join(row_str))

def printBoard(board):
    for i in board:
        printRow(i)
        print('\n')

is_valid_call_count = 0
def isBoardValid(board):
    global is_valid_call_count
    is_valid_call_count = is_valid_call_count + 1
    if is_valid_call_count % 1000000 == 0:
        print("Checked %d boards." % is_valid_call_count)
    # We are not going to check if two of the queens are in the same column.
    # We are only going to look for diagonal conflicts.
    for row in range(K):
        col = board[row]
        # check if the queens in following rows are in conflict
        for following_row in range(row+1 , K):
            following_col = board[following_row]
            if following_row - row == abs(following_col - col):
                return False
    return True

def findq8solution():
    boards = permutations([i for i in range(K)])
    for board in boards:
        if isBoardValid(board):
            printBoard(board)
            return True
    return False

if findq8solution():
    print('FOUND A VALID SOLUTION. STOPPING.')
else:
    print('DID NOT FIND ANY SOLUTION.  :(')