
def identity(x): 
    return x
class OrderedRecordArray(object):
    #Estos se modifican para el ejercicio 2.7
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
        
    #Esto se modifica para el ejercicio 2.7
    """def insert(self, item): # Insertar elemento en la posición correcta
        if self.__nItems >= len(self.__a): # Si la matriz está llena,
            raise Exception("Array overflow") # generar excepción
        j = self.find(self.__key(item)) # Encuentra dónde debe ir el elemento
        for k in range(self.__nItems, j, -1): # Mover elementos más grandes a la derecha
            self.__a[k] = self.__a[k-1]
            self.__a[j] = item # Insertar el artículo
            self.__nItems += 1 # Incrementa el número de elementos"""
    
    def delete(self, item): 
        j = self.find(self.__key(item))  
        if j < self.__nItems and self.__a[j] == item: 
            self.__nItems -= 1 
            for k in range(j, self.__nItems): 
                self.__a[k] = self.__a[k+1]
                return True 
            return False 
            
    #2.7    
    def __init__(self, key_func, records, max_size=10, grow_factor=1.5):
        self.key_func = key_func
        self.records = sorted(records, key=key_func)
        self.max_size = max_size
        self.grow_factor = grow_factor

    def insert(self, record):
        if len(self.records) == self.max_size:
            self.max_size = int(self.max_size * self.grow_factor)
            self.records = self.records + [None] * (self.max_size - len(self.records))
            self.records[len(self.records)] = record
            self.records = sorted(self.records, key=self.key_func)