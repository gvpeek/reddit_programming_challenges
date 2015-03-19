# from collections import defaultdict

class Screen(object):
    def __init__(self, width, height, display):
        self.board={}
        self.tokens = {}
        self.tile_id=0
        self.tiles = {}
        self.width = width
        self.height = height
        self.display = display

    def find_neighbors(self, coords):
        left_coords=(coords[0] - 1, coords[1])
        top_coords=(coords[0], coords[1] - 1)
    
        return self.board.get(left_coords,''), self.board.get(top_coords,'')

    def process_token(self, coords):
        left, top = self.find_neighbors(coords)
        if left in ['', '.'] and top in ['', '.']: # new tile
            # add column to token tracker
            self.tokens[coords[0]] = self.tile_id
            # add token to tile tracker
            self.tiles[self.tile_id] = (self.board.get(coords), [coords])
            self.tile_id += 1
        else: # existing tile
            # this works because there will always be a '.' between tiles
            # so if we are here and 
            for key, value in self.tiles.iteritems():
                if left in value or top in value:
                    self.tiles[key][1].append(coords)
                    break
                    
    def parse_tiles(self):
        lines = self.display.split('\n')
        for row, line in enumerate(lines):
            for col, byte in enumerate(line):
                current_coords = (col,row)
                self.board[current_coords] = byte
                if byte != '.':
                    self.process_token(current_coords)
                else:
                    # if we are on a '.' token and the current column is being tracked
                    # we need to remove it from tracking
                    if col in self.tokens:
                        del(self.tokens[col])          
                    
        for token, coord_list in sorted(self.tiles.values()):
            size = (1 + coord_list[-1][0] - coord_list[0][0],
                    1 + coord_list[-1][1] - coord_list[0][1])
            print "{0} tile of character '{1}' located at {2}".format(str(size),
                                                                      token,
                                                                      coord_list[0])
        
    
    
    
    
if __name__ == '__main__':
    screen=Screen(74,30,
'''..........................................................................
.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbb.ddddddddddddddddddddd.
.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbb.ddddddddddddddddddddd.
.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbb.ddddddddddddddddddddd.
.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbb.ddddddddddddddddddddd.
.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbb.ddddddddddddddddddddd.
.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbb.ddddddddddddddddddddd.
...........................................bbbbbbbb.ddddddddddddddddddddd.
.jjjjjjjjjjjjjjjjjjjjjjjjj.eeeeeeeeeeeeeee.bbbbbbbb.ddddddddddddddddddddd.
.jjjjjjjjjjjjjjjjjjjjjjjjj.eeeeeeeeeeeeeee.bbbbbbbb.ddddddddddddddddddddd.
.jjjjjjjjjjjjjjjjjjjjjjjjj.eeeeeeeeeeeeeee.bbbbbbbb.ddddddddddddddddddddd.
.jjjjjjjjjjjjjjjjjjjjjjjjj.eeeeeeeeeeeeeee.bbbbbbbb.ddddddddddddddddddddd.
.jjjjjjjjjjjjjjjjjjjjjjjjj.eeeeeeeeeeeeeee.bbbbbbbb.......................
.jjjjjjjjjjjjjjjjjjjjjjjjj.eeeeeeeeeeeeeee.bbbbbbbb.ccccccccccccccccccccc.
.jjjjjjjjjjjjjjjjjjjjjjjjj.eeeeeeeeeeeeeee.bbbbbbbb.ccccccccccccccccccccc.
...........................eeeeeeeeeeeeeee.bbbbbbbb.ccccccccccccccccccccc.
.iiiiiiiiii.kkkkkkkkkkkkkk.eeeeeeeeeeeeeee.bbbbbbbb.ccccccccccccccccccccc.
.iiiiiiiiii.kkkkkkkkkkkkkk.eeeeeeeeeeeeeee................................
.iiiiiiiiii.kkkkkkkkkkkkkk.eeeeeeeeeeeeeee.fffffffffffffff.gggggggggggggg.
.iiiiiiiiii.kkkkkkkkkkkkkk.eeeeeeeeeeeeeee.fffffffffffffff.gggggggggggggg.
.iiiiiiiiii.kkkkkkkkkkkkkk.eeeeeeeeeeeeeee.fffffffffffffff.gggggggggggggg.
.iiiiiiiiii.kkkkkkkkkkkkkk.eeeeeeeeeeeeeee.fffffffffffffff.gggggggggggggg.
.iiiiiiiiii................................fffffffffffffff.gggggggggggggg.
.iiiiiiiiii.hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh.fffffffffffffff.gggggggggggggg.
.iiiiiiiiii.hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh.fffffffffffffff.gggggggggggggg.
.iiiiiiiiii.hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh.fffffffffffffff.gggggggggggggg.
.iiiiiiiiii.hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh.fffffffffffffff.gggggggggggggg.
.iiiiiiiiii.hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh.fffffffffffffff.gggggggggggggg.
.iiiiiiiiii.hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh.fffffffffffffff.gggggggggggggg.
..........................................................................''')

    screen.parse_tiles()
    print 
    
    screen = Screen(4, 4,
'''xx.z
xx..
..yy
z.yy''')

    screen.parse_tiles()
    print
    
    screen = Screen(10, 10,
'''..........
.@@@@@.ss.
.@@@@@.ss.
.......ss.
.\\\\\.ss.
.\\\\\....
.\\\\\.\\.
.......\\.
./////.\\.
..........''')


    screen.parse_tiles()
    print
    
    screen = Screen(74, 30,
'''..........................................................................
.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
................................bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.ddddddddddddddddd.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.ddddddddddddddddd.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.ddddddddddddddddd.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
...................cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.eeeeeeeeee.ffffff.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.eeeeeeeeee.ffffff.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.eeeeeeeeee.ffffff.cccccccccccc.bbbbbbbbbb.kkkkkkkkkkkkkkkk.jjjjjjjjjjjjj.
.eeeeeeeeee.ffffff.cccccccccccc.............................jjjjjjjjjjjjj.
.eeeeeeeeee.ffffff.cccccccccccc.hhhhhhhhhhhhhhhhhhhhhhhhhhh.jjjjjjjjjjjjj.
.eeeeeeeeee.ffffff.cccccccccccc.hhhhhhhhhhhhhhhhhhhhhhhhhhh.jjjjjjjjjjjjj.
.eeeeeeeeee.ffffff.cccccccccccc.hhhhhhhhhhhhhhhhhhhhhhhhhhh.jjjjjjjjjjjjj.
.eeeeeeeeee...............................................................
.eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
.eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
.eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
.eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
.eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
.eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
.eeeeeeeeee.gggggggggggggggggggggggggggggggggggggg.iiiiiiiiiiiiiiiiiiiiii.
..........................................................................''')


    screen.parse_tiles()
    print