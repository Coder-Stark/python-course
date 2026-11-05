"""
Methods

count()
index()


len(tuple)
max(tuple)
min(tuple)
tuple(iterable)

"""

fruits = ("apple", "banana", "apple", "orange", "apple")
# fruits = "apple", "banana", "apple", "orange", "apple"       #same as above (without any bracket -> touple)
print(fruits)
print(fruits.count("apple"))
print(fruits[0:2])                           #print range (exclude last idx)


nested_tuple = ((10, 20), (30, 40), (50, 60))
print(nested_tuple)
print(nested_tuple[0])
print(nested_tuple[0][0])

x = fruits.index("apple")
print(x)
y = fruits.index("apple", 1, 4)         #search idx between 1 to 4(excluded)
print(y)

numbers = (20, 31, 45, 66, 10)

z = max(numbers)
print(z)

m = min(numbers)
print(m)

l = len(numbers)
print(l)


numbers = [20, 34, 51, 45, 10]

t = tuple(numbers)                    #convert into tuple
print(t)

str = "hello"
ts = tuple(str)
print(ts)

colors = {"red", "green"}
tst = tuple(colors)
print(tst)

r = range(5)                     #0 to 4
tr = tuple(r)
print(tr)

"""
outputs

('apple', 'banana', 'apple', 'orange', 'apple')
3
('apple', 'banana')
((10, 20), (30, 40), (50, 60))
(10, 20)
10
0
2
66
10
5
(20, 34, 51, 45, 10)
('h', 'e', 'l', 'l', 'o')
('green', 'red')
(0, 1, 2, 3, 4)

"""