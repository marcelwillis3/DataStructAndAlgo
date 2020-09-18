# Sphere Calculator
# Author: Marcel Willis

import math

class sphere:
    
    def __init__(self, radius):
        self.radius = radius
        
    def getRadius(self):
        return self.radius
    
    def setRadius(self,radius):
        self.radius = radius
    
    def surfaceArea(self):
        surfaceArea = 4 * math.pi * self.radius**2
        return surfaceArea
        
    def volume(self):
        volume = (4/3) * math.pi * self.radius**3
        return volume
        
def main():
    radius = float(input("Enter your sphere radius in inches: "))
    Sphere = sphere(radius)
    Sphere.setRadius(radius)
    surfArea = Sphere.surfaceArea()
    vol = Sphere.volume()
    print("The surface area of the sphere is {0:0.2f} in^2".format(surfArea))
    print("The volume of the sphere is {0:0.2f} in^3".format(vol))
    
main()