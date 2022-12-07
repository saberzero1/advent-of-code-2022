# read in.txt and write to out.txt
# we have a file system that we navigate through
# every file has a certain size
# calculate the total size of the files in the file system
# the file system is a tree
# input looks liok this:
# $ cd /
# $ ls
# dir cvt
# 4967 hcqbmwc.gts
# 5512 hsbhwb.clj
# dir hvfvt
# dir phwgv
# 277125 pwgswq.fld
# 42131 qdzr.btl
# dir svw
# 144372 vmbnlzgb.wbd
# dir zft
# calculate the dicectory size of all directories of 1000000 bytes at most
# find the sum of all those directories combined
# file system is a tree
# 3ize is the sum of the size of all files in the directory and subdirectories
# find the total sum of all directories of size 1000000 bytes or less

# read the file
with open('Day 7/in.txt') as f:
    lines = f.readlines()

# build the tree
# if starts with int, it is a file with that size
# if starts with dir, it is a directory contained in the current directory
# if starts with $, a new command is being executed
# if starts with ls after $, it prints the contents of the current directory
# if starts with cd after $, it changes the current directory, moving to the directory specified
# trim the new line character
# add children to the parent

class Node(object):
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.type = 'file' if size != 0 else 'directory'
        self.children = []
        self.parents = []

    def add_child(self, obj):
        self.children.append(obj)

    def add_parent(self, obj):
        self.parents.append(obj)

    def get_size(self):
        return int(self.size)

    def get_name(self):
        return self.name

    def get_children(self):
        return self.children

    # get all unique children of the node and all of its children recursively
    # only if they are directories and not files
    def get_all_unique_children(self):
        children = []
        for child in self.children:
            if child.type == 'directory':
                children.append(child)
                children += child.get_all_unique_children()
        return children

    def get_parents(self):
        return self.parents

    def update_parent_size(self):
        for parent in self.parents:
            parent.update_size()

    def update_size(self):
        self.size = 0
        for child in self.children:
            self.size += child.get_size()
        self.update_parent_size()
        
# loop through the lines

# create the root node
root = Node('/', 0)

# create the current node
current = root

# loop through the lines
for line in lines:
    # split the line
    split = line.split()
    # if the line is a command
    if split[0] == '$':
        # if the command is ls
        if split[1] == 'ls':
            # print the contents of the current directory
            for child in current.get_children():
                print(child.get_name())
        # if the command is cd
        elif split[1] == 'cd':
            # change the current directory
            # if the directory is the root
            if split[2] == '/':
                # set the current directory to the root
                current = root
            if split[2] == '..':
                current = current.get_parents()[0]
            # if the directory is not the root
            else:
                # loop through the children of the current directory
                for child in current.get_children():
                    # if the child is the directory we are looking for
                    if child.get_name() == split[2]:
                        # set the current directory to the child
                        current = child
    # if the line is a file
    elif split[0].isdigit():
        # create a new node
        node = Node(split[1], split[0])
        # add the node to the current directory
        current.add_child(node)
        # add the current directory to the node
        node.add_parent(current)
        # update the size of the current directory
        current.update_size()
    # if the line is a directory
    elif split[0] == 'dir':
        # create a new node
        node = Node(split[1], 0)
        # add the node to the current directory
        current.add_child(node)
        # add the current directory to the node
        node.add_parent(current)
        # update the size of the current directory
        current.update_size()

# find the sum of all directories of size 100000 bytes or less
# loop through the all nodes contained in the root
sum = 0
for child in root.get_all_unique_children():
    # if the size of the child is less than or equal to 100000
    # do this for all unique children
    if child.get_size() <= 100000:
        # add the size of the child to the sum
        sum += child.get_size()

# write the sum to the file
with open('Day 7/out.txt', 'w') as f:
    f.write(str(sum))

# close the file
f.close()

# close the file
f.close()
