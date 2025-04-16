import pygame
import polygon
import random


class EarthLine(polygon.Polygon):
    def __init__(self, dy, color, points, index, finalY, world_width, world_height):
        '''dis = finalY - points[0][1]
        self.dy = (dis%100)%20'''
        self.dy = dy/2
        start_dy = 0
        super().__init__(0, 0, 0, start_dy, 0, world_width, world_height)
        self.points = points
        self.setPolygon(points)
        self.index = index
        self.finalY = finalY
        self.height = abs(points[0][1] - points[1][1])
        self.finished = 0
        
        self.color = color
        
        
    def randomDY(self):
        self.DY = random.randrange(50, 100)
        
    def move(self, dt):
        if self.Y +220 >= self.finalY:
            self.Y = self.finalY
            self.DY = 0
            self.finished = 1
            return
        self.Y = (self.Y + (self.DY * dt))
        self.DY += self.dy/4
        if self.Y >= self.WorldHeight:
            self.Y = self.WorldHeight
            
    def draw(self, surface):
        line = self.translatePointList(self.points)
        pygame.draw.polygon(surface, self.color, line) #self.color