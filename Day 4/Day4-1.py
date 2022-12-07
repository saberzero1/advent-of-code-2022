# read in.txt and write to out.txt
# two ranges of numbers seperated by a comma
# example: 37-42,33-42
# Find the number of lines where one range is fully contained in the other
# example: 37-42,33-42 is valid because 37-42 is fully contained in 33-42
# example: 37-42,33-40 is invalid because 37-42 is not fully contained in 33-40
# Write the number of valid lines to out.txt

# read the file
with open('Day 4/in.txt') as f:
    lines = f.readlines()

# count the number of valid lines
count = 0

# loop through each line
for line in lines:
    # split the line into two ranges
    ranges = line.split(',')
    # split the ranges into two numbers
    range1 = ranges[0].split('-')
    range2 = ranges[1].split('-')
    # convert the strings to integers
    range1 = [int(range1[0]), int(range1[1])]
    range2 = [int(range2[0]), int(range2[1])]
    # check if one range is fully contained in the other
    if (range1[0] >= range2[0] and range1[1] <= range2[1]) or (range1[0] <= range2[0] and range1[1] >= range2[1]):
        # if so, increment the count
        count += 1

# write the count to the file
with open('Day 4/out.txt', 'w') as f:
    f.write(str(count))

# close the in.txt file
f.close()

# close the out.txt file
f.close()
