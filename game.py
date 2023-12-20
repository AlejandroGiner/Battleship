class BattleshipGame():
    def __init__(self, max_turns: int, size: int = 10):
        self.max_turns = max_turns
        self.size = size
        self.current_turn = 0
        self.game_over = False
        #self.board = [['.' for i in range(size)] for i in range(size)]
        self.discovered = [[False for i in range(size)] for i in range(size)]

        # Representa las secciones que quedan en pie de cada barco
        self.ships = {
            'L':1,
            'C':2,
            'S':3,
            'B':4,
            'P':5
        }
        self.rows = 'ABCDEFGHIJ'

        default_board = []
        default_board.append('~~~~~~~~~~')
        default_board.append('~L~~~~~~P~')
        default_board.append('~~~~~~~~P~')
        default_board.append('~~~~~~~~P~')
        default_board.append('~~~CC~~~P~')
        default_board.append('~~~~~~~~P~')
        default_board.append('~~~S~~~~~~')
        default_board.append('~~~S~~~~~~')
        default_board.append('~~~S~~~~~~')
        default_board.append('~~BBBB~~~~')
        self.board = default_board

    
    def get_board(self):
        board = []
        esc = '\x1b'
        colors = {
            '~': '[44m',
            '?': '[45m',
            'L': '[41m',
            'C': '[41m',
            'S': '[41m',
            'B': '[41m',
            'P': '[41m'
        }
 
        # Números de las columnas
        board.append([str(i+1) for i in range(self.size)])

        # Reemplazamos por ? las casillas que no hayan sido exploradas
        for i, row in enumerate(self.board):
            board.append([(cell if self.discovered[i][j] else '?') for j, cell in enumerate(row)])

        board_str = ''
        for n, row in enumerate(board):
            #board_str += ' '.join(row)
            for i in row:
                if i in colors.keys():
                    board_str += f'{esc}{colors.get(i)}'
                board_str += f'{i: ^4}{esc}[0m'
            board_str += f'{self.rows[n-1] if n>0 else "": ^3}\n'
        return board_str

    def comprueba(self, row, col):
        row = self.rows.find(row)
        col -= 1