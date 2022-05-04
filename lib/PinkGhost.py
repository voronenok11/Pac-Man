class PinkGhost:
    position = [14, 13]
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
                if [nvx, nvy] == [14, 5] or [nvx, nvy] == [14, 22]:
                    continue
                if dist[nvx][nvy] == inf:
                    dist[nvx][nvy] = dist[vx][vy] + 1
                    prev[nvx][nvy] = delta
                    que.append([nvx, nvy])
        if dist[pacman.position[0]][pacman.position[1]] == inf:
            for delta in neigh:
                if board.board[self.position[0] + delta[0]][self.position[1] + delta[1]] != '#' and delta != [-self.orientation[0], -self.orientation[1]]:
                    self.orientation = delta
                    break
        else:
            px = pacman.position[0] + pacman.orientation[0] * 4
            py = pacman.position[1] + pacman.orientation[1] * 4
            while px < 0 or py < 0 or px >= board.row or py >= board.column or board.board[px][py] == '#':
                px -= pacman.orientation[0]
                py -= pacman.orientation[1]
            while dist[px][py] > 1 and dist[px][py] != inf:
                px, py = px - prev[px][py][0], py - prev[px][py][1]
            if dist[px][py] == 0:
                px = pacman.position[0]
                py = pacman.position[1]
                while dist[px][py] > 1:
                    px, py = px - prev[px][py][0], py - prev[px][py][1]
                if prev[px][py] == [-self.orientation[0], -self.orientation[1]]:
                    for delta in neigh:
                        if board.board[self.position[0] + delta[0]][self.position[1] + delta[1]] != '#' and delta != [-self.orientation[0], -self.orientation[1]]:
                            self.orientation = delta
                            break
                else:
                    self.orientation = prev[px][py]
            elif dist[px][py] == 1:
                if prev[px][py] == [-self.orientation[0], -self.orientation[1]]:
                    for delta in neigh:
                        if board.board[self.position[0] + delta[0]][self.position[1] + delta[1]] != '#' and delta != [-self.orientation[0], -self.orientation[1]]:
                            self.orientation = delta
                            break
                else:
                    self.orientation = prev[px][py]
            else:
                for delta in neigh:
                    if board.board[self.position[0] + delta[0]][self.position[1] + delta[1]] != '#' and delta != [-self.orientation[0], -self.orientation[1]]:
                        self.orientation = delta
                        break

    def Move(self, board, pacman):
        self.ChangeTactic(board, pacman)
        self.position[0] += self.orientation[0]
        self.position[1] += self.orientation[1]
        if self.position == pacman.position:
            return True
        return False
