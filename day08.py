from collections import defaultdict
import re

expr_dict = {"==": (lambda a,b: a == b),
             "<":  (lambda a,b: a < b),
             ">":  (lambda a,b: a > b),
             "!=": (lambda a,b: a != b),
             "<=": (lambda a,b: a <= b),
             ">=": (lambda a,b: a >= b) }

class Regset(object):
    def __init__(self):
        self.d = defaultdict(int)

    def execute(self, instr):
        if instr[4] not in expr_dict:
            raise Exception("{} not in expression dictionary".format(instr[5]))
        if expr_dict[instr[4]](self.d[instr[3]], int(instr[5])):
            if instr[1] == "inc":
                self.d[instr[0]] += int(instr[2])
            else:
                self.d[instr[0]] -= int(instr[2])

regs = Regset()

r = re.compile("(\w+) (inc|dec) (-?\d+) if (\w+) (==|<|>|<=|>=|!=) (-?\d+)")

with open("day08.txt", "r") as f:
    instr_list = [r.match(s).groups() for s in f.readlines()]

#test = ["b inc 5 if a > 1",
#"a inc 1 if b < 5",
#"c dec -10 if a >= 1",
#"c inc -20 if c == 10"]
#instr_list = [r.match(s).groups() for s in test]

m = 0
for i in instr_list:
    regs.execute(i)
    m = max(m, max(regs.d.values()))

print(m, max(regs.d.values()))



