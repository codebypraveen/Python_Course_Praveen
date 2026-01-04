#tuple Basics

myTuple= (78, 90, 75)
studentTuple=("khushi", "Divya", "Ishaan")

# studentTuple[1]="Aanchal"
# tuples are immutable/ not changeable..

print(studentTuple[1])

# empty Tuple
emptyTuple=()
singleTuple= (1, )
print(type(emptyTuple))
print(type(singleTuple))

print(studentTuple.index("Divya"))
print(studentTuple.count("Aditya"))
