from unittest import TestCase, main

from board import Board


class TestBoard(TestCase):

    def test_validate_candidate(self):
        board = Board([])
        assert board.validate_candidate([(1, 100)]) is None  # bad coord
        candidate = [(1, i) for i in range(100)]
        assert board.validate_candidate(candidate) is None  # too big
        board.ships = [set({(1, 1)})]
        assert board.validate_candidate([(1, 1)]) is None  # place taken
        assert board.validate_candidate([(1, 2)])  # OK

    def test_place_ship(self):
        pass

    def test_initialize_board(self):
        board = Board([2])
        assert len(board.ships) == 1
        assert len(board.ships[0]) == 2
        test_setup = [1, 2, 3, 4]
        board = Board(test_setup)
        assert len(board.ships) == 4
        board = Board([1, 2, 100])
        assert len(board.ships) == 2

    def test_shoot_miss(self):
        pass

    def test_shoot_hit(self):
        pass

    def test_shoot_sink(self):
        pass


if __name__ == '__main__':
    main()
