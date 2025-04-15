import pygame
import polygon
import random

class Tanks(polygon.Polygon):
    
    def __init__(self, x, y, color, world_width, world_height):
        super().__init__(x, y, 0, 0, 0, world_width, world_height)
        self.setPolygon([(0.0, 1.0), (0.0, 2.0), (3.0, 2.0), (3.0, 1.0), (11.0, 1.0), (11.0, 2.0), (13.0, 2.0), (13.0, 0.0), (11.0, 0.0), (11.0, 1.0), (3.0, 1.0), (3.0, 0.0), (0.0, 0.0)])
        self.tank_base = [(0.0, 10.0), (-5.0, 10.0), (-11.5, 7.0), (-11.5, 5.0), (-10.5, 4.0), (10.5, 4.0), (11.5, 5.0), (11.5, 7.0), (5.0, 10.0)]
        self.tank_mid = [(0.0, 4.0), (-9.5, 4.0), (-9.5, 3.0), (-8.0, 2.0), (8.0, 2.0), (9.5, 3.0), (9.5, 4.0)]
        self.tank_top = [(0.0, 2.0), (-5.0, 2.0), (-5.5, 1.5), (-5.5, 0.5), (-2.5, -1.0), (2.5, -1.0), (5.5, 0.5), (5.5, 1.5), (5.0, 2.0)]
        self.tank_barrell = [(0.0, 1.0), (0.0, 2.0), (3.0, 2.0), (3.0, 1.0), (11.0, 1.0), (11.0, 2.0), (13.0, 2.0), (13.0, 0.0), (11.0, 0.0), (11.0, 1.0), (3.0, 1.0), (3.0, 0.0), (0.0, 0.0)]
        self.tank_wheel_1 = [(-4.0, 9.0), (-5.0, 8.0), (-5.0, 6.0), (-4.0, 5.0), (-2.0, 5.0), (-1.0, 6.0), (-1.0, 8.0), (-2.0, 9.0)]
        self.tank_wheel_2 = [(4.0, 9.0), (5.0, 8.0), (5.0, 6.0), (4.0, 5.0), (2.0, 5.0), (1.0, 6.0), (1.0, 8.0), (2.0, 9.0)]
        self.tank_wheel_3 = [(8.5, 7.5), (9.5, 6.5), (9.5, 5.5), (8.5, 4.5), (7.5, 4.5), (6.5, 5.5), (6.5, 6.5), (7.5, 7.5)]
        self.tank_wheel_4 = [(-8.5, 7.5), (-9.5, 6.5), (-9.5, 5.5), (-8.5, 4.5), (-7.5, 4.5), (-6.5, 5.5), (-6.5, 6.5), (-7.5, 7.5)]
        
        
        
        if color == "RED":
            self.Color = (255,0,0)
        elif color == "GREEN":
            self.Color = (0, 255,0)
        elif color == "BLUE":
            self.Color = (0,0,255)
        elif color == "YELLOW":
            self.Color = (255,255,0)
        elif color == "PINK":
            self.Color = (255,0,255)
        elif color == "TEAL":
            self.Color = (0,255,255)
        
        self.Tank_startX = x
        
        self.Stop_drain = 0
        
        self.Fuel = 100
        
        self.Health = 100
        
        self.Power = 100
        
        self.Health_pack = True
        
        self.ammo_stockpile = [99, 8, 4, 2, 1]
        
        
    def getTankWidth(self):
        width = self.tank_base[6][0] - self.tank_base[3][0]
        return (width)
    
    def getTankHeight(self):
        height = self.tank_base[0][1]
        return (height)
    
    def getTankStartX(self):
        startX = self.X - (self.getTankWidth()//2)
        return startX
    
    def getEndBarrellPoint(self):
        tank_barrell = self.rotateAndTranslatePointList(self.tank_barrell)
        end_point = tank_barrell[6]
        return end_point

    
    def drainFuel(self):
        startX = self.getTankStartX()
        if self.Fuel > 0:
            self.Fuel -= abs((startX - self.X)/20)
        else:
            self.Fuel = 0
            
    def refuel(self):
        self.Fuel = 100
        
    def setPower(self, value):
        self.Power += value
        if self.Power >= self.Health:
            self.Power = self.Health
        if self.Power <= 0:
            self.Power = 0
            
    def setHealth(self, value):
        self.Health -= value
        if self.Health <= 0:
            self.Health = 0
        if self.Health >= 100:
            self.Health = 100
        if self.Power > self.Health:
            self.Power = self.Health
            
    def Healthpack(self):
        if self.Health_pack:
            self.setHealth(-25)
            self.Health_pack = False
        
        
    def evolve(self, dt):
        if self.Fuel != 0:
            self.move(dt)
            self.Stop_drain = 1
        if self.Stop_drain == 1:
            self.drainFuel()
            self.Stop_drain = 0
        
        
    def draw(self, surface):
        tank_base = self.translatePointList(self.tank_base)
        tank_mid = self.translatePointList(self.tank_mid)
        tank_top = self.translatePointList(self.tank_top)
        tank_barrell = self.rotateAndTranslatePointList(self.tank_barrell)
        tank_wheel_1 = self.translatePointList(self.tank_wheel_1)
        tank_wheel_2 = self.translatePointList(self.tank_wheel_2)
        tank_wheel_3 = self.translatePointList(self.tank_wheel_3)
        tank_wheel_4 = self.translatePointList(self.tank_wheel_4)


        pygame.draw.polygon(surface, self.Color, tank_barrell)
        pygame.draw.polygon(surface, (0,0,0), tank_barrell, 1)
        pygame.draw.polygon(surface, self.Color, tank_base)
        pygame.draw.polygon(surface, self.Color, tank_mid)
        pygame.draw.polygon(surface, self.Color, tank_top)
        pygame.draw.polygon(surface, (0,0,0), tank_base, 1)
        pygame.draw.polygon(surface, (0,0,0), tank_mid, 1)
        pygame.draw.polygon(surface, (0,0,0), tank_top, 1)
        pygame.draw.polygon(surface, (0,0,0), tank_wheel_1, 1)
        pygame.draw.polygon(surface, (0,0,0), tank_wheel_2, 1)
        pygame.draw.polygon(surface, (0,0,0), tank_wheel_3, 1)
        pygame.draw.polygon(surface, (0,0,0), tank_wheel_4, 1)

        
        
        # tank barrell [(0, 2), (0,4), (6,4), (6,2), (16,2), (16,4), (20,4), (20,0), (16,0), (16,2), (6,2), (6,0), (0,0)]