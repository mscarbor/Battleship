from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print "You have 4 turns"
print "Misses will be shown as 'X' on the board"
print_board(board)

def random_row(board):
    return randint(0, len(board[0]) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# print ship_row <-Prints ship row
# print ship_col <-Prints ship column

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
def game():
    for turn in range(4):
        print "Turn", turn +1
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))
    
        if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations! You sunk my battleship!"
            break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or     guess_col > 4):
                print "Oops, that's not even in the ocean."
            elif(board[guess_row][guess_col] == "X"):
                print "You guessed that one already."
            else:
                if turn == 3:
                    print "Game Over"
                    board[guess_row][guess_col] = "X"
                    board[ship_row][ship_col]="B"
                else:
                    print "You missed my battleship!"
                    board[guess_row][guess_col] = "X"
            # Print (turn + 1) here!
                print_board(board)
    re_play = raw_input("Want to play agian?")
    if (re_play.lower()) == "yes":
        print "Okay, good luck!"
        game()
    else:
        print "Alright"
game()      
