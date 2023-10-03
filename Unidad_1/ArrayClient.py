import Array
maxSize = 10 # Max size of the array
arr = Array.Array(maxSize) # Create an array object
arr.insert(77) # Insert 10 items
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")
arr.insert(-17)
print("Matriz que contiene", len(arr), "elementos")
arr.traverse()
print("Buscar 12 retornos", arr.search(12))
print("Buscar 12.34 devoluciones", arr.search(12.34))
print("Borrar 0 resultados", arr.delete(0))
print("Borrar 17 devoluciones", arr.delete(17))
print("Establecer el elemento del índice 3 en 33")
arr.set(3, 33)
print("La matriz después de los borrados tiene", len(arr), "elementos")
arr.traverse()


# EJERCICIO 2.1
print("-----EJERCICIO 2.1-----")
my_array = Array.Array(10)
my_array.insert(5)
my_array.insert(10)
my_array.insert(2.5)
my_array.insert("No soy un número")

max_number = my_array.getMaxNum()
if max_number is not None:
    print(f"El número más alto en la matriz es: {max_number}")
else:
    print("La matriz no contiene números.")

# EJERCICIO 2.2
print("-----EJERCICIO 2.2-----")
my_array.traverse()
my_array.deleteMaxNum()
print("La matriz después borrar el valor maximo tiene", len(my_array), "elementos")
my_array.traverse()
