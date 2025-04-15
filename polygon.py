import rotatable
import pygame

class Polygon(rotatable.Rotatable):
    
    def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
        super().__init__(x, y, dx, dy, rotation, world_width, world_height)
        self.OriginalPolygon = []
        self.Color = (255, 255, 255)
        
    def getOriginalPolygon(self):
        return self.OriginalPolygon
    
    def getColor(self):
        return self.Color
    
    def getPolygon(self):
        return self.OriginalPolygon
    
    def setPolygon(self, point_list):
        self.OriginalPolygon = point_list
        
    def setColor(self, color):
        self.Color = color
        
    def draw(self, surface):
        polygon_points = self.rotateAndTranslatePointList(self.OriginalPolygon)
        pygame.draw.polygon(surface, self.Color, polygon_points)