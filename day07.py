import re

class ImbalanceException (Exception):
    def __init__(self, p):
        self.program = p


class Program(object):
    def __init__(self, name="", nodeweight=0, children=[]):
        self.name = name
        self.nodeweight = nodeweight
        self.children = children
        self.parent = ""
        self.childnodes = []
        self.parentnode = None
        self.weight = 0

    def calc_weight(self):
        if not self.weight:
            if not self.children:
                self.weight = self.nodeweight
                return self.weight
            weights = [c.calc_weight() for c in self.childnodes]
            if all([weights[0] == w for w in weights]):
                self.weight = self.nodeweight + sum(weights)
            else:
                print("imbalance at node {}; weights are {}".format(self.name, ", ".join([str(w) for w in weights])))
                raise ImbalanceException(self)
        return self.weight



def load_program(input):
    regex = "([a-z]+) \((\d+)\)(?: -> )?([\w, ]+)*"
    stack = {}
    for line in input:
        m = re.match(regex, line)
        p = Program(m.group(1), int(m.group(2)), m.group(3).split(", ") if m.group(3) else [])
        stack[m.group(1)] = p

    for name, prog in stack.items():
        for child in prog.children:
            stack[child].parent = name
            stack[child].parentnode = prog
            prog.childnodes.append(stack[child])

    return stack


with open ("day07.txt", "r") as f:
    input = f.read().splitlines()

testinput = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""".splitlines()

stack = load_program(input)

for p in stack.values():
    try:
        p.calc_weight()
    except ImbalanceException as e:
        print ('\n'.join(["{}: {} total {}".format(p.name, p.nodeweight, p.weight) for p in e.program.childnodes]))
        break

print ([v.name for v in stack.values() if not v.parent])