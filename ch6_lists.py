""""
lists
- collection of data, can be any/all data type in single list, even can contain other collections as list items
- mutable (can be added, removed, changed)
- maintain order (can use index to find an item)
"""
fruits = ["peaches", "pears", "apples"]
years = [3, "1998", 2.5, 987, "1994"]

print(fruits, years)

""""
list method
append - add a single item to the list
extend - allows us to extend the list with another list
remove - taking an item out of a list
pop - to remove an element by index
sort - sorting list
in - to check membership.
count - check membership and the number of items with the count function.
index - check membership as well as the index position of the first item
"""
fruits.append("oranges")
print(fruits)

fruits.sort()
print(fruits)

fruits.extend(years)
print(fruits)

fruits.remove("peaches")
print(fruits)

fruits.pop(0)
print(fruits)

#concept of negative indexing, which starts at the end of a list.
fruits.pop(-1)
print(fruits)

#sort method can only be used with lists of like types.
#sorting fruits fail int & string
#fruits.sort()
#print(fruits)

numbers = [8,4, 6, 1.2, -1]
numbers.sort()
print(numbers)

print("pears" in fruits)
print("apples" in fruits)
fruits.append("apples")
fruits.append("pears")
print(fruits)

print(fruits.count("pears"))
print(fruits.count("apples"))

print(fruits.index("apples"))