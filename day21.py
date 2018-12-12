class Rule (object):
    def __init__(self, rule):
        pattern, self.result = [r.split("/") for r in rule.split (" => ")]
        self.patterns = [pattern]
        for i in range(3):
            pattern = rotate_grid(pattern)
            self.patterns.append(pattern)
        print (self.patterns, self.result)

def rotate_grid(a):
    return ["".join([a[j-1][i] for j in range(len(a),0,-1)]) for i in range(len(a))]

def perms(g):
    r = [g]
    for i in range(3):
        g = rotate_grid(g)
        r.append(g)
    return r
with open("day21.txt", "r") as f:
    patterns = [Rule(r) for r in f.read().splitlines()]

print(len(patterns))

grid = [".#.", "..#", "###"]

