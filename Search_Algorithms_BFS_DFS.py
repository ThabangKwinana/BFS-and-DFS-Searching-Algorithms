import queue
import networkx as nx
import collections
from queue import Queue
from collections import deque
import numpy as np
import sys
sys.setrecursionlimit(1500)


filename = "matrix.txt"

def readMatrixFile(): #The input file is read
    with open("/content/Given 1.txt") as f:
        lines = f.readlines()
    matrix = [[c for c in line.rstrip('\n')] for line in lines]
    return matrix


def getChildNodes(matrix, curr):  # This is a method that gets the neighbor nodes of the current node
    row, col = curr
    neighbors = []

    if row > 0 and matrix[row - 1][col] != ' ': # here you determine which path and direction is valid, that the current node can take
        neighbors.append(('U', (row - 1, col)))

    if row < len(matrix) - 1 and matrix[row + 1][col] != ' ': # here you determine which path and direction is valid, that the current node can take
        neighbors.append(('D', (row + 1, col)))

    if col > 0 and matrix[row][col - 1] != ' ':
        neighbors.append(('L', (row, col - 1)))

    if col < len(matrix[0]) - 1 and matrix[row][col + 1] != ' ': # here you determine which path and direction is valid, that the current node can take
        neighbors.append(('R', (row, col + 1)))

    return neighbors # here you return a list that contains the direction and valid paths of the current node


def defineGraph(matrix): # this method defines the start node and the end node from the matrix
    start = None
    goal = None
    temp = []
     
    print("***The Graph To Be Traversed***")
    for i in range(len(matrix)): # the graph is displayed
       print(matrix[i])
    print("\n")

    for row in range(len(matrix)): # here the start node and end node are assigned
       for col in range(len(matrix[0])):
           cell = matrix[row][col]
           if cell == 'S':
               start = (row, col)
           elif cell == 'G':
               goal = (row, col)
    

    temp = (start, goal)

    return(temp)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

#Depth-first algorithm is implemented recursively.

def DFS_Recursive(matrix, start, goal, visited, stack, curr): # This is a recursive depth-first search method
    print("Current Node: ", curr)  
    if curr == goal: # here we check is the current node is the goal node
        path = [] # if the current node is the goal node we declare a list that that will return the path found
        while curr != start: # here the path is reconstructed from the goal node to the root start node
            path.append(curr)
            direction, curr = visited[curr]
        path.append(start)
        return path[::-1] # the path is returned
    else:
        for direction, neighbor in getChildNodes(matrix, curr): # the method that gets the children of the current node is called
            if neighbor not in visited: 
                stack.append((direction, neighbor)) # the open list is updated by appending the open nodes
                visited[neighbor] = (direction, curr)
        direction, curr = stack.pop()
        return DFS_Recursive(matrix, start, goal, visited, stack, curr) # the method calls itself
    return None # return none if the path was not found


if __name__ == '__main__':
    graph = readMatrixFile() # the graph is created by calling the read file method
    start = None # the start node is declared
    goal = None # the goal node is declared
     
    stack = [] # the open list is declared

    value = defineGraph(graph)
    start = value[0] # the start node is assigned
    goal = value[1]  # the start node is assigned
    visited = {start: (None, None)}  # The visited list is declared
    curr = start
    
    if start == None and goal == None:
        print("No start and goal have been defined, therefore the path cannot be determined")
    else:
        path = DFS_Recursive(graph, start, goal, visited, stack, curr) # the depth first search method is called
        if path == None:
           print("Path could not be found")
        else:
           print("\nDepth-First Search(Recursive) Output Path:")
           print(path) # the path is displayed
		   
#-------------------------------------------------------------------------------------------------------------------------------------------------------
 

#Here the Depth-first algorithm is implemented iteratively.

def DFS_Iterative(matrix, start, goal):  # This is an iterative depth-first search method
    openList = [(None, start)]  # this a queue open list that will store open nodes
    visited = {start: (None, None)}  # this a visited list that will store parent nodes 
    numNodes = 0

    while openList:
        direction, curr = openList.pop() # here the open list is popped to get the current node to evaluate
        numNodes += 1
        print("Current Node: ", curr)
        if curr == goal:
            path = []  # if the current node is the goal node we declare a list that that will return the path found
            while curr != start: # here the path is reconstructed from the goal node to the root start node
                path.append((direction, curr))
                curr, direction = visited[curr]
            path.append((direction, start))
            print("\nNumber of nodes evaluated: ", numNodes)
            return path[::-1]  # the path is returned
        for direction, neighbor in getChildNodes(matrix, curr): # the method that gets the children of the current node is called
            if neighbor not in visited:
                openList.append((direction, neighbor)) # the open list is updated by appending the open nodes
                visited[neighbor] = (curr, direction)
    return None  # return none if the path was not found



def displayPathDFS(path): # this method displays the path
    if validPath == None:
         print("Depth-First Search could not find a path")
    else:
       print("\nDepth-First Search(Iterative) Output Path:")
       for i in range(len(validPath)):
            (direction, node) = validPath[i]
            if node == goal:
                print(node, ": Goal")
            else:
                print(node, ": " , direction)


