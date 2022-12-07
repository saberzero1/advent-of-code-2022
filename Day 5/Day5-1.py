# read in.txt and write to out.txt
# Moving crates
# The input looks like this:
# NZ
# DCM
# P
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
# follow the instructions to move the crates
# a move looks like this:
# move 1 from 1 to 8
# the input is a list of moves
# each move is a list of 3 items
# the first item is the number crates to move
# the second item is the starting position
# the third item is the ending position
# the number of crates to move can exceed the number of crates in the pile
# in that case, all the crates in the pile are moved
# the output is the final position of the first crate of each pile
# when moving, the crate is removed from the start of the pile to the start of the end pile
# crates are moved one at a time with the first crate being at the front of the pile
# the output should look like this:
# CMZ

# read the file
with open('Day 5/in.txt') as f:
    lines = f.readlines()

n = 9
# divide the crates into piles per line fopr first 9 lines, ignoring newline character
piles = [[] for x in range(n)]
for i in range(n):
    for j in range(len(lines[i]) - 1):
        piles[i].append(lines[i][j])

# get the moves
moves = []
for i in range(n, len(lines)):
    moves.append(lines[i].split())

# move the crates
for move in moves:
    # get the number of crates to move
    num = int(move[1])
    # get the start and end piles
    start = int(move[3]) - 1
    end = int(move[5]) - 1
    # move the crates
    for i in range(num):
        # if the start pile is empty, stop moving
        if len(piles[start]) == 0:
            break
        # move the crate
        piles[end].insert(0, piles[start].pop(0))

# get the first crate of each pile
output = ''
for pile in piles:
    output += pile[0]

# write the output to the file
with open('Day 5/out.txt', 'w') as f:
    f.write(output)

# close the in.txt file
f.close()

# close the out.txt file
f.close()
