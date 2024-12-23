import pygame

def getImage(path: str) -> pygame.image:
    #also scales up image by 2x
    return pygame.transform.scale_by(pygame.image.load(path).convert_alpha(), 2)
