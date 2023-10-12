import random
import copy

'''
Rules:
1) Each mini-board has to contain the symbols 1-9.
2) Each symbol can only appear once in a row, column or mini-board.
'''

#Variables
full_board = [] #Main board
rows = [] #Horizontal
cols = [] #Vertical
cells = random.sample(range(1, 10), 9) #Unique range of elements to create cells in each row.

def validate(x, y): #Validates Sudoku patterns
    offsets = (3 * (x % 3) + x // 3 + y) % 9 #Credits to: https://en.wikipedia.org/wiki/Mathematics_of_Sudoku and others. This formula calculates the offsets so the numbers fit on a valid 9x9 Sudoku puzzle.
    return offsets #Gives the correct number to rank.

#Parent Row
for row in random.sample(range(3), 3): #Loops through a random range of 3 numbers.
    for r in random.sample(range(3), 3): #Loops through another random range of 3 numbers, effectively multiplying by 3 and creating a whole row with 9 shuffled elements.
        rows.append(r * 3 + row) #A mathematic property in morphology. Credits to: https://en.wikipedia.org/wiki/Mathematical_morphology If you have a set of numbers and apply a transformation to each element of the set, the elements correspond to a new, unique number. The generalization is dilation of n and translation of n-n, n-(n-1), n-(n-2), ... n-(n-(n-1)). Finally, the set is shuffled for a game of Sudoku, then checked later on.
#Parent Column
for col in random.sample(range(3), 3): #Columns use the same method as the rows.
    for c in random.sample(range(3), 3): #9 elements in a column, all randomized.
        cols.append(c * 3 + col) #Transformation to map the side length of each mini-board to the main board perfectly with unique numbers.

#Main Board
for r in rows: #Building the main board.
    rank = [] #Local variable to append each row later.
    for c in cols: #Two-dimensionalizing the plane.
        rank.append(cells[validate(r, c)]) #Each row is called a rank. Cells are being appended at random, but being validated based off the parent row and column.
    full_board.append(rank) #Append the valid rank to the main board.

hidden_board = copy.deepcopy(full_board) #Gets around Python's list deep copying.

#Difficulty
for rank in hidden_board: #Goes through each rank.
    for cell in range(len(rank)): #Goes through each cell.
        difficulty = 60 #The higher the difficulty, the harder the difficulty.
        if random.randint(1, 100) <= difficulty: #Random chance for difficulty.
            rank[cell] = 0 #"0" is a placeholder for nothing. You fill these in.