import cmd, sys

from board import Board, BOARD_SIZE


class Battleships(cmd.Cmd):
    intro = "Welcome to Battleships \nType help or ? to list commands.\n"
    format_message = 'Letter,number format accepted eg. A3 to shoot\nor Type help or ? to list commands.'
    prompt = "[X]"
    board = Board([4, 4, 5])

    def default(self, line):
        if len(line) != 2:
            print(self.format_message)
            return
        try:
            x = ord(line[0]) - ord('a')
            y = int(line[1])
        except ValueError:
            print(self.format_message)
            return

        if self.board.shoot(x, y) and self.board.have_won:
            print('You have won !!!')
            return True

    def do_q(self, line):
        "Exit"
        return True

    def do_cheat(self, line):
        "You noughty cheater"
        print(self.board.ships)

    def precmd(self, line):
        line = line.lower()
        return line


if __name__ == '__main__':
    Battleships().cmdloop()
