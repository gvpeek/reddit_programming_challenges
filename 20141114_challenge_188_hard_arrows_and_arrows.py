# >>>>v
# ^v<<v
# ^vv^v
# ^>>v<
# ^<<<^

arrows = '''>>>>v
^v<<v
^vv^v
^>>v<
^<<<^'''

determine_next_cell = {
    '^' : (-1,0),
    'v' : (1,0),
    '<' : (0,-1),
    '>' : (0,1)
}

board ={}
visited = []

x=0
y=0
for arrow in arrows:
    if arrow == '\n':
        x += 1
        y = 0 
    else:
        board[(x,y)] = arrow
        y += 1
        
board_x, board_y = x, (y - 1)

next_cell = None
for cell in board.keys():
    cycle_size = 0 
    if cell not in visited:
        print cell
        cycle_size += 1
        visited.append(cell)
        x, y = cell
        while next_cell not in visited:
            visited.append(next_cell)
            cycle_size += 1
            xdelta, ydelta = determine_next_cell[board[(x, y)]]
            print board[(x, y)], xdelta, ydelta
            next_x = x + xdelta
            if next_x > board_x:
                x = 0
            elif next_x < 0:
                x = board_x
            next_y = y + ydelta
            if next_y > board_y:
                y = 0
            elif next_y < 0:
                y = board_y
            next_cell = (next_x, next_y)
            x, y = next_cell
            
            print cycle_size, next_cell, visited
            
            
        