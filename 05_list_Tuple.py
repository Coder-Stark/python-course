#List -> ["x", "y", "z"]
"""
Mutable
Allow Duplicates
Slower (then tuple)
"""
fruits = ["Apple", "Banana", "Mango", "Grapes"]
print(fruits)
print(fruits[0])
print(fruits[-1])

print(fruits[1:3])        #3rd idx excluded

fruits[1] = "Orange"
print(fruits)

number = [10, 20, 30, 40, 10]     #duplicate allowed in list
print(number)

data = ["Shivam", 25, 75.50, True]
print(data)
name, age, marks, bachelor = data
print("Name : ", name)
print("Age : ", age)
print("Marks : ", marks)
print("Is Bachelor: ", bachelor)


#TUPLE -> ("x", "y", "z")
"""
Immutable
Allow Duplicates
Faster (then list)
"""

fruits2 = ("Apple", "Banana", "Mango")
print(fruits2)
print(fruits2[0])
print(fruits2[-1])

# fruits2[1] = "Orange"               #'tuple' object does not support item assignment
# print(fruits2)

veg = ("Potato", "Carrot")
mix = fruits2 + veg
print(mix)

"""
output

['Apple', 'Banana', 'Mango', 'Grapes']
Apple
Grapes
['Banana', 'Mango']
['Apple', 'Orange', 'Mango', 'Grapes']
[10, 20, 30, 40, 10]
['Shivam', 25, 75.5, True]
Name :  Shivam
Age :  25
Marks :  75.5
Is Bachelor:  True
('Apple', 'Banana', 'Mango')
Apple
Mango
('Apple', 'Banana', 'Mango', 'Potato', 'Carrot')

"""