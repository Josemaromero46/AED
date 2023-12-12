#eliminación rápida del elemento de mayor prioridad pero una inserción lenta de elementos nuevos

#tiempo de inserción rápido, O(1), pero una eliminación más lenta del elemento de mayor prioridad.
def identity(x): return x
class PriorityQueue: 
    def __init__(self, size): # Método constructor
        self.__maxSize = size # Tamaño máximo de la cola de prioridad
        self.__que = [None] * size # Cola almacenada como una lista
        self.__nItems = 0 # Contador de elementos en la cola inicializado en cero

    # Método para insertar un elemento en la cola de prioridad
    def insert(self, item):
        # Verificar si la cola de prioridad está llena
        if self.isFull():
            raise Exception("Queue overflow")
        # Insertar el nuevo elemento en la cola de prioridad
        self.__que[self.__nItems] = item
        # Incrementar el contador de elementos en la cola de prioridad
        self.__nItems += 1
        return True

    # Método para remover el elemento de mayor prioridad de la cola de prioridad
    def remove(self):
        # Verificar si la cola de prioridad está vacía
        if self.isEmpty():
            raise Exception("Queue underflow")
        # Encontrar el índice del elemento de mayor prioridad
        maxIndex = 0
        for i in range(1, self.__nItems):
            if self.__que[i] > self.__que[maxIndex]:
                maxIndex = i
        # Guardar el elemento de mayor prioridad
        front = self.__que[maxIndex]
        # Desplazar los elementos hacia atrás
        for i in range(maxIndex+1, self.__nItems):
            self.__que[i-1] = self.__que[i]
        # Disminuir el contador de elementos en la cola de prioridad
        self.__nItems -= 1
        # Retornar el elemento de mayor prioridad
        return front

    # Método para obtener el elemento de mayor prioridad sin removerlo
    def peek(self):
        return None if self.isEmpty() else self.__que[self.__nItems-1]

    # Método para verificar si la cola de prioridad está vacía
    def isEmpty(self):
        return self.__nItems == 0

    # Método para verificar si la cola de prioridad está llena
    def isFull(self):
        return self.__nItems == self.__maxSize

    # Método para obtener el número de elementos en la cola de prioridad
    def __len__(self):
        return self.__nItems

    # Método para convertir la cola de prioridad a una cadena de caracteres
    def __str__(self):
        ans = "["
        for i in range(self.__nItems-1, -1, -1):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__que[i])
        ans += "]"
        return ans
