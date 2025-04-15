import pygame

class Text:

    def __init__( self, string, x, y ):
        self.X = x
        self.Y = y
        self.String = string
        self.Color = ( 255, 255, 255 )
        font_height = 24
        self.Font = pygame.font.SysFont( "Courier New", font_height )
        return

    def setText( self, string ):
        self.String = string
        return

    def setColor( self, color ):
        self.Color = color
        return

    def setSize( self, size ):
        self.Font = pygame.font.SysFont( "Courier New", size )
        return

    def draw( self, surface ):
        text_object = self.Font.render( self.String, False, self.Color )
        text_rect = text_object.get_rect( )
        text_rect.center = ( int( self.X ), int( self.Y ) )
        surface.blit( text_object, text_rect )
        return
