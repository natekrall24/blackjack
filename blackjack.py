import random

# Dictionary representing Blackjack strategy
blackjack_strategy = {
    # Hard hands
    16:    {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    15:    {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    14:    {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    13:    {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    12:    {2: 'H', 3: 'H', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    11:    {2: 'D', 3: 'D', 4: 'D', 5: 'D', 6: 'D', 7: 'D', 8: 'D', 9: 'D', 10: 'D', 'A': 'D'},
    10:    {2: 'D', 3: 'D', 4: 'D', 5: 'D', 6: 'D', 7: 'D', 8: 'D', 9: 'D', 10: 'H', 'A': 'H'},
    9:     {2: 'H', 3: 'D', 4: 'D', 5: 'D', 6: 'D', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},

    # Soft hands
    'A,9': {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 'A': 'S'},
    'A,8': {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 'A': 'S'},
    'A,7': {2: 'S', 3: 'D', 4: 'D', 5: 'D', 6: 'D', 7: 'S', 8: 'S', 9: 'H', 10: 'H', 'A': 'H'},
    'A,6': {2: 'H', 3: 'D', 4: 'D', 5: 'D', 6: 'D', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    'A,5': {2: 'H', 3: 'H', 4: 'D', 5: 'D', 6: 'D', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    'A,4': {2: 'H', 3: 'H', 4: 'D', 5: 'D', 6: 'D', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    'A,3': {2: 'H', 3: 'H', 4: 'H', 5: 'D', 6: 'D', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    'A,2': {2: 'H', 3: 'H', 4: 'H', 5: 'D', 6: 'D', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},

    # Pairs (splitting)
    'A': {2: 'SP', 3: 'SP', 4: 'SP', 5: 'SP', 6: 'SP', 7: 'SP', 8: 'SP', 9: 'SP', 10: 'S', 'A': 'SP'},
    '10': {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 'A': 'S'},
    '9': {2: 'SP', 3: 'SP', 4: 'SP', 5: 'SP', 6: 'SP', 7: 'S', 8: 'SP', 9: 'SP', 10: 'S', 'A': 'S'},
    '8': {2: 'SP', 3: 'SP', 4: 'SP', 5: 'SP', 6: 'SP', 7: 'SP', 8: 'SP', 9: 'SP', 10: 'SP', 'A': 'SP'},
    '7': {2: 'SP', 3: 'SP', 4: 'SP', 5: 'SP', 6: 'SP', 7: 'SP', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    '6': {2: 'SP', 3: 'SP', 4: 'SP', 5: 'SP', 6: 'SP', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    '5': {2: 'D', 3: 'D', 4: 'D', 5: 'D', 6: 'D', 7: 'D', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    '4': {2: 'H', 3: 'H', 4: 'H', 5: 'SP', 6: 'SP', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    '3': {2: 'SP', 3: 'SP', 4: 'SP', 5: 'SP', 6: 'SP', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    '2': {2: 'SP', 3: 'SP', 4: 'SP', 5: 'SP', 6: 'SP', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
}

def get_best_move(playerHand, dealerCard):
    if dealerCard != 'A':
        if dealerCard in 'JQK':
           dealerCard = 10
        dealerCard = int(dealerCard)
    
    if len(playerHand) == 2:
        #pairs
        if playerHand[0] == playerHand[1]:
            return blackjack_strategy[playerHand[0]][dealerCard]
        
        #soft
        elif playerHand[0] == 'A':
            return blackjack_strategy[playerHand[0] + ',' + playerHand[1]][dealerCard]
        
        #all the rest
        for i in range(2):
            if playerHand[i] in 'JQK':
                playerHand[i] = 10
            playerHand[i] = int(playerHand[i])
        total = sum(playerHand)
        if total < 9:
            return 'H'
        if total > 16:
            return 'S'
        return blackjack_strategy[total][dealerCard]

def playHand():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    #draw players cards
    player1, player2 = random.choice(cards), random.choice(cards)

    #Ace major order
    if player2 == 'A':
        temp = player1
        player1 = player2
        player2 = temp
    #dont continue if blackjack
    if player1 == 'A' and player2 in '10JQK':
        print("blackjack!")
        return
    
    #dealer card
    dealer1 = random.choice(cards)

    print("Your cards are: " + player1 + " " + player2)
    print("The dealer is showing: " + dealer1)

    while True:
        move = input("please make a move (H, S, SP, D): ")
        if move not in ['H', 'S', 'SP', 'D']:
            print("That's not a move, silly!")
        else:
            break
    
    playerHand = [player1, player2]
    if move == get_best_move(playerHand, dealer1):
        print("Hooray! you made the right move!")
    else:
        print("you're terrible")

playHand()