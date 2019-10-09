import math
# Base class.
class Shape():
    def __init__(self):
        print("You created a shape!")
        
# All classes below call upon the otherwise meaningless Shape class.        
class Circle(Shape):
    # Each shape requires one or more arguments which defines one or more dimensions.
    # From these dimensions the program calculates greater elements of the shapes such as area and perimeter.
    def __init__(self, radius):
        # Raises an error if an argument is realistically invalid.
        if radius <= 0:
            raise ValueError("The radius must be positive!")
        self.radius = radius
        self.perimeter = 2*math.pi*self.radius
        self.area = math.pi*(self.radius)**2
        self.eccentricity = 0
        print("You created a circle!")
        
    def mod_radius(self, new_radius):
        # Each shape class comes with a mod_xxx function to modify the original arguments.
        if new_radius <= 0:
            raise ValueError("The new radius must be positive!")
        self.radius = new_radius
        self.perimeter = 2*math.pi*self.radius
        self.area = math.pi*(self.radius)**2
        # The function rints the new dimensions, along with whether the resulting shape is a
        # special version of the base shape.
        print(f"The radius is now {self.radius}.")
        
class Ellipse(Shape):
    def __init__(self, major, minor):
        if major <= 0 or minor <= 0:
            raise ValueError("Both axes must be positive!")
        elif major < minor:
            raise ValueError("The major axis must be greater than or equal to the minor axis!")
        self.major = major
        self.minor = minor
        self.axes = [self.major,self.minor]
        # The eliptical perimeter is only an approximation (formula by the Indian mathematician Ramanujan).        
        h = ((self.major - self.minor)/(self.major + self.minor))**2
        self.perimeter = math.pi*(self.major + self.minor)*(1 + 3*h/(10 + (4 - 3*h)**(1/2)))
        self.area = math.pi*self.major*self.minor
        self.eccentricity = (self.major**2 - self.minor**2)**(1/2)/self.major
        print("You created an ellipse!")
        if self.major == self.minor:
            print("...and it happens to be a circle!")
        
    def mod_axes(self, new_major, new_minor):
        if new_major <= 0 or new_minor <= 0:
            raise ValueError("Both axes must be positive!")
        elif new_major < new_minor:
            raise ValueError("The new major axis must be greater than or equal to the new minor axis!")
        self.major = new_major
        self.minor = new_minor
        self.axes = [self.major,self.minor]
        h = ((self.major - self.minor)/(self.major + self.minor))**2
        self.perimeter = math.pi*(self.major + self.minor)*(1 + 3*h/(10 + (4 - 3*h)**(1/2)))
        self.area = math.pi*self.major*self.minor
        self.eccentricity = (self.major**2 - self.minor**2)**(1/2)/self.major
        print(f"The major axis is now {self.major}.")
        print(f"The minor axis is now {self.minor}.")
        if self.major == self.minor:
            print("You now have a circle!")
    
