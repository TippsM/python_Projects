first_name = "Matthew"
last_name = "Tipps"

print(first_name, last_name)

university = "FIU"
year = "2022"

print("{} has been studying at {} since {}".format(first_name, university, year))

a = 10
b = 3
print(a//b)

import math

print(math.sqrt(16))

print("4" + "a")

for i in range(5):
    print(i)
    print("FIU")


professor = ["Greg", "Richard", "Kianoosh", "George"]
print("\n",professor,type(professor), len(professor))
print(professor[2].title())
print(professor[-1])
print(professor[1:3]) # accessing elements 1 & 2
print(professor[1:9])

print(professor[:4]) # accessing elements from beginning to 3
print(professor[1:]) # accessing elements from 1 to end of list

professor.append("Waqas")
print(professor)
professor.insert(2, "Jason")
print(professor)

professor.extend(["Mark", "Leo", "Patricia"])
print(professor)

professor.remove("Leo")
professor.pop(6)
print(professor.pop())

x = professor.index("Mark")

print(x)