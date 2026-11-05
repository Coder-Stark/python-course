#Dictionary

"""
key points to remember

key must be unique
key can be strings, nubmers, tuples, etc.
values can be of any data type
Dictionaries are mutable (changeable)
access values using keys
"""

student = {
    "name": "Shivam",
    "age": 25,
    "city": "Delhi"
}

print(student)
print(type(student))

print(student["name"])           #access via key
print(student["age"])

student["gender"] = "male"       #insert
print(student)

student["age"] = 20              #update
print(student)


student2 = {
    "name": "Kumar",
    "age": 23,
    "city": "UP",
    "marks": "90.5",
    "passed": True,
    "skills": ["MERN", "React Native", "DSA"]
}

print(student2)
print(student2["skills"])
print(student2["skills"][0])               

student3 = {}
# student3 = dict()                  #same as above
print(student3)


student4 = dict(
    name = "Rajbhar",                #no inverted quotes for key
    age = 24
)
print(student4)


students = {                         #nested dictionaries
    "student1": {
        "name": "Ram",
        "age": 20
    },
    "student2": {
        "name": "Shyam",
        "age": 22
    },
}
print(students)
print(students["student1"]["name"])


stud = {
    "name": "Kumar",
    "age": 23,
    "city": "UP",
    "marks": "90.5",
    "passed": True,
    "skills": ["MERN", "React Native", "DSA"]
}

#using for loop print all values
for value in stud.values():
    print(value)

#using for loop rint all keys and values
for key, value in stud.items():
    print(key, " : ", value)


#if condition
if "name" in stud:
    print("Key Found")