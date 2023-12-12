import Array

maxSize = 10                    
arr = Array.Array(maxSize)      

arr.insert(77)                  
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")
arr.insert(-17)

print("Array containing", len(arr), "items")
arr.traverse()

print("Deleting max number returns", arr.deleteMaxNum())

print("Array after deletions has", len(arr), "items")
arr.traverse()

