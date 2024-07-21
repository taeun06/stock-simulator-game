import pygame as pg
import numpy as np

class Graph(pg.sprite.Sprite):

    def __init__(self ,size:tuple ,line_list:list
                ,center = None ,topleft = None ,topright = None ,bottomleft = None ,bottomright = None):
        super().__init__()
        self.image = pg.Surface(size)
        self.rect = self.image.get_rect()

        if   center      is not None: self.rect.center      = center
        elif topleft     is not None: self.rect.topleft     = topleft
        elif topright    is not None: self.rect.topright    = topright
        elif bottomleft  is not None: self.rect.bottomleft  = bottomleft
        elif bottomright is not None: self.rect.bottomright = bottomright
        else: raise ValueError("no position information given in This object")