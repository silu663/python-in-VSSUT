book = {
 "chemistry": "2012",
 "physics": "2020",
 "biology": "2021"
}
book["maths"] = "2022" # addition of a new element
print(book)
book.update({"english": "2025"}) # insert specific item
print(book)
book.pop("biology") # removes an element
print(book)
del book["physics"] # removes a specific value
print(book)
book.clear() # empties the dictionary
print(book)