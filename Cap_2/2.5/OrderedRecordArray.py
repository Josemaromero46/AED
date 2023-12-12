

def identity(x): 
    return x
class OrderedRecordArray(object):
    #se modifica con el ejercicio 2.5
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
    
    def delete(self, item): 
        j = self.find(self.__key(item)) 
        if j < self.__nItems and self.__a[j] == item: 
            self.__nItems -= 1 
            for k in range(j, self.__nItems): 
                self.__a[k] = self.__a[k+1]
                return True 
            return False 
        
    # NEW 2.5
    def __init__(self, key_func, records):
        self.key_func = key_func
        self.records = sorted(records, key=key_func)

    def merge(self, other):
        if self.key_func != other.key_func:
            raise ValueError("Cannot merge arrays with different key functions")
        # Create a new list big enough to hold the current list and the merging list
        merged_records = [None] * (len(self.records) + len(other.records))
        i = j = k = 0
        while i < len(self.records) and j < len(other.records):
            if self.key_func(self.records[i]) < self.key_func(other.records[j]):
                merged_records[k] = self.records[i]
                i += 1
            else:
                merged_records[k] = other.records[j]
                j += 1
            k += 1
        # Copy remaining elements of the current list
        while i < len(self.records):
            merged_records[k] = self.records[i]
            i += 1
            k += 1

        # Copy remaining elements of the merging list
        while j < len(other.records):
            merged_records[k] = other.records[j]
            j += 1
            k += 1

        self.records = merged_records