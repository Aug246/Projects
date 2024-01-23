import pygame
from src.controller import Controller
from src.bird import Bird
from src.background import Background
from src.ground import Ground
from src.movement import Movement
from src.pipe import Pipe

def main():
    pygame.init()
    b = Controller()
    b.mainloop()
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
