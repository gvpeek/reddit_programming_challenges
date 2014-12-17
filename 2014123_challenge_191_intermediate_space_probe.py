from math import floor
from random import choice

def create_grid(size):
    grid = {}
    nbr_asteroids = int(floor(size * size * .3))
    nbr_wells = int(floor(size * size * .1))
    coords = [(x,y) for x in xrange(size) for y in xrange(size)]
    neighbors = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]
    
    for coord in coords:
        grid[coord] = '.'
    
    ## set wells
    for x in xrange(nbr_wells):
        well_set = False
        while not well_set:
            rand_coord = choice(coords)
            if grid[rand_coord] == '.':
                grid[rand_coord] = 'G'
                for coord in neighbors:
                    neighbor = (rand_coord[0]+coord[0], rand_coord[1]+coord[1])
                    if neighbor in coords and grid[neighbor] == '.':
                        grid[neighbor] = 'X'
                well_set = True

    ## set gravity trap area
                
    ## set asteroids
    for x in xrange(nbr_asteroids):
        asteroid_set = False
        while not asteroid_set:
            rand_coord = choice(coords)
            if grid[rand_coord] == '.':
                grid[rand_coord] = 'A'
                asteroid_set = True
    

    for x in xrange(size):
        for y in xrange(size):
            print grid[(x,y)],
        print
        
    print
    print 'wells', nbr_wells, 'asteroids', nbr_asteroids
        

if __name__ == '__main__':
    create_grid(5)