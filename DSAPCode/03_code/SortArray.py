# Implement a sortable Array data structure

class Array(object):
   def __init__(self, initialSize):    # Constructor
      self.__a = [None] * initialSize  # The array stored as a list
      self.nElementos = 0                # No items in array initially

   def __len__(self):                  # Special def for len() func
      return self.nElementos             # Return number of items
   
   def get(self, n):                   # Return the value at index n
      if 0 <= n and n < self.nElementos: # Check if n is in bounds, and
         return self.__a[n]            # only return item if in bounds
   
   def set(self, n, value):            # Set the value at index n
      if 0 <= n and n < self.nElementos: # Check if n is in bounds, and
         self.__a[n] = value           # only set item if in bounds

   def swap(self, j, k):               # Swap the values at 2 indices
      if (0 <= j and j < self.nElementos and # Check if indices are in
          0 <= k and k < self.nElementos): # bounds, before processing
         self.__a[j], self.__a[k] = self.__a[k], self.__a[j]
         
   def insert(self, item):             # Insert item at end
      if self.nElementos >= len(self.__a): # If array is full,
         raise Exception("Array overflow") # raise exception
      self.__a[self.nElementos] = item   # Item goes at current end
      self.nElementos += 1               # Increment number of items

   def find(self, item):               # Find index for item
      for j in range(self.nElementos):   # Among current items
         if self.__a[j] == item:       # If found,
            return j                   # then return index to item
      return -1                        # Not found -> return -1
   
   def search(self, item):             # Search for item
      return self.get(self.find(item)) # and return item if found

   def delete(self, item):             # Delete first occurrence
      for j in range(self.nElementos):   # of an item
         if self.__a[j] == item:       # Found item
            self.nElementos -= 1         # One fewer at end
            for k in range(j, self.nElementos):  # Move items from
               self.__a[k] = self.__a[k+1]     # right over 1
            return True                # Return success flag
      
      return False     # Made it here, so couldn't find the item
   
   def deleteLast(self, n=1):          # Delete last n items
      for j in range(min(n, self.nElementos)): # n defaults to 1
         self.nElementos -= 1            # Decrease number of items
         self.__a[self.nElementos] = None # Free up any space taken
         
   def traverse(self, function=print): # Traverse all items
      for j in range(self.nElementos):   # and apply a function
         function(self.__a[j])

   def __str__(self):                  # Special def for str() func
      ans = "["                        # Surround with square brackets
      for i in range(self.nElementos):   # Loop through items
         if len(ans) > 1:              # Except next to left bracket,
            ans += ", "                # separate items with comma
         ans += str(self.__a[i])       # Add string form of item
      ans += "]"                       # Close with right bracket
      return ans

   def bubbleSort(self):               # Sort comparing adjacent vals
      for last in range(self.nElementos-1, 0, -1):  # and bubble up
         for inner in range(last):     # inner loop goes up to last
            if self.__a[inner] > self.__a[inner+1]:  # If item less
               self.swap(inner, inner+1) # than adjacent item, swap
               
   def selectionSort(self):           # Sort by selecting min and 
      for outer in range(self.nElementos-1): # swapping min to leftmost
         min = outer                  # Assume min is leftmost
         for inner in range(outer+1, self.nElementos): # Hunt to right
            if self.__a[inner] < self.__a[min]: # If we find new min,
               min = inner            # update the min index
               
         # __a[min] is smallest among __a[outer]...__a[nElementos-1]
         self.swap(outer, min)        # Swap leftmost and min
         
   def insertionSort(self):           # Sort by repeated inserts
      for outer in range(1, self.nElementos): # Mark one item
         temp = self.__a[outer]       # Store marked item in temp
         inner = outer                # Inner loop starts at mark
         while inner > 0 and temp < self.__a[inner-1]: # If marked
            self.__a[inner] = self.__a[inner-1] # item smaller, then
            inner -= 1                # shift item to right
         self.__a[inner] = temp       # Move marked item to 'hole'
