#tic-tac-toe in python
from random import randrange
import sys
board_fields = [1,2,3,4,5,6,7,8,9]


def display_board():
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    cells = board_fields
    
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   {0}   |   {1}   |   {2}   |'.format(cells[0],cells[1],cells[2]))
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   {0}   |   {1}   |   {2}   |'.format(cells[3],cells[4],cells[5]))
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   {0}   |   {1}   |   {2}   |'.format(cells[6],cells[7],cells[8]))
    print('|       |       |       |')
    print('+-------+-------+-------+')
    result()

def enter_move():
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
    
    # using while loop for any matches
    while True:               
        
        # code for computer and user moves
        free_fields = make_list_of_free_fields()
        computer_move = randrange(1,10)
        user_move = int(input("\nEnter your move :: "))
        print()
        print("Computer Choice :: ",computer_move)
        print("Your choice :: ",user_move)
        print()
        
        # loggic for movers
        if computer_move == user_move:
            print("|Sorry, computer and you cannot choose same move|")
            continue
        elif user_move-1 not in free_fields:
            print("|Sorry that field is occupied|")
            continue
        elif computer_move-1 not in free_fields:
            print("Sorry computer has chosen the move which is not free.")
            continue
        else:
            board_fields[user_move-1] = 'x'
            board_fields[computer_move-1] = 'o'
            display_board()
            break
        
    


def make_list_of_free_fields():
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    
    free_fields = []
    for i in range(len(board_fields)):
        if board_fields[i] == 'o' or board_fields[i] == 'x':
            continue
        else:
            free_fields.append(i)
        
    return free_fields
    
    


def victory_for():
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    for i in board_fields:
        #Logic for victory of user.
        if (board_fields[0]=='x' and board_fields[1]=='x' and board_fields[2]=='x') or (board_fields[3]=='x' and board_fields[4]=='x' and board_fields[5]=='x') or (board_fields[6]=='x' and board_fields[7]=='x' and board_fields[8]=='x'):
            print("\nYou Win!!!!!")
            return True
        elif (board_fields[0]=='x' and board_fields[3]=='x' and board_fields[6]=='x') or (board_fields[1]=='x' and board_fields[4]=='x' and board_fields[7]=='x') or (board_fields[2]=='x' and board_fields[5]=='x' and board_fields[8]=='x'):
            print("\nYou Win!!!!!")
            return True
        elif (board_fields[0]=='x' and board_fields[4]=='x' and board_fields[8]=='x') or (board_fields[2]=='x' and board_fields[4]=='x' and board_fields[6]=='x'):
            print("\nYou Win!!!!!")
            return True
        
        #Logic for victory of computer.
        if (board_fields[0]=='o' and board_fields[1]=='o' and board_fields[2]=='o') or (board_fields[3]=='o' and board_fields[4]=='o' and board_fields[5]=='o') or (board_fields[6]=='o' and board_fields[7]=='o' and board_fields[8]=='o'):
            print("\nYou Lose!!!!!")
            return True
        elif (board_fields[0]=='o' and board_fields[3]=='o' and board_fields[6]=='o') or (board_fields[1]=='o' and board_fields[4]=='o' and board_fields[7]=='o') or (board_fields[2]=='o' and board_fields[5]=='o' and board_fields[8]=='o'):
            print("\nYou Lose!!!!!")
            return True
        elif (board_fields[0]=='o' and board_fields[4]=='o' and board_fields[8]=='o') or (board_fields[2]=='o' and board_fields[4]=='o' and board_fields[6]=='o'):
            print("\nYou Lose!!!!!")
            return True
            
        

def result():
    # The function draws the computer's move and updates the board.
    if victory_for():
        choice = input("Do you want to play more?|(y/n)")
        if choice.lower() == 'y':
            for i in range(len(board_fields)):
                board_fields[i] = i+1;
            display_board()
        else:
            sys.exit()
    else:
        enter_move()

# calling function 
if __name__=="__main__":
    display_board()
