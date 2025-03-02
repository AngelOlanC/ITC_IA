class MovementMaker:
    def __init__(self):
        self.moves = [-1, 1, -3, 3]
        self.moveName = ["Left", "Right", "Up", "Down"]

    def can_make_move(self, board, movement):
        idx = board.index("0")
        next_idx = idx + self.moves[movement]
        if next_idx < 0 or next_idx > 8:
            return False
        if idx % 3 == 0 and movement == 0:
            return False
        if idx % 3 == 2 and movement == 1:
            return False
        if idx // 3 == 0 and movement == 2:
            return False
        if idx // 3 == 2 and movement == 3:
            return False
        return True

    def make_move(self, board, movement):
        idx = board.index("0")
        next_idx = idx + self.moves[movement]
        new_board = ""
        for i in range(9):
            if i == idx:
                new_board += board[next_idx]
            elif i == next_idx:
                new_board += board[idx]
            else:
                new_board += board[i]
        return new_board

    def move_name(self, movement):
        return self.moveName[movement]