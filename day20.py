import re

def solve_quad (a,b,c):
    if a == 0: return [0]
    return [v for v in [(-b - (b**2-4*a*c)**0.5)/(2*a), (-b + (b**2-4*a*c)**0.5)/(2*a)] if v>0]

class Point (object):
    def __init__ (self, id, vec):
        self.id = id
        vec = [int(i) for i in vec]
        self.p = vec[:3]
        self.v = vec[3:6]
        self.a = vec[6:]
        self.killed = 0

    def __lt__(self, other):
        a1 = sum([i**2 for i in self.a])
        a2 = sum([i**2 for i in other.a])
        if a1 == a2:
            return sum([i**2 for i in self.v]) < sum([i**2 for i in other.v])
        else:
            return a1 < a2

    def tick(self):
        for i in range(3):
            self.v[i] += self.a[i]
            self.p[i] += self.v[i]

    def dist(self):
        return abs(self.p[0])+abs(self.p[1])+abs(self.p[2])

def check_coll (p1, p2):
    t = [solve_quad(p2.p[i]-p1.p[i], p2.v[i]-p1.v[i], p2.a[i]-p1.a[i]) for i in range(3)]
    if t[0][0] >= 0 and t[0][0] in t[1] and t[0][0] in t[2]: return t[0][0]
    if t[0][1] >= 0 and t[0][1] in t[1] and t[0][1] in t[2]: return t[0][1]
    return -1


with open ("day20.txt", "r") as f:
    data = [Point(i, re.findall("-?\d+", s)) for i,s in enumerate(f.read().splitlines())]

print (sorted(data)[0].id)

for i in range(1000):
    for p in data: p.tick()
    pos = [d.p for d in data]
    data = [d for d in data if pos.count(d.p) == 1]
    print (len(data))

print (colls)




