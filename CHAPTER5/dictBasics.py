#  Dictionary Basics

student= {
    "name" : "Saumya Singh",
    "age"  : 25,
    "city" : "Delhi",
    "RollNumber" : 23,
    "name" : "Khushi"
    }
print(type(student))
print(student["name"])
print(student)
print(student["city"])

student["city"] = "Hyderabad"
print(student)

student["favSubject"] = "Chemistry"
print(student)

student.pop("favSubject")
print(student)

print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))



