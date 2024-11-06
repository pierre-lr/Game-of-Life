import collections

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
        pass

    def __str__(self):
        #BUG : TypeError: __str__ returned non-string (type NoneType)
        return (
            f"{self.pattern.name}:\n"
            f"Alive cells -> {sorted(self.pattern.alive_cells)}"
        )