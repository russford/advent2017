def n_steps (num):

    if num == 1: return 0

    n = int(num ** 0.5)
    if n%2 == 0: n = n-1
    n = (n-1)//2 + 1

    quads = [4*n*n-3*n+1, 4*n*n-n+1, 4*n*n+n+1, 4*n*n+3*n+1]

    return min([abs(num-q) for q in quads])+n

def part1 ():
    inputs = [1, 12, 23, 1024, 277678]

    for i in inputs:
        print (i, n_steps(i))

def grid_str(grid):
    return '\n'.join([str(g) for g in grid])

class Grid (object):
    def __init__(self, n):
        self.size = n
        self.grid = [0] * n
        for i in range(n):
            self.grid[i] = [0]*n
        self.cx = n//2
        self.cy = n//2
        self.grid[n//2][n//2] = 1

    def g(self, x, y):
        if x>=0 and x<self.size and y>=0 and y<self.size:
            return self.grid[x][y]
        else:
            return 0

    def calc_at (self, x, y):
        if self.grid[x][y] != 0:
            raise ValueError ("grid {},{} has already been calculated: {}".format(x,y,self.grid[x][y]))
        self.grid[x][y] = sum([sum([self.g(i,j) for j in [y-1, y, y+1]]) for i in [x-1, x, x+1]])
        #print ("{}, {} now {}".format(x,y,self.grid[x][y]))
        return self.grid[x][y]

    def calc (self):
        return self.calc_at(self.cx, self.cy)

    def walk (self, dirn):
        #print("walking from {},{} by {}".format(self.cx, self.cy, dirn))
        self.cx += dirn[0]
        self.cy += dirn[1]

    def __str__ (self):
        return '\n'.join([str(g) for g in self.grid])


def do_grid (n, target):
    g = Grid(n)
    pos_list = [(1,0), (0,-1), (-1,0), (0,1)]
    pos = 0
    for i in range (n//2):
        for p in range(4):
            for j in range(i*2+1+p//2):
                g.walk(pos_list[p])
                a = g.calc()
                if a > target:
                    print (a)
                    return
                print(g)


def part2 ():
    do_grid(11,277678)

#part1()
part2()
