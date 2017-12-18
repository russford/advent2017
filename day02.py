def checksum_pt1 (l):
    return sum([max(r)-min(r) for r in l])

def checksum_pt2 (l):
    return sum([checksum_pt2_row(r) for r in l])

def checksum_pt2_row (l):
    l = sorted(l, reverse=True)
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] % l[j] == 0:
                return l[i]//l[j]
    raise ValueError ("no checksum!")



test_inp_1 = [[5, 1, 9, 5],
            [7, 5, 3],
            [2, 4, 6, 8]]

test_inp_2 = [[5, 9, 2, 8],
              [9, 4, 7, 3],
              [3, 8, 6, 5]]

with open("day02.txt") as f:
    puz_inp = [[int(p) for p in l.split()] for l in f.readlines()]

print (checksum_pt2(test_inp_2))
print (checksum_pt2(puz_inp))



