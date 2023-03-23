import random
#This line imports the random module, which we will use to generate random numbers for the initial state of the board.

def get_attacking_pairs(board):
  #it is basically taking board configuration as an input 
  #it then calculates the number of attacking pairs based on the idea if any two queens are in the same diagnol or column or row 
  
    pairs = 0
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            if board[i] == board[j] or abs(board[i]-board[j]) == abs(i-j):
                pairs += 1 #increment the number each time we find an attacking pair 
    return pairs

def get_neighbors(board):
  #we are generating the neighboring states of the board here 
    neighbors = []
    for col in range(len(board)): #checking all the columns 
        for row in range(len(board)): #checking all the rows 
            if row != board[col]: #if a differnt row can be placed in a column to generate a new state 
                new_board = list(board)
                new_board[col] = row
                neighbors.append(new_board)
    return neighbors
#If a new state is generated, it is added to the list of neighbors    

def hill_climbing():
    
    # Initialize the board with random positions
    board = [random.randint(0,3) for _ in range(4)]
    pairs = get_attacking_pairs(board) #evaluating the objective function that is number of attacking pairs in a particular setting of the board
    iterations = 0
    
    # Repeat until the objective function is zero (there are no attacking pairs of queens) 
    #it also find if we are at a local minima 
    while pairs > 0:
        iterations += 1
        print(f"Iteration {iterations}: {board} ({pairs} pairs)") # here we are printing the number of iteration and the attacking pairs 
                                                                  #in that particular board setting 
        # Generate all neighboring states of the current state
        neighbors = get_neighbors(board)
        
        # Find the neighbor with the lowest objective function
        best_neighbor = None
        best_pairs = pairs
        for neighbor in neighbors:
          #Inside the loop, the function generates all neighboring states of the current state and finds the neighbor with the lowest objective function (i.e., the fewest attacking pairs).
          #If there is a better neighbor, it selects it as the new current state and updates the objective function. If no better neighbor is found, the function stops the algorithm.
            neighbor_pairs = get_attacking_pairs(neighbor)
            if neighbor_pairs < best_pairs:
                best_neighbor = neighbor #will lowest objective function 
                best_pairs = neighbor_pairs
        
        # If there is a better neighbor, select it as the new current state
        if best_neighbor is not None:
            board = best_neighbor
            pairs = best_pairs
        else:
            break
    
    print(f"Solution found in {iterations} iterations: {board}")
    return board

hill_climbing()
