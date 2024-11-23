import numpy as np

# Grid dimensions

grid_width = 10

grid_height = 6

 

def rotate(figure, angle):

    """Rotate figure by 90, 180, or 270 degrees."""

    if angle == 90:

        return [(c, -r) for r, c in figure]

    elif angle == 180:

        return [(-r, -c) for r, c in figure]

    elif angle == 270:

        return [(-c, r) for r, c in figure]

    return figure

 

def flip_horizontal(figure):

    """Flip figure horizontally."""

    return [(r, -c) for r, c in figure]

 

def generate_all_orientations(figure):

    """Generate all distinct orientations of a figure."""

    orientations = set()

    for angle in [0, 90, 180, 270]:

        rotated = rotate(figure, angle)

        orientations.add(tuple(sorted(rotated)))

        orientations.add(tuple(sorted(flip_horizontal(rotated))))

    return [list(orientation) for orientation in orientations]

 

def generate_pentominoes():

    pentominoes = []
    # F shape
    pentominoes.append([(0, 1), (1, 0), (1, 1), (1, 2), (2, 0)])
    # I shape
    pentominoes.append([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)])
    # L shape
    pentominoes.append([(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)])
    # N shape
    pentominoes.append([(0, 0), (1, 0), (1, 1), (2, 1), (3, 1)])
    # P shape
    pentominoes.append([(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)])
    # T shape
    pentominoes.append([(0, 0), (0, 1), (0, 2), (1, 1), (2, 1)])
    # U shape
    pentominoes.append([(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)])
    # V shape
    pentominoes.append([(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)])
    # W shape
    pentominoes.append([(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)])
    # X shape
    pentominoes.append([(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)])
    # Y shape
    pentominoes.append([(0, 1), (1, 0), (1, 1), (2, 1), (3, 1)])
    # Z shape
    pentominoes.append([(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)])

    all_orientations = []

   # for pentomino in pentominoes:

    #    all_orientations.extend(generate_all_orientations(pentomino))

    return all_orientations 

def generate_figure_positions(grid_width, grid_height, figure):

    positions = []

 

    for row in range(grid_height):

        for col in range(grid_width):

            placed_positions = [(row + r, col + c) for r, c in figure]

            if all(0 <= r < grid_height and 0 <= c < grid_width for r, c in placed_positions):

                positions.append(placed_positions)

 

    return positions

 

def can_place_figure(grid, positions):

    return all(grid[r, c] == 0 for r, c in positions)

 

def place_figure(grid, positions, figure_id):

    for (r, c) in positions:

        grid[r, c] = figure_id

 

def remove_figure(grid, positions):

    for (r, c) in positions:

        grid[r, c] = 0

 

def fill_grid(grid, figures):

    if np.all(grid != 0):

        return True  # Grid fully filled

 

    for figure_idx, current_figure in enumerate(figures):

        positions_list = generate_figure_positions(grid_width, grid_height, current_figure)

 

        for positions in positions_list:

            if can_place_figure(grid, positions):

                place_figure(grid, positions, figure_idx + 1)

                if fill_grid(grid, figures):

                    return True

                remove_figure(grid, positions)  # Backtrack

 

    return False

 

def solve_grid(grid_width, grid_height):

    grid = np.zeros((grid_height, grid_width), dtype=int)

    pentominoes = generate_pentominoes()

 

    if fill_grid(grid, pentominoes):

        return grid

    else:

        return None  # No solution found

 

def display_grid(grid):

    for row in grid:

        print(' '.join(str(int(cell)) if cell > 0 else '.' for cell in row))

 

# Solve the grid

solved_grid = solve_grid(grid_width, grid_height)

 

if solved_grid is not None:

    display_grid(solved_grid)

else:

    print("No solution found.")

 