def check (grid, r, c, d):
    try:
        if grid[r+d[0]][c+d[1]] != " ": return 1
    except IndexError:
        pass
    return 0

def walk(grid):
    dirs = [(0,1), (0,-1), (-1,0), (1,0)]
    r = 0
    c = grid[0].index("|")
    dir = (1, 0)
    s = ""
    steps = 0
    while True:
        r += dir[0]
        c += dir[1]
        steps += 1
        if grid[r][c].isalpha():
            s = s + grid[r][c]
        if grid[r][c] == "+":
            for d in dirs:
                if check (grid, r, c, d) and d[0] != -dir[0] and d[1] != -dir[1]:
                    dir = d
                    break
            else:
                break
        if grid[r][c] == " ":
            break
    print (s, steps)

test = """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ """.split('\n')

with open ("day19.txt", "r") as f:
    data = f.read().splitlines()

walk(data)


