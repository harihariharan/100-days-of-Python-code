#excercise 1: Balck jack project

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
user_score = 0 
computer_score = 0
is_game_over = False

def deal_card():
    return random.choice(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has BlackJack."
    elif user_score == 0:
        return "Win with a BlackJack."
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win."
    elif user_score > computer_score:
        return "You Win."
    else:
        return "You lose."

def calculate_score(deck):
    score = 0
    score = sum(deck)
    if score == 21 and len(deck) == 2:
        return 0
    elif score > 21:
        score = 0
        if 11 in deck:
            deck.remove(11)
            deck.append(1)
            score = sum(deck)
            return score    
        else:
            return score
    else:
        return score 
   
def play_game():
    print(logo)   
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []
    user_score = 0 
    computer_score = 0
    is_game_over = False

    for i in range(0,2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_decision = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_decision == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True   

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)  

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score} ")
    print(compare(user_score, computer_score))      

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower() == 'y':
    play_game()