def writePathDFS(path):
    for i in range(len(path)):
            (direction, node) = path[i]
            if node == goal:
                continue
            else:
               with open('PATH.txt', 'a') as file:
                     file.write(direction)


if __name__ == '__main__':
    graph = read_file()   # the graph is created by calling the read file method
    start = None;   # the start node is declared
    goal = None;  # the goal node is declared
    values = []

    value = defineGraph(graph)
    start = value[0]  # the start node is assigned
    goal = value[1]  # the goal node is assigned

    if start == None or goal == None:   # here we check if the start and goal node are clearly defined
        print("Start or goal not defined, cannot solve path")
    else:
        validPath = DFS_Iterative(graph, start, goal)  #  here the depth-first search nethod is called
        displayPathDFS(validPath) # here the display path method is called
        writePathDFS(validPath) # here the write to file method is called
 
#-----------------------------------------------------------------------------------------------------------------------------------------------

# Here the Breadth-First Search is implemented recursively.

def BFS_Recursive(matrix, start, goal, visited, queue, curr): # this a bredath-first recursive method
    (direction, curr) = queue.pop(0) # the current node is popped from the open list
    print("Current Node: ", curr)
    if curr == goal: # here we check if the current node is the goal
      path = [] # if the current node is the goal node we declare a list that that will return the path found
      while curr is not None: # here the path is reconstructed
         path.append(curr)
         (direction, curr) = visited[curr]
      return path[::-1] # the path is returned
    else:
       for (direction, neighbor) in getChildNodes(matrix, curr): # the method that gets the children of the current node is called
           if neighbor not in visited:
              queue.append((direction, neighbor)) # the open list is updated
              visited[neighbor] = ((direction, curr))
       return BFS_Recursive(matrix, start, goal, visited, queue, curr) # the method calls itself
    return None # return none if the path was not found



if __name__ == '__main__':
    matrix = readMatrixFile() # the graph is created by calling the read file method
    start = None # the start node is declared
    goal = None # the goal node is declared
    
  
    value = defineGraph(graph)
    
    start = value[0]
    goal = value[1]

    visited = {start: (None, None)} # the visited list is declared
    queue = [(None, start)] # the open list is declared

    curr = start
    
    if start == None and goal == None: # here we check if the start & goal goal are defined 
        print("No start and goal have been defined, therefore the path cannot be determined")
    else:
        path = BFS_Recursive(matrix, start, goal, visited, queue, curr) # the breadth first search method is called
        if path == None:
           print("Path could not be found")
        else:
           print("\nBreadth-First(Recursive) Output Path:")
           print(path) # the path is printed
		   
#------------------------------------------------------------------------------------------------------------------------------------------------------------
 
# Here the Breadth-First Search is implemented iteratively.

def BFS_Iterative(graph, start, goal):    # This is an iterative breadth-first search method
    openList = [(None, start)]   # this a queue open list that will store open nodes 
    visited = {start: (None, None)}   # this a visited list that will store parent nodes 
    numNodes = 0

    while openList: 
        (direction, currentNode) = openList.pop(0)   # here the open list is popped to get the current node to evaluate
        numNodes += 1
        print("Current node: ", currentNode)
        if currentNode == goal:    # here we check is the current node is the goal node
            path = []        # if the current node is the goal node we declare a list that that will return the path found
            while currentNode is not None:     # here the path is reconstructed from the goal node to the root start node
                path.append((direction, currentNode))
                (direction, currentNode) = visited[currentNode]  
            print("\nNumber of nodes evaluated: ", numNodes)    
            return path[::-1]    # the path is returned
        for direction, neighbor in get_neighbors(graph, currentNode):    # the method that gets the children of the current node is called
              if neighbor not in visited:
                 openList.append((direction, neighbor))    # the open list is updated by appending the open nodes
                 visited[neighbor] = ((direction, currentNode))
    return None   # return none if the path was not found


def writePathBFS(path):   # this method writes the path found in a text file, for future reference
    for i in range(len(path)):
            (direction, node) = path[i]
            if node == goal:
                continue
            else:
               with open('PATH.txt', 'a') as file:
                     file.write(direction)


def displayPathBFS(path):  # this method displays the path
    if validPath == None:
         print("Breadth-First Search could not find a path")
    else:
       print("\nBreadth-First(Iterative) Output Path:")
       for i in range(len(validPath)):
            (direction, node) = validPath[i]
            if node == goal:
                print(node, ": Goal")
            else:
                print(node, ": " , direction)

if __name__ == '__main__':
    graph = read_file()   # the graph is created by calling the read file method
    start = None; # the start node is declared
    goal = None; # the goal node is declared
    values = []

    value = defineGraph(graph)
    start = value[0] # the start node is assigned
    goal = value[1] # the goal node is assigned

    if start == None or goal == None: # here check if the start and goal node are clearly defined
        print("Start or goal not defined, cannot solve path")
    else:
        validPath = BFS_Iterative(graph, start, goal) #  here the breadth-first search nethod is called
        displayPathBFS(validPath) # here the display path method is called
        writePathBFS(validPath) # here the write to file method is called
		
		
#------------------------------------------------------------------------------------------------------------------------------------------