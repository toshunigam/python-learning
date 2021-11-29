class Student:
    student_count = 0
    name = None
    age = None
    stream = None
    def __init__(self, name, age, stream):
        self.name = name
        self.age = age
        self.stream = stream
        Student.student_count += 1
        return
    def display_student(self):
        print self.name, self.age, self.stream
        return
    def display_studentcount(self):
        print "Student Count is:",self.student_count
        return
stdnt1 = Student("Toshu",34,"IT")
stdnt2 = Student("Indra",35,"CS")
stdnt3 = Student("Satish",32,"EC")
stdnt1.display_student()
stdnt2.display_student()
stdnt3.display_student()
stdnt3.display_studentcount()
