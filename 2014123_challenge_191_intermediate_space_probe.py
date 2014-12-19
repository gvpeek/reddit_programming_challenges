import heapq

from math import floor
from random import choice
from collections import OrderedDict

neighbors = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]

def create_board(size):
    grid = {}
    start = None
    end = None
    nbr_asteroids = int(floor(size * size * .1))## .3))
    nbr_wells = int(floor(size * size * .05 )) ##.1))
    coords = [(x,y) for x in xrange(size) for y in xrange(size)]
        
    for coord in coords:
        grid[coord] = '.'

    ## set start point
    while not start:
        rand_coord = choice(coords)
        if grid[rand_coord] == '.':
            grid[rand_coord] = 'S'
            start = rand_coord

    ## set end point
    while not end:
        rand_coord = choice(coords)
        if grid[rand_coord] == '.':
            grid[rand_coord] = 'E'
            end = rand_coord
    
    ## set wells
    for x in xrange(nbr_wells):
        well_set = False
        while not well_set:
            rand_coord = choice(coords)
            if grid[rand_coord] == '.':
                grid[rand_coord] = 'G'
                ## set gravity trap area
                for coord in neighbors:
                    neighbor = (rand_coord[0]+coord[0], rand_coord[1]+coord[1])
                    if neighbor in coords and grid[neighbor] == '.':
                        grid[neighbor] = 'X'
                well_set = True
                
    ## set asteroids
    for x in xrange(nbr_asteroids):
        asteroid_set = False
        while not asteroid_set:
            rand_coord = choice(coords)
            if grid[rand_coord] == 'X' or grid[rand_coord] == '.':
                grid[rand_coord] = 'A'
                asteroid_set = True
                
    print 'wells', nbr_wells, 'asteroids', nbr_asteroids
    
    return {'grid': grid,
            'start': start,
            'end': end}

def calculate_cost(node, end):
    return abs(node[0] - end[0]) + abs(node[1] - end[1])

def a_star(grid, start, end):
    visited = []
    frontier =[]
    heapq.heappush(frontier, (None, start))
    coords = grid.keys()
    came_from = OrderedDict()
    cost_so_far = {}
    
    
    visited.append(start)
    while frontier:
        current = heapq.heappop(frontier)[1]
        # print 'visiting: ', current
        if current == end:
            print 'End Found!'
            break
        for coord in neighbors:
            ncoord = (current[0]+coord[0], current[1]+coord[1])
            ## make sure node exists on the board
            if ncoord in coords:
                if ncoord not in visited and grid[ncoord] not in ['A', 'G', 'X']:
                    new_cost = calculate_cost(ncoord, end)
                    if ncoord not in cost_so_far or new_cost < cost_so_far[ncoord]:
                        # print 'appending: ', ncoord, new_cost
                        heapq.heappush(frontier, (new_cost, ncoord))
                        print frontier
                        came_from[ncoord] = current
                        cost_so_far[ncoord] = new_cost
                visited.append(ncoord)
                
            
    # print 'frontier', frontier
    # print 'visited', visited
    # print 'Came From: ', came_from
    print 'cost_so_far', cost_so_far
    
    return came_from

def reconstruct_path(came_from, start, end):
   current = end
   path = [current]
   while current != start:
      current = came_from[current]
      path.append(current)
      print path
   return path

if __name__ == '__main__':
    size = 25
    board = create_board(size)
    
    came_from = a_star(board['grid'], board['start'], board['end'])
    
    path=[]
    if board['end'] in came_from:
        path = reconstruct_path(came_from, board['start'], board['end'])
        print 'Path:', path
    
    print board['start'], board['end']
    for x in xrange(size):
        for y in xrange(size):
            if (x,y) in path and (x,y) != board['start'] and (x,y) != board['end']:
                print 'O',
            elif board['grid'][(x,y)] == 'X':
                print '.',
            else:
                print board['grid'][(x,y)],
        print