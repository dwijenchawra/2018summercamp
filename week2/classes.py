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
#print(x.perimeter())


class Rectangle(Quadrilateral):
    def __init__(self,side1,side2):
        super().__init__(side1,side2,side1,side2)
    def area(self):
        return self.side1 * self.side2
    def whatAmI(self):
        super().whatAmI()
        print("I am a rectangle")
y = Rectangle(3, 4)
#print(y.area())
#print(y.perimeter())

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)

z = Square(20)
#print(z.area())
#print(z.perimeter())


#x.whatAmI()
#y.whatAmI()
#z.whatAmI()


class SumOfNum:
    def sayHello(self, num1=None, num2=None, num3=None):
        if num3 is not None:
            print(num1+num2+num3)
        elif num2 is not None:
            print(num1+num2)
        elif num1 is not None:
            print(num1)
        else:
            print("0")

def foo():
    return "foo"

print(foo())

def foo2():
    sqr = Square(4)
    return sqr

x = input("input something")
input = "oops"
print(input)
y = input("oops")

obj = SumOfNum()
obj.sayHello(3)
obj.sayHello(3, 4)
obj.sayHello(3, 4, 5)
obj.sayHello()
