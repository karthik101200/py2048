import random as random #mod for inserting random 2
import sys
import os               #mod required for clear screen so that the game looks like being played on the same board
import msvcrt           #so that user doesnt need to press "enter" eerytime
import math
import copy             #this mod is used to copy 1 list to another ...changes made to 1st one wont copy to the 2nd.

def clear():
    os.system("cls")


def board_size():                                              
    default_size=5
    bsize=int(input("enter the board size-") or default_size)
    
    return bsize

def win_val():
    default_val=2048                                       
    win=int(input("enter winning value-") or default_val)   #decides winning value(eg 128) that is user defined or def
    if math.log(win, 2).is_integer()==True:
        return win
    else:
        print("input a valid power of 2")
        return win_val()
clear()
print("You are about start the game \n use keys wasd for movement\n use 'e' to exit while playing\n press any key to continue ")
ent=msvcrt.getch()
clear()
bsize=board_size()
win=win_val()

boardmat=[]
for i in range(bsize):          #creates a matrix of 0s of user defined size or def value
    boardmat.append([0]*bsize)

def print_board(boardmat):
    for row in boardmat:
        print(row)


def random_int(boardmat):
    r1 =random.randint(0,len(boardmat)-1)
    r2 =random.randint(0,len(boardmat)-1)
    while boardmat[r1][r2]!=0:                   #random algo to insert random 2 after every valid move
        r1= random.randint(0,len(boardmat)-1)
        r2= random.randint(0,len(boardmat)-1)
    boardmat[r1][r2]=2
    print_board(boardmat)
    return boardmat

random_int(boardmat)

def win_game(win,boardmat):
    value=win
    wlog = value in (item for sublist in boardmat for item in sublist)  #winning algo that checks whether given value is present in the matrix
    if wlog:
        clear()
        print_board(boardmat)
        print("u win")
        exit()
    else:
        return(boardmat)

def lose_game(boardmat):
    count=0
    for i in range(len(boardmat)-1):
        for j in range(len(boardmat[0])-1):
            if boardmat[i][j] == boardmat[i+1][j] or boardmat[i][j+1] == boardmat[i][j]:
                count+=1
    for i in range(len(boardmat)):
        for j in range(len(boardmat[0])):
            if boardmat[i][j] == 0:                              #losing algo-checks whether there is an open space(0) or if a valid move is possible
                count+=1
    for k in range(len(boardmat)-1):
        if boardmat[len(boardmat)-1][k] == boardmat[len(boardmat)-1][k+1]:
            count+=1
    for j in range(len(boardmat)-1):
        if boardmat[j][len(boardmat)-1] == boardmat[j+1][len(boardmat)-1]:
            count+=1
    if count==0:
        clear()
        print_board(boardmat)
        print("u lose")
        exit()
#shifting and merging algo for wasd or up,left,right and down resp    

def left_shift(boardmat):
    temp=copy.deepcopy(boardmat) 
    for i in range(len(boardmat)):
        count = 0
        for j in  range(len(boardmat)):
                                                                   
            for k in range(len(boardmat)-1):
                
                if boardmat[i][k] == 0:
                    (boardmat[i][k+1],boardmat[i][k])=(boardmat[i][k],boardmat[i][k+1])
                elif boardmat[i][k] == boardmat[i][k+1] and count==0:
                    (boardmat[i][k], boardmat[i][k + 1]) = (2 * boardmat[i][k], 0)
                    count+=1
                
    win_game(win, boardmat)
    lose_game(boardmat)
    if temp==boardmat:
        print("try another move")
        user_inp()
    else:
        random_int(boardmat)

def up_shift(boardmat):
    temp=copy.deepcopy(boardmat) 
    for i in range(len(boardmat)):
        count = 0
        for j in  range(len(boardmat)):
            
            for k in range(len(boardmat) - 1):
                
                if boardmat[k][i] == 0:
                    (boardmat[k+1][i],boardmat[k][i])=(boardmat[k][i],boardmat[k+1][i])
                elif boardmat[k][i]==boardmat[k+1][i] and count==0:
                    (boardmat[k][i],boardmat[k+1][i])=(2*boardmat[k][i],0)
                    count+=1
    win_game(win,boardmat)
    lose_game(boardmat)
    if temp==boardmat:
        print("try another move")
        user_inp()
    else:
        random_int(boardmat)

def right_shift(boardmat):
    temp=copy.deepcopy(boardmat) 
    for i in range(len(boardmat)):
        count = 0
        
        
        for j in range(len(boardmat)):
            
            for k in range(len(boardmat)-1,0,-1):
                if boardmat [i][k]==0:
                    (boardmat[i][k],boardmat[i][k-1])=(boardmat[i][k-1],boardmat[i][k])
                elif boardmat[i][k]==boardmat[i][k-1] and count==0:
                    (boardmat[i][k],boardmat[i][k-1])=[2*boardmat[i][k],0]
                    count+=1
    win_game(win,boardmat)
    lose_game(boardmat)
    if temp==boardmat:
        print("try another move")
        user_inp()
    else:
        random_int(boardmat)

def down_shift(boardmat):
    temp=copy.deepcopy(boardmat) 
    for i in range(len(boardmat)):
        count = 0
        for j in  range(len(boardmat)):
           
            for k in range(len(boardmat) - 1,0,-1):
                
                if boardmat[k][i] == 0:
                    (boardmat[k][i],boardmat[k-1][i])=(boardmat[k-1][i],boardmat[k][i])
                elif boardmat[k][i]==boardmat[k-1][i] and count==0 :
                    (boardmat[k][i],boardmat[k-1][i])=(2*boardmat[k][i],0)
                    count+=1
    win_game(win,boardmat)
    lose_game(boardmat)
    if temp==boardmat:
        print("try another move")
        user_inp()
    else:
        random_int(boardmat)
#algo fn for valid user input
def user_inp():
    inp=msvcrt.getch()
    if inp.lower()==b'a':
        clear()
        left_shift(boardmat)
        user_inp()


    elif inp.lower()==b'w':
        clear()
        up_shift(boardmat)
        user_inp()


    elif inp.lower()==b'd':
        clear()
        right_shift(boardmat)
        user_inp()

    elif inp.lower()==b's':
        clear()
        down_shift(boardmat)
        user_inp()

    elif inp.lower()==b'e':
        clear( )
        sys.exit()

    else:
        clear()
        print("invalid input try again")
        user_inp()


user_inp()
