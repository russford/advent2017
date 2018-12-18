from collections import defaultdict


# PART 1
# To avoid detection, the virus carrier works in bursts; in each burst, it wakes up,
# does some work, and goes back to sleep. The following steps are all executed in order
# one time each burst:
#
# If the current node is infected, it turns to its right.
# Otherwise, it turns to its left. (Turning is done in-place; the current node does not
# change.)
# If the current node is clean, it becomes infected.
# Otherwise, it becomes cleaned. (This is done after the node is considered
# for the purposes of changing direction.)
#
# The virus carrier moves forward one node in the direction it is facing.

# PART 2
# Now, before it infects a clean node, it will weaken it to disable your defenses.
# If it encounters an infected node, it will instead flag the node to be cleaned in the future. So:
#
# Clean nodes become weakened.
# Weakened nodes become infected.
# Infected nodes become flagged.
# Flagged nodes become clean.
# Every node is always in exactly one of the above states.
#
# The virus carrier still functions in a similar way, but now uses the following logic during its bursts of action:
#
# Decide which way to turn based on the current node:
# If it is clean, it turns left.
# If it is weakened, it does not turn, and will continue moving in the same direction.
# If it is infected, it turns right.
# If it is flagged, it reverses direction, and will go back the way it came.
# Modify the state of the current node, as described above.
# The virus carrier moves forward one node in the direction it is facing.


class Virus(object):
    def __init__(self):
        self.dirs = [(-1,0), (0, 1), (1,0), (0,-1) ]
        self.dir = 0
        self.pos = (0,0)
        self.grid = defaultdict(int)
        self.state_count = defaultdict(int)

    def load_map (self, data, state=1):
        for i, g in enumerate(data):
            for j, c in enumerate(g):
                if c == "#":
                    self.grid[(i-len(data)//2, j-len(data)//2)] = state

    def walk(self):
        self.pos = (self.pos[0] + self.dirs[self.dir][0], self.pos[1] + self.dirs[self.dir][1])

    def step1 (self):
        if self.grid[self.pos]:
            self.dir = (self.dir + 1) % 4
        else:
            self.dir = (self.dir - 1) % 4

        self.grid[self.pos] = (self.grid[self.pos] + 1) % 2
        self.state_count[self.grid[self.pos]] += 1
        self.walk()

    def step2 (self):
        if self.grid[self.pos] == 0:
            self.dir = (self.dir - 1) % 4
        elif self.grid[self.pos] == 2:
            self.dir = (self.dir + 1) % 4
        elif self.grid[self.pos] == 3:
            self.dir = (self.dir + 2) % 4

        self.grid[self.pos] = (self.grid[self.pos] + 1) % 4
        self.state_count[self.grid[self.pos]] += 1
        self.walk()

    def print(self):
        min_r = min([a[0] for a in self.grid.keys()])
        max_r = max([a[0] for a in self.grid.keys()])
        min_c = min([a[1] for a in self.grid.keys()])
        max_c = max([a[1] for a in self.grid.keys()])

        chars = [".", "W", "#", "F"]

        print ('\n'.join([''.join([chars[self.grid[(r,c)]] for c in range(min_c, max_c+1)]) for r in range(min_r, max_r+1)]))

    def count_state (self):
        print('\n'.join(["{}: {}".format(k, v) for k, v in self.state_count.items()]))


v = Virus()

data = """..#
#..
...""".splitlines()

with open("day22.txt", "r") as f:
    data = f.read().splitlines()

v.load_map(data, 2)

for i in range(10000000):
    v.step2()
v.count_state()



