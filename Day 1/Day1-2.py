# read in.txt and write to out2.txt
# add all numbers on subsequent lines seperated by a blank line
# add the sum to the array based on the size of the sum
# output the first three sums
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
sums = []
output = 0

# loop through content
for i in range(len(content)):
    # if the next line is blank, add the sum to the max_sum
    if content[i] == 0:
        if sum > max_sum:
            max_sum = sum
        sums.append(sum)
        sum = 0
    # otherwise add the number to the sum
    else:
        sum += content[i]

# write the three highest max_sum to out.txt
with open('Day 1/out2.txt', 'w') as f:
    sums.sort(reverse=True)
    for i in range(3):
        output += sums[i]
    f.write(str(output))

# close in.txt
f.close()

# close out2.txt
f.close()