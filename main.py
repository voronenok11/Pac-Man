from Board import Board
board = Board()
board.new_level()
for i in range(board.row):
    for j in range(board.column):
        print(board.board[i][j], end='')
    print()
