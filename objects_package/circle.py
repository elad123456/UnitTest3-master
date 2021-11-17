class circle:
    def __init__(self):
        self.radius=0
        self.pi=3.14
    def area(self):
        return self.radius*self.radius*self.pi
    def circumference(self):
        return 2*self.radius*self.pi
circle1=circle()
circle1.radius=int(input("enter the circel's radius: "))
print(circle1.area())
print(circle1.circumference())