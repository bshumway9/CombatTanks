import movable
import math

class Rotatable(movable.Movable):
    
    def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
        super().__init__(x, y, dx, dy, world_width, world_height)
        self.rotation = rotation
        self.d_rotation = self.rotation

    def getRotation(self):
        return (self.rotation)
    
    def getDRotation(self):
        return (self.d_rotation)

    def rotate(self, delta_rotation):
        self.rotation = round((self.rotation + (delta_rotation))%360)
        if self.rotation < 180 and self.rotation > 90:
            self.rotation = 180
        if self.rotation > 0 and self.rotation < 90:
            self.rotation = 360
        self.rotation_boundaries()
        
            
    def rotation_boundaries(self):
        if self.rotation <= 360 and self.rotation >= 270:
            self.d_rotation = -(self.rotation - 360)
        if self.rotation < 270 and self.rotation >= 180:
            self.d_rotation = (self.rotation - 180)
        
        
    def splitDeltaVIntoXAndY(self, rotation, delta_velocity):
        angle = math.radians(rotation)
        dx = math.cos(angle) * delta_velocity
        dy = math.sin(angle) * delta_velocity
        return dx, dy
    
    def drive(self, delta_velocity):
        dx, dy = self.splitDeltaVIntoXAndY(self.rotation, delta_velocity)
        dx = round(dx, 10)
        if dx > 0:
            self.DX = 25
        if dx < 0:
            self.DX = -25
        if dx == 0:
            self.DX = 0
        '''self.DX += dx
        if self.DX > 25:
            self.DX = 25
        if self.DX < -25:
            self.DX = -25'''
        #self.DY += dy
        
    def rotatePoint(self, x, y):
        angle = math.degrees(math.atan2(y,x))
        newangle = angle + self.rotation
        d = math.sqrt(x**2 + y**2)
        return self.splitDeltaVIntoXAndY(newangle, d)
    
    def translatePoint(self, x, y):
        newx = self.getX() + x
        newy = self.getY() + y
        return newx, newy
    
    def rotateAndTranslatePoint(self, x, y):
        x, y = self.rotatePoint(x, y)
        x, y = self.translatePoint(x, y)
        return x, y
    
    def rotateAndTranslatePointList(self, points):
        new_points = []
        for point in points:
            new_point = self.rotateAndTranslatePoint(*point)
            new_points.append(new_point)
        return new_points
    
    def translatePointList(self, points):
        new_points = []
        for point in points:
            new_point = self.translatePoint(*point)
            new_points.append(new_point)
        return new_points
    