# Class Circle
# ************

class Circle:

    # TODO: Define an instance attribute for PI
    PI = 3.14

    def __init__(self, radius=1.0):

        # TODO: Define an instance attribute for the radius
        self.radius=radius

    # TODO: Define the string representation method and print
    # r = {self.radius} c = {self.get_circumference()} a = {self.get_area()}
    def __str__(self):
        return f"r = {self.radius} c = {self.get_circumference()} a = {self.get_area()}"

    # TODO: Define a get_area() method and return the area
    def get_area(self):
        The_area = Circle.PI * self.radius * self.radius  
        return The_area

    
    # TODO: Define a get_circumference() method and return the circumference
    def get_circumference(self):
        The_circumference = 2 * Circle.PI * self.radius   
        return The_circumference

    # TODO: Define a set_color(color) method which sets the object attribute
    def set_color(self, color):
        self.color = color
    
    # TODO: Define a get_color() method which returns the object attribute
    def get_color(self):
        return self.color 

# Playground

# TODO: Create two circles one with radius 3, and one with the default radius
A = Circle(3)
B = Circle()

# TODO: Set the colors of your circles using the setter method
A.set_color('Yellow')
B.set_color('Black')

# TODO: Print the colors of your circles using the getter method
print(A.get_color())
print(B.get_color())

# TODO: Print your circles. How does this work?
print(A)
print(B)

# TODO: Print the radius and areas of your cricles
print (f"The radius of first circles  {A.radius}  {A.get_area()}")
print (f"The radius of Secound circles {B.radius}  {B.get_area()}")

# TODO: Print the circumference of your circles using the getter methods
print (f"The circumference of first circles   {A.get_circumference()}")
print (f"The circumference of Secound circles {B.get_circumference()}")