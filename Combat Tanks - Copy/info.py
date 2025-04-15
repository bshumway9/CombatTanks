import pygame
import text

class Info:
    
    def __init__(self, x, y, player_num, angle, health, power, wind, ammo, ammo_stockpile, over, width, height):
        self.X = x
        self.Y = y
        self.Width = width
        self.Height = height
        self.player_num = player_num
        self.angle = angle
        self.health = health
        self.power = power
        self.ammo = ammo
        self.ammo_stockpile = ammo_stockpile
        self.game_over = over
        if wind >=0:
            self.wind = "Wind: " + str(wind) + "->"
        else:
            self.wind = "Wind: " + "<-" + str(abs(wind))

        
        
    def getX(self):
        return(self.X)
    
    def getY(self):
        return(self.Y)
    
    def getWidth(self):
        return(self.Width)
    
    def getHeight(self):
        return(self.Height)
    
    def getPlayerNum(self):
        return(self.player_num)
        
        
            
            
    def draw(self, surface):
        angle = (text.Text("Angle:" + str(self.angle), self.X + 325, self.Y + 10))
        health = (text.Text("Health:" + str(round(self.health)), self.X + 460, self.Y + 10))
        power = (text.Text("Power:" + str(round(self.power)), self.X + 610, self.Y + 10))
        ammo = (text.Text("->" + str(self.ammo) + " " + str(self.ammo_stockpile), self.X + 790, self.Y + 10))

        wind = (text.Text(self.wind, self.Width - 75, self.Y + 10))
        player = (self.player_num)
        fuel = (text.Text("FUEL", self.X + 200, self.Y +10))
        info = (text.Text(player, self.X +75, self.Y + 10))
        game_over = (text.Text(player + " Wins!", self.Width//2, self.Height//3))
        if self.game_over:
            game_over.draw(surface)
        info.draw(surface)
        fuel.draw(surface)
        wind.draw(surface)
        angle.draw(surface)
        health.draw(surface)
        power.draw(surface)
        ammo.draw(surface)