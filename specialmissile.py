import pygame
import polygon
import math

class SpecialMissile(polygon.Polygon):

    def __init__(self, x, y, rotation, power, wind, world_width, world_height):
        dx,dy = self.splitPowerIntoXAndY(rotation, power * 7)
        super().__init__(x, y, dx,dy,rotation, world_width, world_height)
        self.setPolygon([(0,0),(-1,1),(-3,1),(-3,-1),(-1,-1)])
        self.missile = [(0,0),(-1,1),(-3,1),(-3,-1),(-1,-1)]
        self.windspeed = wind
        
    def splitPowerIntoXAndY(self, rotation, power):
        angle = math.radians(rotation)
        dx = math.cos(angle) * (power)
        dy = math.sin(angle) * (power)
        return dx, dy
        
    def move(self, dt):
        self.X = (self.X + (self.DX * dt) + (self.windspeed * dt))
        self.Y = (self.Y + (self.DY * dt))
        self.DY += 490 *dt
        if self.X >= self.WorldWidth:
            self.X -= self.WorldWidth
        if self.X < 0:
            self.X += self.WorldWidth
        if self.Y >= self.WorldHeight:
            self.Y = self.WorldHeight
       # if self.Y < 0:
          #  self.Y += self.WorldHeight
          
    
    def evolve(self, dt):
        self.move(dt)
    
    def draw(self, surface):
        missile = self.rotateAndTranslatePointList(self.missile)
        
        pygame.draw.polygon(surface, (0,0,0), missile)