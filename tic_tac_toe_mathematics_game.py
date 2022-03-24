# faculty of computers and artificial intelligence at Cairo University
# Author : shahd osama hamed
# E-mail : shahdosama734@gmail.com
# tic_tac_toe_mathematics_game_2
# Version : 1.0

board = ['a','b','c','d','e','f','g','h','i']
odd_numbers = [1,3,5,7,9]
even_numbers = [0,2,4,6,8]

def the_board_of_the_game(board):
    print(" ******************* ")
    print(" | " , board[0] , " | " , board[1] , " | " , board[2] , " | ")
    print(" ******************* ")
    print(" | " , board[3] , " | " , board[4] , " | " , board[5] , " | ")
    print(" ******************* ")
    print(" | " , board[6] , " | " , board[7] , " | " , board[8] , " | ")
    print(" ******************* ")
print(the_board_of_the_game(board))

def checking_for_sum_15 (a,b,c):   # this function to check if there is a sum of 3 numbers equal 15 or not
    if (type(board[a]) == int) and (type(board[b]) == int) and (type(board[c]) == int):
        if (board[a] + board[b] + board[c]) == 15:
            return True
    return False

# this function to check if a player won or not , the player won if he puts the last num which makes the summation of 3 nums = 15
def is_winner():
    return checking_for_sum_15(0,4,8) or checking_for_sum_15(2,4,6,) or \
           checking_for_sum_15(0,1,2) or checking_for_sum_15(3,4,5) or \
           checking_for_sum_15(6,7,8) or checking_for_sum_15(0,3,6) or \
           checking_for_sum_15(1,4,7) or checking_for_sum_15(2,5,8)

j = 0
while j < 9: # the loop of startting the game
            print(odd_numbers)
            player1 = input(" first_player :- pick an odd number : ")
# to check the player1 if he enters a character or enter a space and tell him to enter a digit not chatacter or space :
            while (player1 == "") or (type(player1) == str) or ((type(player1) == str) and (player1.isdigit())):
                if ((player1 == "") or (type(player1) == str)) and (player1.isdigit() == False):
                    print(" this number is not in odd_numbers ")
                    player1 = input(" first_player :- choose another odd number : ")
                if player1.isdigit():
                    break
            player1 = int(player1)
# checking if the number which the player1 entered in odd_numbers or not and checking if the number is even or odd :
            while (player1 not in odd_numbers) or (player1 in even_numbers):
                print(" this number is not in odd_numbers ")
                player1 = int(input(" first_player :- choose another odd number : "))
            odd_numbers.pop(odd_numbers.index(player1))
            
            print(the_board_of_the_game(board))
            cell_game_for_player1 = input(" first_player :- choose the cell you want : ")
# checking if the cell in board or not :
            while cell_game_for_player1 not in board:
                print(" this cell doesn't exist")
                cell_game_for_player1 = input(" first_player :- choose another cell : ")
            board[board.index(cell_game_for_player1)] = player1
            print(the_board_of_the_game(board))
# calling the function which check if there is a player won or not if player1 won break from the loop of startting the game :
            if is_winner():
                print(" player1 wins ")
                break
# if player1 starts the game and there is only 9 cells so player1 will end all his nums and there is always only one num in the list of player2
# so this is checking if there is a draw condition or not if true break from the loop of startting the game :
            if len(odd_numbers) == 0 and (len(even_numbers) == 1):
                print(" the game finished ")
                print(" Draw")
                break
            else:
                print(even_numbers)
                player2 = input(" second_player :- pick an even number  : ")
# to check the player2 if he enters a character or enter a space and tell him to enter a digit not chatacter or space :
                while (player2 == "") or (type(player2) == str) or ((type(player2) == str) and (player2.isdigit())):
                    if (player2 == "" or type(player2) == str) and (player2.isdigit() == False):
                        print(" this number is not in even_numbers ")
                        player2 = input(" second_player :- choose another even number  : ")
                    if player2.isdigit():
                        break
                player2 = int(player2)
# checking if the number which the player2 entered in even_numbers or not and checking if the number is even or odd :
                while (player2 not in even_numbers) or (player2 in odd_numbers):
                    print(" this number is not in even_numbers ")
                    player2 = int(input(" second_player :- choose another even number: "))
                even_numbers.pop(even_numbers.index(player2))
                
                print(the_board_of_the_game(board))
                cell_game_for_player2 = input(" second_player :- choose the cell you want : ")
# checking if the cell in board or not :
                while cell_game_for_player2 not in board:
                    print(" this cell doesn't exist ")
                    cell_game_for_player2 = input(" second_player :- choose another cell : ")
                board[board.index(cell_game_for_player2)] = player2
                print(the_board_of_the_game(board))
# calling the function which check if there is a player won or not if player2 won break from the loop of startting the game :
                if is_winner():
                    print(" player2 wins ")
                    break
            j += 1