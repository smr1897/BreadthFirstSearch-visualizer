import pygame as pg
from random import random
from collections import deque

cols = 20
rows = 10
TILE = 50

def get_rect(x,y):
    return x*TILE + 1, y * TILE + 1, TILE - 1, TILE -1

def get_next_nodes(x,y):
    check_next_node = lambda x,y: True if 0 <= x < cols and 0 <= y < rows and not grid[y][x] else False
    ways = [-1,0],[0,-1],[1,0],[0,1],[-1,-1],[1,-1],[-1,1],[1,1]
    return [(x+dx,y+dy) for dx,dy in ways if check_next_node(x+dx,y+dy)]

def get_click_mouse_pos():
    x,y = pg.mouse.get_pos()
    grid_x,grid_y = x // TILE, y // TILE
    pg.draw.rect(screen,pg.Color('orange'),get_rect(grid_x,grid_y))
    click = pg.mouse.get_pressed()
    return (grid_x,grid_y) if click[0] else False

def bfs(start,goal,graph):
    queue = deque([start])
    visited = {start:None}

    while queue:
        current_node = queue.popleft()
        if current_node == goal:
            break

        next_nodes = graph[current_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = current_node
    
    return queue,visited



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
goal = start
queue = deque([start])
visited = {start:None}


while(True):
    screen.fill(pg.Color('black'))

    #draw the grid
    [[pg.draw.rect(screen,pg.Color('darkgreen'),get_rect(x,y),border_radius= TILE // 5)
     for x,col in enumerate(row) if col] for y , row in enumerate(grid)]
    
    [pg.draw.rect(screen,pg.Color('yellow'),get_rect(x,y)) for x,y in visited]
    [pg.draw.rect(screen,pg.Color('darkblue'),get_rect(x,y)) for x,y in queue]

    mouse_pos = get_click_mouse_pos()
    if mouse_pos and not grid[mouse_pos[1]][mouse_pos[0]]:
        queue,visited = bfs(start,mouse_pos,graph)
        goal = mouse_pos

    #draw the path
    path_head,path_segment = goal,goal
    while path_segment and path_segment in visited:
        pg.draw.rect(screen,pg.Color('white'),get_rect(*path_segment),TILE,border_radius = TILE // 5)
        path_segment = visited[path_segment]
    pg.draw.rect(screen,pg.Color('red'),get_rect(*start),border_radius = TILE // 3)
    pg.draw.rect(screen,pg.Color('magenta'),get_rect(*path_head),border_radius = TILE // 3)

    [exit() for event in pg.event.get() if event.type == pg.QUIT]
    pg.display.flip()
    clock.tick(7)