import pygame
import missile

class SmallMissile(missile.Missile):
    
    def __init__(self, x, y, rotation, power, world_width, world_height):
        super().__init__(x, y, rotation, power, world_width, world_height)
        self.blast_radius = 10
        #self.blast =
        self.center = (self.getX(), self.getY())
        
    def evolve(self, dt):
        if self.getDX() == 0 and self.getDY() == 0:
            pass
        self.move(dt)
        
        
    def draw(surface):
        
        
        pygame.draw.circle(surface, (255,0,0), self.center, self.blast_radius)
