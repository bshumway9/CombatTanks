import polygon
import random
import math

class Rock(polygon.Polygon):
    
    def __init__(self, x, y, world_width, world_height):
        rotation = random.uniform(0, 359.9)
        polygon_radius = random.uniform(10,60)
        polygon_num_points = random.randrange(10, 20)
        super().__init__(x, y, 0, 0, rotation, world_width, world_height)
        self.setPolygon(self.createRandomPolygon(polygon_radius, polygon_num_points)) #make random radius and random amount of points here
        self.SpinRate = random.uniform(-90, 90)
        self.accelerate(random.randrange(10,20))
        
    def createRandomPolygon(self, radius, number_of_points):
        gap = 360/number_of_points
        angle = 0
        points = []
        for i in range(number_of_points):
            d = random.uniform(.7, 1.3) * radius
            x = math.cos(math.radians(angle)) * d
            y = math.sin(math.radians(angle)) * d
            points.append((x,y))
            angle += gap
        return points
    
    def getSpinRate(self):
        return self.SpinRate
    
    def setSpinRate(self, spin_rate):
        self.SpinRate = spin_rate
    
    def evolve(self, dt):
        self.move(dt)
        self.rotate(dt * self.SpinRate)
        
        