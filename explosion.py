import time
import pygame

class Explosion:
    
    def __init__(self, x, y, ammo):
        self.x = x
        self.y = y
        self.ammo = ammo
        self.ammo_list = {"missile": 1, "nuke": 4, "moab": 3, "babymissile": .5, "babynuke": 2, "roller": 1, "bigroller": 2}
        self.ammo_power_list = {"missile": 1.75, "nuke": 4, "moab": 3, "babymissile": 2.5, "babynuke": 2, "roller": 1.75, "bigroller": 2}
        self.ammo_power = self.ammo_power_list[ammo]
        self.radius_max = self.ammo_list[ammo]
        self.growth_rate = self.radius_max / 10
        self.DRadius = 0
        self.finished = False
        self.radius = self.DRadius * 25
        self.damage = False
        
        
    '''def explode(self):
        self.DRadius+= .2
        if self.DRadius>= self.radius_max:
            self.DRadius= self.radius_max
            time.sleep(1)
            self.DRadius= 0'''
    
    
    #work on driving abilities
    def move(self, dt):
        if not self.finished:
            self.DRadius+= self.growth_rate
            if self.DRadius>= self.radius_max:
                self.DRadius= self.radius_max
                self.damage = True
                self.finished = True
                time.sleep(1)#change to 1
        if self.finished:
            self.DRadius= 0
            
    
    def evolve(self, dt):
        self.move(dt)
            
        
    def draw(self, surface):
        self.radius = self.DRadius * 25
        pygame.draw.circle(surface, (255,0,0), (self.x, self.y), (self.radius))