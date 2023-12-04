import pygame
import sys

# Función que verifica si un movimiento es válido
def validar_movimiento(tablero, move, n):
    x, y = move
    return 0 <= x < n and 0 <= y < n and tablero[x][y] == -1

# Función principal que resuelve el problema del Tour del Caballero
def tour_caballero(n, x_inicial, y_inicial):
    pygame.init()

    # Configura el tamaño de la ventana y su título
    size = n * 80  # Ajusta el tamaño según sea necesario
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption("El Tour del Caballero")

    # Configura el reloj de pygame y el retardo entre movimientos
    clock = pygame.time.Clock()
    move_delay = 10  # Milisegundos entre movimientos

    # Crea el tablero y otras variables necesarias
    tablero = [[-1 for _ in range(n)] for _ in range(n)]
    contador_moves = 0
    moves_x = [2, 1, -1, -2, -2, -1, 1, 2]
    moves_y = [1, 2, 2, 1, -1, -2, -2, -1]
    caballo_moves = []

    # Función interna que realiza la búsqueda en profundidad
    def depthFirst(x, y, contador_moves):
        nonlocal tablero
        nonlocal moves_x
        nonlocal moves_y
        nonlocal caballo_moves

        # Si se ha completado el recorrido del tablero, retorna True
        if contador_moves == n * n:
            return True

        # Genera los movimientos posibles
        posible_moves = [(x + moves_x[i], y + moves_y[i]) for i in range(8)]
        posible_moves = [(px, py) for px, py in posible_moves if validar_movimiento(tablero, (px, py), n)]

        # Ordena los posibles movimientos según la cantidad de siguientes movimientos posibles
        posible_moves.sort(key=lambda move: sum(validar_movimiento(tablero, (move[0] + moves_x[i], move[1] + moves_y[i]), n) for i in range(8)))

        # Itera sobre los posibles movimientos
        for move in posible_moves:
            next_x, next_y = move

            # Actualiza el tablero y la lista de movimientos
            tablero[next_x][next_y] = contador_moves
            caballo_moves.append((next_x, next_y))

            # Dibuja el estado actual del tablero en la pantalla
            dibujar_tablero(n, screen, tablero)
            pygame.display.flip()

            # Maneja eventos (por ejemplo, cierre de ventana)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Retardo entre movimientos
            pygame.time.delay(move_delay)

            # Llamada recursiva para explorar el siguiente movimiento
            if depthFirst(next_x, next_y, contador_moves + 1):
                return True

            # Retrocede si no se encuentra una solución
            tablero[next_x][next_y] = -1
            caballo_moves.pop()

        return False

    # Función interna que dibuja el estado actual del tablero
    def dibujar_tablero(n, screen, tablero):
        screen.fill((255, 255, 255))  # Limpia la pantalla antes de dibujar

        cell_size = size // n
        for i in range(n):
            for j in range(n):
                pygame.draw.rect(screen, (255, 255, 255), (j * cell_size, i * cell_size, cell_size, cell_size), 0)
                pygame.draw.rect(screen, (0, 0, 0), (j * cell_size, i * cell_size, cell_size, cell_size), 1)

                if tablero[i][j] != -1:
                    font = pygame.font.Font(None, 36)
                    text = font.render(str(tablero[i][j]), True, (0, 0, 0))
                    screen.blit(text, (j * cell_size + cell_size // 3, i * cell_size + cell_size // 3))

        pygame.display.flip()

    # Establece la posición inicial en el tablero
    tablero[x_inicial][y_inicial] = contador_moves
    caballo_moves.append((x_inicial, y_inicial))

    # Dibuja el estado inicial del tablero
    dibujar_tablero(n, screen, tablero)
    pygame.display.flip()

    # Bucle infinito para mantener la ventana abierta
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Llamada inicial a la búsqueda en profundidad
        depthFirst(x_inicial, y_inicial, contador_moves + 1)

# Obtiene la entrada del usuario
n = int(input("Ingrese el tamaño del tablero (n): "))
x_inicial = int(input("Ingrese la coordenada x de inicio: "))
y_inicial = int(input("Ingrese la coordenada y de inicio: "))

# Ejemplo: Resuelve el Tour del Caballero
tour_caballero(n, x_inicial, y_inicial)
