"""
String
Integer
Float
Boolean
List                 ["x", "y", "z"]
Tuple                ("x", "y", "z")
Dictionary           {first: "Jane", age: 25}
Set                  {"read", "green"}

#less used
Complex               x = 4 + 6j
Range                 x = range(5)
frozenset             x = frozenset([1, 2, 3])
None                  x = None
Bytes                 x = b"Hello"
Bytearray             x = bytearray([65, 66, 67])
Memoryview            x = memoryview(bytes([65, 66, 67]))


Category wise
Numeric               int, float, complex
Boolean               bool
Text                  str
Sequence              list, tuple, range
Mapping               dict
Set                   set, frozenset
Binary                bytes, bytearray, memoryview
Special               NoneType(None)
"""

x = "hello world"
print(type(x))        #<class 'str'>
y = 20
print(type(y))        #<class 'int'>
b = True
print(type(b))        #<class 'float'>
z = 30.50
print(type(z))        #<class 'bool'>

i = 4 + 6j
print(type(i))        #<class 'complex'>

l = ["apple", "banana", "mango"]
print(type(l))        #<class 'list'>

d = {
    "name": "Shivam",
    "age": 25,
    "course": "Python"
}
print(type(d))       #<class 'dict'>

n = None
print(type(n))       #<class 'NoneType'>

ba = bytearray([65, 66, 67])
print(ba)            #bytearray(b'ABC')
print(type(ba))      #<class 'bytearray'>