import pygame
import sys
from lib.Board import Board
from lib.RedGhost import RedGhost
from lib.BlueGhost import BlueGhost
from lib.PinkGhost import PinkGhost
from lib.YellowGhost import YellowGhost
from lib.Pacman import Pacman
def DrawBoard():
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 1600, 1300), 0)
    for i in range(board.column):
        for j in range(board.row):
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(i * 40, j * 40, 40, 40), 1)
    for i in range(board.column):
        for j in range(board.row):
            if board.board[j][i] == '#':
                pygame.draw.rect(screen, (0, 0, 139), pygame.Rect(i * 40, j * 40, 40, 40), 0)
            if board.board[j][i] == '*':
                pygame.draw.circle(screen, (255, 165, 0), (i * 40 + 20, j * 40 + 20), 5, 0)
    pygame.draw.circle(screen, (255, 0, 0), (red_ghost.position[1] * 40 + 20, red_ghost.position[0] * 40 + 20), 10, 0)
    pygame.draw.circle(screen, (0, 191, 255), (blue_ghost.position[1] * 40 + 20, blue_ghost.position[0] * 40 + 20), 10, 0)
    pygame.draw.circle(screen, (255, 160, 122), (yellow_ghost.position[1] * 40 + 20, yellow_ghost.position[0] * 40 + 20), 10, 0)
    pygame.draw.circle(screen, (255, 105, 180), (pink_ghost.position[1] * 40 + 20, pink_ghost.position[0] * 40 + 20), 10, 0)
    pygame.draw.circle(screen, (255, 255, 0), (pacman.position[1] * 40 + 20, pacman.position[0] * 40 + 20), 10, 0)
    now_points = ""
    x = pacman.points
    for i in range(6):
        now_points = chr(ord('0') + x % 10) + now_points
        x //= 10
    screen.blit(my_font.render("Cчёт: " + now_points, True, (255, 255, 255)), (1200, 200))
    now_level = ""
    x = board.level
    while x > 0:
        now_level = chr(ord('0') + x % 10) + now_level
        x //= 10
    screen.blit(my_font.render("Уровень: " + now_level, True, (255, 255, 255)), (1200, 280))
def Draw_end_game():
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 1600, 1300), 0)
    now_points = ""
    x = pacman.points
    while x > 0:
        now_points = chr(ord('0') + x % 10) + now_points
        x //= 10
    screen.blit(my_font.render("Вы проиграли", True, (255, 255, 255)), (650, 550))
    screen.blit(my_font.render("Ваш счёт: " + now_points, True, (255, 255, 255)), (650, 600))
def NewLevel():
    board.Fill()
    board.level += 1
    board.number_of_dots = 0
    blue_ghost.time_of_dead = 0
    yellow_ghost.time_of_dead = 0
    for i in range(board.row):
        for j in range(board.column):
            if board.board[i][j] == '*':
                board.number_of_dots += 1
    pacman.number_of_eaten_dots = 0
    pacman.position = [23, 13]
    pacman.orientation = [0, 0]
    red_ghost.position = [11, 13]
    red_ghost.orientation = [0, 0]
    blue_ghost.position = [14, 11]
    blue_ghost.orientation = [0, 0]
    pink_ghost.position = [14, 13]
    pink_ghost.orientation = [0, 0]
    yellow_ghost.position = [14, 15]
    yellow_ghost.orientation = [0, 0]
def ResetLevel():
    pacman.health -= 1
    blue_ghost.time_of_dead = 0
    yellow_ghost.time_of_dead = 0
    pacman.position = [23, 13]
    pacman.orientation = [0, 0]
    red_ghost.position = [11, 13]
    red_ghost.orientation = [0, 0]
    blue_ghost.position = [14, 11]
    blue_ghost.orientation = [0, 0]
    pink_ghost.position = [14, 13]
    pink_ghost.orientation = [0, 0]
    yellow_ghost.position = [14, 15]
    yellow_ghost.orientation = [0, 0]
board = Board()
red_ghost = RedGhost()
blue_ghost = BlueGhost()
pink_ghost = PinkGhost()
yellow_ghost = YellowGhost()
pacman = Pacman()
NewLevel()
pygame.init()
screen = pygame.display.set_mode((1600, 1300))
my_font = pygame.font.SysFont('arial', 60)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            prev_orientation = pacman.orientation
            change_orientation = False
            if event.key == pygame.K_LEFT and pacman.orientation != [0, 1]:
                pacman.orientation = [0, -1]
                change_orientation = True
            elif event.key == pygame.K_RIGHT and pacman.orientation != [0, -1]:
                pacman.orientation = [0, 1]
                change_orientation = True
            elif event.key == pygame.K_UP and pacman.orientation != [1, 0]:
                pacman.orientation = [-1, 0]
                change_orientation = True
            elif event.key == pygame.K_DOWN and pacman.orientation != [-1, 0]:
                pacman.orientation = [1, 0]
                change_orientation = True
            if change_orientation and (board.board[pacman.position[0] + pacman.orientation[0]][pacman.position[1] + pacman.orientation[1]] == '#' or [pacman.position[0] + pacman.orientation[0], pacman.position[1] + pacman.orientation[1]] == [12, 13] or [pacman.position[0] + pacman.orientation[0], pacman.position[1] + pacman.orientation[1]] == [12, 14]):

                pacman.orientation = prev_orientation
    if pacman.health != 0:
        was_caught = False
        if pacman.Move(board, red_ghost, blue_ghost, pink_ghost, yellow_ghost):
            was_caught = True
        if red_ghost.Move(board, pacman):
            was_caught = True
        if blue_ghost.Move(board, pacman, red_ghost):
            was_caught = True
        if pink_ghost.Move(board, pacman):
            was_caught = True
        if yellow_ghost.Move(board, pacman):
            was_caught = True
        DrawBoard()
        if was_caught:
            ResetLevel()
        if pacman.health != 0:
            if pacman.number_of_eaten_dots == board.number_of_dots:
                NewLevel()
            board.time_of_game += 1
            blue_ghost.time_of_dead += 1
            yellow_ghost.time_of_dead += 1
    else:
        Draw_end_game()
    pygame.display.flip()
    clock.tick(3)
