import pygame
import game
import combattanks
import menu
import time

class PygameApp( game.Game ):

    def __init__( self, width, height, frame_rate ):
        self.Width = width
        self.Height = height
        self.start_menu = False # set True
        self.game_play = True # set False
        self.round_num = 1
        self.rounds = 5
        self.players = 2
        self.player_names = ["BOB", "JOE"]
        self.player_colors = ["RED", "BLUE"]
        #self.Game = menu.Menu(width, height)
        self.Game = combattanks.CombatTanks(self.Width, self.Height, self.players, self.player_names, self.player_colors)


        # title of the application is "Combat Tanks"
        game.Game.__init__( self, "COMBAT TANKS",
                                  width,
                                  height,
                                  frame_rate )
        # create a game instance
        
        return


    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):
        x = mouse_position[ 0 ]
        y = mouse_position[ 1 ]

        if pygame.K_a in keys or pygame.K_LEFT in newkeys:
            self.Game.turnShipLeft( .55 )

        if pygame.K_d in keys or pygame.K_RIGHT in newkeys:
            self.Game.turnShipRight( .55 )
            
        if pygame.K_COMMA in keys:
            self.Game.turnShipLeft( .55 )

        if pygame.K_PERIOD in keys:
            self.Game.turnShipRight( .55 )

        if pygame.K_w in keys:
            self.Game.accelerateShip( 2.0 )
            
        if pygame.K_UP in keys:
            self.Game.raisePower(1)
            
        if pygame.K_DOWN in keys:
            self.Game.lowerPower(1)
        
        if pygame.K_1 in newkeys:
            self.Game.updateAmmo(0)
            
        if pygame.K_2 in newkeys:
            self.Game.updateAmmo(1)
            
        if pygame.K_3 in newkeys:
            self.Game.updateAmmo(2)
            
        if pygame.K_4 in newkeys:
            self.Game.updateAmmo(3)
            
        if pygame.K_5 in newkeys:
            self.Game.updateAmmo(4)
        
        if pygame.K_6 in newkeys:
            self.Game.updateAmmo(5)
            
        if pygame.K_7 in newkeys:
            self.Game.updateAmmo(6)
            
        if pygame.K_h in newkeys:
            self.Game.Tanks[self.Game.player_num].Healthpack()
            
            
        if pygame.K_RETURN in newkeys:
            if self.Game.Tanks[self.Game.player_num].ammo_stockpile[self.Game.ammo] > 0:
                self.Game.Tanks[self.Game.player_num].ammo_stockpile[self.Game.ammo] -= 1
                self.Game.fireWeapon()
                #time.sleep(0)
                for i in self.Game.Tanks:
                    i.DX = 0
                    i.refuel()
                self.Game.nextPlayer()
            
        if pygame.K_s in newkeys:
            self.Game.stopTank()

        if 1 in newbuttons:
            print("button clicked")

        self.Game.evolve( dt )

        return
    
    def menu_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):
        x = mouse_position[ 0 ]
        y = mouse_position[ 1 ]
        self.Game.evolve(dt)

        if pygame.K_0 in newkeys:
            self.Game.input += "0"
        if pygame.K_1 in newkeys:
            self.Game.input += "1"
        if pygame.K_2 in newkeys:
            self.Game.input += "2"
        if pygame.K_3 in newkeys:
            self.Game.input += "3"
        if pygame.K_4 in newkeys:
            self.Game.input += "4"
        if pygame.K_5 in newkeys:
            self.Game.input += "5"
        if pygame.K_6 in newkeys:
            self.Game.input += "6"
        if pygame.K_7 in newkeys:
            self.Game.input += "7"
        if pygame.K_8 in newkeys:
            self.Game.input += "8"
        if pygame.K_9 in newkeys:
            self.Game.input += "9"
        
        if pygame.K_BACKSPACE in newkeys:
            if len(self.Game.input) > 0:
                self.Game.input = self.Game.input[:-1]
                
        if pygame.K_a in newkeys:
            self.Game.input += "A"

        if pygame.K_b in newkeys:
            self.Game.input += "B"

        if pygame.K_c in newkeys:
            self.Game.input += "C"

        if pygame.K_d in newkeys:
            self.Game.input += "D"

        if pygame.K_e in newkeys:
            self.Game.input += "E"

        if pygame.K_f in newkeys:
            self.Game.input += "F"

        if pygame.K_g in newkeys:
            self.Game.input += "G"

        if pygame.K_h in newkeys:
            self.Game.input += "H"

        if pygame.K_i in newkeys:
            self.Game.input += "I"

        if pygame.K_j in newkeys:
            self.Game.input += "J"

        if pygame.K_k in newkeys:
            self.Game.input += "K"

        if pygame.K_l in newkeys:
            self.Game.input += "L"

        if pygame.K_m in newkeys:
            self.Game.input += "M"

        if pygame.K_n in newkeys:
            self.Game.input += "N"

        if pygame.K_o in newkeys:
            self.Game.input += "O"

        if pygame.K_p in newkeys:
            self.Game.input += "P"

        if pygame.K_q in newkeys:
            self.Game.input += "Q"

        if pygame.K_r in newkeys:
            self.Game.input += "R"

        if pygame.K_s in newkeys:
            self.Game.input += "S"

        if pygame.K_t in newkeys:
            self.Game.input += "T"

        if pygame.K_u in newkeys:
            self.Game.input += "U"

        if pygame.K_v in newkeys:
            self.Game.input += "V"

        if pygame.K_w in newkeys:
            self.Game.input += "W"

        if pygame.K_x in newkeys:
            self.Game.input += "X"

        if pygame.K_y in newkeys:
            self.Game.input += "Y"

        if pygame.K_z in newkeys:
            self.Game.input += "Z"


        
        if pygame.K_RETURN in newkeys:
            self.Game.inputValid()
            self.Game.fireWeapon()
            if self.Game.inputColor and len(self.Game.player_names) == len(self.Game.player_colors):
                self.gameStart()
        
    def gameStart(self):
        self.players = int(self.Game.players)
        self.player_names = self.Game.player_names
        self.player_colors = self.Game.player_colors
        self.start_menu = False
        self.game_play = True
        self.Game = combattanks.CombatTanks(self.Width, self.Height, self.players, self.player_names, self.player_colors)
        
        

    def paint( self, surface ):
        self.Game.draw( surface )
        return

def main():
    pygame.font.init( )
    game = PygameApp( 1290, 640, 60 ) #1400. 700, 30 #1200,600 #fullscreen 1300, 640
    game.main_loop( )

if __name__ == "__main__":
    main()
    