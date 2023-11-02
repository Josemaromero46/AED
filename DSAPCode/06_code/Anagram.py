# Calcular los anagramas de una cadena de caracteres

def factorial(n):         # Obtener el factorial de n
   if n < 1: return 1     # Es 1 para cualquier número < 1
   return (n *            # De lo contrario, multiplica n
   factorial(n - 1))      # por el factorial anterior

def anagramas(palabra):                 # Devuelve una lista de anagramas para la palabra
   if len(palabra) <= 1:                # Palabras vacías y letras individuales
      return [palabra]                  # tienen un solo anagrama, ellos mismos
   resultado = []                       # Comenzar con una lista vacía
   for parte in anagramas(palabra[1:]): # Iterar sobre anagramas más pequeños
      for i in range(len(parte) + 1):   # Para cada índice en la palabra más pequeña
         resultado.append(              # Agregar un nuevo anagrama con
            parte[:i] +                 # la palabra más pequeña hasta el índice
            palabra[0] +                # más el primer carácter de esta palabra
            parte[i:])                  # más el resto de la palabra más pequeña
   return resultado                     # Devolver la lista de anagramas más grandes

word = input("\nIngrese una palabra: ")
print(f"\nCantidad de Anagramas de {word}: {factorial(len(word))}")
print(f"\nAnagramas de {word}: {anagramas(word)}")