class BlueGhost:
    position = [14, 11]
    orientation = [0, 0]
    time_of_dead = 0
    def ChangeTactic(self, board, pacman, red_ghost):
        if self.time_of_dead < 50:
            return
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
        if pacman.number_of_eaten_dots < 70:
            px = board.row - 2
            py = board.column - 2
            while dist[px][py] > 1:
                px, py = px - prev[px][py][0], py - prev[px][py][1]
            if dist[px][py] == 0:
                for delta in neigh:
                    if board.board[self.position[0] + delta[0]][self.position[1] + delta[1]] != '#' and delta != [-self.orientation[0], -self.orientation[1]]:
                        self.orientation = delta
                        break
            elif prev[px][py] == [-self.orientation[0], -self.orientation[1]]:
                for delta in neigh:
                    if board.board[self.position[0] + delta[0]][self.position[1] + delta[1]] != '#' and delta != [-self.orientation[0], -self.orientation[1]]:
                        self.orientation = delta
                        break
            else:
                self.orientation = prev[px][py]
        else:
            vx = pacman.position[0] + 2 * pacman.orientation[0] - red_ghost.position[0]
            vy = pacman.position[1] + 2 * pacman.orientation[1] - red_ghost.position[1]
            px = red_ghost.position[0] + 2 * vx
            py = red_ghost.position[1] + 2 * vy
            while px < 0 or py < 0 or px >= board.row or py >= board.column or board.board[px][py] == '#':
                px -= vx
                py -= vy
            if dist[px][py] == inf:
                for delta in neigh:
                    if board.board[self.position[0] + delta[0]][self.position[1] + delta[1]] != '#' and delta != [-self.orientation[0], -self.orientation[1]]:
                        self.orientation = delta
                        break

            elif dist[px][py] == 0:
                for delta in neigh:
                    if board.board[self.position[0] + delta[0]][self.position[1] + delta[1]] != '#' and delta != [-self.orientation[0], -self.orientation[1]]:
                        self.orientation = delta
                        break
            else:
                while dist[px][py] > 1:
                    px, py = px - prev[px][py][0], py - prev[px][py][1]
                if prev[px][py] == [-self.orientation[0], -self.orientation[1]]:
                    for delta in neigh:
                        if board.board[self.position[0] + delta[0]][self.position[1] + delta[1]] != '#' and delta != [-self.orientation[0], -self.orientation[1]]:
                            self.orientation = delta
                            break
                else:
                    self.orientation = prev[px][py]



            
        
    def Move(self, board, pacman, red_ghost):
        self.ChangeTactic(board, pacman, red_ghost)
        self.position[0] += self.orientation[0]
        self.position[1] += self.orientation[1]
        if self.position == pacman.position:
            return True
        return False
