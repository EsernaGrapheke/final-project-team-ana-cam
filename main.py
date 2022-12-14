from time import sleep


def dibujarMatriz(matriz):
    """
    Show the matrix in the screen
    :param matriz: any 2D matrix of any size
    """
    print("\n"*80)
    print("Best Solution:")
    for renglon in matriz:
        for columna in renglon:
            print(columna, end='')
        print()
    sleep(0.5)


def copyMatrix(matriz):
    """
    Copy a matrix
    :param matriz: any 2D matrix of any size
    :return: a copy of the matrix
    """
    matrizCopiada = []
    for renglon in matriz:
        matrizCopiada.append([])
        for columna in renglon:
            matrizCopiada[-1].append(columna)
    return matrizCopiada


def copyList(lista):
    """
    Copy a list
    :param lista: any list of any size
    :return: a copy of the list
    """
    listaCopiada = []
    for elemento in lista:
        listaCopiada.append(elemento)
    return listaCopiada


def checkIfNextToSolution(matriz, xcoordinate, ycoordinate):
    """
    Check if the current position is next to the solution
    :param matriz: any 2D matrix of any size
    :param xcoordinate: the x coordinate of the current position
    :param ycoordinate: the y coordinate of the current position
    :return: True if the current position is next to the solution, False otherwise
    """
    if matriz[xcoordinate][ycoordinate - 1] == 'S' or \
            matriz[xcoordinate - 1][ycoordinate] == 'S' or \
            tempMatrix[xcoordinate][ycoordinate + 1] == 'S' or \
            tempMatrix[xcoordinate + 1][ycoordinate] == 'S':
        return True
    else:
        return False


labyrinth = [['x', 'x', 'x', 'x', 'x', 'x'],
             ['x', ' ', ' ', ' ', 'S', 'x'],
             ['x', ' ', 'x', 'x', ' ', 'x'],
             ['x', ' ', 'x', 'x', ' ', 'x'],
             ['x', ' ', 'x', 'x', ' ', 'x'],
             ['x', ' ', 'x', ' ', ' ', 'x'],
             ['x', ' ', 'x', ' ', 'x', 'x'],
             ['x', ' ', ' ', 'E', ' ', 'x'],
             ['x', 'x', 'x', 'x', 'x', 'x']]

# labyrinth = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
#              ['x', ' ', 'x', ' ', ' ', ' ', ' ', 'x'],
#              ['x', ' ', 'x', 'x', ' ', 'x', ' ', 'x'],
#              ['x', ' ', 'x', 'x', ' ', 'x', ' ', 'x'],
#              ['x', ' ', 'x', 'x', ' ', 'x', ' ', 'x'],
#              ['x', 'E', ' ', ' ', ' ', ' ', 'S', 'x'],
#              ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

tempMatrix = copyMatrix(labyrinth)
optimalSteps = 10000
solution = [[]]

y=0
while y<len(labyrinth):
    x=0
    while x<len(labyrinth[0]):
        if labyrinth[y][x]=="E":
            originx=x
            originy=y
        x=x+1
    y=y+1



currentlocationx=originx
currentlocationy=originy
while checkIfNextToSolution (maze, currentlocationx, currentlocationy) is False:
    if maze[currentlocationy][currentlocationx -1] == " ":
        PathLeft = True
        numberOfpaths += 1
    if maze[currentlocationy][currentlocationx +1] == " ":
        PathRight = True
        numberOfpaths += 1
    if maze[currentlocationy-1][currentlocationx] == " ":
        PathUp = True
        numberOfpaths += 1
    if maze[currentlocationy+1][currentlocationx] == " ":
        PathDown = True
        numberOfpaths += 1
    if PathLeft is True:
        maze[currentlocationy][currentlocationx-1] = "??"
        currentlocationx -=1
    if PathRight is True:
        maze[currentlocationy][currentlocationx+1] = "??"
        currentlocationx +=1
    if PathUp is True:
        maze[currentlocationy-1][currentlocationx] = "??"
        currentlocationy -=1
    if PathDown is True:
        maze[currentlocationy+1][currentlocationx] = "??"
        currentlocationy +=1
    
    if numberOfpaths > 1:
        checkpointx = originx
        checkpointy = originy

if checkIfNextToSolution (maze, currentlocationx, currentlocationy) is True:
    print ("Congratulations, you have succesfully solved this maze")
    print ("The number of steps it took to solve this maze was ",numberOfpaths)


dibujarMatriz(solution)
print("Optimum number of steps:", optimalSteps)
