class RedGhost:
    position = [11, 13]
    orientation = [0, 0]
    def ChangeTactic(self, board, pacman):
        dist = []
        prev = []
        neigh = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        inf = 10000
        for i in range(board.row):
            dist.append([])
            prev.append([])
            for j in range(board.column):
                dist[i].append(inf)
                prev[i].append([-1, -1])
        que = []
        que.append(self.position)
        dist[self.position[0]][self.position[1]] = 0
        while len(que) > 0:
            vx = que[0][0]
            vy = que[0][1]
            que = que[1:]
            for delta in neigh:
                nvx = vx + delta[0]
                nvy = vy + delta[1]
                if not (0 <= nvx <= board.row - 1 and 0 <= nvy <= board.column - 1):
                    continue
                if board.board[nvx][nvy] == '#':
                    continue
                if dist[nvx][nvy] == inf:
                    dist[nvx][nvy] = dist[vx][vy] + 1
                    prev[nvx][nvy] = delta
                    que.append([nvx, nvy])
        px = pacman.position[0]
        py = pacman.position[1]
        while dist[px][py] > 1:
            px, py = px - prev[px][py][0], py - prev[px][py][1]
        self.orientation = prev[px][py]
    def Move(self, board, pacman):
        self.ChangeTactic(board, pacman)
        self.position[0] += self.orientation[0]
        self.position[1] += self.orientation[1]
        if self.position == pacman.position:
            return True
        return False
            
