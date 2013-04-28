all_lines = {"A1": (("A2", "A3"), ("B1", "C1"), ("B2", "C3")),
    "A2": (("A1", "A3"), ("B2", "C2")),
    "A3": (("A1", "A2"), ("B3", "C3"), ("B2", "C1")),
    "B1": (("B2", "B3"), ("A1", "C1")),
    "B2": (("B1", "B3"), ("A2", "C2"),
        ("A1", "C3"), ("A3", "C1")),
    "B3": (("B1", "B2"), ("A3", "C3")),
    "C1": (("C2", "C3"), ("A1", "B1"), ("A3", "C2")),
    "C2": (("C1", "C3"), ("A2", "B2")),
    "C3": (("C1", "C2"), ("A3", "B3"), ("A1", "B2"))}


class InvalidKey(Exception):
    pass


class InvalidMove(Exception):
    pass


class InvalidValue(Exception):
    pass


class NotYourTurn(Exception):
    pass


class TicTacToeBoard:
    def __init__(self):
        self.board = {"A1": ' ', "A2": ' ', "A3": ' ',
            "B1": ' ', "B2": ' ', "B3": ' ',
            "C1": ' ', "C2": ' ', "C3": ' '}
        self.cache = ' '
        self.status = 'Game in progress.'

    def winner(self, key, value):
        b = self.board
        key_lines = all_lines[key]
        for line in key_lines:
            if b[line[0]] == value and b[line[1]] == value:
                return value
        return False

    def update_status(self, key, value):
        s = self.status
        if s != 'Game in progress.':
            return s
        b = self.board
        if ' ' not in b.values():
            return 'Draw!'
        else:
            player = self.winner(key, value)
            if player:
                return '{} wins!'.format(player)
            else:
                return 'Game in progress.'

    def __setitem__(self, key, value):
        b = self.board
        if key not in b.keys():
            raise InvalidKey('There is no key {}!'.format(key))
        elif b[key] != ' ':
            raise InvalidMove('{} is taken!'.format(key))
        elif value not in ('X', 'O'):
            raise InvalidValue('{} is invalid!'.format(value))
        elif value == self.cache:
            raise NotYourTurn('It is not your turn to play!')
        else:
            b[key] = value
            self.cache = value
            self.status = self.update_status(key, value)

    def __getitem__(self, key):
        return self.board[key]

    def __str__(self):
        b = self.board
        return '\n  -------------\n' +\
            '3 | {} | {} | {} |\n'.format(b["A3"], b["B3"], b["C3"]) +\
            '  -------------\n' +\
            '2 | {} | {} | {} |\n'.format(b["A2"], b["B2"], b["C2"]) +\
            '  -------------\n' +\
            '1 | {} | {} | {} |\n'.format(b["A1"], b["B1"], b["C1"]) +\
            '  -------------\n' +\
            '    A   B   C  \n'

    def game_status(self):
        return self.status
