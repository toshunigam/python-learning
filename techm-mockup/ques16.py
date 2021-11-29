class Shape:
    def draw(self):
        print "This is generic shape"
        return
    def rotate(self):
        print "Rotating generically"
        return

class Circle(Shape):
    def draw(self):
        print "Circle Drawn"
        return
    def rotate(self):
        print "Circle rotated"
        return
class Rectangle(Shape):
    def draw(self):
        print "Rectable drawn"
        return
    def rotate(self):
        print "Rectangle rotated"
        return
cir1 = Circle()
rec1 = Rectangle()
cir1.draw()
cir1.rotate()
rec1.draw()
rec1.rotate()


