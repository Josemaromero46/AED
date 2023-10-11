
def Fibonacci():
    previous = 0
    current = 1
    while True:
        yield current
        #print (current , ' - ')
        next = previous + current 
        previous = current 
        current = next

# gen = Fibonacci()
# print(gen.__next__() ) # 1  # previus: 0, current: 1,  next = 0 
# print(gen.__next__() ) # 1  # next = 0+1 = 1  previus: 1, current: 1,  
# print(gen.__next__() ) # 2  # next = 1 + 1 = 2  previus: 1, current: 2 
# print(gen.__next__() ) # 3
# print(gen.__next__() ) # 5

# print( Fibonacci() )
# print( Fibonacci() )
# print( Fibonacci() )
# print( Fibonacci() )
# print( Fibonacci() )
# print( Fibonacci() )
count = 15
print('The first', count, 'numbers in the Fibonacci series are:')
for x in Fibonacci():
    if count < 1:
       break
    print(x)
    count -= 1