from collections import deque
from MovementMaker import MovementMaker

class Board:
    def __init__(self, initial_state):
        self.movement_to_here = dict()
        self.distance = dict()
        self.base_state = initial_state
        q = deque()
        q.append(initial_state)
        self.distance[initial_state] = 0

        movement_maker = MovementMaker()

        while len(q) > 0:
            current_state = q.popleft()
            current_distance = self.distance[current_state]
            for movement in range(4):
                if not movement_maker.can_make_move(current_state, movement):
                    continue
                next_state = movement_maker.make_move(current_state, movement)
                if next_state not in self.distance:
                    self.distance[next_state] = current_distance + 1
                    self.movement_to_here[next_state] = movement
                    q.append(next_state)

    def is_reachable(self, final_state):
        return final_state in self.distance

    def get_movements(self, final_state):
        movements = list()

        movement_maker = MovementMaker()

        def go_backwards(state):
            if state == self.base_state:
                return
            movement = self.movement_to_here[state]
            next_state = movement_maker.make_move(state, movement ^ 1)
            go_backwards(next_state)
            movements.append(movement)
        go_backwards(final_state)

        return movements

    def get_steps(self, final_state):
        movements = self.get_movements(final_state)

        movement_maker = MovementMaker()

        for i in range(len(movements)):
            movements[i] = movement_maker.move_name(movements[i])
        
        return movements
    
    def get_board_transitions(self, board, final_state):
        movements = self.get_movements(final_state)
        boards = list()
        boards.append(self.get_pretty_board(board))
        movement_maker = MovementMaker()
        for movement in movements:
            board = movement_maker.make_move(board, movement)
            boards.append(self.get_pretty_board(board))
        return boards
    
    def get_pretty_board(self, board):
        return board[:3] + "\n" + board[3:6] + "\n" + board[6:9]