from game_data import data
from art import logo
from art import vs
import random


def play_game():
    print(logo)
    game_over = False
    score = 0

    def pull_option():
        selected = random.choice(data)
        return selected

    choice_one = pull_option()
    choice_two = pull_option()

    if choice_two == choice_one:
        choice_two = pull_option()

    choice_one_count = int(choice_one['follower_count'])
    choice_two_count = int(choice_two['follower_count'])

    if choice_one_count > choice_two_count:
        win = "lower"
    elif choice_one_count < choice_two_count:
        win = "higher"
    else:
        print("There is an error in the program")

    while game_over == False:
        #print(choice_one_count)
        #print(choice_two_count)
        #print(score)
        choice_statement = "This person or business is {} from {} and is a/an {}."
        print(choice_statement.format(choice_one['name'],choice_one['country'],choice_one['description']))
        print(vs)
        print(choice_statement.format(choice_two['name'],choice_two['country'],choice_two['description']))

        user_choice = input("is {} higher or lower than {}?  Type higher or lower and enter or return. \n".format(choice_two['name'],choice_one['name']))

        if user_choice == win:
            score += 1
            print("You are right! Your score is {score}.")
            choice_one = choice_two
            choice_two = pull_option()
        elif user_choice != win:
            print(f"Sorry you loose :( You ended the game with a score of {score}")
            play_again = input("Would you like to play again?")
            if play_again == "yes":
                play_game()
            else:
                print("I hope you enjoyed the game, see you again soon.")
            game_over = True

            #show results
            #return choice_two as choice_one, re-roll for choice_two

play_game()
