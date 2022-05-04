class Pacman:
    points = 0
    position = [23, 13]
    orientation = [0, 0]
    number_of_eaten_dots = 0
    health = 3
    def Move(self, board, red_ghost, blue_ghost, pink_ghost, yellow_ghost):
        self.position[0] += self.orientation[0]
        self.position[1] += self.orientation[1]
        if self.position == [14, -1]:
            self.position[1] = board.column - 1
        if self.position == [14, board.column]:
            self.position[1] = 0
        if board.board[self.position[0]][self.position[1]] == '#':
            self.position[0] -= self.orientation[0]
            self.position[1] -= self.orientation[1]
        if board.board[self.position[0]][self.position[1]] == '*':
            self.points += 100 * board.level
            self.number_of_eaten_dots += 1
            board.board[self.position[0]][self.position[1]] = '.'
        if self.position == red_ghost.position or self.position == blue_ghost.position or self.position == pink_ghost.position or self.position == yellow_ghost.position:
            return True
        return False

