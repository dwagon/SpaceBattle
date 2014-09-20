#!/usr/bin/env python

import sys
import pygame
import space

screensize = screenwidth, screenheight = 1280, 800


##########################################################################
##########################################################################
##########################################################################
class Game:

    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.space = space.Space(
            width=self.width, height=self.height, screen=self.screen)
        self.space.initShips()

    ######################################################################
    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(screensize)
        clock = pygame.time.Clock()

        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.space.shipList()
                    sys.exit()
            self.screen.fill((0, 0, 0))
            if self.space.turn():
                self.space.shipList()
                return
            self.space.draw()
            pygame.display.flip()
            clock.tick(80)

##########################################################################
if __name__ == "__main__":
    g = Game(screenwidth, screenheight)
    g.run()

# EOF
