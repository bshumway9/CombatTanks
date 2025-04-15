class Movable:
    
    def __init__ (self, x, y, dx, dy, WorldWidth, WorldHeight):
        self.X = x
        self.Y = y
        self.DX = dx
        self.DY = dy
        self.WorldWidth = WorldWidth
        self.WorldHeight = WorldHeight
        
    def getX(self):
        return self.X
    
    def getY(self):
        return self.Y
    
    def getDX(self):
        return self.DX
    
    def getDY(self):
        return self.DY
    
    def setDX(self, value):
        self.DX = 0
        
    def setDY(self, value):
        self.DY = 0
    
    def getWorldWidth(self):
        return self.WorldWidth
    
    def getWorldHeight(self):
        return self.WorldHeight
    
    def setY(self, value):
        self.Y = value
        if self.Y > self.WorldHeight:
            self.Y = self.WorldHeight
        if self.Y < 0:
            self.Y = 0
    
    def move(self, dt):
        self.X = (self.X + (self.DX * dt))
        #self.Y = (self.Y + (self.DY * dt))
        if self.X >= self.WorldWidth:
            self.X -= self.WorldWidth
        if self.X < 0:
            self.X += self.WorldWidth
        if self.Y >= self.WorldHeight:
            self.Y -= self.WorldHeight
        if self.Y < 0:
            self.Y += self.WorldHeight
    
    def accelerate(self, delta_velocity):
        raise NotImplementedError
    
    def evolve(self, dt):
        raise NotImplementedError
    
    def draw(self, surface):
        raise NotImplementedError