from art import logo
import random
def blackjack():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # player_card_count = 0
    cards_on_table = []

    #deal 2 cards to player and 1 to dealer and reveal both
    player_card1 = random.choice(cards)
    player_card2 = random.choice(cards)
    player_total = player_card1 + player_card2
    cards_on_table = random.choice(cards)
    ## if card is ACE##
    if player_card1 == 11:
        ace_value = int(input("You drew an Ace! Choose the value (1 or 11): "))
        player_total = player_card2 + ace_value
        print(player_card2) 
    elif player_card2 == 11:
        ace_value = int(input("You drew an Ace! Choose the value (1 or 11): "))
        player_total = player_card1 + ace_value
        print(player_card2) 

    print(f"Players Cards Total: {player_total}")
    print(f"Dealers Cards Total: {cards_on_table}")
    if player_total > 21:
        print("Busted on Deal, Reshuffling...")
        blackjack()
#player hit or stay
    hit = input("Hit or Stay (hit/stay): ")
    if hit == "hit":
        player_total =+ player_total + random.choice(cards)
        print(f"Players Cards Total: {player_total}")
        print(f"Dealers Cards Total: {cards_on_table}")
        
        if player_total > 21:
            print("You Went Bust!")
            play_again()
    elif hit == "stay":
        print(f"Players Cards Total: {player_total}")
        print(f"Dealers Cards Total: {cards_on_table}")
    elif hit != "hit" or "stay":
        print("You got confused and drew a card!?")
        cards_on_table =+ random.choice(cards)
    ## Dealer Card 2 Reveal
    # def dealer_reveal():
    cards_on_table =+ cards_on_table + random.choice(cards)
    print(f"The dealer has revealed the second card on the table Table Total: {cards_on_table}")
    print(f"Your Card Total: {player_total}")
    ## Player Hit chance #2
    hit_2 = input("Hit or Stay (hit/stay)")
    if hit_2 == "hit":
        player_total = + player_total + random.choice(cards)
        print(f"Players Cards Total: {player_total}")
        print(f"Dealers Cards Total: {cards_on_table}")
    elif hit_2 == "stay":
        print(f"Players Cards Total: {player_total}")
        print(f"Dealers Cards Total: {cards_on_table}")
    elif hit_2 != "hit" or "stay":
        print("You got confused and drew a card!?")
        cards_on_table = + random.choice(cards)

    if player_total > cards_on_table and player_total < 22:
        print("Congratulations! You Won!")
        play_again()
    else:
        print("Sorry. The House Always Wins!")
        play_again()
def play_again():
    playagain = input("Would you like to play again? (y/n)")
    if playagain == "y":
        blackjack()
    else:
        print("Goodbye, See you next time!")
        exit(0)

# def dealer_reveal():
#     cards_on_table =+ cards_on_table + random.choice(cards)
#     print(f"The dealer has revealed the second card on the table Table Total: {cards_on_table}")
#     print(f"Your Card Total: {player_total}")

blackjack()