import pygame

class pygameWindow:

    def __init__(self, screenWidth:int, screenHeight:int, fps:int, ) -> None:
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.fps = fps
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.clock = pygame.time.Clock()

    def pygameSetup(self):
        pygame.init()
