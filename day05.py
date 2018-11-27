def process (code, part_2 = False):
    cp = 0
    steps = 0
    while cp >= 0 and cp < len(code):
        cp_i = cp + code[cp]

        if part_2 and code[cp] >= 3:
            code[cp] -= 1
        else:
            code[cp] += 1
        cp = cp_i
        steps += 1
    print (steps)

with open ("day05.txt") as f:
    code = [int(a.strip('\n')) for a in f.readlines()]

#code = [0,3,0,1,-3]

process(code, 1)