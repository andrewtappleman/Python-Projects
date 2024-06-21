class Position:
    def setX(self, x):
        self.myX = x

    def setY(self, y):
        self.myY = y

    def getX(self):
        return self.myX

    def printPosition(self):
        print("(",self.myX, ",", self.myY, ")")


class Shape:
    def __init__(self, name):
        self.nameId = name
        print("Create Shape instance: ", self.nameId)

    def print(self):
        print("Shape.print: ", self.nameId)

class Rectangle:
    def __init__(self, name, w, l):
        self.width = w
        self.length = l
        self.nameId = name
        print("Created Rectangle instance:", self.nameId, ",", self.width, ",", self.length)

    def print(self):
        print("Rectangle.print: ", self.nameId)

    def getPerimeter(self):
        return (2*self.length) + (2*self.width)

    def getArea(self):
        return (self.length * self.width)


if __name__ == "__main__":

    # create some instances of Shape class
    #s1 = Shape("myShape1")
    #s2 = Shape("myShape2")
    #create an instance of Rectangle class
    r1 = Rectangle("myRect1", 5, 8)
    r2 = Rectangle("Andrew", 7, 27)

    Luna = Position()
    Luna.setX(4.5)
    Luna.setY(-14.6)
    Luna.printPosition();

    Molly = Position()
    


    print(r1.width)

    # invoke print methods
    #s1.print()
    r1.print()
    r2.print()

    print("r1 area = ", r1.getArea())
    print("r1 perimeter = ", r1.getPerimeter())

    
