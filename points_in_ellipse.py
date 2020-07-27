from math import pi, sqrt, sin, cos
class Points_in_ellipse:

    """
    Points_in_ellipse( a, b, n )
    Constructor
    param a: horizontal radius of the ellipse.
    param b: vertical radius of the ellipse.
    param n: number of points around the ellipse.
    """ 
    def __init__(self, a, b, n):

       
        self.__a = a # Horizontal radius
        self.__b = b # Vertical radius
        self.__n = n # Points count
        self.__p = 0 # Ellipse perimeter
        self.__l = 0 # Distance between points

        self.set_size(a, b) # Set the size of the ellipse
        self.set_count(n)   # Set the points count

        # The position of the last point, initially (a, 0)
        self.__x = a
        self.__y = 0

    @property
    def perimeter(self):
        return self.__p
    @property
    def size(self):
        return (self.__a, self.__b)
    @property
    def count(self):
        return self.__n
    @property
    def length(self):
        return self.__l

    """
    set_size(a, b)
    Change the radius of the ellipse
    param a: the new horizontal radius.
    param b: the new vertical radius.
    """
    def set_size(self, a, b):
        # Set the radius
        self.__a = a
        self.__b = b
        # Calculate the perimeter approximation
        self.__p = pi*(3*(a+b)-sqrt((3*a+b)*(a+3*b)))
        self.__l = self.__p/self.__n
        return self
    """
    set_count(n)
    Change the number of points around the ellipse.
    param n: The number of points.
    """
    def set_count(self, n):
        self.__n = n
        self.__l = self.__p/n
        return self

    def get_points(self):
        points = list()

        angle = 0
        for i in range(self.__n):
            points.append(( self.__x, self.__y ))
            angle = self.__angle_approx(angle)

            self.__x += self.__l*cos(angle)
            self.__y += self.__l*sin(angle)

        self.__x = self.__a
        self.__y = 0
        return points

    """
    __identity(angle)
    Gets the value of the ellipse equation for the given angle and
    the current point coordinates.
    param angle: The angle to evaluate.
    """
    def __identity(self, angle):
        val  = ((self.__x + self.__l*cos(angle))/self.__a)**2
        val += ((self.__y + self.__l*sin(angle))/self.__b)**2
        val -= 1
        return val
    """
    __angle_approx(angle)
    Gets the approximate next angle for the given angle and current
    point coordinates.
    param angle: The angle to evaluate.
    """
    def __angle_approx(self, angle, prec=1e-6):
        a = angle
        b = angle + pi

        for i in range(10000):
            c = (a + b)/2

            p = self.__identity(c)
            if abs(p) <= prec:
                return c

            q = self.__identity(a)
            if p*q < 0:
                b = c
            else:
                a = c
        return a