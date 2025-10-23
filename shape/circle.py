from math import sqrt
class Circle:

    def __init__(self, centre, radius):

        if len(centre) != 2:
            raise  ValueError("Centre must be a sequence of length 2")
        if radius <= 0:
            raise ValueError("Radius must be positive")
        
        self.centre = tuple(centre)  
        self.radius = radius
    
    def __contains__(self, x):
        centre = self.centre
        dx = centre[0] - x[0]
        dy = centre[1] - x[1]
        if sqrt(dx**2+dy**2) < self.radius:
            return True
        else:
            return False 