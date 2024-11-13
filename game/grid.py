import collections

ALIVE = "o"
DEAD = "."

class LifeGrid:
    """
    The LifeGrid class takes care of two specific tasks:
            Evolving the grid to the next generation
            Providing a string representation of the grid
    """
    def __init__(self,pattern):
        self.pattern = pattern
    
    def evolve(self):
        #check the currently alive cells and their neighbors to determine the next generation of alive cells
        neighbors = ( #Delta coordiates of neighbors
            (-1, -1),  # Above left
            (-1, 0),  # Above
            (-1, 1),  # Above right
            (0, -1),  # Left
            (0, 1),  # Right
            (1, -1),  # Below left
            (1, 0),  # Below
            (1, 1),  # Below right
        )
        #check neighborhood
        num_neighbors = collections.defaultdict(int)
        #count number of alive neighbor
        for row, col in self.pattern.alive_cells:
            for drow, dcol in neighbors:
                num_neighbors[(row + drow, col + dcol)] += 1
        #sets are defined using list comprehension (for in if ...)
        stay_alive = {
            cell for cell, num in num_neighbors.items() if num in {2, 3}
        } & self.pattern.alive_cells
        come_alive = {
            cell for cell, num in num_neighbors.items() if num == 3
        } - self.pattern.alive_cells

        self.pattern.alive_cells = stay_alive | come_alive #union of stay_alive and come_alive sets

        #decide next state 
        pass

    def as_string(self, bbox):
        #represent the grid as a string that to be displayed in the terminal window
        #bbox defines which part of the grid is diplayed in the terminal window
        start_col, start_row, end_col, end_row = bbox
        display = [self.pattern.name.center(2*(end_col - start_col))]
        for row in range(start_row, end_row):
            display_row = [
                ALIVE if (row,col) in self.pattern.alive_cells else DEAD for col in range(start_col, end_col)
            ]
            display.append(" ".join(display_row))
        return "\n ".join(display)

    def __str__(self):
        return (
            f"{self.pattern.name}:\n"
            f"Alive cells -> {sorted(self.pattern.alive_cells)}"
        )