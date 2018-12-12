

def part_1():
    s = [0]
    pos = 0
    steps = 3
    for i in range(1, 2018):
        pos = (pos + steps+1) % len(s)
        s = s[:pos+1] + [i] + s[pos+1:]
        if pos == 0: print (pos, i)

    print (s[s.index(0)+1])

def part_2():
    length = 1
    pos = 0
    steps = 343
    for i in range(1, 50000000):
        pos = (pos + steps + 1) % length
        length += 1
        if pos == 0: print(pos, i)

part_2()