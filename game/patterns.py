from dataclasses import dataclass

@dataclass # @decorator is just a shorter way of saying fct = decorator(fct)
class Pattern:
    name: str
    alive_cells: set[tuple[int,int]] #each tuple of the set represents the coordinates of an alive cell