class Quadrilateral:
    #side1 = 0
    def __init__(self,side1,side2,side3,side4):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4
    def perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4
    def whatAmI(self):
        print( "I am a quadrilateral")

x = Quadrilateral(1, 33, 57, 2)
print(x.perimeter())


class Rectangle(Quadrilateral):
    def __init__(self,side1,side2):
        super().__init__(side1,side2,side1,side2)
    def area(self):
        return self.side1 * self.side2
    def whatAmI(self):
        super().whatAmI()
        print("I am a rectangle")
y = Rectangle(3, 4)
print(y.area())
print(y.perimeter())

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)

z = Square(20)
print(z.area())
print(z.perimeter())


x.whatAmI()
y.whatAmI()
z.whatAmI()
