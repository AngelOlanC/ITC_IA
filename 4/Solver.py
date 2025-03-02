from Board import Board

class Solver:
    def __init__(self):
        self.boards = []
        for i in range(9):
            initialState = ""
            k = 0
            for j in range(9):
                if i != j:
                    initialState += str(j + 1 - k)
                else:
                    initialState += "0"
                    k = 1
            self.boards.append(Board(initialState))

    def query(self, starting_board, final_board, get_transition_boards=False):
        map = dict()
        map["0"] = "0"
        j = 1
        for i in range(9):
            c = starting_board[i]
            if c == "0":
                pos0 = i
            else:
                map[c] = str(j)
                j += 1
        new_final_board = ""
        for i in range(9):
            new_final_board += map[final_board[i]]
        pos0 = starting_board.index("0")
        if not self.boards[pos0].is_reachable(new_final_board):
            return ["No hay solucion"]
        if get_transition_boards:
            return self.boards[pos0].get_board_transitions(starting_board, new_final_board)
        return self.boards[pos0].get_steps(new_final_board)