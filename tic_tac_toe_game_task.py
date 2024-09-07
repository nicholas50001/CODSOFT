import math

board = [' ' for _ in range(9)]

def print_the_board():
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def check_the_winner(player):
    winning_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_board_full():
    return ' ' not in board

def minimax(is_maximizing):
    if check_the_winner('O'):
        return 1  
    if check_winner('X'):
        return -1  
    if is_board_full():
        return 0  

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    print_the_board()
    while True:
        
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] == ' ':
            board[move] = 'X'
            if check_the_winner('X'):
                print_the_board()
                print("You win!!")
                break
            if is_board_full():
                print_the_board()
                print("It's a draw!")
                break

            
            ai_move = best_move()
            board[ai_move] = 'O'
            print_the_board()

            if check_the_winner('O'):
                print("AI wins!")
                break
            if is_board_full():
                print("It's a draw!")
                break
        else:
            print("Invalid move! Try again.")

play_game()
