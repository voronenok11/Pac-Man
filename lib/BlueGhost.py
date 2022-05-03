class BlueGhost:
    position = [14, 11]
    orientation = [0, 0]
    tactic = "not activated"
    def ChangeTactic(self, board, pacman):
        pass
    def Move(self, board, pacman):
        self.ChangeTactic(board, pacman)
        self.position[0] += self.orientation[0]
        self.position[1] += self.orientation[1]
        if self.position == pacman.position:
            return True
        return False
