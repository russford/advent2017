from day10 import full_knot_hash


input_str = "jzgqcdpd"
#input_str = "flqrgnkx"

def part_1():
    count = 0
    for row in range(128):
        hash = full_knot_hash("{}-{}".format(input_str, row))
        s = ("0"*128+bin(int("0x"+hash, 16))[2:])[-128:]
        count += s.count("1")
    print (count)

def mark (grid, color, x, y):
    stack = []
    stack.append((x,y))
    while stack:
        (a,b) = stack.pop()
        grid[a][b] = color
        if a > 0 and grid[a-1][b] == -1:
            stack.append ((a-1, b))
        if a < 127 and grid[a+1][b] == -1:
            stack.append ((a+1, b))
        if b > 0 and grid[a][b-1] == -1:
            stack.append((a, b-1))
        if b < 127 and grid[a][b+1] == -1:
            stack.append((a, b+1))

def part_2():
    grid = []
    color = 1
    for row in range(128):
        hash = full_knot_hash("{}-{}".format(input_str, row))
        s = ("0"*128+bin(int("0x"+hash, 16))[2:])[-128:]
        grid.append([-1 if a =="1" else 0 for a in s])
    for x in range(128):
        for y in range(128):
            if grid[x][y] == -1:
                mark(grid, color, x, y)
                color = color + 1

    print (max([max(g) for g in grid]))






part_2()