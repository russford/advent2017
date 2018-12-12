
dir_dict = {"nw": [-1, +1,  0],
            "n" : [ 0, +1, -1],
            "ne": [+1,  0, -1],
            "sw": [-1,  0, +1],
            "s" : [ 0, -1, +1],
            "se": [+1, -1,  0] }


class Hexwalk (object):
    def __init__(self):
        self.p = [0,0,0]

    def distance(self):
        return sum([abs(a) for a in self.p])//2

    def walk(self, dir):
        self.p = [a+b for a,b in zip(self.p, dir_dict[dir])]

test = ["ne,ne,ne", "ne,ne,sw,sw", "ne,ne,s,s", "se,sw,se,sw,sw"]

h = Hexwalk()
for t in test:
    h.p = [0,0,0]
    for dir in t.split(","):
        h.walk(dir)
    print (h.distance())

h = Hexwalk()
m = 0
with open("day11.txt", "r") as f:
    for dir in f.readline().split(","):
        h.walk(dir)
        m = max(m, h.distance())
    print (h.distance(), m)
