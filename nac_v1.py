# This is my first noughts-and-crosses bot. It borrows functions heavily from 
# the default script provided by aigaming.com.
# Specifically, it borrows functions for choosing a random move, blocking an opponent's 2-in-a-row, 
# and winning the game if you have a 2-in-a-row.

# Bot Strategy:
    # Do the following every turn:
        # Check for winning move
        # Check to block opponent's winning move if it exists
        # Take center square if possible
        # Take a random corner if possible
        # Take a random remaining square if necessary
        
# Results
    # Out of 100 matches against "housebot-practise", this bot won 84 and drew 16.
    # Out of 100 matches against "housebot-competition", this bot drew all 100.
    # There are no other players available to play against.
    

botName='switch-1'

import random

def calculateMove(gameState):
    
    ret = dict()
    
    if twoInRow(gameState) != -1:  # Check for winning move
        ret['Position'] = twoInRow(gameState)
        return ret
    
    if oppTwoInRow(gameState) != -1:  # Check to block opponent's winning move
        ret['Position'] = oppTwoInRow(gameState)
        return ret
    
    pos = random_plus(gameState)
    print('My move is '+str(pos)+' OpponentId: '+gameState['OpponentId'])
    ret['Position'] = pos
    return ret
    
# This function takes the center square if possible and otherwise guesses a 
# game state randomly.
def random_plus(gameState):
    
    gsb = gameState['Board']  # Simplify code
    
    if gsb[4] == " ":  # Take center square if available
        return(4)
        
    # If center square is taken, guess a corner.
    if (gsb[0] == " ") or (gsb[2] == " ") or (gsb[6] == " ") or (gsb[8] == " "):
           
           move = random.sample([0, 2, 6, 8], 1)
           while(gsb[move[0]] != " "): #If taken...
                move = random.sample([0, 2, 6, 8], 1)

           return(move[0])
        
    # Else guess randomly
    move = random.sample([1, 3, 5, 7], 1)
    while(gsb[move[0]] != " "): #If taken...
        move = random.sample([1, 3, 5, 7], 1) #... keep random guessing until found one
    return(move[0])
    
def oppTwoInRow(gameState): #Returns the (first) location that will block your opponent from winning, returns -1 otherwise
    myRole = gameState["Role"]
    gsb = gameState['Board']  # Simplify code
    if(myRole=="X"):
        oppRole = "O"
    else:
        oppRole = "X"
    if(((gsb[1]==oppRole and gsb[2]==oppRole)or(gsb[3]==oppRole and gsb[6]==oppRole)or(gsb[4]==oppRole and gsb[8]==oppRole))and gsb[0]==" "):
        move = 0
    elif(((gsb[0]==oppRole and gsb[2]==oppRole)or(gsb[4]==oppRole and gsb[7]==oppRole))and gsb[1]==" "):
        move = 1
    elif(((gsb[0]==oppRole and gsb[1]==oppRole)or(gsb[4]==oppRole and gsb[6]==oppRole)or(gsb[5]==oppRole and gsb[8]==oppRole))and gsb[2]==" "):
        move = 2
    elif(((gsb[0]==oppRole and gsb[6]==oppRole)or(gsb[4]==oppRole and gsb[5]==oppRole))and gsb[3]==" "):
        move = 3
    elif(((gsb[0]==oppRole and gsb[8]==oppRole)or(gsb[1]==oppRole and gsb[7]==oppRole)or(gsb[2]==oppRole and gsb[6]==oppRole)or(gsb[3]==oppRole and gsb[5]==oppRole))and gsb[4]==" "):
        move = 4
    elif(((gsb[2]==oppRole and gsb[8]==oppRole)or(gsb[3]==oppRole and gsb[4]==oppRole))and gsb[5]==" "):
        move = 5
    elif(((gsb[0]==oppRole and gsb[3]==oppRole)or(gsb[2]==oppRole and gsb[4]==oppRole)or(gsb[7]==oppRole and gsb[8]==oppRole))and gsb[6]==" "):
        move = 6
    elif(((gsb[1]==oppRole and gsb[4]==oppRole)or(gsb[6]==oppRole and gsb[8]==oppRole))and gsb[7]==" "):
        move = 7
    elif(((gsb[0]==oppRole and gsb[4]==oppRole)or(gsb[2]==oppRole and gsb[5]==oppRole)or(gsb[6]==oppRole and gsb[7]==oppRole))and gsb[8]==" "):
        move = 8
    else:
        move = -1
    return move

def twoInRow(gameState): #Returns the (first) location that will give you three in a row, returns -1 if none exist
    myRole = gameState["Role"]
    gsb = gameState['Board']  # Simplify code
    if(((gsb[1]==myRole and gsb[2]==myRole)or(gsb[3]==myRole and gsb[6]==myRole)or(gsb[4]==myRole and gsb[8]==myRole))and gsb[0]==" "):
        move = 0
    elif(((gsb[0]==myRole and gsb[2]==myRole)or(gsb[4]==myRole and gsb[7]==myRole))and gsb[1]==" "):
        move = 1
    elif(((gsb[0]==myRole and gsb[1]==myRole)or(gsb[4]==myRole and gsb[6]==myRole)or(gsb[5]==myRole and gsb[8]==myRole))and gsb[2]==" "):
        move = 2
    elif(((gsb[0]==myRole and gsb[6]==myRole)or(gsb[4]==myRole and gsb[5]==myRole))and gsb[3]==" "):
        move = 3
    elif(((gsb[0]==myRole and gsb[8]==myRole)or(gsb[1]==myRole and gsb[7]==myRole)or(gsb[2]==myRole and gsb[6]==myRole)or(gsb[3]==myRole and gsb[5]==myRole))and gsb[4]==" "):
        move = 4
    elif(((gsb[2]==myRole and gsb[8]==myRole)or(gsb[3]==myRole and gsb[4]==myRole))and gsb[5]==" "):
        move = 5
    elif(((gsb[0]==myRole and gsb[3]==myRole)or(gsb[2]==myRole and gsb[4]==myRole)or(gsb[7]==myRole and gsb[8]==myRole))and gsb[6]==" "):
        move = 6
    elif(((gsb[1]==myRole and gsb[4]==myRole)or(gsb[6]==myRole and gsb[8]==myRole))and gsb[7]==" "):
        move = 7
    elif(((gsb[0]==myRole and gsb[4]==myRole)or(gsb[2]==myRole and gsb[5]==myRole)or(gsb[6]==myRole and gsb[7]==myRole))and gsb[8]==" "):
        move = 8
    else:
        move = -1
    return move