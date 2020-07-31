# This is the default noughts and crosses bot from aigaming.com.
# It contains functions for choosing a random move, blocking an opponent's 2-in-a-row, 
# and winning the game if you have a 2-in-a-row.


#   _   _                   _     _            _              _    ____                             
#  | \ | | ___  _   _  __ _| |__ | |_ ___     / \   _ __   __| |  / ___|_ __ ___  ___ ___  ___  ___ 
#  |  \| |/ _ \| | | |/ _` | '_ \| __/ __|   / _ \ | '_ \ / _` | | |   | '__/ _ \/ __/ __|/ _ \/ __|
#  | |\  | (_) | |_| | (_| | | | | |_\__ \  / ___ \| | | | (_| | | |___| | | (_) \__ \__ \  __/\__ \
#  |_| \_|\___/ \__,_|\__, |_| |_|\__|___/ /_/   \_\_| |_|\__,_|  \____|_|  \___/|___/___/\___||___/
#                     |___/                                                                         
botName='switch-1'

import random
import json
from random import randint

# These are the only additional libraries available to you. Uncomment them
# to use them in your solution.
#
#import numpy    # Base N-dimensional array package
#import pandas   # Data structures & analysis


# =============================================================================
# This calculateMove() function is where you need to write your code. When it
# is first loaded, it will play a complete game for you using the Helper
# functions that are defined below. The Helper functions give great example
# code that shows you how to manipulate the data you receive and the move
# that you have to return.
#

def calculateMove(gameState):
    ret = dict()
    pos = randomGuesser(gameState)
    print('My move is '+str(pos)+' OpponentId: '+gameState['OpponentId'])
    ret['Position'] = pos
    return ret

def randomGuesser(gameState): #Randomly guesses a position
    move = randint(0,8) #Random guess
    while(gameState["Board"][move] != " "): #If taken...
        move = randint(0,8) #... keep random guessing until found one
    return move

def oppTwoInRow(gameState): #Returns the (first) location that will block your opponent from winning, returns -1 otherwise
    myRole = gameState["Role"]
    if(myRole=="X"):
        oppRole = "O"
    else:
        oppRole = "X"
    if(((gameState["Board"][1]==oppRole and gameState["Board"][2]==oppRole)or(gameState["Board"][3]==oppRole and gameState["Board"][6]==oppRole)or(gameState["Board"][4]==oppRole and gameState["Board"][8]==oppRole))and gameState["Board"][0]==" "):
        move = 0
    elif(((gameState["Board"][0]==oppRole and gameState["Board"][2]==oppRole)or(gameState["Board"][4]==oppRole and gameState["Board"][7]==oppRole))and gameState["Board"][1]==" "):
        move = 1
    elif(((gameState["Board"][0]==oppRole and gameState["Board"][1]==oppRole)or(gameState["Board"][4]==oppRole and gameState["Board"][6]==oppRole)or(gameState["Board"][5]==oppRole and gameState["Board"][8]==oppRole))and gameState["Board"][2]==" "):
        move = 2
    elif(((gameState["Board"][0]==oppRole and gameState["Board"][6]==oppRole)or(gameState["Board"][4]==oppRole and gameState["Board"][5]==oppRole))and gameState["Board"][3]==" "):
        move = 3
    elif(((gameState["Board"][0]==oppRole and gameState["Board"][8]==oppRole)or(gameState["Board"][1]==oppRole and gameState["Board"][7]==oppRole)or(gameState["Board"][2]==oppRole and gameState["Board"][6]==oppRole)or(gameState["Board"][3]==oppRole and gameState["Board"][5]==oppRole))and gameState["Board"][4]==" "):
        move = 4
    elif(((gameState["Board"][2]==oppRole and gameState["Board"][8]==oppRole)or(gameState["Board"][3]==oppRole and gameState["Board"][4]==oppRole))and gameState["Board"][5]==" "):
        move = 5
    elif(((gameState["Board"][0]==oppRole and gameState["Board"][3]==oppRole)or(gameState["Board"][2]==oppRole and gameState["Board"][4]==oppRole)or(gameState["Board"][7]==oppRole and gameState["Board"][8]==oppRole))and gameState["Board"][6]==" "):
        move = 6
    elif(((gameState["Board"][1]==oppRole and gameState["Board"][4]==oppRole)or(gameState["Board"][6]==oppRole and gameState["Board"][8]==oppRole))and gameState["Board"][7]==" "):
        move = 7
    elif(((gameState["Board"][0]==oppRole and gameState["Board"][4]==oppRole)or(gameState["Board"][2]==oppRole and gameState["Board"][5]==oppRole)or(gameState["Board"][6]==oppRole and gameState["Board"][7]==oppRole))and gameState["Board"][8]==" "):
        move = 8
    else:
        move = -1
    return move

def twoInRow(gameState): #Returns the (first) location that will give you three in a row, returns -1 if none exist
    myRole = gameState["Role"]
    if(((gameState["Board"][1]==myRole and gameState["Board"][2]==myRole)or(gameState["Board"][3]==myRole and gameState["Board"][6]==myRole)or(gameState["Board"][4]==myRole and gameState["Board"][8]==myRole))and gameState["Board"][0]==" "):
        move = 0
    elif(((gameState["Board"][0]==myRole and gameState["Board"][2]==myRole)or(gameState["Board"][4]==myRole and gameState["Board"][7]==myRole))and gameState["Board"][1]==" "):
        move = 1
    elif(((gameState["Board"][0]==myRole and gameState["Board"][1]==myRole)or(gameState["Board"][4]==myRole and gameState["Board"][6]==myRole)or(gameState["Board"][5]==myRole and gameState["Board"][8]==myRole))and gameState["Board"][2]==" "):
        move = 2
    elif(((gameState["Board"][0]==myRole and gameState["Board"][6]==myRole)or(gameState["Board"][4]==myRole and gameState["Board"][5]==myRole))and gameState["Board"][3]==" "):
        move = 3
    elif(((gameState["Board"][0]==myRole and gameState["Board"][8]==myRole)or(gameState["Board"][1]==myRole and gameState["Board"][7]==myRole)or(gameState["Board"][2]==myRole and gameState["Board"][6]==myRole)or(gameState["Board"][3]==myRole and gameState["Board"][5]==myRole))and gameState["Board"][4]==" "):
        move = 4
    elif(((gameState["Board"][2]==myRole and gameState["Board"][8]==myRole)or(gameState["Board"][3]==myRole and gameState["Board"][4]==myRole))and gameState["Board"][5]==" "):
        move = 5
    elif(((gameState["Board"][0]==myRole and gameState["Board"][3]==myRole)or(gameState["Board"][2]==myRole and gameState["Board"][4]==myRole)or(gameState["Board"][7]==myRole and gameState["Board"][8]==myRole))and gameState["Board"][6]==" "):
        move = 6
    elif(((gameState["Board"][1]==myRole and gameState["Board"][4]==myRole)or(gameState["Board"][6]==myRole and gameState["Board"][8]==myRole))and gameState["Board"][7]==" "):
        move = 7
    elif(((gameState["Board"][0]==myRole and gameState["Board"][4]==myRole)or(gameState["Board"][2]==myRole and gameState["Board"][5]==myRole)or(gameState["Board"][6]==myRole and gameState["Board"][7]==myRole))and gameState["Board"][8]==" "):
        move = 8
    else:
        move = -1
    return move
