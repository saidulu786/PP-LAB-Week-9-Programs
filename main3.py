class Circle:
    PI = 3.142
    
    def __init__(self, radius):
        self.radius = radius
        
    def area (self):
        return (Circle.PI * self.radius * self.radius)
    
    def circumference(self):
        return (2 * Circle.PI * self.radius)

r = int(input("Enter the radius of circle"))
c1 = Circle(r)
print ("Area of C1 circle is: ", c1.area())
print ("Circumference of C1 Circle is: ", c1.circumference())