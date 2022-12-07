# Rock paper scissors game
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
# Rock is 1 and paper is 2 and scissors is 3
# Loss is 0 and win is 6 and tie is 3
# Player 1 chooses A B or C
# Player 2 chooses X Y or Z
# A is rock
# B is paper
# C is scissors
# X is you need to lose
# Y is you need to tie
# Z is you need to win
# input consists of lines of the form: A X
# score for each round is the match score plus the result of the match
# score is the sum of the scores of each round
# output is the score

# open in.txt located in current directory and read content
with open('Day 2/in.txt', 'r') as f:
    content = f.readlines()

# replace newline characters with spaces
content = [x.strip() for x in content]

# initialize variables
score = 0

# loop through content
for i in range(len(content)):
    # if the next line is blank, add the sum to the max_sum
    if content[i] == 'A X':
        score += 3
    elif content[i] == 'A Y':
        score += 4
    elif content[i] == 'A Z':
        score += 8
    elif content[i] == 'B X':
        score += 1
    elif content[i] == 'B Y':
        score += 5
    elif content[i] == 'B Z':
        score += 9
    elif content[i] == 'C X':
        score += 2
    elif content[i] == 'C Y':
        score += 6
    elif content[i] == 'C Z':
        score += 7

# write the max_sum to out2.txt
with open('Day 2/out2.txt', 'w') as f:
    f.write(str(score))

# close in.txt
f.close()

# close out1.txt
f.close()
