# Isabel Ojeda
# HW 4 Q1
import math 

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self):
        totald = (self.x *self.x) + (self.y*self.y)
        return math.sqrt(totald)
    
    def print(self):
        print(f"({self.x}, {self.y})")

    def __gt__(self, other): 
        return (self.distance() > other.distance())
    
    def __ge__(self, other): 
        return (self.distance() >= other.distance())
    
    def __eq__(self, other): 
        return (self.distance() == other.distance())
    
    def __lt__(self, other): 
        return (self.distance() < other.distance())
    
    def __le__(self, other): 
        return (self.distance() <= other.distance())

p1 = Point(2,3)  
p2 = Point(-3,1) 
p3 = Point(-2,-3)
print(p1 > p2) # prints True because p1 is more distant to the origin than p2
print(p1 == p2) # prints False because p1 and p2 are not equally distant to the origin 
print(p1 < p2) # prints False because p1 is not closer to the origin as compared to p2
print(p1 == p3) # prints True  because p1 and p3 are equally distant to the origin
    
