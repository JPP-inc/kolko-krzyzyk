def display_board(board):
    for row in board:
        print(" | ".join(row))
     print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
            
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    
    while True:
        display_board(board)
        player = players[turn % 2]
        print(f"Ruch gracza {player}")
        
        while True:
            try:
                row, col = map(int, input("Podaj wiersz i kolumnę (0-2) oddzielone spacją: ").split())
                if board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("To pole jest już zajęte, spróbuj ponownie.")
            except (ValueError, IndexError):
                print("Nieprawidłowy ruch. Podaj dwie liczby od 0 do 2.")
        
        if check_winner(board, player):
            display_board(board)
            print(f"Gracz {player} wygrywa")
            break
        
        if is_draw(board):
            display_board(board)
            print("Jest remis :) ")
            break
        
        turn += 1

if __name__ == "__main__":
    tic_tac_toe()

