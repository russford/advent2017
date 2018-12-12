from functools import reduce

def knot_hash_i(inp, hash_len, pos):
    if pos+hash_len < len(inp):
        s2 = inp[pos:pos+hash_len]
        s2.reverse()
        return inp[:pos] + s2 + inp[pos+hash_len:]
    else:
        s2 = inp[pos:]+inp[:pos+hash_len-len(inp)]
        s2.reverse()
        return s2[len(inp)-pos:] + inp[pos+hash_len-len(inp):pos] + s2[:len(inp)-pos]

def simple_hash (inp_str):
    lengths = [int(a) for a in inp_str.split(",")]
    inp = [i for i in range(256)]
    pos = 0
    skip = 0
    for l in lengths:
        inp = knot_hash_i (inp, l, pos)
        pos = (pos+skip+l) % len(inp)
        skip += 1
    return inp[0] * inp[1]

def full_knot_hash (inp_str):
    lengths = [ord(c) for c in inp_str] + [17, 31, 73, 47, 23]
    inp = [i for i in range(256)]
    pos = 0
    skip = 0
    for r in range(64):
        for l in lengths:
            inp = knot_hash_i (inp, l, pos)
            pos = (pos+skip+l) % len(inp)
            skip += 1
    dense_hash = [reduce((lambda x,y: x^y), inp[i*16:(i+1)*16]) for i in range(16)]
    return ''.join([('0'+hex(a)[2:])[-2:] for a in dense_hash])


inp_str = "63,144,180,149,1,255,167,84,125,65,188,0,2,254,229,24"
simple_hash (inp_str)
full_knot_hash (inp_str)

