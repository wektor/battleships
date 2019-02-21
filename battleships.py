import cmd

from board import Board

FORMAT_MESSAGE = 'Letter,number format accepted eg. A3 to shoot\nor Type help or ? to list commands.'


def parse_line(line):
    if len(line) != 2:
        print(FORMAT_MESSAGE)
        return
    try:
        x = ord(line[0]) - ord('a')
        y = int(line[1])
    except ValueError:
        print(FORMAT_MESSAGE)
        return
    return x, y


class Battleships(cmd.Cmd):
    intro = "Welcome to Battleships \nType help or ? to list commands.\n"
    prompt = "[X]"
    board = Board([4, 4, 5])

    def default(self, line):
        """Default shoot command"""
        coords = parse_line(line)
        if coords and self.board.shoot(*coords) and self.board.have_won:
            print('You have won !!!')
            return True

    def do_q(self, line):
        """Exit"""
        return True

    def do_cheat(self, line):
        """You noughty cheater - take a look at ships on board"""
        print(self.board.ships)

    def precmd(self, line):
        line = line.lower()
        return line


if __name__ == '__main__':
    Battleships().cmdloop()
