import math
class Point:
    
    def _init_(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y
        
    def distance_to(self, p):
        return (self - p).length()
    
    def move_to(self, x, y):
        self.x = x
        self.y = y
        
newpoint = Point(3,7)
print()