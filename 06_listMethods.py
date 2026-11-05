"""
Methods

insert()
append()
count()
clear()
copy()
extend()
index()
pop()
remove()
reverse()
sort()

len(list)
max(list)
min(list)
list(seq)
"""

fruits = ["apple", "banana", "cherry"]

print(fruits)

fruits.append("Mango")          #at the end
print(fruits)

fruits.insert(1, "Grapes")      #at 1 (index)
print(fruits)

fruits.remove("banana")         #remove particular value
print(fruits)

fruits.pop()                    #remove last index's value
print(fruits)

fruits.pop(0)                   #remove particular index's value
print(fruits)

fruits.clear()                  #clear all list
print(fruits)


veg = ["potato", "tomato", "pea", "brinjal"]
print(veg)

veg.sort()
print(veg)

veg.sort(reverse=True)
print(veg)

veg2 = ["potato", "Tomato", "pea", "brinjal", "Z"]
print(veg2)

veg2.sort()                  #first sort Capital letter then small letter (ascii value)
print(veg2)

veg2.reverse()
print(veg2)


x = veg2.copy()
print(x)
y = list(veg2)              #same as copy
print(y)
z = veg2[:]                 #same as copy
print(z)

a = veg2[1:]                #copy from index to end
print(a)

b = veg2[0:2]              #copy from index to index (excluded idx)
print(b)

fruits2 = ["cherry", "guava", "papaya", "cherry"]
fruits2.extend(veg2)       #merge 
print(fruits2)

j = fruits2.index("cherry")     #write its first index (if exist) else error
print(j)                    
k = fruits2.index("cherry", 3)  #search from idx to end
print(k)

m = fruits2.index("cherry", 3, 5)  #search from idx to idx
print(m)


n = fruits2.count("cherry")     #count of occurance
print(n)

num = [10, 20, 50, 40, 0]

o = len(num)                #total length of list
print(o)

p = max(num)
print(p)

q = min(num)
print(q)


colors = ("red", "green")
color_list = list(colors)        #convert to list (from tuple)
print(color_list)

color = "red"
color_list2 = list(color)       #convert to list (with letters)
print(color_list2)


"""
outputs

['apple', 'banana', 'cherry']
['apple', 'banana', 'cherry', 'Mango']
['apple', 'Grapes', 'banana', 'cherry', 'Mango']
['apple', 'Grapes', 'cherry', 'Mango']
['apple', 'Grapes', 'cherry']
['Grapes', 'cherry']
[]
['potato', 'tomato', 'pea', 'brinjal']
['brinjal', 'pea', 'potato', 'tomato']
['tomato', 'potato', 'pea', 'brinjal']
['potato', 'Tomato', 'pea', 'brinjal', 'Z']
['Tomato', 'Z', 'brinjal', 'pea', 'potato']
['potato', 'pea', 'brinjal', 'Z', 'Tomato']
['potato', 'pea', 'brinjal', 'Z', 'Tomato']
['potato', 'pea', 'brinjal', 'Z', 'Tomato']
['potato', 'pea', 'brinjal', 'Z', 'Tomato']
['pea', 'brinjal', 'Z', 'Tomato']
['potato', 'pea']
['cherry', 'guava', 'papaya', 'cherry', 'potato', 'pea', 'brinjal', 'Z', 'Tomato']
0
3
3
2
5
50
0
['red', 'green']
['r', 'e', 'd']

"""