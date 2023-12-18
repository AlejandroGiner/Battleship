class BattleshipGame():
    def __init__(self, max_turns: int, size: int):
        self.max_turns = max_turns
        self.board = [['.' for i in range(size)] for i in range(size)]
        self.discovered = [[False for i in range(size)] for i in range(size)]
    
    def get_board(self):
        board = []
        for i, row in enumerate(self.board):
            board.append([(cell if self.discovered[i][j] else '?') for j, cell in enumerate(row)])
        board_str = ''
        for row in board:
            board_str += ''.join(row)
            board_str += '\n'
        return board_str
