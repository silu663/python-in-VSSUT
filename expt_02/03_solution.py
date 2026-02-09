# programme on pop opeataion

square = set([i**2 for i in range(1, 11)])
cube = set([i**3 for i in range(1, 11)])
print(square)
print(cube)
square.update(cube) # updates a new value to set
print(square)
square.pop() # removes a random value
print(square)
square.remove(343) # removes a specific element
print(square)
square.add(121) # addition of a new element
print(print(square))
square.clear() # empties the set
print(square)