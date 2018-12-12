from collections import defaultdict, deque

class Machine(object):
    def __init__(self, prog_id=0):
        self.regs = defaultdict(int)
        self.regs["p"] = prog_id
        self.snd = -1
        self.cp = 0
        self.code = []
        self.queue = deque()


    def load (self, filename):
        with open (filename, "r") as f:
            self.code = f.read().splitlines()

    def push (self, a):
        self.queue.append(a)

    def exec (self):
        instr = self.code[self.cp].split(' ')
        cp_i = self.cp
        if len(instr) == 3:
            if instr[2] in self.regs.keys():
                instr[2] = self.regs[instr[2]]
            else:
                instr[2] = int(instr[2])
        if instr[0] == "snd":
            if instr[1] in self.regs.keys(): instr[1] = self.regs[instr[1]]
            self.snd = instr[1]
        if instr[0] == "set":
            self.regs[instr[1]] = instr[2]
        if instr[0] == "add":
            self.regs[instr[1]] = self.regs[instr[1]] + instr[2]
        if instr[0] == "mul":
            self.regs[instr[1]] = self.regs[instr[1]] * instr[2]
        if instr[0] == "mod":
            self.regs[instr[1]] = self.regs[instr[1]] % instr[2]

        # part 1
        if instr[0] == "rcv1":
            if instr[1] in self.regs:
                instr[1] = self.regs[instr[1]]
            else:
                instr[1] = int(instr[1])
            if (instr[1]) > 0:
                print ("sound {}".format(self.snd))
                return 1

        # part 2
        if instr[0] == "rcv":
            if self.queue:
                self.regs[instr[1]] = self.queue.popleft()
            else:
                return 1

        if instr[0] == "jgz":
            if instr[1] in self.regs.keys():
                instr[1] = self.regs[instr[1]]
            else:
                instr[1] = int(instr[1])
            if instr[1] > 0:
                cp_i = self.cp + instr[2]

        if cp_i == self.cp:
            self.cp += 1
        else:
            self.cp = cp_i

        return 0

def part_1():
    m = Machine()
    m.code = """set a 1
    add a 2
    mul a a
    mod a 5
    snd a
    set a 0
    rcv a
    jgz a -1
    set a 1
    jgz a -2""".split('\n')

    m.load ("day18.txt")

    while not m.exec():
        pass

def part_2():
    machines = [Machine(0), Machine(1)]
    for m in machines:
        m.load("day18.txt")
    m = 0
    val_count = [0,0]
    while True:
        while machines[m].exec() == 0:
            if machines[m].snd != -1:
                print("program {} sent value {}".format(m, machines[m].snd))
                val_count[m] += 1
                machines[(m+1) % 2].push(machines[m].snd)
                machines[m].snd = -1

        m = (m+1) % 2

        if not machines[0].queue and not machines[1].queue:
            print (val_count)
            break
    print (val_count)

part_2()