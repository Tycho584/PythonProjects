import pygame

class Player:

    def __init__(self, screen:str, xPosition:int, yPosition:int) -> None:
        self.screen = screen
        self.width = 100
        self.height = 200
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.image = "pygameProjects\ZombieDefence\Images\Player.png"
        self.ableToWalk = True
        self.ableToJump = True
        self.ableToShoot = True
        self.isAlive = True
        self.canBeRevived = False


    def initialLoadOfPlayer(self):
        self.player = pygame.image.load(self.image)
        self.player = pygame.transform.scale(self.player, (self.width, self.height))

    def loadPlayeronScreen(self):
        self.screen.blit(self.player, (self.xPosition, self.yPosition))

    def leftMovePlayer(self):
        self.xPosition += 3
        print(self.xPosition)

    def rightMovePlayer(self):
        self.xPosition -= 3

    def upMovePlayer(self):
        self.yPosition -= 3

    def downMovePlayer(self):
        self.yPosition += 3

    def checkIfPlayerShouldBeMoved(self):
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    Player.leftMovePlayer()
                if event.key == pygame.K_d:
                    Player.rightMovePlayer()
                if event.key == pygame.K_w:
                    Player.upMovePlayer()
                if event.key == pygame.K_s:
                    Player.downMovePlayer()