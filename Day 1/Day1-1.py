# read in.txt and write to out.txt
# add all numbers on subsequent lines seperated by a blank line
# output the maximum sum
# write the maximum sum to out.txt

# open in.txt located in current directory and read content
with open('Day 1/in.txt', 'r') as f:
    content = f.readlines()

# replace newline characters with spaces
content = [x.strip() for x in content]

# convert non-empty lines to integers
for i in range(len(content)):
    if content[i] != '':
        content[i] = int(content[i])
    else:
        content[i] = 0

# initialize variables
max_sum = 0
sum = 0

# loop through content
for i in range(len(content)):
    # if the next line is blank, add the sum to the max_sum
    if content[i] == 0:
        if sum > max_sum:
            max_sum = sum
        sum = 0
    # otherwise add the number to the sum
    else:
        sum += content[i]

# write the max_sum to out.txt
with open('Day 1/out.txt', 'w') as f:
    f.write(str(max_sum))

# close in.txt
f.close()

# close out.txt
f.close()