class Triangle_Sides(Shape):
    def __init__(self, side1, side2, side3):
        lesser_sides = [side1, side2, side3]
        maximum = lesser_sides.pop(lesser_sides.index(max(lesser_sides)))
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("All sides must be positive!")
        elif maximum >= sum(lesser_sides):
            raise ValueError("The maximum side length must be less than the othe two sides in order for this triangle to be possible.")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.sides = [self.side1,self.side2,self.side3]
        self.perimeter = sum(self.sides)
        p = self.perimeter/2
        self.area = math.sqrt(p*(p - self.side1)*(p - self.side2)*(p - self.side3))
        print("You created a triangle!")
        if (self.side1 == self.side2) or (self.side2 == self.side3) or (self.side3 == self.side1):
            print("...and it is icosceles! If you use the 'TriangleIcosceles' class with the side of this triangle which is NOT equal to the other two (or any side if they are all equal) as the first argument, and <name>.height as the second, you can gain for information on the triangle.")
            if self.side1 == self.side2:
                self.height = math.sqrt(self.side1**2 - (self.side3/2)**2)
            elif self.side2 == self.side3:
                self.height = math.sqrt(self.side2**2 - (self.side1/2)**2)
            elif self.side3 == self.side1:
                self.height = math.sqrt(self.side3**2 - (self.side2/2)**2)
            if self.side1 == self.side2 == self.side3:
                print("...and the sides are equal in length, so it is also equilateral!")
        
    def mod_sides(self, new_side1, new_side2, new_side3):
        lesser_sides = [new_side1, new_side2, new_side3]
        maximum = lesser_sides.pop(lesser_sides.index(max(lesser_sides)))
        if new_side1 <= 0 or new_side2 <= 0 or new_side3 <= 0:
            raise ValueError("All sides must be positive!")
        elif maximum >= sum(lesser_sides):
            raise ValueError("The maximum side length must be less than the othe two sides in order for this triangle to be possible.")
        self.side1 = new_side1
        self.side2 = new_side2
        self.side3 = new_side3
        self.sides = [self.side1,self.side2,self.side3]
        self.perimeter = sum(self.sides)
        p = self.perimeter/2
        self.area = math.sqrt(p*(p - self.side1)*(p - self.side2)*(p - self.side3))
        print(f"Side 1's length is now {self.side1}.")
        print(f"Side 2's length is now {self.side2}.")
        print(f"Side 3's length is now {self.side3}.")
        if (self.side1 == self.side2) or (self.side2 == self.side3) or (self.side3 == self.side1):
            print("Your triangle is now isosceles! If you use the 'TriangleIcosceles' class with the side of this triangle which is NOT equal to the other two (or any side if they are all equal) as the first argument and <name>.height as the second, you can gain more information on your happy little triangle.")
            if self.side1 == self.side2:
                self.height = math.sqrt(self.side1**2 - (self.side3/2)**2)
            elif self.side2 == self.side3:
                self.height = math.sqrt(self.side2**2 - (self.side1/2)**2)
            elif self.side3 == self.side1:
                self.height = math.sqrt(self.side3**2 - (self.side2/2)**2)
        else:
            del self.height
    
