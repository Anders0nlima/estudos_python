class Student:

    class_year = 2025
    num_student = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1

student1 = Student("Anderson", 20)
student2 = Student("Ana", 19)
student3 = Student("Leticia", 21)

print(student1.name)
print(student1.age)
print(Student.class_year)
print(Student.num_student)

