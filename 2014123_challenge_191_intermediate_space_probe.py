from math import floor
from random import choice

neighbors = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]

def create_board(size):
    grid = {}
    start = None
    end = None
    nbr_asteroids = int(floor(size * size * .3))
    nbr_wells = int(floor(size * size * .1))
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

def a_star(grid, start, end):
    visited = []
    frontier =[start]
    coords = grid.keys()
    came_from = {}
    cost_so_far = {}
    
    
    visited.append(start)
    while frontier:
        current = frontier.pop()
        print 'visiting: ', current
        if current == end:
            print 'End Found!'
            break
        for coord in neighbors:
            ncoord = (current[0]+coord[0], current[1]+coord[1])
            if not ncoord in visited and ncoord in coords and grid[ncoord] not in ['A', 'G', 'X']:
                print 'appending: ', ncoord
                frontier.append(ncoord)
            visited.append(ncoord)
            came_from[ncoord] = current
            
    print 'frontier', frontier
    print 'visited', visited
    print 'Came From: ', came_from


if __name__ == '__main__':
    size = 25
    board = create_board(size)
    
    a_star(board['grid'], board['start'], board['end'])
    
    print board['start'], board['end']
    for x in xrange(size):
        for y in xrange(size):
            print board['grid'][(x,y)],
        print