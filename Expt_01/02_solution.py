# write a programme to  calculate the distance between to coordinates

x1 = float(input('Enter X1 : '))
x2 = float(input('Enter X2 : '))
y1 = float(input('Enter Y1 : '))
y2 = float(input('Enter Y2 : '))

distance = (((x2 - x1)**2) + ((y2 - y1)**2))**0.5

print('distance between two point is = ',str(distance))

