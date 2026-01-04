# You are given a list of programming languages:
# ["Python", "Java", "C++", "Python", "Java", "C"]
# Convert it into a set and print how many unique languages Divya knows.

programmingList= ["Python", "Java", "C++", "Python", "Java", "C"]
print(type(programmingList))

# convert a list into sets

programmingSet= set(programmingList)
print(programmingSet)
print(type(programmingSet))
print("Divya knows these languages", len(programmingSet))