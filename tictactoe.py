yeslist = ["yes", "yeah", "yep", "y", "sure", "ok", "okay", "absolutely"]
# board_squares = ["1","2","3","4","5","6","7","8","9"]

def main():

    print("Welcome to Kathryn's Tic Tac Toe")

    while True:
        board_squares = ["1","2","3","4","5","6","7","8","9"]
        winner = False
        play_again = input('Would you like to start a game? ')

        if play_again.lower() in yeslist:
            print()
            print("Let's Go!")
            print()

            

            while True:

                winner = check_winner(board_squares)
                
                if winner == False:

                    print("X - It's your turn!")
                    print()
                
                    draw_board(board_squares)
                    print()

                    place_xo("X", board_squares)
                    print()

                    winner = check_winner(board_squares)

                

                    if winner == False:          

                        print("O - It's your turn!")
                        print()

                        place_xo("O", board_squares)
                        print()

                    else: 
                        break

                else:
                    break
                






        else:
            print("Thanks for playing! Let's do this again soon.")
            break




def draw_board(squares_list):
    print(f" {squares_list[0]} | {squares_list[1]} | {squares_list[2]}")
    print("---+---+---")
    print(f" {squares_list[3]} | {squares_list[4]} | {squares_list[5]}")
    print("---+---+---")
    print(f" {squares_list[6]} | {squares_list[7]} | {squares_list[8]}")

def place_xo(team, squares_list):
    
    while True:

        position = int(input(f"In which numerical position would you like to place an '{team}'? "))
            
        if squares_list[position-1].lower() != "x" and squares_list[position-1].lower() != "o":
            squares_list[position - 1] = team
            draw_board(squares_list)
            break

        else:
                print("That position is already taken. Please try again.")    
    
    return squares_list

def check_winner(squares_list):
    winner = False
    if squares_list[0] == squares_list[3] and squares_list[0] == squares_list[6]:
        winner = True
        winner_team = squares_list[0]
        declare_winner(winner_team)
    elif squares_list[1] == squares_list[4] and squares_list[1] == squares_list[7]:
        winner = True
        winner_team = squares_list[1]
        declare_winner(winner_team)
    elif squares_list[2] == squares_list[5] and squares_list[2] == squares_list[8]:
        winner = True
        winner_team = squares_list[2]
        declare_winner(winner_team)
    elif squares_list[0] == squares_list[1] and squares_list[0] == squares_list[2]:
        winner = True
        winner_team = squares_list[0]
        declare_winner(winner_team)
    elif squares_list[3] == squares_list[4] and squares_list[3] == squares_list[5]:
        winner = True
        winner_team = squares_list[3]
        declare_winner(winner_team)
    elif squares_list[6] == squares_list[7] and squares_list[6] == squares_list[8]:
        winner = True
        winner_team = squares_list[6]
        declare_winner(winner_team)
    elif squares_list[6] == squares_list[4] and squares_list[6] == squares_list[2]:
        winner = True
        winner_team = squares_list[6]
        declare_winner(winner_team)
    elif squares_list[0] == squares_list[4] and squares_list[0] == squares_list[8]:
        winner = True
        winner_team = squares_list[0]
        declare_winner(winner_team)
    elif squares_list[0] != "1" and squares_list[1] != "2" and squares_list[2] != "3" and squares_list[3] != "4" and squares_list[4] != "5" and squares_list[5] != "6" and squares_list[6] != "7" and squares_list[7] != "8" and squares_list[8] != "9":
        winner = True
        print("It's a tie!")
    else:
        winner = False

    return winner

def declare_winner(team):
    print(f'You win, Team {team}!')



if __name__ == "__main__":
    main()