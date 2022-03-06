def main(ans_2=1):
    #
    # ans_2 is a parameter with a known value as it is going to be used for when the players want to play again
    #
    print("Hello and welcome to our game!\n")
    ans_1 = int(
        input("Do you want to know the rules of the game?\nIf yes then please enter 1, if no then enter 0: "))
    #
    # a greeting message is printed to the players and a question: whether they want to know the rules of the game or
    # not
    #
    if ans_1 == 1:
        print(
            "\nThis game begins with an arbitrary number of tokens in a single row.\nTwo players alternate "
            "turns.\nDuring their turn, the player may remove either one or two adjacent tokens.\nThe player who "
            "removes the last token wins\n")
    while ans_2 == 1:
        name_player1 = input("Please enter 1st player's name: ")
        name_player2 = input("Please enter 2nd player's name: ")
        #
        # to make the game more realistic and customized, the game asks for the players' names so it can use it in each
        # turn
        #
        while name_player2 == name_player1:
            name_player2 = input("Name has been taken, please re-enter 2nd player's name: ")
        #
        # if the 2nd players name is the same as the 1st, the game asks the 2nd player to re-enter his name so the turns
        # don't get mixed up
        #
        ans_3 = input(
            "Please choose the difficulty level between easy, moderated and hard\nEasy = E\nModerated = M\nHard = "
            "H\nChoice: ").upper()
        #
        # to make the game more realistic and customized, the game asks the players' to enter the difficulty level
        #
        while ans_3 not in ["H", "M", "E"]:
            ans_3 = input("Entry must be either E, M or H, please re-enter the difficulty level: ").upper()
        #
        # this while loop checks if the entry is E, M or H, so the players don"t enter any other wrong letters
        #
        game_row = []
        finished_game = []
        if ans_3 == 'E':
            game_row = [i for i in range(1, 11)]
            for i in range(1, 11):
                finished_game.append('*')
        elif ans_3 == 'M':
            game_row = [i for i in range(1, 21)]
            for i in range(1, 11):
                finished_game.append('*')
        elif ans_3 == 'H':
            game_row = [i for i in range(1, 31)]
            for i in range(1, 11):
                finished_game.append('*')
        print(game_row)
        #
        # the above code checks the difficulty level and accordingly, it creates an array called game_row which contains
        # the number of tokens to be removed from the array. Example: if the difficulty level is E: easy, number of
        # token tokens is going to be 10
        #
        # the finished_game array is used for 2 purposes: to check if the game_row array is empty; therefore one of the
        # players won and is displayed to show the game it's done
        #
        while game_row != finished_game:
            player = 1
            if player == 1:
                print("It's ", name_player1, "'s turn.")
                if check_adjacent(game_row):
                    tokens_number = int(input("Player 1, choose number of removed tokens 1 or 2: "))
                    while tokens_number != 1 and tokens_number != 2:
                        tokens_number = int(
                            input("Number of removed tokens has to be either 1 or 2, please re-enter the "
                                  "number: "))
                else:
                    print("Looks like there are no adjacent tokens, you have to remove only 1")
                    tokens_number = 1
                player_turn(tokens_number, game_row)
                if game_row == finished_game:
                    print("Player 1 is the winner!!")
            player = 2
            if player == 2:
                print("It's ", name_player2, "'s turn.")
                if check_adjacent(game_row):
                    tokens_number = int(input("Player 2, choose number of removed tokens 1 or 2: "))
                    while tokens_number != 1 and tokens_number != 2:
                        tokens_number = int(
                            input("Number of removed tokens has to be either 1 or 2, please re-enter the "
                                  "number: "))
                else:
                    print("Looks like there are no adjacent tokens, you have to remove only 1")
                    tokens_number = 1
                player_turn(tokens_number, game_row)
                if game_row == finished_game:
                    print("Player 2 is the winner!!")
        print("End of the game. Thank you for playing!!")
        ans_2 = int(input("Do you want to play again?\nIf yes then enter 1, if no enter 0: "))
    if ans_2 == 0:
        print("Goodbye!!!")
    #
    # this piece of code takes the variable player and check if it contains 1 or 2 to check whose turn is it,
    # then it checks if there any adjacent token or not, if there is, it displays to the player that they do have the
    # option of choosing to withdraw/remove 1 or 2 tokens, if there isn't any adjacent tokens, it displays a
    # message that the only available option is to withdraw only 1 token.
    # after that, it checks if the game_row list is empty or not, if it's empty, if shows a message that the player has
    # won.
    #


def check_adjacent(lst):
    c = 0
    for i in lst:
        if i != "*":
            c += 1
        else:
            c = 0
        if c == 2:
            return True
    return False
    #
    # this function goes through all elements of the list to check if there are any adjacent tokens left, this way it
    # will allow the player to choose either 1 or 2 tokens, for if there are no adjacent tokens, both players will not
    # be able to choose the "remove 2 tokens" option.
    #


def player_turn(tokens_number, game_row):
    #
    # this piece of code is used to run some conditions on the number of tokens to be removed and the token index in the
    # array; it's done in a separate function to make it easier to edit instead of including it twice in the code above
    # and having to edit it twice for every time an edit is needed, it is also done to make the code shorter so that it
    # takes less time to compile.
    #
    if tokens_number == 1:
        token = int(input("Choose a number: "))
        while token not in game_row:
            token = int(input("This number has been chosen before, please choose another number: "))
        if token in game_row:
            game_row[token - 1] = '*'
            print(game_row)
    #
    # this while loop checks if the token index entered is in the list or not; if yes, it asks the player to change the
    # token index entered, if no, it removes the number from the list and replace it by "*"
    #
    elif tokens_number == 2:
        token = int(input("Choose the 1st number: "))
        while token not in game_row:
            token = int(input("This number has been chosen before, please choose another number: "))
    #
    # this while loop checks if the token index entered is in the list or not; if yes, it asks the player to change
    # the token index entered.
    #
        while (game_row[token - 2] == "") and (game_row[token] == ""):
            token = int(input("Numbers chosen have to be adjacent, please choose again: "))
    #
    # this while loop checks if both numbers, on the left and on the right of the number entered, is removed or not
    # as when the player chooses to remove 2 tokens, they have to be adjacent, and if either numbers beside the
    # number chosen is already removed, this means that the chosen numbers are not going to be adjacent
    #
        if token in game_row:
            game_row[token - 1] = '*'
            print(game_row)
        first_token = token
    #
    # if the token is inside the list and has not been chosen nor does it have any of the besides numbers removed,
    # this means it can be chosen to be removed from the list
    #
        token = int(input("Choose the 2st number: "))
        while token not in game_row:
            token = int(input("This number has been chosen before, please choose another number: "))
        while abs(token - first_token) != 1:
            token = int(input("The second number isn't adjacent to the first, please choose again: "))
        if token in game_row:
            game_row[token - 1] = '*'
            print(game_row)
    #
    # the same above-conditions are to be checked again for the 2nd chosen token
    #


main()
