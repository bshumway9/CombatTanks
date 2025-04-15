import pygame
import random

class Earth:
    
    def __init__(self, world_width, world_height, height_factor):
        self.world_width = world_width
        self.world_height = world_height
        self.start_pos = []
        self.end_pos = []
        colors = [(200,200,255), (236,204,162), (38,139,7), (118,85,43), (127,131,134), (255,250,250)]
        self.color = colors[random.randrange(0, 6)]
        self.height_factor = height_factor
        
        current_width = 0
        
        min_y = ((self.world_height // 10)*self.height_factor)
        max_y = ((self.world_height *75)//100)
        
        height = random.uniform(min_y, max_y)
        current_height = height
        
        
        while current_width < world_width:
            x = int(min(random.uniform(self.world_width//20, self.world_width//4), self.world_width- current_width))
            y = int(random.uniform(min_y, max_y))

            #y = int(max(min(random.uniform((self.world_height // 10), (((self.world_height *65)//100- current_height)),self.world_height *65)//100),self.world_height // 10))))
            
            distance_x = x
            distance_y = y - current_height
            slope = distance_y// distance_x
            #print(x, y, current_width, current_height, distance_x, distance_y, slope)
            
            
            
            for i in range(distance_x):
                if current_height < 50 or current_height > self.world_height - 50:
                    slope = 1
                next_height = current_height + slope + int(random.uniform(-5,5))
                real_height = self.world_height - next_height
                self.start_pos.append((current_width, self.world_height))
                self.end_pos.append((current_width, next_height))
                current_width += 1
                current_height = next_height
            
    def getTankHeight(self, x, width):
        greatest_height = 0
        for i in self.end_pos:
            if i[0] in range(int(x), int(x + width)):
                if i[1] > greatest_height:
                    greatest_height = i[1]
        return greatest_height
            
    '''def getTankHeight(self, x, width):
        total_height = 0
        for i in self.end_pos:
            if i[0] in range(int(x), int(x+width)):
                total_height += i[1]
        average_height = self.world_height - (total_height//(width))
        return average_height
        '''
        
        #creates lines of different heights to fill the width of the map
    def draw(self, surface):
        count = 0
        for i in self.start_pos:
            pygame.draw.line(surface, self.color, self.start_pos[count], self.end_pos[count], 1)
            count += 1