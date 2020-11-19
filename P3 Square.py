# Class Square
class Square:

   
    def __init__(self, length, width):
        # TODO: Define the instance attributes
        self.length = int(length)
        self.width = int(width)

    # TODO: Define the string representation method and print the details of your square
    def __str__(self):
        return f"The length = {self.length} The width {self.width} a = {self.find_area()}"

    # TODO: Define a find_area() method and return the area
    def find_area(self):
        The_area = self.length * self.width
        return f"The area of the square is = {The_area}"
        

    # TODO: Define a find_perimeter() method and return the perimeter
    def find_perimeter(self):
        The_perimete = 2 * self.length + 2* self.width
        return f"The perimete of the square is = {The_perimete}"
    
    # TODO: Define a set_color(color) method which sets the object attribute
    def set_color(self, color):
        self.color = color
     
    
    # TODO: Define a get_color() method which returns the object attribute
    def get_color(self):
        return self.color

# Playground

# TODO: Create two squares
A = Square('2','5')
B = Square('1','4')

# TODO: Set the colors of your squares using the setter method
A.set_color('Black')
B.set_color('Red')

# TODO: Print the colors of your squares using the getter method
print(A.get_color())
print(B.get_color())

# TODO: Print your squares. How does this work?
print(A)
print(B)

# TODO: Print the length, width, and area of your squares
print (f"The length of A  {A.length} and the width {A.width} and the area {A.find_area()}")
print (f"The length of B  {B.length} and the width {B.width} and the area {B.find_area()}")

# TODO: Print the perimeter of your circles using the find_perimeter() method
print (f"The perimeter of A   {A.find_perimeter()}")
print (f"The perimeter of B {B.find_perimeter()}")