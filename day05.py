def process (code):
    cp = 0
    steps = 0
    while cp >= 0 and cp < len(code):
        cp_i = cp + code[cp]

        if code[cp] >= 3:
            code[cp] -= 1
        else:
            code[cp] += 1
        cp = cp_i
        steps += 1
    print (steps)

with open ("day05.txt") as f:
    code = [int(a.strip('\n')) for a in f.readlines()]

process(code)