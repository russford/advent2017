
def process(input):
    while "!" in input:
        input = input[:input.index("!")]+input[input.index("!")+2:]

    garbage = 0
    while "<" in input:
        garbage += input.index(">") - input.index("<") - 1
        input = input[:input.index("<")]+input[input.index(">")+1:]

    level = 0
    score = 0

    for c in input:
        if c == "{":
            level += 1
        if c == "}":
            score += level
            level -= 1

    print (score)
    print (garbage)

testinput = "<{o\"i!a,<{i<a>"

with open("day09.txt") as f:
    input = f.read().strip('\n')

process (input)