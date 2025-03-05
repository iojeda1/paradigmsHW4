# Isabel Ojeda
# HW 4 Q1
import math 

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # get euclidean distance 
    def distance(self):
        totald = (self.x *self.x) + (self.y*self.y)
        return math.sqrt(totald)
    
    def print(self):
        print(f"({self.x}, {self.y})")
    # return true if p1 is more distant to the origin than p2
    def __gt__(self, other): 
        return (self.distance() > other.distance())
    # return true if p1 is greater than or equally distant to the origin compared to p2
    def __ge__(self, other): 
        return (self.distance() >= other.distance())
    # return true if p1 is equally distant to the origin as p2 
    def __eq__(self, other): 
        return (self.distance() == other.distance())
    # return true if p1 is not closer to the origin compared to p2
    def __lt__(self, other): 
        return (self.distance() < other.distance())
    # return true if p1 is less than or equally distant to the origin compared to p2
    def __le__(self, other): 
        return (self.distance() <= other.distance())

p1 = Point(2,3)  
p2 = Point(-3,1) 
p3 = Point(-2,-3)
print(p1 > p2) # prints True because p1 is more distant to the origin than p2
print(p1 == p2) # prints False because p1 and p2 are not equally distant to the origin 
print(p1 < p2) # prints False because p1 is not closer to the origin as compared to p2
print(p1 == p3) # prints True  because p1 and p3 are equally distant to the origin
    
