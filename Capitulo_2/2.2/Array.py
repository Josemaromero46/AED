class Array(object):
    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nItems = 0

    def __len__(self):
        return self.__nItems

    def get(self, n):
        if 0 <= n and n < self.__nItems:
            return self.__a[n]

    def set(self, n, value):
        if 0 <= n and n < self.__nItems:
            self.__a[n] = value

    def insert(self, item):
        self.__a[self.__nItems] = item
        self.__nItems += 1

    def find(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                return j
        return -1

    def search(self, item):
        return self.get(self.find(item))

    def delete(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                self.__nItems -= 1
                for k in range(j, self.__nItems):
                    self.__a[k] = self.__a[k+1]
                return True
        return False
    
    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])   
             
 # NEW    
    def deleteMaxNum(self):
        max_num = None
        max_num_index = None
        for i in range(self.__nItems):
            if isinstance(self.__a[i], (int, float)):
                if max_num is None or self.__a[i] > max_num:
                    max_num = self.__a[i]
                    max_num_index = i
        if max_num is not None:
            self.delete(max_num)
        return max_num


