class Student:
    name=None
    age=None
    course=None
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course
        return
    def display_student_details(self):
        print self.name, self.age, self.course
        return
class Employee:
    eid=None
    designation=None
    def __init__(self, eid, designation):
        self.eid = eid
        self.designation = designation
        return
    def display_employee_details(self):
        print self.eid, self.designation
        return
class Person(Student,Employee):
    name=None
    age=None
    course=None
    eid=None
    designation=None
    def __init__(self,name,age,course,eid,designation):
        self.name = name
        self.age = age
        self.course = course
        self.eid = eid
        self.designation = designation
        Student(name, age, course)
        Employee(eid, designation)
        return
    def display_person_details(self):
        print self.name, self.age, self.course, self.eid, self.designation
        return
person1 = Person('Toshu',34,"Python",795345,'tech lead')
person1.display_person_details()
person1.display_student_details()
person1.display_employee_details()
