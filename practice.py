from math import factorial

from pandas.io.formats.printing import pprint_thing


class Student():

    def __init__(self, first_name, last_name, student_id, major):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.major = major

Student1 = Student("Matthew", "Tipps", "0229232", "Computer Science")

def student_info(student):
    print("Student Information:")
    print("First and Last name: " + student.last_name + ", " + student.first_name)
    print("Student ID: " + student.student_id)
    print("Major: " + student.major)


student_info(Student1)

