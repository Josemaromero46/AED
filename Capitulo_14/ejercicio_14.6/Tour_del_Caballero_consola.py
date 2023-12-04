
def validar_movimiento(tablero, move, n):
    # Función que verifica si un movimiento es válido
    x, y = move
    # Verifica que las coordenadas estén dentro del tablero y la casilla no haya sido visitada
    return 0 <= x < n and 0 <= y < n and tablero[x][y] == -1

def tour_caballero(n, x_inicial, y_inicial):
    # Función principal que realiza la búsqueda en profundidad para el Tour del Caballero
    tablero = [[-1 for _ in range(n)] for _ in range(n)]  # Inicializa el tablero con todas las casillas como no visitadas
    move_count = 0  
    moves_x = [2, 1, -1, -2, -2, -1, 1, 2]  # Desplazamientos en el eje x para el caballero
    moves_y = [1, 2, 2, 1, -1, -2, -2, -1]  # Desplazamientos en el eje y para el caballero
    secuencia_move = []  # Almacena la secuencia de movimientos del caballero

    def profundidad_search(x, y, move_count):
        # Función interna que implementa la búsqueda en profundidad
        nonlocal tablero, moves_x, moves_y, secuencia_move

        if move_count == n * n:
            # Si se han realizado todos los movimientos posibles, se ha encontrado una solución
            return True

        for i in range(8):
            next_x = x + moves_x[i]
            next_y = y + moves_y[i]
            next_move = (next_x, next_y)

            if validar_movimiento(tablero, next_move, n):
                # Si el movimiento es válido, se marca en el tablero y se agrega a la secuencia
                tablero[next_x][next_y] = move_count
                secuencia_move.append((next_x, next_y))
                
                if profundidad_search(next_x, next_y, move_count + 1):
                    # Llamada recursiva para continuar con la búsqueda en profundidad
                    return True

                # Backtrack si la búsqueda en profundidad no lleva a una solución
                tablero[next_x][next_y] = -1
                secuencia_move.pop()

        return False

    # Establece la posición inicial
    tablero[x_inicial][y_inicial] = move_count
    secuencia_move.append((x_inicial, y_inicial))

    if not profundidad_search(x_inicial, y_inicial, move_count + 1):
        print("No encontre una solución.")
    else:
        # Si se encuentra una solución, imprime el tablero y la secuencia de movimientos
        imprimir_tablero(tablero, secuencia_move)

def imprimir_tablero(tablero, secuencia_move):
    # Función para imprimir el tablero y la secuencia de movimientos
    print("El Tour del Caballero:")
    for row in tablero:
        print(row)
    print("Secuencia de Movimientos:")
    print(secuencia_move)

# Entrada del usuario
n = int(input("Ingrese el tamaño del tablero (NxN): "))
x_inicial = int(input("Ingrese la coordenada x de inicio: "))
y_inicial = int(input("Ingrese la coordenada y de inicio: "))

# Test
tour_caballero(n, x_inicial, y_inicial)
