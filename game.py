class BattleshipGame():
    def __init__(self, max_turns: int, size: int = 10):
        self.max_turns = max_turns
        self.size = size
        self.current_turn = 0
        self.game_over = False
        #self.board = [['.' for i in range(size)] for i in range(size)]
        self.discovered = [[False for i in range(size)] for i in range(size)]

        # Shows how many sections are still standing for each ship
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
        """Returns the string representation of the game board, showing each cell as unexplored, water, or a ship type."""
        board = []
        esc = '\x1b'
        colors = {
            '~': '[44m',        # Blue
            '?': '[45m',        # Purple
            'L': '[41m',        # Red
            'C': '[41m',        # Red
            'S': '[41m',        # Red
            'B': '[41m',        # Red
            'P': '[41m'         # Red
        }
 
        # Column numbers on top
        board.append([str(i+1) for i in range(self.size)])

        # Unexplored cells are replaced by question marks
        for i, row in enumerate(self.board):
            board.append([(cell if self.discovered[i][j] else '?') for j, cell in enumerate(row)])

        board_str = ''
        for n, row in enumerate(board):
            for i in row:
                # Add background colors and padding
                board_str += f'{esc}{colors.get(i)}{i: ^4}{esc}[0m'
            board_str += f'{self.rows[n-1] if n>0 else "": ^3}\n'
        return board_str

    def comprueba(self, row, col):
        row = self.rows.find(row)
        col -= 1