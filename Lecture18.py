"""
OOP
"""


class Student:

    number_of_students = 0
    school = 'Science School'

    def __init__(self, first_name, last_name, major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        Student.number_of_students += 1

    def full_name_with_major(self):
        return f'{self.first_name} {self.last_name} is a {self.major} major'

    def full_name_major_school(self):
        return f'{self.first_name} {self.last_name} is a {self.major} major from the {self.school}'

    @classmethod
    def set_school(cls, school):
        cls.school = school



student_1 = Student('Diego', 'Manuel', 'Computer Science')
student_2 = Student('Lara', 'Manuel', 'Pure Mathematics')

print(student_1.first_name)
print(student_1.last_name)
print(student_1.major)
print(student_2.__dict__)
print(student_2.full_name_with_major())
print(Student.full_name_with_major(student_1))

print(student_2.full_name_major_school())
print(Student.full_name_major_school(student_1))

print(student_1.number_of_students)
print(student_2.number_of_students)
print(Student.number_of_students)

print(Student.school)
print(student_1.school)
print(student_2.school)
Student.set_school('Porto Polytechnic')
student_1.set_school('UNISA')
student_2.set_school('Universidade Nova de Lisboa')
print(Student.school)
print(student_1.school)
print(student_2.school)
