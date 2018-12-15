class Rule (object):
    def __init__(self, rule):
        pattern, self.result = [r.split("/") for r in rule.split (" => ")]
        self.patterns = [pattern]
        for i in range(3):
            pattern = rotate_grid(pattern)
            self.patterns.append(pattern)
        print (self.patterns, self.result)


def rotate_store(a, patterns, result):
    for i in range(4):
        a = ["".join([a[j-1][i] for j in range(len(a),0,-1)]) for i in range(len(a))]
        patterns['/'.join(a)] = result

def flip_grid(a):
    return ["".join([a[i][j-1] for j in range(len(a),0,-1)]) for i in range(len(a))]


def build_patterns (rule_list):
    rules = {}
    for rule in rule_list:
        pattern, result = [r.split("/") for r in rule.split (" => ")]
        rotate_store (pattern, rules, result)
        pattern = flip_grid (pattern)
        rotate_store (pattern, rules, result)
    return rules


def iterate (grid, patterns):
    n = 3 if len(grid) % 2 else 2
    print ("n: {}, g: {}".format(n, len(grid)))
    g2 = [["0"]*(n+1)*(len(grid)//n) for i in range((n+1)*len(grid)//n)]
    for i in range(len(grid)//n):
        for j in range(len(grid)//n):
            g2_i = ["".join(g[j*n:(j+1)*n]) for g in grid[i*n:(i+1)*n]]
            g2_i = patterns['/'.join(g2_i)]
            for k in range(n+1):
                for l in range(n+1):
                    g2[i*(n+1)+k][j*(n+1)+l] = g2_i[k][l]
    return g2


with open("day21.txt", "r") as f:
    patterns = build_patterns (f.read().splitlines())


print(len(patterns))
#for k,v in patterns.items():
#    print ("{} {}".format(k,v))


test = [["1","2","3"], ["4", "5", "6"], ["7", "8", "9"]]
p = build_patterns(["123/456/789 => 111/222/333"])
print ("\n".join(p.keys()))

grid = [".#.", "..#", "###"]
for i in range(18):
    grid = iterate(grid, patterns)
    print ("{}: {}".format(i+1, sum([g.count("#") for g in grid])))
    #print ('\n'.join([''.join(g) for g in grid]))