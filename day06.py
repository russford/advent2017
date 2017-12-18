def reallocate (blocks):
    for i in range(len(blocks)):
        if blocks[i] == max(blocks):
            break
    n = blocks[i]
    r = n - len(blocks) * (n // len(blocks))
    blocks[i] = 0
    for j in range(len(blocks)):
        blocks[(i+j+1)%len(blocks)] += n // len(blocks) + (1 if j<r else 0)

blocks = [0, 2, 7, 0]
blocks = [0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11]
states = []

while True:
    states.append(blocks.copy())
    reallocate (blocks)
    if blocks in states: break

print (len(states))

states.clear()
while True:
    states.append(blocks.copy())
    reallocate (blocks)
    if blocks in states: break

print (len(states))
