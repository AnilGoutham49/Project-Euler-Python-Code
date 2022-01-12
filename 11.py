import numpy as np
import pandas as pd

df = pd.read_csv('eleven.csv', sep=',', header=None)
grid = df.to_numpy()

def largest_prod():
    largest_horizontal = np.amax(np.prod(grid[:, 0:4], axis=1))
    largest_vertical = np.amax(np.prod(grid[0:4], axis=0))
    for i in range(1, grid.shape[1]-4):
        temp_horiz = np.amax(np.prod(grid[:, i:i+4], axis=1))
        temp_verti = np.amax(np.prod(grid[i:i+4], axis=0))
        if temp_horiz > largest_horizontal: largest_horizontal = temp_horiz
        if temp_verti > largest_vertical: largest_vertical = temp_verti
    # Diagonals from Left to Right
    l1 = []
    for i in range(-grid.shape[1] + 4, grid.shape[1] - 3):
        l1.append(grid.diagonal(i))
    diagonal_1 = np.prod(l1[0])
    for a in l1:
        for i in range(0, a.size-3):
            temp_diag = np.prod(a[i:i+4])
            if temp_diag > diagonal_1: diagonal_1 = temp_diag
    # Diagonals from Right to Left
    grid_rev = grid[:, ::-1]
    l2 = []
    for i in range(-grid_rev.shape[1] + 4, grid_rev.shape[1] -3):
        l2.append(grid_rev.diagonal(i))
    diagonal_2 = np.prod(l2[0])
    for a in l2:
        for i in range(0, a.size-3):
            temp_diag = np.prod(a[i:i+4])
            if temp_diag > diagonal_2: diagonal_2 = temp_diag
    return max(largest_horizontal, largest_vertical, diagonal_1, diagonal_2)

print(largest_prod())
