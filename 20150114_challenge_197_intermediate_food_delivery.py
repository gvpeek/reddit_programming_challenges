streets = [('A', 'B', "South Acorn Drive", 5, 10, 5, 10),
           ('B', 'C', "Acorn Drive", 15, 5, 15, 5),
           ('C', 'D', "North Acorn Drive", 7, 10, 15, 7),
           ('H', 'G', "South Almond Way", 10, 10, 10, 10),
           ('G', 'F', "Almond Way", 15, 20, 15, 20),
           ('F', 'E', "North Almond Way", 5, 6, 5, 6),
           ('I', 'J', "South Peanut Lane", 8, 9, 10, 11),
           ('J', 'K', "Peanut Lane", 11, 10, 9, 8),
           ('K', 'L', "North Peanut Lane", 7, 5, 7, 5),
           ('P', 'O', "South Walnut", 6, 5, 6, 5),
           ('O', 'N', "Walnut", 10, 8, 10, 8),
           ('N', 'M', "North Walnut", 9, 6, 9, 6),
           ('D', 'E', "West Elm Street", 10, 8, 12, 7),
           ('E', 'L', "Elm Street", 12, 11, 12, 8),
           ('L', 'M', "East Elm Street", 5, 4, 5, 4),
           ('C', 'F', "West Central Avenue", 9, 8, 9, 8),
           ('F', 'K', "Central Avenue", 5, 4, 5, 4),
           ('K', 'N', "East Central Avenue", 9, 9, 9, 9),
           ('B', 'G', "West Pine Road", 7, 6, 7, 6),
           ('G', 'J', "Pine Road", 9, 8, 9, 8),
           ('J', 'O', "East Pine Road", 6, 5, 6, 5),
           ('A', 'H', "West Oak Expressway", 9, 8, 7, 7),
           ('H', 'I', "Oak Expressway", 10, 10, 10, 10),
           ('I', 'P', "East Oak Expressway", 8, 7, 8, 7)]
           
class Node():
    def __init__(self, start, end, name, T1, T2, T3, T4):
        self.start = start
        self.end = end
        self.name = name
        self.T1 = T1
        self.T2 = T2
        self.T3 = T3
        self.T4 = T4

nodes = [Node(*street) for street in streets]

for node in nodes:
    print vars(node)
    