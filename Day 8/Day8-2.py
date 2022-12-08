# consider a forest with tree heights
# input like this:
# 30373
# 25512
# 65332
# 33549
# 35390
# number is a height
# the outside trees can be seen
# the trees in the middle can be seen if the height of the tree is greater than the height of the trees on the outside when looking at the tree from the outside along the rows or columns
# find the number of trees that can be seen from the outside
# the outside trees can always be seen

score = 0

# read the file
with open('Day 8/in.txt') as f:
    lines = f.readlines()

# convert the characters to a grid of integers
grid = [[int(char) for char in line.strip()] for line in lines]

# create a boolean grid reprexenting the forest of equal size to the grid
# True means the tree is visible
# False means the tree is not visible
# the grid is initialized to False except for the first and last row and column
# the first and last row and column are initialized to True
# the grid is the size of the number of lines in the file by the length of the first line in the file
# the grid is initialized to False
grid1 = [[False for i in range(len(lines[0].strip()))] for j in range(len(lines))]
# set the first and last row to True
for i in range(len(grid)):
    grid1[i][0] = True
    grid1[i][-1] = True
# set the first and last column to True
for i in range(len(grid[0])):
    grid1[0][i] = True
    grid1[-1][i] = True

# loop through the grid
# check visibility of each tree
def tree_visibility(grid):
    # loop through the rows
    for i in range(len(grid)):
        # loop through the columns
        for j in range(len(grid[i])):
            # if the tree is visible
            if visible(grid, i, j):
                # mark the tree as visible
                grid1[i][j] = True

# visible if the tree is taller than the tallest tree in the row or column
def visible(grid, i, j):
    # if the tree is visible from the north
    if visible_from_north(grid, i, j):
        # the tree is visible
        return True
    # if the tree is visible from the south
    if visible_from_south(grid, i, j):
        # the tree is visible
        return True
    # if the tree is visible from the east
    if visible_from_east(grid, i, j):
        # the tree is visible
        return True
    # if the tree is visible from the west
    if visible_from_west(grid, i, j):
        # the tree is visible
        return True
    # the tree is not visible
    return False


# visible from east if the tallest tree to the east is shorter than the tree
def visible_from_east(grid, i, j):
    # loop through the trees to the east
    current = grid[i][j]
    for k in range(j + 1, len(grid[i])):
        # if the tree is taller than the tree at (i, j)
        if grid[i][k] >= current:
            # the tree at (i, j) is not visible
            return False
    return True


# visible from west if the tallest tree to the west is shorter than the tree
def visible_from_west(grid, i, j):
    # loop through the trees to the west
    current = grid[i][j]
    for k in range(j - 1, -1, -1):
        # if the tree is taller than the tree at (i, j)
        if grid[i][k] >= current:
            # the tree at (i, j) is not visible
            return False
    return True

# visible from north if the tallest tree to the north is shorter than the tree
def visible_from_north(grid, i, j):
    # loop through the trees to the north
    current = grid[i][j]
    for k in range(i - 1, -1, -1):
        # if the tree is taller than the tree at (i, j)
        if grid[k][j] >= current:
            # the tree at (i, j) is not visible
            return False
    return True

# visible from south if the tallest tree to the south is shorter than the tree
def visible_from_south(grid, i, j):
    # loop through the trees to the south
    current = grid[i][j]
    for k in range(i + 1, len(grid)):
        # if the tree is taller than the tree at (i, j)
        if grid[k][j] >= current:
            # the tree at (i, j) is not visible
            return False
    return True


# loop through the grid
# check visibility of each tree
tree_visibility(grid)

# scene score is the number of visible trees from a specific point of view
# the scene score is the number of visible trees from the north multiplied by the number of visible trees from the south multiplied by the number of visible trees from the east multiplied by the number of visible trees from the west
# find the tree with the highest scene score
# the return value is the highest scene score
def find_scene_score(grid):
    # loop through the rows
    score = 0
    for i in range(len(grid)):
        # loop through the columns
        for j in range(len(grid[i])):
            # if the tree is visible
            if grid1[i][j]:
                # calculate the scene score
                scene_score = scene_score_north(grid, i, j) * scene_score_south(grid, i, j) * scene_score_east(grid, i, j) * scene_score_west(grid, i, j)
                # if the scene score is greater than the current score
                if scene_score > score:
                    # update the score
                    score = scene_score
    return score

# scene score from the north is the number of visible trees from the north
def scene_score_north(grid, i, j):
    # loop through the trees to the north
    current = grid[i][j]
    count = 0
    for k in range(i - 1, -1, -1):
        # if the tree is taller than the tree at (i, j)
        if grid[k][j] >= current:
            # the tree at (i, j) is not visible
            count += 1
            return count
        # increment the count
        count += 1
    return count

# scene score from the south is the number of visible trees from the south
def scene_score_south(grid, i, j):
    # loop through the trees to the south
    current = grid[i][j]
    count = 0
    for k in range(i + 1, len(grid)):
        # if the tree is taller than the tree at (i, j)
        if grid[k][j] >= current:
            # the tree at (i, j) is not visible
            count += 1
            return count
        # increment the count
        count += 1
    return count

# scene score from the east is the number of visible trees from the east
def scene_score_east(grid, i, j):
    # loop through the trees to the east
    current = grid[i][j]
    count = 0
    for k in range(j + 1, len(grid[i])):
        # if the tree is taller than the tree at (i, j)
        if grid[i][k] >= current:
            # the tree at (i, j) is not visible
            count += 1
            return count
        # increment the count
        count += 1
    return count

# scene score from the west is the number of visible trees from the west
def scene_score_west(grid, i, j):
    # loop through the trees to the west
    current = grid[i][j]
    count = 0
    for k in range(j - 1, -1, -1):
        # if the tree is taller than the tree at (i, j)
        if grid[i][k] >= current:
            # the tree at (i, j) is not visible
            count += 1
            return count
        # increment the count
        count += 1
    return count

score = find_scene_score(grid)

# write the count to the file
with open('Day 8/out2.txt', 'w') as f:
    f.write(str(score))

# close the in.txt file
f.close()

# close the out.txt file
f.close()