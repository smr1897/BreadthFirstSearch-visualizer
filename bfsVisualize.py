import pygame as pg
from random import random
from collections import deque

cols = 15
rows = 10
TILE = 60

pg.init()
screen = pg.display.set_mode((cols*TILE,rows*TILE))
clock = pg.time.Clock()

while(True):
    screen.fill(pg.Color('black'))

    [exit() for event in pg.event.get() if event.type == pg.QUIT]
    pg.display.flip()
    clock.tick(7)