'''With her LAMBCHOP doomsday device finished, Commander Lambda is preparing for her debut on the galactic stage - but in order to make a grand entrance, she needs a grand staircase! As her personal assistant, you've been tasked with figuring out how to build the best staircase EVER.

Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with each amount of bricks, so she can pick the one with the most options.

Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step must be lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having a height of 1: (# indicates a brick)

#
##
21

When N = 4, you still only have 1 staircase choice:

#
#
##
31

But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) or (3, 2), as shown below:

#
#
#
##
41

#
##
##
32

Write a function called answer(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!

'''
'''
def answer(n):

    #n = n if n & 1 else n - 1
    print n
    steps = determine_steps(n)
    dem = 2 ** (steps * (steps + 1) / 2)
    num = n ** steps #npr(n, steps)
    print num,dem
    return int(round(num/ dem))

def npr(n, steps):
    return reduce(lambda x, y: x * y , range(n, n - steps, -1))

def determine_steps(n):
    steps = 0;
    while (2 ** steps) < n:
        steps += 1
    print "steps=", steps
    return steps - 1

print answer(200)
'''
def answer(n):
    n = n if n & 1 else n - 1
    #steps = determine_steps(n)

    return count(1,n) - 1
def count(height, left):
    # all the bricks have been used
    if left == 0:
        return 1

    # not enough bricks to build a new stair
    if left < height:
        return 0

    # either build a new stair now or try the next height (height + 1)
    return count(height + 1, left - height) + count(height + 1, left)
print answer(200)
