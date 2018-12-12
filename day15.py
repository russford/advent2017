a = 65
b = 8921
a = 883
b = 879


def part_1 (a,b):
    a_f = 16807
    b_f = 48271
    mask = int("1"*16, 2)
    match = 0
    for i in range(40000000):
        a = (a * a_f) % 2147483647
        b = (b * b_f) % 2147483647
        if a & mask == b & mask:
            match += 1
    print (match)

def part_2 (a,b):
    a_f = 16807
    b_f = 48271
    mask = int("1" * 16, 2)
    match = 0
    for i in range(5000000):
        a = (a * a_f) % 2147483647
        while (a&3): a = (a * a_f) % 2147483647
        b = (b * b_f) % 2147483647
        while (b&7): b = (b * b_f) % 2147483647
        if a & mask == b & mask:
            match += 1
    print(match)

part_2(a,b)