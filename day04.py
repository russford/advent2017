def is_pass (s):
    if len(s.split(' ')) == len(set(s.split(' '))):
        return 1
    return 0

def is_pass_sorted(s):
    if len(s.split(' ')) == len(set([''.join(sorted(s2)) for s2 in s.split(' ')])):
        return 1
    return 0

with open ("day04.txt") as f:
    passwords = [l.strip('\n') for l in f.readlines()]
    print (sum([is_pass(p) for p in passwords]))
    print (sum([is_pass_sorted(p) for p in passwords]))
    print (len(passwords))

