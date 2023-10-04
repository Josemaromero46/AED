import Array

maxSize = 10                    
arr = Array.Array(maxSize)      

arr.insert(77)                  
arr.insert(99)
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert(-17)

print("Array containing", len(arr), "items")
arr.traverse()

# NEW Bubble sort
for i in range(len(arr) - 1):
    for j in range(len(arr) - 1 - i):
        a = arr.get(j)
        b = arr.get(j+1)
        if isinstance(a, (int, float)) and isinstance(b, (int, float)) and a > b:
            arr.set(j, b)
            arr.set(j+1, a)

print("Array after sorting has", len(arr), "items")
arr.traverse()
