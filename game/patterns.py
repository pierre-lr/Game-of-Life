from dataclasses import dataclass

@dataclass # @decorator is just a shorter way of saying fct = decorator(fct)
class Pattern:
    name: str
    alive_cells: set[tuple[int,int]] #each tuple of the set represents the coordinates of an alive cell

    @classmethod
    def from_toml(cls,name,toml_data):
        return cls(
            name,
            alive_cells={tuple(cell) for cell in toml_data["alive_cells"]},
        )