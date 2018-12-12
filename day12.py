import re

test = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""

def get_data(inp):
    r = re.compile ('(\d+) <-> (.+)')
    data = [r.match(t).groups() for t in inp.split("\n")]
    dict = {}
    for d in data:
        dict[int(d[0])] = [int(a) for a in d[1].split(", ")]
    return dict

with open("day12.txt", "r") as f:
    data = get_data(f.read())
print(data)

def get_group (data, prog):
    con = [prog]
    i = 0
    while i < len(con):
        for c in data[con[i]]:
            if c not in con:
                con.append(c)
        i = i+1
    return con

groups = 0
while (data):
    prog = sorted(data.keys())[0]
    con = get_group(data, prog)
    print (prog, len(con))
    for c in con:
        del data[c]
    groups += 1

print(groups)


