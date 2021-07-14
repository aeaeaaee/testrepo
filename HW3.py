import time 

def neighbors(currentGen, row, column):
    """
        This function takes a 2D array and the row number and
        the column number of the target cell and returns the
        number of neighbor cells that are 1.
    """
    count = 0
    if row - 1 < 0:
        minRow = 0
    else:
        minRow = row - 1

    if column - 1 < 0:
        minCol = 0
    else:
        minCol = column - 1
    for rows in currentGen[minRow:row+2]:
        for cell in rows[minCol:column+2]:
            if cell == 1:
                count = count + 1
    if currentGen[row][column] == 1:
        count = count - 1
    return count


def nextgen(currentGen):
    """
        This function takes a 2D array and returns the next
        generation according to the rules of Conway's Game of
        Life. This function uses neighbors() shown above.
    """
    output = []
    for row in range(len(currentGen)):
        newRow = []
        for col in range(len(currentGen[row])):
            numNeighbours = neighbors(currentGen, row, col)
            if currentGen[row][col] == 0:
                if numNeighbours == 3:
                    newRow.append(1)
                else:
                    newRow.append(0)
            elif currentGen[row][col] == 1:
                if (numNeighbours == 2 or numNeighbours == 3) :
                    newRow.append(1)
                else:
                    newRow.append(0)
        output.append(newRow)
    return output


def print_life(currentGen):
    """
        This function prints the input 2D array. Every cell
        that is 1 is printed as a '#' and every cell that is 0
        is printed as an empty space.
    """

    output = ""

    for row in currentGen:
        for cell in row:
            if cell == 0:
                output = output + " "
            else:
                output = output + "#"

        output = output + "\n"

    output = output + "\n"

    # Print the output
    print(output)

def life(currentGen, generation):
    """
        This function implements Conway's Game of Life.
    """
    print("\n" * 100)
    print("Initial generation:")
    print(currentGen)
    time.sleep(1)
    newGen = currentGen
    
    for i in range(1,generation+1):
        newGen = nextgen(newGen)
        print("\n" * 100)
        print ("Generation " + str(i)+ " :" )
        print_life(newGen)
        time.sleep(1)
        


start = [
[0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0], 
[0, 1, 1, 1, 0], 
[0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0]
]



# Here are some interesting 2D arrays with initial values
# (some lines use '\' because they may be too long to fit on
# one line)

tumbler = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0],
[0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0],
[0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
# It's better if you use at least 30 for the number of
# generations

face = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
[0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0],
[0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0],
[0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
# It's better if you use at least 30 for the number of
# generations

glider_gun = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
 0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
 0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,\
 0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,\
 0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],
[0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,\
 0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,\
 0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,\
 0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,\
 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,\
 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
# It's better if you use at least 50 for the number of
# generations
