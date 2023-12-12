import Array
maxSize = 14                    # Max size of the array
arr = Array.Array(maxSize)      # Create an array object

arr.insert(77)                  # Insert 10 items
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")
arr.insert(-17)
# agregamos nuevos elementos
arr.insert("bar")
arr.insert(55)

print("Array containing", len(arr), "items")

print("Array before removing duplicates:")
arr.traverse()

arr.removeDupes()
print("Array after removing duplicates:")
arr.traverse()
