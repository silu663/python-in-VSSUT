#  Programme of dictionary 

# dict.keys() - returns all the keys
my_self = {"name": "prayank", "class": "3", "section": "A"}
print(my_self.keys())
# dict.values() - returns all the values
my_self = {"name": "prayank", "class": "3", "section": "A"}
print(my_self.values())
# dict.items() - returns all the key value pairs as tuples
my_self = {"name": "prayank", "class": "3", "section": "A"}
print(my_self.items())
# del dict[] - removes a specific value
my_self = {"name": "prayank", "class": "3", "section": "A"}
del my_self["section"]
print(my_self)
# dict.update - insert specific item in the dictionary
book = {"chemistry": "2012", "physics": "2020", "biology": 
"2021"}
book.update({"english": "2025"})
print(book)
# pop() - removing an element
book = {"chemistry": "2012", "physics": "2020", "biology": 
"2021"}
book.pop("biology")
print(book)
# dict.clear() - empties the dictionary
book = {"chemistry": "2012", "physics": "2020", "biology": 
"2021"}
book.clear()
print(book)