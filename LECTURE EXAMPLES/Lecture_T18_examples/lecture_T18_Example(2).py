#Create parent class
class Person:
    #Define contructor
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

class Student(Person):
    def __init__(self, name, surname, age, student_no):
        super().__init__(name, surname, age)
        self.student_no = student_no

class Lecturer(Person):
    def __init__(self, name, surname, age, staff_no):
        super().__init__(name, surname, age)
        self.staff_no = staff_no


def main():
    student1 = Student("Samantha", "Clarke", 19, 123456)
    lecturer1 = Lecturer("Yolandi", "Viljoen", 29, 523689 )

    print(lecturer1.name) # name = "Samantha"
    print(lecturer1.surname)
    print(lecturer1.age)
    print(lecturer1.staff_no)


main()    

