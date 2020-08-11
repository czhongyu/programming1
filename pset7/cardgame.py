# Implements a cards shuffler and dealer.
import random


# TODO
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __str__(self):
        return f"{self.value} of {self.suit}"
    

class Deck:
    def __init__(self):
        self.suits = ['Hearts','Diamonds','Clubs','Spades']
        self.values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = []
        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(suit, value))
        
    def __str__(self):
        return f"{len(self.cards)} cards in the deck"
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        card = self.cards[0]
        self.cards.remove(self.cards[0])
        return card

if __name__ == "__main__":
    card = Card("spades", "Ace")
    print(card)
    
    deck = Deck()
    print(deck)

    deck.shuffle()
    card = deck.deal()
    print(card)
