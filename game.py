class BattleshipGame():
    def __init__(self, max_turns: int, size: int):
        self.max_turns = max_turns
        self.current_turn = 0
        self.game_over = False
        #self.board = [['.' for i in range(size)] for i in range(size)]
        self.discovered = [[False for i in range(size)] for i in range(size)]

        default_board = []
        default_board.append('..........')
        default_board.append('.L......P.')
        default_board.append('........P.')
        default_board.append('........P.')
        default_board.append('...CC...P.')
        default_board.append('........P.')
        default_board.append('...S......')
        default_board.append('...S......')
        default_board.append('...S......')
        default_board.append('..BBBB....')
        self.board = default_board

    
    def get_board(self):
        board = []
        for i, row in enumerate(self.board):
            board.append([(cell if self.discovered[i][j] else '?') for j, cell in enumerate(row)])
        board_str = ''
        for row in board:
            board_str += ''.join(row)
            board_str += '\n'
        return board_str

    def comprueba(self, row, col):
        row = 'ABCDEFGHIJ'.find(row)
        col -= 1