class Triangle_WidthHeight(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Both the width and the height must be positive!")
        self.width = width
        self.height = height
        self.area = self.width*self.height/2
        print("You created a triangle!")
        if self.width == self.height:
            print("...and it is isosceles! If you use the 'TriangleIcosceles' class with the same arguements, you can get more information on your happy little triangle.")
        
    def mod_width_height(self,new_width,new_height):
        if new_width <= 0 or new_height <= 0:
            raise ValueError("Both the width and the height must be positive!")
        if self.width == self.height:
            iso = True
        else:
            iso = False
        self.width = new_width
        self.height = new_height
        self.area = self.width*self.height/2
        print(f"The width is now {self.width}")
        print(f"The height is now {self.height}")
        if self.width == self.height and not iso:
            self.height_iso = math.hypot(self.width,self.height/2)
            print("Your triangle is now isosceles!\nIf you use the 'TriangleIcosceles' class with either the width or the height as the first argument and <name>.height_iso as the second argument, you can gain additioinal information on your happy little triangle.")
        else:
            try:
                del self.height_iso
            except:
                pass
            if iso:
                self.height_iso = math.hypot(self.width,self.height/2)      

# The next two shapes use the same arguments/dimensions as Triangle_WidthHeight,
# so they uses Triangle_WidthHeight as the base class.
class Triangle_Right(Triangle_WidthHeight):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Both the width and the height must be positive!")
        self.width = width
        self.height = height
        self.area = self.width*self.height/2
        self.hypotenuse = math.hypot(self.width,self.height)
        self.sides = [self.width, self.height, self.hypotenuse]
        self.perimeter = sum(self.sides)
        self.angle_bottom = math.atan(self.height/self.width)
        self.angle_bottom_degrees = math.degrees(self.angle_bottom)
        self.angle_top = math.atan(self.width/self.height)
        self.angle_top_degrees = math.degrees(self.angle_top)
        self.angles = [self.angle_bottom, self.angle_top, math.pi/2]
        self.angles_degrees = [self.angle_bottom_degrees, self.angle_top_degrees, 90]
        print("You created a right triangle!")
        if self.width == self.height:
            print("...and it is isosceles!")    
            
    def mod_width_height(self, new_width, new_height):
        if new_width <= 0 or new_height <= 0:
            raise ValueError("Both the width and the height must be positive!")
        if self.width == self.height:
            iso = True
        else:
            iso = False
        self.width = new_width
        self.height = new_height
        self.area = self.width*self.height/2
        self.hypotenuse = math.hypot(self.width,self.height)
        self.sides = [self.width, self.height, self.hypotenuse]
        self.perimeter = sum(self.sides)
        self.angle_bottom = math.atan(self.height/self.width)
        self.angle_bottom_degrees = math.degrees(self.angle_bottom)
        self.angle_top = math.atan(self.width/self.height)
        self.angle_top_degrees = math.degrees(self.angle_top)
        self.angles = [self.angle_bottom, self.angle_top, math.pi/2]
        self.angles_degrees = [self.angle_bottom_degrees, self.angle_top_degrees, 90]
        print(f"The width is now {self.width}")
        print(f"The height is now {self.height}")
        if self.width == self.height and not iso:
            if iso:
                print("Your triangle is still icosceles.")
            else:
                print("Your triangle is now isosceles!")
        elif self.width != self.height and iso:
            print("Your triangle is no longer isosceles.")
                
class Triangle_Isosceles(Triangle_WidthHeight):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Both the width and the height must be positive!")
        self.width = width
        self.height = height
        self.area = self.width*self.height/2
        self.side = math.hypot(self.width/2, self.height)
        self.sides = [self.width, self.side, self.side]
        self.perimeter = self.width + 2*self.side
        self.side_angle = math.atan(self.height/(self.width/2))
        self.side_angle_degrees = math.degrees(self.side_angle)
        self.top_angle = math.pi - 2*self.side_angle
        self.top_angle_degrees = math.degrees(self.top_angle)
        self.angles = [self.top_angle, self.side_angle, self.side_angle]
        self.angles_degrees = [self.top_angle_degrees, self.side_angle_degrees, self.side_angle_degrees]
        print("You created an icoseles triangle!")
        if self.top_angle == math.pi/2:
            print("...and it is also right!")
        elif math.isclose(self.top_angle, math.pi/3):
            print("...and it is also equilateral!")
        
    def mod_width_height(self, new_width, new_height):
        if new_width <= 0 or new_height <= 0:
            raise ValueError("Both the width and the height must be positive!")
        if self.top_angle == math.pi/2:
            right = True
        else:
            right = False
        if math.isclose(self.top_angle, math.pi/3):
            equi = True
        else:
            equi = False
        self.width = new_width
        self.height = new_height
        self.area = self.width*self.height/2
        self.side = math.hypot(self.width/2, self.height)
        self.sides = [self.width, self.side, self.side]
        self.perimeter = self.width + 2*self.side
        self.side_angle = math.atan(self.height/(self.width/2))
        self.side_angle_degrees = math.degrees(self.side_angle)
        self.top_angle = math.pi - 2*self.side_angle
        self.top_angle_degrees = math.degrees(self.top_angle)
        self.angles = [self.top_angle, self.side_angle, self.side_angle]
        self.angles_degrees = [self.top_angle_degrees, self.side_angle_degrees, self.side_angle_degrees]
        print(f"The width is now {self.width}")
        print(f"The height is now {self.height}")
        if math.isclose(self.top_angle, math.pi/3):
            if equi:
                print("You still have an equilateral triangle.")
            else:
                if right:
                    print("Your triangle is no longer right...\n...but it is now equilateral!")
                else:
                    print("You now also have an equilateral triangle!")
        elif self.top_angle == math.pi/2:
            if right:
                print("You still have a right trinagle.")
            else:
                if equi:
                    print("Your triangle is no longer equilateral...\n...but it is now right!")
                else:
                    print("You now also have a right triangle!")
        elif not math.isclose(self.top_angle, math.pi/3):
            if equi:
                print("You no longer have an equilateral triangle.")
        elif self.top_angle != math.pi/2:
            if right:
                print("You no longer have a right triangle.")

class Square(Shape):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("The sides must be positive!")
        self.side = side
        self.perimeter = 4*self.side
        self.area = self.side**2
        print("You created a square!")
        
    def mod_side(self, new_side):
        if new_side <= 0:
            raise ValueError("The new sides must be positive!")
        self.side = new_side
        self.perimeter = 4*self.side
        self.area = self.side**2
        print(f"The sides now have a length of {self.side}.")
        
class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Both the width and the height must be positive!")
        self.width = width
        self.height = height
        self.perimeter = 2*(self.width + self.height)
        self.area = self.width*self.height
        print("You created a rectangle!")
        if self.width == self.height:
            print("...and it happens to be a square!")
            
    def mod_sides(self, new_width, new_height):
        if new_width <= 0 or new_height <= 0:
            raise ValueError("Both the width and the height must be positive!")
        if self.width == self.height:
            square = True
        else:
            square = False
        self.width = new_width
        self.height = new_height
        self.perimeter = 2*(self.width + self.height)
        self.area = self.width*self.height      
        print(f"The width now has a length of {self.width}.")
        print(f"The height now has a length of {self.height}.")
        if self.width == self.height:
            if square:
                print("You still have a square.")
            elif not square:
                print("You now also have a square!")
        else:
            if square:
                print("You no longer have a square.")
    
class Parallelogram(Shape):
    def __init__(self, width, diagonal, angle):
        if width <= 0 or diagonal <= 0:
            raise ValueError("Both the width and the diagonal must be positive!")
        if angle <= 0 or angle >= math.pi:
            raise ValueError("This angle does not belong on a parallelogram. Please make sure you are using radians, not degrees.")            
        self.width = width
        self.diagonal = diagonal
        self.sides = [self.width, self.diagonal, self.width, self.diagonal]
        self.angle = angle
        self.angle_degrees = round(math.degrees(self.angle), 4)
        self.angles = [self.angle, math.pi - self.angle, self.angle, math.pi - self.angle]
        self.angles_degrees = [self.angle_degrees, 180 - self.angle_degrees, self.angle_degrees, 180 - self.angle_degrees]
        self.height = self.diagonal*math.sin(self.angle)
        self.area = self.width*self.height
        self.perimeter = 2*(self.width*self.diagonal)
        print("You created a parallelogram!")
        if self.width == self.diagonal:
            print("The sides are equal, so it is also a rhombus!")
            if self.angle == math.pi/2:
                print("The angles are right, so it is also a rectangle!")
                print("The angles are right AND the sides are congruent, so it is also a square!")
        elif self.angle == math.pi/2:
            print("The angles are right, so it is also a rectangle!")
            
    def mod_parallelogram(self, new_width, new_diagonal, new_angle):
        if self.width == self.diagonal:
            rhom = True
        else:
            rhom = False
        if self.angle == math.pi/2:
            right = True
        else:
            right = False
        self.width = new_width
        self.diagonal = new_diagonal
        self.sides = [self.width, self.diagonal, self.width, self.diagonal]
        if self.angle <= 0 or self.angle >= math.pi:
            raise ValueError("This angle does not belong on a parallelogram. Please make sure you are using radians, not degrees.")
        self.angle = new_angle
        self.angle_degrees = round(math.degrees(self.angle), 4)
        self.angles = [self.angle, math.pi - self.angle, self.angle, math.pi - self.angle]
        self.angles_degrees = [self.angle_degrees, 180 - self.angle_degrees, self.angle_degrees, 180 - self.angle_degrees]
        self.height = self.diagonal*math.sin(self.angle)
        self.area = self.width*self.height
        self.perimeter = 2*(self.width*self.diagonal)
        print(f"The width is now {self.width}.")
        print(f"The side diagonal to the width is now {self.diagonal}.")
        print(f"One of the angles is now {self.angle} ({self.angle_degrees} in degrees).")
        if self.width == self.diagonal:
            if rhom:
                if right:
                    if self.angle == math.pi/2:
                        print("You still have a rhombus.")
                        print("You still have a rectangle.")
                        print("You still have a square.")
                    else:
                        print("You no longer have a rectangle or a square, but you still have a rhombus!")
                else:
                    if self.angle == math.pi/2:
                        print("You still have a rhombus.")
                        print("The angles are right, so it is also a rectangle!")
                        print("The angles are right AND the sides are congruent, so it is also a square!")
                    else:
                        print("You still have a rhombus.")
            else:                
                if right:
                    if self.angle == math.pi/2:
                        print("The sides are congruent, so you now also have a rhombus!")
                        print("The angles are right AND the sides are congruent, so it is also a square!")
                    else:
                        print("You no longer have a rectangle, but the sides are congruent, so you now have a rhombus!")
                else:
                    if self.angle == math.pi/2:
                        print("The angles are right, so it is also a rectangle!")
                        print("The angles are right AND the sides are congruent, so it is also a square!")
                    else:
                        print("You now also have a rhombus!")                       
        elif self.angle == math.pi/2:
            if right:
                if rhom:
                    print("You no longer have square or a rhobmus, but you still have a rectangle!")
                else:
                    print("You still have a rectangle.")
            else:
                if rhom:
                    print("You no longer have a rhombus, but the angles are right, so you now have a rectangle!")
                else:
                    print("The angles are right, so you now have a rectangle!")
        elif self.width != self.diagonal and self.angle != math.pi/2:
            if right:
                if rhom:
                    print("You no longer have a square, rhombus, or rectangle.")
                else:
                    print("You no longer have a rectangle.")
            elif rhom:
                print("You no longer have a rhombus.")
                
class Pentagon(Shape):
    def __init__(self,side):
        if side <= 0:
            raise ValueError("The sides must have a positive length!")
        self.side = side
        self.apothem = side*(math.tan(0.3*math.pi))/2
        self.area = 5/2*self.side*self.apothem        
        self.perimeter = 5*self.side
        print("You created a regular pentagon!")

    def mod_sides(self,new_side):
        if new_side <= 0:
            raise ValueError("The sides must have a positive length!")
        self.side = new_side
        self.apothem = new_side*(math.tan(0.3*math.pi))/2
        self.area = 5/2*self.side*self.apothem        
        self.perimeter = 5*self.side
        print(f"The side length is now {self.side}.")
    
class Hexagon(Shape):
    def __init__(self,side):
        if side <= 0:
            raise ValueError("The sides must have a positive length!")
        self.side = side
        self.apothem = side*(math.tan(math.pi/3))/2
        self.area = 3*self.side*self.apothem
        self.perimeter = 6*self.side
        print("You created a regular hexagon!")

    def mod_sides(self,new_side):
        if new_side <= 0:
            raise ValueError("The sides must have a positive length!")
        self.side = new_side
        self.apothem = new_side*(math.tan(0.3*math.pi))/2
        self.area = 3*self.side*self.apothem        
        self.perimeter = 6*self.side
        print(f"The side length is now {self.side}.")

# Notice that when you call this shape with a high number of sides, the area and perimeter
# are close to the area and perimeter of a circle with the apothem as the radius.   
class Polygon(Shape):
    def __init__(self,number_of_sides,side_length):
        if number_of_sides < 3:
            raise ValueError("A polygon must have at least three sides, so 'number_of_sides' must be greater than or equal to 3.")
        elif type(number_of_sides) != int:
            raise TypeError("The number of sides must be an integer!")
        if side_length <= 0:
            raise ValueError("The sides must have a positive length!")
        self.side_length = side_length
        self.number_of_sides = number_of_sides
        self.apothem = self.side_length*(math.tan((self.number_of_sides-2)*math.pi/2/self.number_of_sides))/2
        self.area = self.number_of_sides/2*self.side_length*self.apothem
        self.perimeter = self.number_of_sides*self.side_length
        print("You created a regular polygon!")
        
    def mod_polygon(self, new_number_of_sides, new_side_length):
        if new_number_of_sides < 3:
            raise ValueError("A polygon must have at least three sides, so 'number_of_sides' must be greater than or equal to 3.")
        elif type(new_number_of_sides) != int:
            raise TypeError("The number of sides must be an integer!")
        if new_side_length <= 0:
            raise ValueError("The sides must have a positive length!")
        self.side_length = new_side_length
        self.number_of_sides = new_number_of_sides
        self.apothem = self.side_length*(math.tan((self.number_of_sides-2)*math.pi/2/self.number_of_sides))/2
        self.area = self.number_of_sides/2*self.side_length*self.apothem
        self.perimeter = self.number_of_sides*self.side_length
        print(f"The number of sides is now {self.number_of_sides}.")
        print(f"The side length is now {self.side_length}.")
