import pygame
import text
import earth
import tanks
import random
import missile
import explosion

class Menu:
    
    def __init__(self, world_width, world_height):
        self.Width = world_width
        self.Height = world_height
        self.players = ""
        self.rounds = ""
        self.player_names = []
        self.player_colors = []
        self.input = ""
        self.inputNum = 0
        self.inputNumMax = 1
        self.playerNum = 1
        self.inputColor = False
        self.player_color_count = 0
        self.available_colors = ["RED", "BLUE", "GREEN", "YELLOW", "PINK", "TEAL", "ORANGE"]
        self.Earth = earth.Earth(world_width, world_height+300, 5) #5 #main has 3
        self.Tanks = []
        self.Missiles = []
        self.Explosion = []
        self.ammo_list = ["babymissile", "missile", "babynuke", "moab", "nuke"]
        self.tankNum = 0
        
        tank_start_range = self.Width//(7)
        extra_gap = (self.Width//(7))//(7)
        start_range = 0
        end_range = tank_start_range
        for i in self.available_colors:
            color = i
            tank_x = random.randrange(start_range, end_range)
            tank_y = 100
            start_range += tank_start_range + extra_gap
            end_range += tank_start_range + extra_gap
            self.Tanks.append(tanks.Tanks(tank_x, tank_y, color, world_width, world_height))
        
    def evolve(self, dt):
        for j in self.Tanks:
            newY = self.Earth.getTankHeight(j.getTankStartX(), j.getTankWidth()) - (j.getTankHeight() *2) + 6
            if newY >= self.Height:
                j.Y = self.Height - (j.getTankHeight() *2) + 10
            else:
                j.Y = newY
        if self.Missiles:
            self.Missiles.evolve(dt)
            self.impact(dt)
                
    def fireWeapon(self):
        self.Explosion = []
        x,y = self.Tanks[self.tankNum].getEndBarrellPoint()
        new_x = x
        new_y = y - 1
        self.Tanks[self.tankNum].rotation = random.randrange(200,341)
        rotation = self.Tanks[self.tankNum].rotation
        self.Tanks[self.tankNum].Power = random.randrange(40,100)
        power = self.Tanks[self.tankNum].Power
        wind = random.randrange(-40, 40)
        self.Missiles = missile.Missile(new_x, new_y, rotation, power, wind, self.Width, self.Height)
        if self.tankNum == 6:
            self.tankNum = 0
        else:
            self.tankNum +=1

    def impact(self, dt):
        missile_x = int(self.Missiles.getX())
        missile_y = int(self.Missiles.getY())
        earth_y = int(self.Earth.end_pos[missile_x-1][1])
        if earth_y <= missile_y or missile_y >= self.Height:
            self.Missiles.setDX(0)
            self.Missiles.setDY(0)
            self.Missiles.windspeed = 0
            if self.Explosion == []:
                ammo = self.ammo_list[random.randrange(0, 5)]
                self.Explosion = explosion.Explosion(missile_x, missile_y, ammo)
            if self.Explosion:
                self.Explosion.evolve(dt)







        
    def inputValid(self):
        if self.inputNum == 0:
            if self.input not in ["2","3","4","5","6", "7"]:
                self.input = ""
                return False
            if self.input in ["2","3","4","5","6", "7"]:
                self.players = self.input
                self.nextInput()
                self.inputNumMax += int(self.players)
                self.input = ""
                return True
        if self.inputNum > 0 and self.inputNum < self.inputNumMax:
            if len(self.input) > 0:
                self.player_names.append(self.input)
                self.nextInput()
                self.playerNum += 1
                self.input = ""
            if self.inputNum == self.inputNumMax:
                self.inputColor = True
                return True
            else:
                return False
        if self.inputColor:
            if self.player_color_count < int(self.players):
                if self.input in self.available_colors:
                    self.player_colors.append(self.input)
                    count = 0
                    for item in self.available_colors:
                        if self.input == item:
                            color = count
                        count += 1
                    self.available_colors.pop(color)#
                    self.input = ""
                    self.player_color_count += 1


                
    
    
    def nextInput(self):
        self.inputNum += 1
    
    
        
    def draw(self, surface):
        surface.fill((120,120,120))
        self.Earth.draw(surface)
        for i in self.Tanks:
            i.draw(surface)
        if self.Missiles:
            self.Missiles.draw(surface)
        if self.Explosion:
            self.Explosion.draw(surface)
        
        welcome = (text.Text("WELCOME TO COMBAT TANKS" , self.Width/2, 25))
        pygame.draw.line(surface, (0,0,0), (self.Width/2 - 165, 10), (self.Width/2 + 165, 10), 1)
        pygame.draw.line(surface, (0,0,0), (self.Width/2 - 165, 10), (self.Width/2 - 165, 40), 1)
        pygame.draw.line(surface, (160,160,160), (self.Width/2 - 165, 40), (self.Width/2 + 165, 40), 1)
        pygame.draw.line(surface, (160,160,160), (self.Width/2 + 165, 10), (self.Width/2 + 165, 40), 1)
        welcome.draw(surface)
        player_max = (text.Text("2-7 PLAYERS", self.Width/2, 100))
        pygame.draw.line(surface, (0,0,0), (self.Width/2 - 80, 85), (self.Width/2 + 80, 85), 1)
        pygame.draw.line(surface, (0,0,0), (self.Width/2 - 80, 85), (self.Width/2 - 80, 115), 1)
        pygame.draw.line(surface, (160,160,160), (self.Width/2 - 80, 115), (self.Width/2 + 80, 115), 1)
        pygame.draw.line(surface, (160,160,160), (self.Width/2 + 80, 85), (self.Width/2 + 80, 115), 1)
        player_max.draw(surface)
        
        players = (text.Text("HOW MANY PLAYERS: " + self.input, self.Width/2, 175))
        pygame.draw.line(surface, (0,0,0), (self.Width/2 - 135, 160), (self.Width/2 + 135, 160), 1)
        pygame.draw.line(surface, (0,0,0), (self.Width/2 - 135, 160), (self.Width/2 - 135, 190), 1)
        pygame.draw.line(surface, (160,160,160), (self.Width/2 - 135, 190), (self.Width/2 + 135, 190), 1)
        pygame.draw.line(surface, (160,160,160), (self.Width/2 + 135, 160), (self.Width/2 + 135, 190), 1)
        if self.inputNum == 0:
            players.draw(surface)
        playernum = (text.Text("HOW MANY PLAYERS: " + self.players, self.Width/2, 175))
        if self.inputNum > 0:
            playernum.draw(surface)
        name_input = (text.Text("PLAYER " + str(self.playerNum) + " NAME: " + self.input, self.Width/2, 250))
        if not self.inputColor:
            if self.inputNum >0:
                name_input.draw(surface)
        if len(self.player_names) >=1 and self.player_color_count < int(self.players):
            color_input = (text.Text(self.player_names[self.player_color_count] + "'s Tank Color: " + self.input, self.Width/2, 250))
            if self.inputColor:
                color_input.draw(surface)
        available_colors = (text.Text("AVAILABLE COLORS: " + str(self.available_colors), self.Width/2, 325))
        if self.inputColor:

            available_colors.draw(surface)
        
        
