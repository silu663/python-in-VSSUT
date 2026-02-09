list1 = []
a = int(input("Enter the beginning of the list: "))
b = int(input("Enter the end of the list: "))
c = int(input("Enter the step of the list: "))
for i in range(a, b, c):
 list1.append(i)
print(list1)
list1.reverse() 
print(list1)