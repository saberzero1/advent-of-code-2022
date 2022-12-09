# read in.txt and write to out.txt
# we have a rope with head H and tail T
# we have a list of instructions
# the instructions are like thise:
# R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2

# R 4 means move the rope head of the rope 4 steps to the right
# U 4 means move the rope head of the rope 4 steps up
# L 3 means move the rope head of the rope 3 steps to the left
# D 1 means move the rope head of the rope 1 step down
# R 4 means move the rope head of the rope 4 steps to the right
# D 1 means move the rope head of the rope 1 step down
# L 5 means move the rope head of the rope 5 steps to the left
# R 2 means move the rope head of the rope 2 steps to the right

# the rope head is the current position of the rope
# the rope tail follows the rope head
# the rope tail trails the rope head by 1 step
# the rope tail moves after the rope head moves
# the rope tail makes sure that it is always directly next to the rope head
# the rope tail can move diagonally to the rope head
# the rope head and tail can overlap

# the rope head and tail are represented by a letter in a grid
# the grid is 10000x10000
# the grid is a 2D array
# the grid is initialized with the letter 'H' for the rope head and 'T' for the rope tail
# the grid is initialized with the rope head at the bottom left corner of the grid

# record the movement of the rope head and tail
# output is the number of unique visited spaces by the rope head and tail combined
# the rope head and tail can overlap
# the rope head and tail can visit the same space
# the rope head and tail can visit the same space more than once
# the rope head and tail can visit the same space at the same time

# read the file
with open('Day 9/in.txt') as f:
    lines = f.readlines()

# create the grid
# the grid is 10000x10000
# the grid is a 2D array
# the grid is initialized with the letter 'H' for the rope head and 'T' for the rope tail
# the grid is initialized with the rope head at the bottom left corner of the grid
visited_spaces = [[False for i in range(10000)] for j in range(10000)]

head_x = 5000
head_y = 5000
tail_x = 5000
tail_y = 5000
count = 0

visited_spaces[5000][5000] = True


# simulate the rope head and tail
def main():
    global head_x
    global head_y
    global tail_x
    global tail_y
    head_x = 5000
    head_y = 5000
    tail_x = 5000
    tail_y = 5000
    for line in lines:
        # get the direction and distance
        direction = line[0]
        distance = int(line[1:])
        # move the rope head and tail
        move(direction, distance)

def move(direction, distance):
    global head_x
    global head_y
    global tail_x
    global tail_y
    # move the rope head and tail
    # updated the positions of the rope head and tail
    # updated the visited spaces
    steps = distance
    # move the rope head and tail
    while steps > 0:
        # move the rope head
        move_rope_head(direction)
        # move the rope tail
        move_rope_tail()
        update_visited_spaces(visited_spaces)
        # decrement the number of steps
        steps -= 1

def move_rope_head(direction):
    global head_x
    global head_y
    global tail_x
    global tail_y
    # move the rope head
    if direction == 'R':
        # move the rope head one step to the right
        head_x += 1
    elif direction == 'U':
        # move the rope head one step up
        head_y += 1
    elif direction == 'L':
        # move the rope head one step to the left
        head_x -= 1
    elif direction == 'D':
        # move the rope head one step down
        head_y -= 1

def move_rope_tail():
    global head_x
    global head_y
    global tail_x
    global tail_y
    # move the rope tail
    if head_x - tail_x > 1 and head_y != tail_y:
        # the rope head is to the right of the rope tail
        # move the rope tail one step to the right
        tail_x += 1
        tail_y = head_y
    elif head_x - tail_x < -1 and head_y != tail_y:
        # the rope head is to the left of the rope tail
        # move the rope tail one step to the left
        tail_x -= 1
        tail_y = head_y
    elif head_y - tail_y > 1 and head_x != tail_x:
        # the rope head is above the rope tail
        # move the rope tail one step up
        tail_y += 1
        tail_x = head_x
    elif head_y - tail_y < -1 and head_x != tail_x:
        # the rope head is below the rope tail
        # move the rope tail one step down
        tail_y -= 1
        tail_x = head_x
    elif head_x - tail_x == 2 and head_y == tail_y:
        # the rope head is two steps to the right of the rope tail
        # move the rope tail one step to the right
        tail_x += 1
    elif head_x - tail_x == -2 and head_y == tail_y:
        # the rope head is two steps to the left of the rope tail
        # move the rope tail one step to the left
        tail_x -= 1
    elif head_y - tail_y == 2 and head_x == tail_x:
        # the rope head is two steps above the rope tail
        # move the rope tail one step up
        tail_y += 1
    elif head_y - tail_y == -2 and head_x == tail_x:
        # the rope head is two steps below the rope tail
        # move the rope tail one step down
        tail_y -= 1

def update_visited_spaces(visited_spaces):
    global head_x
    global head_y
    global tail_x
    global tail_y
    # update the visited spaces
    visited_spaces[tail_x][tail_y] = True

main()

# count the number of unique visited spaces by the rope head and tail combined
for i in range(10000):
    for j in range(10000):
        if visited_spaces[i][j]:
            count += 1

# output the number of unique visited spaces by the rope head and tail combined to out.txt
with open('Day 9/out.txt', 'w') as f:
    f.write(str(count))

# close the file
f.close()

# close the file
f.close()
