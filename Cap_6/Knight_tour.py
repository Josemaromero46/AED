def is_valid_move(board, x, y, N):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def knight_tour_util(board, x, y, move_count, N, x_moves, y_moves):
    if move_count == N * N:
        return True

    for i in range(8):
        next_x = x + x_moves[i]
        next_y = y + y_moves[i]

        if is_valid_move(board, next_x, next_y, N):
            board[next_x][next_y] = move_count

            if knight_tour_util(board, next_x, next_y, move_count + 1, N, x_moves, y_moves):
                return True

            # Backtrack
            board[next_x][next_y] = -1

    return False

def knight_tour(N):
    # Inicializar el tablero
    board = [[-1 for _ in range(N)] for _ in range(N)]

    # Movimientos del caballo en el eje x e y
    x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
    y_moves = [1, 2, 2, 1, -1, -2, -2, -1]

    # Iniciar desde la esquina superior izquierda
    start_x, start_y = 0, 0
    board[start_x][start_y] = 0

    if knight_tour_util(board, start_x, start_y, 1, N, x_moves, y_moves):
        print("Solución encontrada:")
        for row in board:
            print(row)
    else:
        print("No se encontró solución.")

# Tamaño del tablero 
N = 8
knight_tour(N)