# read in.txt and write to out.txt
# find the duplicate character in each line when split in half
# the character is case sensitive
# the character is worth 1-26 for a through z
# the character is worth 27-52 for A through Z
# output the sum of the common characters between all lines
# write the sum of the common characters to out.txt

# open in.txt located in current directory and read content
with open('Day 3/in.txt', 'r') as f:
    content = f.readlines()

# replace newline characters with spaces
content = [x.strip() for x in content]

# initialize variables
sum = 0
char = ''

# loop through content
for i in range(len(content)):
    # split the line in half
    line = content[i]
    half = int(len(line) / 2)
    first = line[:half]
    second = line[half:]

    # loop through the first half of the line
    for j in range(len(first)):
        # if the character is in the second half of the line
        if first[j] in second:
            # if the character is worth more than the current character
            char = first[j]

    # add the character's value to the sum
    if char.islower():
        sum += (ord(char) - 96)
    else:
        sum += (ord(char) - 38)

    # reset the character
    char = ''

# write the sum to out.txt
with open('Day 3/out.txt', 'w') as f:
    f.write(str(sum))

# close in.txt
f.close()

# close out.txt
f.close()
