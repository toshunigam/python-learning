class Rectangle:
    length=0
    breadth=0
    def __init__(self, length, breadth):
        self.length = length
        self.breadth= breadth
        return
    def cal_area(self):
        c = self.length*self.breadth
        return c
len1 = int(raw_input("Enter length:"))
bre1 = int(raw_input("Enter Breadth:"))
rec1 = Rectangle(len1,bre1)

len2 = int(raw_input("Enter length:"))
bre2 = int(raw_input("Enter Breadth:"))
rec2 = Rectangle(len2,bre2)

len3 = int(raw_input("Enter length:"))
bre3 = int(raw_input("Enter Breadth:"))
rec3 = Rectangle(len3,bre3)

len4 = int(raw_input("Enter length:"))
bre4 = int(raw_input("Enter Breadth:"))
rec4 = Rectangle(len4,bre4)

len5 = int(raw_input("Enter length:"))
bre5 = int(raw_input("Enter Breadth:"))
rec5 = Rectangle(len5,bre5)

print "Rectable 1:",rec1.cal_area()
print "Rectable 2:",rec2.cal_area()
print "Rectable 3:",rec3.cal_area()
print "Rectable 4:",rec4.cal_area()
print "Rectable 5:",rec5.cal_area()
