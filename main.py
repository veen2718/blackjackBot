from cards import *


def getVal(value):
    if value in ['King','Queen','Jack']:
        return 10
    else:
        return int(value)

def main():
    Deck = deck()
    dealerCard = 'Hearts,2'#input("Dealer Card: ")
    playerCard1 = 'Spades,Jack'#input("Player Card 1: ")
    playerCard2 = 'Diamonds,4'#input("Player Card 2: ")
    
    dealerValue = Deck.remove(dealerCard)
    playerValue1 = Deck.remove(playerCard1)
    playerValue2 = Deck.remove(playerCard2)


    goodHits = 0
    badHits = 0

    for pCard in Deck.cards:
        value = pCard.value
        allCards = [playerValue1, playerValue2,value]
        print(allCards)
        if allCards.count('Ace') != 0: #If a card is an ace, then no matter what the player will not bust
            goodHits += 1
            print("Ace => goodhit")


        else:
            totalSum = sum([getVal(c) for c in allCards])
            if totalSum <= 21:
                goodHits += 1
                print(totalSum, "goodHit, no Aces")
            else:
                badHits += 1
                print(totalSum, "badHit, no Aces")
    print(f"GoodHits: {goodHits}, badHits: {badHits}")

        




if __name__ == '__main__':
    main()