import numpy as np


def displayPathtoPrincess(n, grid):
    pos = list(zip(*np.where(grid == 'm')))
    x = pos[0][0]
    y = pos[0][1]
    if not isRescued(n, grid, x, y):


def move(x, y):


def isSafe(n, grid, x, y):
    if x >= 0 and y >= 0 and x < n and y < n:
        return True
    return False


def isRescued(n, grid, x, y):
    if grid[x][y] == 'p':
        return True


n = int(input())
grid = []
for i in range(n):
    grid.append([*input().strip()])
grid = np.array(grid)
print(grid)
displayPathtoPrincess(n, grid)
