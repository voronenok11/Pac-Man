# Pac-Man
Game Pac-Man
Реализована игра: Pac-Man. В папке UML хранятся UML-диаграммы.
Ghosts.pdf - диаграмма клаccов каждого из призраков,
Board.pdf - диаграмма класса игрового поля,
Pacman.pdf - диаграмма класса Pac-Man'a.
В папке lib реализованы соответствующие классы сущности игры
В реализации паттерны не используются, так как для привидений создавать один общий класс, от которого отнаследуется каждый из призраков, не имеет смысла, потому что в реализации функция для pacman-a будет передаваться отдельно каждый из призраков и классы призраков, кроме методов движения других не будут иметь. Паттерн же наблюдатель не используется, так как это привёдет к награмождению кода, а лгече просто передавать, как аргументы объект класса.

Чтобы запустить игру, нужно скачать графическую библиотеку pygame с помощью pip install pygame.
Чтобы запустить саму игру, нужно написать python3 main.py
