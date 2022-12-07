# read in.txt and write to out.txt
# find the duplicate character in each set of three lines
# the character is case sensitive
# the character is worth 1-26 for a through z
# the character is worth 27-52 for A through Z
# output the sum of the common characters between all sets of three lines
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
for i in range(0, len(content), 3):
    # seperate the lines
    line1 = content[i]
    line2 = content[i + 1]
    line3 = content[i + 2]

    # loop through the first line
    for j in range(len(line1)):
        # if the character is in the second and third lines
        if line1[j] in line2 and line1[j] in line3:
            # if the character is worth more than the current character
            char = line1[j]

    # add the character's value to the sum
    if char.islower():
        sum += (ord(char) - 96)
    else:
        sum += (ord(char) - 38)

    # reset the character
    char = ''

# write the sum to out.txt
with open('Day 3/out2.txt', 'w') as f:
    f.write(str(sum))

# close in.txt
f.close()

# close out.txt
f.close()
