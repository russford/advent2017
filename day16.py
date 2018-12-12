

s = list("abcdefghijklmnop")
s2 = s.copy()

with open("day16.txt", "r") as f:
    instr = f.read().split(",")

def dance(s, instr):
    for i in instr:
        if i[0] == "s":
            n = int(i[1:])
            s = s[-n:]+s[:-n]
        if i[0] == "x":
            n = [int(a) for a in i[1:].split("/")]
            s[n[0]], s[n[1]] = s[n[1]], s[n[0]]
        if i[0] == "p":
            n = s.index(i[1]), s.index(i[3])
            s[n[0]], s[n[1]] = s[n[1]], s[n[0]]
    return s

c = 0
for i in range(10):
    s = dance(s, instr)
    c += 1
    print (s)
    if s == s2:
        print(c)
        break

print (''.join(s))