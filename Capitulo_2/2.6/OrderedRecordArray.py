# Implementar una estructura de matriz ordenada de registros
def identity(x): # La función identidad
    return x
class OrderedRecordArray(object):
    #Se modifica con el ejercicio 2.6
    """def __init__(self, initialSize, key=identity): # Constructor
        self.__a = [None] * initialSize #  La matriz almacenada como una lista
        self.__nItems = 0 # No hay elementos en la matriz inicialmente
        self.__key = key # La función de tecla obtiene la clave de registro"""
    
    def __len__(self):  
        return self.__nItems  

    def get(self, n):
        if n >= 0 and n < self.__nItems:  
            return self.__a[n] 
        raise IndexError("Index " + str(n) + " is out of range")
    
    def traverse(self, function=print): 
        for j in range(self.__nItems):  
           function(self.__a[j])
            
    def __str__(self): 
        ans = "[" 
        for i in range(self.__nItems): 
            if len(ans) > 1:
                ans += ", " 
            ans += str(self.__a[i]) 
        ans += "]" 
        return ans

    def find(self, key): 
        lo = 0
        hi = self.__nItems-1 
        while lo <= hi:
            mid = (lo + hi) // 2 
            if self.__key(self.__a[mid]) == key: 
                return mid 
            elif self.__key(self.__a[mid]) < key: 
                lo = mid + 1 
            else:
                hi = mid - 1 
                return lo 
        
    def search(self, key):
        idx = self.find(key) 
        if idx < self.__nItems and self.__key(self.__a[idx]) == key:
            return self.__a[idx] 
    
    def insert(self, item): 
        if self.__nItems >= len(self.__a): 
            raise Exception("Array overflow") 
        j = self.find(self.__key(item)) 
        for k in range(self.__nItems, j, -1): 
            self.__a[k] = self.__a[k-1]
            self.__a[j] = item 
            self.__nItems += 1 
    
    #Se modifica con el ejercicio 2.6
    """def delete(self, item): # Eliminar cualquier ocurrencia
        j = self.find(self.__key(item))  # Intenta encontrar el item
        if j < self.__nItems and self.__a[j] == item: # Si se encuentra,
            self.__nItems -= 1 # Uno menos al final
            for k in range(j, self.__nItems): # Mover elementos más grandes a la izquierda
                self.__a[k] = self.__a[k+1]
                return True # Devuelve el indicador de éxito
            return False # Hecho aquí; objeto no encontrado"""
        
    #2.6
    def __init__(self, key_func, records):
        self.key_func = key_func
        self.records = sorted(records, key=key_func)

    def delete(self, item):
        index = None
        for i, record in enumerate(self.records):
            if self.key_func(record) == item:
                index = i
                break
            if index is not None:
                self.records = self.records[:index] + self.records[index+1:]