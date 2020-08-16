# Tic Tac Toe

board = [' ' for i in range(10)]
# range() takes (0-9) because the user will give position in (1-9), 0th index will be free.

def insert_letter(position, letter):
    # insert 'X' or 'O' in the position.
    board[position] = letter

def is_space_free(board, position):
    return board[position] == ' '

def is_board_full(board):
    # 0th position has ' ', board is not full if two spaces are still there.
    if(board.count(' ') > 1):
        return False
    else:
        return True

def print_board(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def is_winner(b, l): # 'l' stands for 'letter' ('X' or 'O')
    return ((b[1] == b[2] == b[3] == l) or (b[4] == b[5] == b[6] == l) or\
           (b[7] == b[8] == b[9] == l) or (b[1] == b[4] == b[7] == l) or\
           (b[2] == b[5] == b[8] == l) or (b[3] == b[6] == b[9] == l) or\
           (b[1] == b[5] == b[9] == l) or (b[7] == b[5] == b[3] == l))

def player_move():
    run = True
    while run:
        try:
            move = int(input('Enter a position for \'X\' ranging (1-9): '))
            if(move > 0 and move < 10):
                if(is_space_free(board, move)):
                    run = False
                    insert_letter(move, 'X')
                else:
                    print('This space is occupied, try different position!')
            else:
                print('Enter a number in range (1-9)!')
        except:
            print('Please, enter a valid number!')
                
def computer_move():
    possible_positions = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0 # default position
                
    for letter in ['O', 'X']:
        for i in possible_positions:
            board_copy = board[:] # making a clone of board
            board_copy[i] = letter
            # checking if computer can win...
            if(is_winner(board_copy, letter)):
                move = i
                return move
        
    open_corners = []
    for i in possible_positions:
        if i in [1, 3, 7, 9]:
            open_corners.append(i)
    
    if(len(open_corners) > 0):
        move = select_random(open_corners)
        return move
        
    if(5 in possible_positions):
        move = 5
        return move
        
    open_edges = []
    for i in possible_positions:
        if i in [2, 4, 6, 8]:
            open_edges.append(i)
    
    if(len(open_edges) > 0):
        move = select_random(open_edges)
    
    return move
    
def select_random(List):
    from random import randrange
    length = len(List)
    choice = randrange(0, length)
    return List[choice]
    
def main():
    print('Welcome to Tic Tac Toe vs Alex, our computer!')
    print(print_board(board)) 
    
    while(not(is_board_full(board))):
        if(not(is_winner(board, 'O'))):
            player_move()
            print_board(board)
            
        else:
            print('Sorry, Alex\'s won this time!')
            break
        
        if(not(is_winner(board, 'X'))):
            move = computer_move()
            if(move == 0):
            # computer_move() returns 0, if no move is possible
                print('It\'s a TIE...')
                break
            
            else:
                insert_letter(move, 'O')
                print('Alex placed an \'O\' in position', move, '.')
                print_board(board)
            
        else:
            print('You won this time! Good Job!')
            break
    
    if(is_board_full(board)):
        print('It\'s a TIE')

main()
