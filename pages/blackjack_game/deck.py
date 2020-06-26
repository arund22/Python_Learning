import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
          'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank+" of "+self.suit
        pass

class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+ card.__str__()
        return "The Deck has : "+deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand():

    def __init__(self):

        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        # card passed from in
        # from Deck.deal()
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -=10
            self.aces -= 1

class Chips():

    def __init__(self,total = 100):
        self.total = total
        self.bet = 0

    def win_bet(self):

        self.total +=self.bet

    def lose_bet(self):

        self.total -=self.bet


def take_bet(player_chips):

    while True:

        try:
            player_chips.bet = int(input('How many chips you want to bet'))

        except:
            print("Sorry provide an Integer")

        else:

            if player_chips.bet > player_chips.total:
                print('Sorry, you dont have enough chips you have {}'.format(player_chips.total))

            else:
                break



def hit(deck,hand):
    single_card = test_deck.deal()
    player_hand.add_card(single_card)
    player_hand.adjust_for_ace()

def hit_or_stand(deck,hand):

    global playing

    while True:
        x = input('Hit or stand? Type h or s:   ')

        print(x)

        if x[0].lower() == 'h':
            hit(deck,hand)


        elif x[0].lower() == 's':
            print('Player wants to stand')
            playing = False

        else:
            print('Did not understand the input')
            continue

        break


def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

while True:

    print('Welcome to BlackJack')
    test_deck = Deck()
    test_deck.shuffle()
    player_hand = Hand()
    player_hand.add_card(test_deck.deal())
    player_hand.add_card(test_deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(test_deck.deal())
    dealer_hand.add_card(test_deck.deal())

    player_chips = Chips()

    take_bet(player_chips)
    show_some(player_hand,dealer_hand)

    while playing:

        hit_or_stand(test_deck,player_hand)

        show_some(player_hand,dealer_hand)

        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    if player_hand.value <=21:
        while dealer_hand.value < 17:
            hit(test_deck,dealer_hand)
        show_all(player_hand,dealer_hand)

        if dealer_hand.value >21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)

     # Inform Player of their chips total
    print("\nPlayer's winnings stand at",player_chips.total)

            # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
         print("Thanks for playing!")
         break
