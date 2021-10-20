COLOR_NO_COLOR = -1
COLOR_RED = 0
COLOR_BLUE = 1
COLOR_GREEN = 2


class Region:
    def __init__(self, name: str, color: int):
        self.name = name
        self.neighbors = tuple()
        self.color = color

    def add_neighbors(self, neighbors: tuple):
        self.neighbors = neighbors


class Map:
    def __init__(self):
        pass


def check_constraints(first_region: Region, color: int):
    color_taken = all([neighbor_color == color for neighbor_color in first_region.neighbors if color != COLOR_NO_COLOR])

    if not color_taken:
        print("Constraint satisfied.")
        first_region.color = color
    else:
        print("Constraint not satisfied.")


def main():
    regions = [
        Region("WA", COLOR_NO_COLOR),
        Region("SA", COLOR_NO_COLOR),
        Region("NT", COLOR_NO_COLOR)
    ]

    regions[0].add_neighbors((regions[1], regions[2]))
    regions[1].add_neighbors((regions[0], regions[2]))
    regions[2].add_neighbors((regions[0], regions[1]))

    check_constraints(regions[0], COLOR_RED)
    check_constraints(regions[1], COLOR_GREEN)
    check_constraints(regions[2], COLOR_BLUE)


if __name__ == '__main__':
    main()
