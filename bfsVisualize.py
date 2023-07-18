import pygame as pg
from random import random
from collections import deque

cols = 15
rows = 10
TILE = 60

def get_rect(x,y):
    return x*TILE + 1, y * TILE + 1, TILE - 1, TILE -1

def get_next_nodes(x,y):
    check_next_node = lambda x,y: True if 0 <= x < cols and 0 <= y < rows and not grid[y][x] else False
    ways = [-1,0],[0,-1],[1,0],[0,1]
    return [(x+dx,y+dy) for dx,dy in ways if check_next_node(x+dx,y+dy)]

pg.init()
screen = pg.display.set_mode((cols*TILE,rows*TILE))
clock = pg.time.Clock()

#making the grid
grid = [[1 if random() < 0.2 else 0 for col in range(cols)] for row in range(rows)]

#dictionary of adjacency lists
graph = {}
for y,row in enumerate(grid):
    for x,col in enumerate(row):
        if not col:
            graph[(x,y)] = graph.get((x,y),[]) + get_next_nodes(x,y)

start = (0,0)
queue = deque([start])
visited = {start:None}
current_node = start


while(True):
    screen.fill(pg.Color('black'))

    #draw the grid
    [[pg.draw.rect(screen,pg.Color('darkgreen'),get_rect(x,y),border_radius= TILE // 5)
     for x,col in enumerate(row) if col] for y , row in enumerate(grid)]
    
    [pg.draw.rect(screen,pg.Color('yellow'),get_rect(x,y)) for x,y in visited]
    [pg.draw.rect(screen,pg.Color('darkblue'),get_rect(x,y)) for x,y in queue]

    #BFS
    if queue:
        current_node = queue.popleft()
        
        next_nodes = graph[current_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = current_node

    #draw the path
    

    [exit() for event in pg.event.get() if event.type == pg.QUIT]
    pg.display.flip()
    clock.tick(7)