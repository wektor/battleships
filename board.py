from random import randint
import itertools

BOARD_SIZE = 10


def validate_coordinate(c):
    if c < 0 or c >= BOARD_SIZE:
        print(f'Board size is {BOARD_SIZE}')
        return False
    return True


def validate_coordinates(x, y):
    return validate_coordinate(x) and validate_coordinate(y)


class Board:
    def __init__(self, ship_sizes):
        self.ships = []
        for size in ship_sizes:
            self.place_ship(size)

    @property
    def board(self):
        # reduce nest level
        return set(itertools.chain(*self.ships))

    @property
    def ships_left(self):
        return len(self.ships)

    @property
    def sections_left(self):
        return len(self.board)

    @property
    def have_won(self):
        return self.ships_left == 0

    def validate_candidate(self, ship_candidate):
        """Validates and places a ship if valid"""
        for coord in ship_candidate:
            x, y = coord
            if not validate_coordinates(x, y):
                print(f'Invalid coordinates {coord}')
                return
        if not self.board.intersection(ship_candidate):  # sections of new ship don't overlap with the existing ones
            self.ships.append(ship_candidate)
            return True

    def place_ship_h(self, size):
        """Place ship horizontally"""
        x = randint(0, BOARD_SIZE - size - 1)
        y = randint(0, BOARD_SIZE - 1)
        ship_candidate = set()
        for i in range(size):
            ship_candidate.add((x + i, y))
        return self.validate_candidate(ship_candidate)

    def place_ship_v(self, size):
        """Place ship vertically"""
        x = randint(0, BOARD_SIZE - 1)
        y = randint(0, BOARD_SIZE - size - 1)
        ship_candidate = set()
        for i in range(size):
            ship_candidate.add((x, y + i))
        return self.validate_candidate(ship_candidate)

    def place_ship(self, size):
        """Place ship on the board"""
        if size > BOARD_SIZE:
            print(f'Ship size({size}) cannot be bigger than board({BOARD_SIZE})')
            return
        while True:  # possible improvement
            orientation = randint(0, 1)
            if orientation == 0:
                x = self.place_ship_h(size)
            else:
                x = self.place_ship_v(size)
            if x:
                return

    def shoot(self, x, y):
        """Check if there is a ship under coordinates x,y and if so check if Miss, Hit, Sink"""
        if not validate_coordinates(x, y):
            return
        for ship in self.ships:
            if (x, y) in ship:
                if len(ship) == 1:
                    self.ships.remove(ship)
                    print(f"Sink!! ({self.ships_left} ships left)")
                    return 'sink'  # evaluates to True, result used for testing
                else:
                    ship.remove((x, y))
                    print(f'Hit! ({self.sections_left} sections left)')
                    return 'hit'  # evaluates to True, result used for testing
        print('Miss')



