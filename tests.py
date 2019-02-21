from unittest import TestCase, main

from board import Board
from battleships import parse_line, Battleships


class TestBattleships(TestCase):
    def test_parse_line(self):
        assert parse_line('a3') == (0, 3)
        assert parse_line('a-3') is None
        assert parse_line('3') is None
        assert parse_line('j3') == (9, 3)
        assert parse_line('k3') == (10, 3)
        assert parse_line('ka') is None

    def test_default(self):
        bs = Battleships()
        bs.board.ships = [{(1, 1)}]
        assert bs.default('a3') is None  # miss
        assert bs.default('a3') is None  # miss
        assert bs.default('aa') is None  # parse error
        assert bs.default('za') is None  # invalid coordinates
        assert bs.default('b1')  # sink and win


class TestBoard(TestCase):

    def test_validate_candidate(self):
        board = Board([])
        assert board.validate_candidate([(10, 1)]) is None  # bad coord
        candidate = [(1, i) for i in range(10)]
        assert board.validate_candidate(candidate)  # max size
        candidate = [(1, i) for i in range(11)]
        assert board.validate_candidate(candidate) is None  # too big
        board.ships = [{(1, 1)}]  # a list of sets of tuples
        assert board.validate_candidate([(1, 1)]) is None  # place taken
        assert board.validate_candidate([(1, 1), (1, 2), (1, 3), (1, 4)]) is None  # place taken
        assert board.validate_candidate([(1, 2)])  # OK

    def test_place_ship(self):
        board = Board([])
        board.place_ship(4)
        assert len(board.ships) == 1
        assert len(board.ships[0]) == 4
        assert len(board.board) == 4
        board.place_ship(5)
        assert len(board.ships) == 2
        assert len(board.ships[1]) == 5
        assert len(board.board) == 9
        board.place_ship(6)
        assert len(board.ships) == 3
        assert len(board.ships[2]) == 6
        assert len(board.board) == 15

    def test_initialize_board(self):
        board = Board([2])
        assert len(board.ships) == 1
        assert len(board.ships[0]) == 2
        test_setup = [1, 2, 3, 4]
        board = Board(test_setup)
        assert len(board.ships) == 4
        board = Board([1, 2, 100])
        assert len(board.ships) == 2

    def test_shoot_invalid_coords(self):
        board = Board([])
        board.ships = [{(1, 1)}]
        assert board.shoot(-1, 0) is None
        assert board.shoot(0, 10) is None
        assert board.shoot(10, -10) is None
        assert board.shoot(-1, 110) is None
        assert board.shoot(0, 0) is None
        assert board.shoot(1, 1)

    def test_shoot_miss(self):
        board = Board([])
        board.ships = [{(1, 1)}]
        assert board.shoot(1, 0) is None
        assert board.shoot(0, 1) is None
        assert board.shoot(0, 9) is None
        assert board.ships == [{(1, 1)}]

    def test_shoot_hit_sink_win(self):
        board = Board([])
        board.ships = [{(1, 1), (1, 2), (1, 3)}, {(5, 5)}]
        assert board.shoot(1, 1) == 'hit'
        assert board.ships == [{(1, 2), (1, 3)}, {(5, 5)}]
        print(board.board)
        assert board.board == {(1, 2), (1, 3), (5, 5)}
        assert board.shoot(1, 2) == 'hit'
        assert board.ships == [{(1, 3)}, {(5, 5)}]
        assert board.board == {(1, 3), (5, 5)}
        assert board.shoot(1, 1) is None  # miss
        assert board.ships == [{(1, 3)}, {(5, 5)}]
        assert board.board == {(1, 3), (5, 5)}
        assert board.shoot(5, 5) == 'sink'
        assert board.ships == [{(1, 3)}]
        assert board.board == {(1, 3)}
        assert board.shoot(1, 1) is None  # miss
        assert board.ships == [{(1, 3)}]
        assert board.board == {(1, 3)}
        assert board.shoot(1, 3) == 'sink'
        assert board.ships == []
        assert board.board == set()
        assert board.have_won


if __name__ == '__main__':
    main()
