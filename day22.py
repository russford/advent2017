from collections import defaultdict


class Virus(object):
    def __init__(self):
        self.dirs = [[-1,0], [0, 1], [1,0], [0,-1] ]
        self.dir = 0
        self.pos = (0,0)
        self.grid = defaultdict(int)

    def load_map (self, data):
        for i,g in enumerate(data):
            for j,c in enumerate(g):
                if c == "#":
                    self.grid[(i-len(data)//2, j-len(data)//2)] = 1

    def step (self):



