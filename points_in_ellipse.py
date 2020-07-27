from math import pi, sqrt
class Points_in_ellipse:

    """
    Points_in_ellipse( a, b, n )
    Constructor
    param a: horizontal radius of the ellipse.
    param b: vertical radius of the ellipse.
    param n: number of points around the ellipse.
    """ 
    def __init__(self, a, b, n):
        self.set_size(a, b)
        self.set_count(n)

    """
    set_size(a, b)
    Change the radious of the ellipse
    param a: the new horizontal radius.
    param b: the new vertical radius.
    """
    def set_size(self, a, b):
        self.a = a
        self.b = b
        self.p = pi*(3*(a+b)-sqrt((3*a+b)*(a+3*b)))
    
    def set_count(self, n):
        self.n = n
        self.l = self.p/self.n