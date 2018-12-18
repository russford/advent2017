class Processor(object):
    def __init__(self, codeset):
        self.regs = {c: 0 for c in ["a", "b", "c", "d", "e", "f", "g", "h"]}
        self.cp = 0
        self.code = [c.split(" ") for c in codeset]
        self.mul_count = 0

    def execute(self):
        if self.cp < 0 or self.cp >= len(self.code): return 0
        instr, lval, rval = self.code[self.cp]
        cp_i = self.cp + 1
        rval = self.regs[rval] if rval in self.regs else int(rval)
        if instr == "set":
            self.regs[lval] = rval
        if instr == "sub":
            self.regs[lval] -= rval
        if instr == "mul":
            self.mul_count += 1
            self.regs[lval] *= rval
        if instr == "jnz":
            lval = self.regs[lval] if lval in self.regs else int(lval)
            if lval != 0:
                cp_i = self.cp + rval
        self.debug()
        self.cp = cp_i
        return 1

    def debug(self):
        print (" ".join(["{}: {}".format(k,v) for k,v in self.regs.items()])+" "+' '.join(self.code[self.cp]))

with open("day23.txt", "r") as f:
    code = f.read().splitlines()

p = Processor (code)

# while p.execute():
#     pass
# print (p.mul_count)


def optimized():
    b = 108400
    c = 125400
    h = 0
    while True:
        f = 1
        d = 2
        while True:
            if b % d == 0:
                f = 0
            d = d+1
            if d == b: break
        if f == 0: h += 1
        if b == c: break
        b += 17
    return h

def opt2 ():
    return sum([1 if any([i%j == 0 for j in range(2, int(i**0.5))]) else 0 for i in range(108400, 125401, 17)])


print (opt2())

