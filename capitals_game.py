# Write a game where the user should guess the capital of the country that you have in your dictionary.

# capitals = {
#         'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin',
#         'Italy': 'Rome', 'USA': 'Washington', 'Canada': 'Ottawa', '
#         'Switzerland': 'Bern', 'Austria': 'Vienna',
#         'Belgium': 'Brussels',  'Sweden': 'Stockholm',
#         'Norway': 'Oslo', 'Denmark': 'Copenhagen',
#         'Finland': 'Helsinki', 'Poland': 'Warsaw',
#         'Romania': 'Bucharest', 'Bulgaria': 'Sofia', 'Greece': 'Athens', ...
# }

# You should show the user a random country from the list and ask him to guess the capital. 
# If the user inputs the right capital, print "You are right!", add a point and ask him to guess another country.
# If not, you should ask again. The user should be able to quit the game by typing "exit".

# You should print the current score after each round. Also, you should print the final score before the user quit the game.

# Optional:

# 1. Give the user a hint if he guesses wrong. The hint should look like the first letter of the capital. 
# If the user makes another mistake, you should print one more letter from the capital.

# 2. If a user makes a mistake you should decrement his life. The initial amount of lives is 3. 
# The game will end when the user has no lives left. You should print the final score after the user has no lives left.
capitals = {
    'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin',
    'Italy': 'Rome', 'USA': 'Washington', 'Canada': 'Ottawa', 
    'Switzerland': 'Bern', 'Austria': 'Vienna',
    'Belgium': 'Brussels',  'Sweden': 'Stockholm',
    'Norway': 'Oslo', 'Denmark': 'Copenhagen',
    'Finland': 'Helsinki', 'Poland': 'Warsaw',
    'Romania': 'Bucharest', 'Bulgaria': 'Sofia', 'Greece': 'Athens',
    }
import random

def game_capitals():
    country_list = list(capitals.keys())
    print("Welcome to the capitals game")
    points = 0
    hp = 3
    amount_of_cities = len(capitals) 
    while hp>0:
        contry =country_list[random.randint(1,amount_of_cities)]
        answer = input(f"What is the capital of {contry}?   ")
        if capitals[contry] == answer:
            print("You`re right")
            points +=1
            print(f"You have {points} points!")
            continue
        elif answer.lower() == "exit":
            print(f"You scored {points} points. Goodbye :D ")
            exit()
        else:
            x = 1
            while capitals[contry] != answer:
                print("It`s not true.")
                print(f"First letter is -> {capitals[contry][0:x]}")    
                answer = input(f"Try again.What is the capital of {contry}?  ")
                x +=1
                if answer.lower() == "exit":
                    print(f"You scored {points} points. Goodbye :D ")
                    exit()
                elif x == 3:
                    hp -= 1
                    print(f"Wrong. You have {points} points!")
                    break
    print(f"You lost, because you don`t have any hitpoints.Your socore -> {points}")


game_capitals()