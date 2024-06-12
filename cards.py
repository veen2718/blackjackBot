import random
class deck:
    def __init__(self):
        self.played = []
        suits = ['Hearts', 'Diamonds', 'Clubs','Spades']
        ranks = [str(i) for i in range(2,11)] + ['Ace','Jack','Queen','King']
        self.cards = [card(val,suit) for val in ranks for suit in suits]
        self.cardNames = [f'{suit},{val}' for val in ranks for suit in suits]
        print(len(self.cards))

    def shuffle(self):
        random.shuffle(self.cards)
    def get(self):
        return self.cards.pop()
    def display(self):
        for card1 in self.cards:
            print(card1.suit, card1.value)
    def remove(self,cardName):
        i = self.cardNames.index(cardName)
        self.cardNames.pop(i)
        x = self.cards.pop(i)
        return x.value
    
    

class card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
    def display(self):
        print(self.suit, self.value)
