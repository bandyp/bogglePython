def make_grid(width, height):
    """
    Createsa grid that will hold all if the tiles
    """
    return{(row, col): ' ' for row in range(height)
        for col in range(width)
    }