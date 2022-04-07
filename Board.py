class Board:
    board = []
    level = 0
    number_of_dots = 0
    time_of_game = 0
    row = 31
    column = 28
    def fill(self):
        self.board = []
        for i in range(self.row):
            self.board.append([])
            for j in range(self.column):
                self.board[i].append('.')
        #row 0
        for i in range(self.column):
            self.board[0][i] = '#'
        #row 1
        self.board[1][0] = '#'
        for i in range(1, 13):
            self.board[1][i] = '*'
        self.board[1][13] = '#'
        self.board[1][14] = '#'
        for i in range(15, self.column - 1):
            self.board[1][i] = '*'
        self.board[1][-1] = '#'
        #row 2-4
        for i in range(2, 5):
            for j in range(self.column):
                self.board[i][j] = '#'
            self.board[i][1] = '*'
            self.board[i][6] = '*'
            self.board[i][12] = '*'
            self.board[i][15] = '*'
            self.board[i][21] = '*'
            self.board[i][26] = '*'
        #row 5
        self.board[5][0] = '#'
        self.board[5][-1] = '#'
        for i in range(1, self.column - 1):
            self.board[5][i] = '*'
        #row 6-7
        for j in range(6, 8):
            for i in range(self.column):
                self.board[j][i] = '#'
            self.board[j][1] = '*'
            self.board[j][6] = '*'
            self.board[j][9] = '*'
            self.board[j][18] = '*'
            self.board[j][21] = '*'
            self.board[j][-2] = '*'
        #row 8
        for i in range(self.column):
            self.board[8][i] = '*'
        self.board[8][0] = '#'
        self.board[8][7] = '#'
        self.board[8][8] = '#'
        self.board[8][13] = '#'
        self.board[8][14] = '#'
        self.board[8][19] = '#'
        self.board[8][20] = '#'
        self.board[8][-1] = '#'
        #row 9-10
        for i in range(9, 11):
            for j in range(self.column):
                self.board[i][j] = '#'
            self.board[i][6] = '*'
            self.board[i][12] = '.'
            self.board[i][15] = '.'
            self.board[i][21] = '.'
        #row 11 and 12 and 13
        for j in range(11, 14):
            for i in range(6):
                self.board[j][i] = '#'
            self.board[j][6] = '*'
            self.board[j][7] = '#'
            self.board[j][8] = '#'
            self.board[j][-9] = '#'
            self.board[j][-8] = '#'
            self.board[j][-7] = '*'
            for i in range(-6, 0):
                self.board[j][i] = '#'
        for i in range(10, 18):
            self.board[12][i] = '#'
        self.board[12][13] = '$'
        self.board[12][14] = '$'
        self.board[13][10] = '#'
        self.board[13][17] = '#'
        #row 14
        self.board[14][6] = '*'
        self.board[14][10] = '#'
        self.board[14][17] = '#'
        self.board[14][-7] = '*'
        #row 15 and 16 and 17
        for i in range(self.column):
            self.board[15][i] = self.board[13][i]
            self.board[16][i] = self.board[12][i]
            self.board[17][i] = self.board[11][i]
        self.board[16][13] = '#'
        self.board[16][14] = '#'
        #row 18 and 19
        for i in range(self.column):
            self.board[18][i] = self.board[17][i]
            self.board[19][i] = self.board[17][i]
        for i in range(10, 18):
            self.board[18][i] = '#'
            self.board[19][i] = '#'
        #row 20
        for i in range(self.column):
            self.board[20][i] = '*'
        self.board[20][0] = '#'
        self.board[20][13] = '#'
        self.board[20][14] = '#'
        self.board[20][-1] = '#'
        #row 21-22
        for i in range(21, 23):
            for j in range(self.column):
                self.board[i][j] = '#'
            self.board[i][1] = '*'
            self.board[i][6] = '*'
            self.board[i][12] = '*'
            self.board[i][15] = '*'
            self.board[i][21] = '*'
            self.board[i][-2] = '*'
        #row 23
        for i in range(self.column):
            self.board[23][i] = '*'
        self.board[23][0] = '#'
        self.board[23][4] = '#'
        self.board[23][5] = '#'
        self.board[23][-6] = '#'
        self.board[23][-5] = '#'
        self.board[23][-1] = '#'
        #row 24 and 25
        for i in range(24, 26):
            for j in range(self.column):
                self.board[i][j] = '#'
            self.board[i][3] = '*'
            self.board[i][6] = '*'
            self.board[i][9] = '*'
            self.board[i][18] = '*'
            self.board[i][21] = '*'
            self.board[i][24] = '*'
        #row 26
        for i in range(self.column):
            self.board[26][i] = '*'
        self.board[26][0] = '#'
        self.board[26][7] = '#'
        self.board[26][8] = '#'
        self.board[26][13] = '#'
        self.board[26][14] = '#'
        self.board[26][19] = '#'
        self.board[26][20] = '#'
        self.board[26][21] = '#'
        self.board[26][-1] = '#'
        #row 27-28
        for i in range(27, 29):
            for j in range(self.column):
                self.board[i][j] = '#'
            self.board[i][1] = '*'
            self.board[i][12] = '*'
            self.board[i][15] = '*'
            self.board[i][-2] = '*'
        #row 29
        for i in range(self.column):
            self.board[29][i] = '*'
        self.board[29][0] = '#'
        self.board[29][-1] = '#'
        #row 30
        for i in range(self.column):
            self.board[30][i] = '#'
    def new_level(self):
        self.fill()
        self.level += 1
        self.number_of_dots = 0
        for i in range(self.row):
            for j in range(self.column):
                if self.board[i][j] == '*':
                    self.number_of_dots += 1
