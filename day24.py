


data = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
""".splitlines()

with open("day24.txt", "r") as f:
    data = f.read().splitlines()

tiles = { str(i+1): v.split('/') for i, v in enumerate(data)}

tiles["0"] = ["0", "0"]
queue = [("0", "0")]
max_score = 0
max_length = 0
max_length_score = 0
while (queue):
    run, val = queue.pop()
    run_list = run.split(',')
    candidates = [k for k,v in tiles.items() if k not in run_list and val in v]
    if candidates:
        for tile in candidates:
            v = tiles[tile][0]
            if v == val: v = tiles[tile][1]
            queue.append((run+","+tile, v))
    else:
        score = sum(sum([int(a) for a in tiles[v]]) for v in run.split(","))
        length = len(run.split(","))
        if score > max_score:
            max_score = score
            print ("max score is now {}".format(score))
        if length > max_length:
            max_length = length
            max_length_score = score
            print ("new max length is {} and score is {}".format(length, score))
        elif length == max_length:
            if score > max_length_score:
                max_length_score = score
                print ("max length still {} but max score is {}".format(length, score))




