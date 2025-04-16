import pygame
import polygon
import random
import earthline

class FallingEarth:
    
    def __init__(self, color, world_width, world_height):
        self.world_width = world_width
        self.world_height = world_height
        self.start_pos = []
        self.end_pos = []
        self.lines = []
        self.index = []

        self.color = color
        
    def exists(self):
        if self.start_pos == []:
            return False
        return True
    
    def delete(self, index):
        self.start_pos.pop(index)
        self.end_pos.pop(index)
        self.lines.pop(index)
        self.index.pop(index)
        if len(self.lines) == 0:
            self.reset()
            
    def addLine(self, start_pos, end_pos, index, finalY):
        self.start_pos.append(start_pos)
        self.end_pos.append(end_pos)
        self.index.append((index, finalY))
    
    def isFrozen(self):
        if len(self.lines) > 0:
            if self.lines[0].DY == 0 and self.lines[-1].DY == 0:
                return True
        return False
        
    def randomDY(self):
        for line in self.lines:
            line.randomDY()
        
    def reset(self):
        self.start_pos = []
        self.end_pos = []
        self.lines = []
        
        
        
    def evolve(self, dt):
        if len(self.start_pos) == len(self.lines):
            for i in self.lines:
                i.move(dt)
            return
        count = 0
        for x in self.start_pos:
            dy = random.randrange(10 ,20)#(430,550)
            a,b = self.start_pos[count]
            c,d = self.end_pos[count]
            index, finalY = self.index[count]
            points = [(a,b), (c,d), (c+1,d), (a+1,b)]
            self.lines.append(earthline.EarthLine(dy, self.color, points, index, finalY, self.world_width, self.world_height))

            count += 1
            
            
#draw lines of earth
    def draw(self, surface):
        
        for line in self.lines:
            line.draw(surface)
    
        
        
        
        '''count = 0
        for i in self.start_pos:
            pygame.draw.line(surface, self.color, self.start_pos[count], self.end_pos[count], 1)
            count += 1'''