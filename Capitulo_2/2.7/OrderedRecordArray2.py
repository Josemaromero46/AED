class OrderedRecordArray(object):
    
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
    
    def delete(self, item): 
        j = self.find(self.__key(item))  
        if j < self.__nItems and self.__a[j] == item: 
            self.__nItems -= 1 
            for k in range(j, self.__nItems): 
                self.__a[k] = self.__a[k+1]
                return True 
            return False 
        
    #2.5
    def merge(self, item): # Eliminar cualquier ocurrencia
        j = self.find(self.__key(item))  # Intenta encontrar el item
        if j < self.__nItems and self.__a[j] == item: # Si se encuentra,
            self.__nItems -= 1 # Uno menos al final
            for k in range(j, self.__nItems): # Mover elementos más grandes a la izquierda
                self.__a[k] = self.__a[k+1]
                return True # Devuelve el indicador de éxito
            return False # Hecho aquí; objeto no encontrado