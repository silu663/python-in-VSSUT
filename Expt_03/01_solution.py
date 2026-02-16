#  datatype conversion list , tuple ,dictionary etc
#  list to dictionary
my_list = [1,2,3,4,5]
list_squre = [1,4,9,16,25]

d1 = zip(my_list,list_squre)
print('list ➡️   dictionary',dict(d1))

# tuple to dictionary
num_tuple= (1,2,3)
num_tuple_sq= (1,4,9)

d2 = zip(num_tuple,num_tuple_sq)
print('tuple ➡️  dictionary ',dict(d2))

# list to set 
my_set = set(my_list)
print('list ➡️  set',my_set)

# set to tuple
my_tuple = tuple(my_set)
print('set ➡️  tuple',my_tuple)

# list to tuple
list2 = (1,2,3)
converted_tuple = tuple(list2)
print('list ➡️  tuple',converted_tuple)

# set to dictionary
my_set = {1,2,3,4,5}
set_squre = {1,4,9,16,25}

dictionary1 = zip(my_set,set_squre)
print('set ➡️  dictionary ',dict(dictionary1))







