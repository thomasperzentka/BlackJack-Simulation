import random

def make_deck():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', 'A']
    deck = cards * 4 * 6
    random.shuffle(deck)
    return deck
def draw_card(current_deck, count_cards, running_count):
    if len(current_deck) < 15:
        current_deck = make_deck()
        running_count = 0
    if count_cards:
        card = random.choice(current_deck)
        current_deck.remove(card)
        if card == "A":
            running_count -= 1
        elif int(card) <= 6:
            running_count += 1
        elif int(card) <= 9:
            running_count += 0
        else:
            running_count -= 1
        
        
        
        return card
    else:
        return random.choice(current_deck)
        

def total(hand):
    total = 0
    soft = False
    if "A" in  hand:
        soft = True
        for card in hand:
            if card == "A":
                total += 11
            else:
                total += int(card)
        if total > 21:
            total -= 10
            soft = False
    else:
        for card in hand:
            total += int(card)
    return total, soft
            
        
    
    