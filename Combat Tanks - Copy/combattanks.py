import pygame
import rock
import ship
import tanks
import earth
import info
import random
import missile
import explosion
import time
import math


class CombatTanks:
    
    def __init__(self, world_width, world_height, players, names, colors):
        self.players = players
        self.player_names = names
        self.player_colors = colors
        self.player_num = 0
        self.world_width = world_width
        self.world_height = world_height
        self.Objects = []
        self.Tanks = []
        self.LivingTanks = []
        self.Explosion = []
        self.Earth = earth.Earth(world_width, world_height, 3)
        self.wind = random.randrange(-50, 50)
        sky_colors = [(135,206,235), (46,68,130)]
        self.sky = sky_colors[random.randrange(0,2)]
        
        #Tank initializing
        tank_start_range = self.world_width//(self.players+1)
        extra_gap = (self.world_width//(self.players+1))//(self.players+1)
        start_range = 0
        end_range = tank_start_range
        for i in range(0, self.players):
            name = self.player_names[i]
            color = self.player_colors[i]
            tank_x = random.randrange(start_range, end_range)
            tank_y = 100
            start_range += tank_start_range + extra_gap
            end_range += tank_start_range + extra_gap
            self.Tanks.append(tanks.Tanks(tank_x, tank_y, color, world_width, world_height))
        self.LivingTanks += self.Tanks
        self.ammo_list = ["babymissile", "missile", "babynuke", "moab", "nuke"]
        self.ammo = 0
        self.game_over = False
        
        #Display info
        self.angle = self.Tanks[self.player_num].getDRotation()
        self.health = self.Tanks[self.player_num].Health
        self.power = self.Tanks[self.player_num].Power
        self.ammo_name = self.ammo_list[self.ammo]
        self.info = info.Info(0,0, self.player_names[self.player_num], self.angle, self.health, self.power, self.wind, self.ammo_name, self.Tanks[self.player_num].ammo_stockpile[self.ammo], self.game_over, world_width, world_height)
        
        
        #Missiles
        self.Missiles = []
        
        
    def nextPlayer(self):
        self.Explosion = []
        #self.updateAmmo(0)
        self.player_num +=1
        if self.player_num > self.players - 1:
            self.player_num = 0
            
    def gameOver(self):
        if len(self.LivingTanks) <= 1:
            self.game_over = True

        
        
    def getWorldWidth(self):
        return self.world_width
    
    def getWorldHeight(self):
        return self.world_height
    
    def getShip(self):
        return self.Ship
    
    def getTanks(self):
        return self.Tanks
    
    def getRocks(self):
        return self.Rocks
    
    def getObjects(self):
        return self.Objects
    
    
    def turnShipLeft(self, delta_rotation):
        self.Tanks[self.player_num].rotate(-delta_rotation) 
    
    def turnShipRight(self, delta_rotation):
        self.Tanks[self.player_num].rotate(delta_rotation) 

    def accelerateShip(self, delta_velocity):
        self.Tanks[self.player_num].Stop_drain = 1
        self.Tanks[self.player_num].drive(delta_velocity)
        
    def raisePower(self, delta_power):
        self.Tanks[self.player_num].setPower(delta_power)
        
    def lowerPower(self, delta_power):
        self.Tanks[self.player_num].setPower(-delta_power)
        
    def fireWeapon(self):
        x,y = self.Tanks[self.player_num].getEndBarrellPoint()
        new_x = x
        new_y = y - 1
        rotation = self.Tanks[self.player_num].getRotation()
        power = self.Tanks[self.player_num].Power
        self.Missiles = missile.Missile(new_x, new_y, rotation, power, self.wind, self.world_width, self.world_height)
        
    def stopTank(self):
        for i in self.Tanks:
            i.DX = 0
            self.Stop_drain = 0
            
    def updateAmmo(self, num):
        self.ammo = num
        self.ammo_name = self.ammo_list[self.ammo]
        
    def adjustWind(self):
        self.wind = self.wind + random.randrange(-5,5)
        
    def tankInRadius(self, tankX, tankY, x, y, radius, ammo_power):
        if radius > 0:
            if tankX -11 <= x + radius and tankX +11 >= x - radius:
                if tankY <= y + radius and tankY +self.Tanks[0].getTankHeight() >= y - radius:
                    dx = tankX - x
                    dy = tankY - y
                    tank_radius = math.sqrt(dx*dx + dy*dy)
                    distance = abs(tank_radius - radius)
                    power = ammo_power * 4
                    w = self.Tanks[0].getTankWidth()
                    h = self.Tanks[0].getTankHeight()
                    tank_area = w * h
                    area_in_radius = 0
                    for s in range(int(tankX) -11, int(tankX)+12):
                        for t in range (int(tankY), int(tankY) +11):
                            if math.sqrt((s-x)*(s-x) + (t-y)*(t-y)) <= radius:
                                area_in_radius +=1
                    value = (distance/radius) * (area_in_radius/tank_area) * power
                    #print (value)
                    return (value)
        return (0)
    
    def removeEarth(self, x, y, radius):
        if self.Explosion.damage == True:
            left = x - radius
            right = x + radius
            if right > self.world_width:
                right = self.world_width
            if left < 0:
                left = 0
            for i in range(int(left), int(right)):
                h,k = self.Earth.end_pos[i]
                newH = x - h
                overlap = 0
                if newH < radius:
                    overlap = math.sqrt((radius* radius)- (newH*newH))
                if k > (y - overlap) and k < (y + overlap):
                    amount = y + overlap
                    self.Earth.end_pos[i] = (h, amount)
                elif k < (y - overlap):
                    extra = k + (overlap*2)
                    self.Earth.end_pos[i] = (h, extra)
            self.Explosion.damage = False

            
            
    def adjustEarth(self, x, y, radius, count):
        left = x - radius - 20
        right = x + radius + 20
        left = int(left)
        right = int(right)
        if left <= 0:
            left = 1
        a,b = self.Earth.end_pos[left-1]
        c,d = self.Earth.end_pos[left]
        while b < d:
            if left -1 <= 0:
                left = 0
                break
            left = left -1
            a,b = self.Earth.end_pos[left-1]
            c,d = self.Earth.end_pos[left]
        while d < b:
            if left -1 <= 0:
                left = 0
                break
            left = left -1
            a,b = self.Earth.end_pos[left-1]
            c,d = self.Earth.end_pos[left]
        if right >= self.world_width:
            right = self.world_width -2
        a,b = self.Earth.end_pos[right]
        c,d = self.Earth.end_pos[right +1]
        while b < d:
            if right +1 >= self.world_width-1:
                right = self.world_width -2
                break
            right = right +1
            a,b = self.Earth.end_pos[right]
            c,d = self.Earth.end_pos[right +1]
        while d < b:
            if right +1 >= self.world_width-1:
                right = self.world_width -2
                break
            right = right +1
            a,b = self.Earth.end_pos[right]
            c,d = self.Earth.end_pos[right +1]
            
        if right > self.world_width:
            right = self.world_width -2
        if left < 0:
            left = 0
        level = True
        times = count
        times += 1
        for i in range(int(left), int(right)):
            h,k = self.Earth.end_pos[i]
            w,z = self.Earth.end_pos[i+1]
            dif = k - z
            if dif > 0:
                level = False
                self.Earth.end_pos[i+1] = (w, z + (dif//2))
                self.Earth.end_pos[i] = (h, k - (dif//2) )
                
            elif dif < 0:
                level = False
                self.Earth.end_pos[i] = (h, z + (dif//2))
                self.Earth.end_pos[i+1] = (w, k - (dif//2))
                
        if times > 200:
            level = True
            for i in range(int(left), int(right)):
                h,k = self.Earth.end_pos[i]
                self.Earth.end_pos[i] = (h, k + int(random.uniform(-3, 3)))
        if level == False:
            self.adjustEarth(x, y, radius, times)
                
            
        
        
        
    def impact(self, dt):
        missile_x = int(self.Missiles.getX())
        missile_y = int(self.Missiles.getY())
        earth_y = int(self.Earth.end_pos[missile_x-1][1])
        if earth_y <= missile_y or missile_y >= self.world_height:
            self.Missiles.setDX(0)
            self.Missiles.setDY(0)
            self.Missiles.windspeed = 0
            if self.Explosion == []:
                self.Explosion = explosion.Explosion(missile_x, missile_y, self.ammo_name)
                #self.Missiles = []
            if self.Explosion:
                self.Explosion.evolve(dt)
        for tank in self.LivingTanks:
            health = 0
            if self.Explosion:
                health = self.tankInRadius(tank.getX(), tank.getY(), missile_x, missile_y, self.Explosion.radius, self.Explosion.ammo_power)
                if health > 0:
                    tank.setHealth(health)
            if tank.Health == 0:
                self.LivingTanks.remove(tank)
            if self.Explosion:
                if self.Explosion.damage:
                    self.removeEarth(missile_x, missile_y, (self.Explosion.radius_max *25))
                    self.adjustEarth(missile_x, missile_y, (self.Explosion.radius_max *25), 0)
                    self.adjustWind()
                    
        
            #create explosion instance here
                
    def updateInfo(self):
        self.gameOver()
        self.angle = self.Tanks[self.player_num].getDRotation()
        self.health = self.Tanks[self.player_num].Health
        self.power = self.Tanks[self.player_num].Power
        self.info = info.Info(0,0, self.player_names[self.player_num], self.angle, self.health, self.power, self.wind, self.ammo_name, self.Tanks[self.player_num].ammo_stockpile[self.ammo], self.game_over, self.world_width, self.world_height)
    
    def evolve(self, dt):
        for i in self.Objects:
            i.evolve(dt)
        for j in self.Tanks:
            newY = self.Earth.getTankHeight(j.getTankStartX(), j.getTankWidth()) - (j.getTankHeight() *2) + 6
            if newY >= self.world_height:
                j.Y = self.world_height - (j.getTankHeight() *2) + 10
            else:
                j.Y = newY 
        if self.Tanks[self.player_num].Stop_drain == 1:
            self.Tanks[self.player_num].evolve(dt)
        self.updateInfo()
        if self.Missiles:
            self.Missiles.evolve(dt)
            self.impact(dt)
            
            
        if self.Tanks[self.player_num].Health == 0:
            self.player_num +=1
            if self.player_num > self.players -1:
                self.player_num = 0
        
            
    
    def draw(self, surface):
        surface.fill(self.sky)
        
        self.Earth.draw(surface)
        
        for i in self.Objects:
            i.draw(surface)
        
        for i in self.LivingTanks:
            i.draw(surface)
         
        if self.Missiles: 
            self.Missiles.draw(surface)
        
        if self.Explosion:
            self.Explosion.draw(surface)
        
        #Fuel gage
        pygame.draw.line(surface, (255,220,150), (150, 20), (self.Tanks[self.player_num].Fuel + 150,20), 5)
        r = pygame.Rect((150,17), (102, 7))
        pygame.draw.rect(surface, (255,255,255), r, 2)
        
        #Info display
        self.info.draw(surface)
