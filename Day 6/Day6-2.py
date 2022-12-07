# read in.txt and write to out.txt# read in.txt and write to out2.txt
# find the first sequence of 14 characters that are all unique
# keep track of the position of the last character in the sequence of unique characters

# read the file
with open('Day 6/in.txt') as f:
    lines = f.readlines()

# get the string
string = lines[0]

# keep track of the position of the last character in the sequence of unique characters
last = 0

# find the first sequence of 4 characters that are all unique
for i in range(len(string) - 13):
    # get the 4 characters
    chars = string[i:i+14]
    # check if the characters are all unique
    if len(chars) == len(set(chars)):
        # update the position of the last character in the sequence of unique characters
        last = i + 14
        # stop looking
        break

# write the output to the file
with open('Day 6/out2.txt', 'w') as f:
    f.write(str(last))

# close the in.txt file
f.close()

# close the out2.txt file
f.close()
