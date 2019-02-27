"""The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.



Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
-2 (K) 	-3 	3
-5 	-10 	1
10 	30 	-5 (P)



Note:

    The knight's health has no upper bound.
    Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
"""


import itertools
import time

dungeon1 = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
dungeon2 = [[1,-4,5,-99],[2,-2,-2,-1]]
dungeon4 = [[-2,-3,3,-4],[-5,-10,1,2],[10,30,-5,-3]]
dungeon5 = [[-2,-3,3,3,5],[-5,-10,1,-3,-2],[10,30,-5,5,3],[10,30,-5,5,3],[10,30,-5,5,3]]
dungeon6 = [[-2,-3,3,3,5,6],[-5,-10,1,-3,-2,3],[10,30,-5,5,3,-1],[10,30,-5,5,3,-4],[10,30,-5,5,3,-19],[11,20,-5,5,3,-19]]
dungeon7 = [[-2,-3,3,3,5,6,5],[-5,-10,1,-3,-2,3,84,-6],[10,30,-5,5,3,-1,-11,-10],[10,30,-5,5,3,-4,10,-3],[10,30,-5,5,3,-19,5,-5],[-12,7,11,20,-5,5,3,-19],[-4,7,11,20,-5,5,3,-19]]
dungeon8 = [[0,-74,-47,-20,-23,-39,-48],[37,-30,37,-65,-82,28,-27],[-76,-33,7,42,3,49,-93],[37,-41,35,-16,-96,-56,38],[-52,19,-37,14,-65,-42,9],[5,-26,-30,-65,11,5,16],[-60,9,36,-36,41,-47,-86],[-22,19,-5,-41,-8,-96,-95]]


"""This is the slow brute force method.  Faster method below."""

def calculateMinimumHP(dungeon):

    start = time.time()   #so slow I was timing it

    width = len(dungeon)-1
    height = len(dungeon[0])-1
    direction_instructions = str()    #producing a list of binary instructions
    for _ in range (width):
        direction_instructions += '1'  #1 will mean go right
    for _ in range (height):
        direction_instructions += '0'   #0 will mean go down
    direction = set()                   #get rid of duplicates using a set
    [direction.add(i) for i in itertools.permutations(direction_instructions, height + width)]
    direction = list(direction)      #Make it iterable

       #the following goes through every path and calculates the life hit
    result_set = set()
    counter = 0
    for x in direction:
        i = 0
        j = 0
        life = 0
        trial = set()
        life += dungeon[i][j]     #starting Square
        trial.add(life)           #each amount of life gets updated to the trial list
        for y in x:
            counter += 1          #just to keep track of how many iterations for curiosity
            print(counter)
            if y == '1':          # if the instruction is a 1 we go down
                i+= 1
            else:                 #if the instruction is 0 we go right
                j += 1
                                    #life starts at zero, and is
            life += dungeon[i][j]   #updated every step
            trial.add(life)         #trial value is added to a list or set
        result_set.add(min(trial))  #The min value is key to remember
    if max(result_set) > 0:         #If you won't die going through maze
            print( 1)               #The min start value would be 1
    print(1-max(result_set))        #Otherwise it's this value.
    end = time.time()
    print("time = ",end - start)    #This is for curiosity

#calculateMinimumHP(dungeon1)  #This take forever for large dungeons



"""The following second take at this challange produced a faster algorithm.
I learned a better way of looking at his type of problem.  """


def calculateMinimumHP2(dungeon):
    start = time.time()
    width = len(dungeon[0])-1
    height = len(dungeon)-1
    for i in range(height,-1,-1):
        for j in range(width,-1,-1):
            print('i',i,'j',j,'width',width,'height',height)
            [print(x) for x in dungeon]
            print('dungeon[i][j] = ',dungeon[i][j])

            if i == height and j == width:
                dungeon[i][j] = max([1,1-dungeon[i][j]])
            elif i == height:
                dungeon[i][j] = max([1,dungeon[i][j+1] - dungeon[i][j]])

            elif j == width:
                dungeon[i][j] = max([1,dungeon[i+1][j] - dungeon[i][j]])

            else:
                tempi = dungeon[i][j+1] - dungeon[i][j]
                tempj = dungeon[i+1][j] - dungeon[i][j]
                dungeon[i][j] = max(1,min([tempi,tempj]))
    end = time.time()
    print("time = ",end - start)    #This is for curiosity
    return dungeon[0][0]



calculateMinimumHP2(dungeon8)
