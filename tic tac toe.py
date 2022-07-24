import random

def displayBoard(board):
    for list in board:
        print(*list, sep =' ') #I really wanted to fix the visuals of it so that the columns were straight but I could not find any solution to this that would not be tedious in the time I had

def checkIfLegal (number, board):
    count = 1
    if number > 0 and number <= (len(board) * len(board)): #check to see if value is in range
        for i in range(len(board)):
            for j in range(len(board)):
                if count == number:
                    if board[i][j] != 'X' and board[i][j] != 'O': #check to see if position is already taken
                        return True
                    return False
                count += 1
    return False

def checkWinner (board):
    condition = True
    for line in board: #horizontal check
        condition = True
        for i in range(1, len(board)):
            if line[i] != line[i-1]:
                condition = False
                break
        if condition:
            return True
            
    for j in range(len(board)): #vertical check
        condition = True
        for i in range(1, len(board)):
            if board[i][j] != board[i-1][j]:
                condition = False
                break
        if condition:
            return True

    condition = True
    for i in range(1, len(board)): #diagonal check 1
        if board[i][i] != board [i-1][i-1]:
            condition = False
            break
    if condition:
        return True

    condition = True
    for i in range(1, len(board)): #diagonal check 2
        if board[i][len(board)-1-i] != board [i-1][len(board)-i]:
            condition = False
            break
    if condition:
        return True

def computerMove (board):
    while True:
        number = random.randint(1, len(board)**2)
        if checkIfLegal(number, board): #only returns number if its valid
            return number

def smartComputerMove (board, n):
        tempboard = []
        count = 1

        for i in range(n): #creates the board
            l = []
            for j in range (n):
                l.append(count)
                count += 1
            tempboard.append(l)

        for list in board: #to block player horizontally
            count = 0
            for i in list:
                if i == 'X':
                    count += 1
            if count == 4:
                for j in range(len(list)):
                    if checkIfLegal(list[j], board):
                        return list[j]

        for list in board: #to win as a computer horizontally
            count = 0
            for i in list:
                if i == 'O':
                    count += 1
            if count == 4:
                for j in range(len(list)):
                    if checkIfLegal(list[j], board):
                        return list[j]

        count = 0
        for i in range(len(board)): #to block player vertically
            for j in range(len(board)):
                if board[i][j] == 'X':
                    count += 1
            if count == 4:
                for k in range(len(board)):
                    if checkIfLegal(tempboard[i][k], board):
                        return tempboard[i][k]

        count = 0
        for i in range(len(board)): #to win as a computer horizontally
            for j in range(len(board)):
                if board[i][j] == 'O':
                    count += 1
            if count == 4:
                for k in range(len(board)):
                    if checkIfLegal(tempboard[i][k], board):
                        return tempboard[i][k]

def change(number, board, symbol):
    count = 1
    for i in range(len(board)):
        for j in range(len(board)):
            if count == number:
                board[i][j] = symbol
                return
            count += 1

def main():
    
    print('\nHello and welcome to the Tic-Tac-Toe Comp 208 challenge: Player against Computer.\n')
    print('The board is numbered from 1 to 25 as per the following:\n')
    print(' 1  2  3  4  5\n 6  7  8  9 10\n11 12 13 14 15\n16 17 18 19 20\n21 22 23 24 25\n')
    print('Player starts first. Simply input the number of the cell you want to occupy. Player’s move is marked with X. Computer’s move is marked with O.\n')
    
    start = input('Start? (y/n):')
    if start == 'y':
        board = []
        move = 0
        count = 1
        n = 0

        while True:
            n = int(input('Enter dimentions of the board: \n'))
            if n>=3:
                break
            else:
                print('Value needs to be more than 2! Try Again.')

        for i in range(n): #creates the board
            l = []
            for j in range (n):
                l.append(count)
                count += 1
            board.append(l)
        displayBoard(board)

        while move <= (len(board) * len(board)):
            if move == (len(board) * len(board)):
                print("It's a tie!")
                exit(0)
            if move%2 == 0: #to decide if players turn
                while True:
                    number = int(input('Enter Number: '))
                    if checkIfLegal(number, board):
                        break
                    else:
                        print('Invalid or unavailable number. Try Again!')
                change(number, board, 'X')
                displayBoard(board)
                if checkWinner(board):
                    print("Congratulations. Player wins.")
                    exit(0)
            else:
                number = smartComputerMove(board, n) #computers move
                if number == None:
                    number = computerMove(board)
                print('Computer Number = ', number)
                change(number, board, 'O')
                displayBoard(board)
                if checkWinner(board):
                    print("Congratulations. Computer wins.")
                    exit(0)
            move += 1
    elif start != 'n':
        print('Enter either y or n please! Rerun code please!')
    else:
        print('Bye Bye!')
    return

main()