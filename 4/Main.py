from Solver import Solver
import time

def main():
    start_time = time.time()
    solver = Solver()
    end_time = time.time()
    print(f"Tiempo de precalculo: {end_time - start_time:.6f} segundos")

    while True:
        starting_board = "".join(input("Ingrese el tablero inicial:\n").split())
        final_board = "".join(input("Ingrese el tablero final:\n").split())
        wanna_see_transition_boards = input("¿Desea ver las transiciones (S/N)? ")

        start_time = time.time()
        solution = solver.query(starting_board, final_board, wanna_see_transition_boards[0] == "S")
        end_time = time.time()
        print(f"Tiempo de consulta: {end_time - start_time:.6f} segundos")

        for x in solution:
            print(x + "\n")

        op = input("¿Desea hacer otra consulta (S/N)? ")
        if op[0] != 'S':
            break

if __name__ == '__main__':
    main()