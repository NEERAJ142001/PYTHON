import random

from art import logo


# 1 getting a random card from the list
def deal_card():
    # Creating a list Ace =11 and jack,king and queen==10
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


# 2 calculate_score adding the sum of random 2 cards
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""

    # sum() return the sum and at the same time it will check the length==2 10 and 11=21 check for a blackjack (a
    # hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our
    # game.
    # if someone get blackjack(10+11) automatically other looses
    # value of deal_cards=0
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # if Ace=11 in the cards as well as sum is going greater than 21 then change the ace value form 11 to 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


# 3 compare function have all the possible outcomes
def compare(user_score, computer_score):
    # Bug fix. If you and the computer are both over, you lose.
    # both scored greater than 21 ,I lose
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    # if score is equal then draw
    if user_score == computer_score:
        return "Draw 🙃"
    # if computer score is equal to 0 then computer has blackjack and win
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"

    #  if user score is equal to 0 then user has blackjack and win
    elif user_score == 0:
        return "Win with a Blackjack 😎"

    # if user score goes more than 21 ,user lost
    elif user_score > 21:
        return "You went over. You lose 😭"

    # if computer score goes more than 21 ,user win
    elif computer_score > 21:
        return "Opponent went over. You win 😁"

    # if user score is greater than computer score then u win
    elif user_score > computer_score:
        return "You win 😃"

    # otherwise u lost means computer score is greater than user score
    else:
        return "You lose 😤"


# 4 main function
def play_game():
    print(logo)

    # making a list for user and computer
    user_cards = []
    computer_cards = []
    is_game_over = True

    # this loop fetches two random card for user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # this while loop is for user
    while is_game_over:
        # in user_score ,we get the total score of user
        user_score = calculate_score(user_cards)
        # in computer_score ,we get the total score of computer
        computer_score = calculate_score(computer_cards)

        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's  card: {computer_cards}, computer score: {computer_score} ")

        # If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = False
        else:
            # if user choose yes than call a deal_card method to get a random card
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = False

    # Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as
    #  long as it has a score less than 17.
    # this while loop is for computer
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': \n ") == "y":
    play_game()
