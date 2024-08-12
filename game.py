from strategies import *
from functions import *
import math

def game(initial_bet, rounds, count_cards=True):
    
    # initial setup
    soft_hands = df_soft_hands
    hard_hands = df_hard_hands
    pairs = df_pairs 
    money_change = 0
    wins = 0
    ties = 0
    losses = 0
    current_deck = make_deck()
    running_count = 0
    bet = initial_bet
    
    # game loop
    
    while(rounds > 0):
        # setup for new round
        up_card = draw_card(current_deck, count_cards, running_count)
        down_card = draw_card(current_deck, count_cards, running_count)
        card1 = draw_card(current_deck, count_cards, running_count)
        card2 = draw_card(current_deck, count_cards, running_count)
        bet_hands = [bet]
        player_hands = [[card1, card2]]
        dealer_hand = [up_card, down_card]
        
        # check for blackjack
        
        if total(dealer_hand)[0]  == 21 and total(player_hands[0])[0] == 21:
            ties += 1
            continue
        elif total(player_hands[0])[0] == 21:
            money_change += bet * 1.5
            wins += 1
            continue
        elif  total(dealer_hand)[0] == 21:
            money_change -= bet
            losses += 1
            continue
        
        # check for splits
        double_aces = False
        if player_hands[0][0] == player_hands[0][1]:
            if player_hands[0][0] == 'A' and player_hands[0][1] == 'A':
                player_hands[0][1] = draw_card(current_deck, count_cards, running_count)
                player_hands.append([player_hands[0][0], draw_card(current_deck, count_cards, running_count)])
                bet_hands.append(bet)
                double_aces = True
                
            else:   
                i = 0 
                while i < len(player_hands):
                    if len(player_hands) <= 3:
                        break
                    first_card = player_hands[i][0]
                    second_card = player_hands[i][1]
                    if first_card == second_card and pairs.loc[str(player_hands[i][0]), up_card] == "SP":
                        second_card = draw_card(current_deck, count_cards, running_count)
                        player_hands.append([first_card, draw_card(current_deck, count_cards, running_count)])
                        bet_hands.append(bet)
                    else:
                        i += 1
            
        
        # player turn
        if double_aces == False:
            for i in range(len(player_hands)):
                while total(player_hands[i])[0] < 21:
                    if player_hands[i][0] == player_hands[i][1] and len(player_hands[i]) == 2:
                        next_move = pairs.loc[player_hands[i][0], up_card]
                        
                    elif total(player_hands[i])[1]:
                        next_move = soft_hands.loc[str(total(player_hands[i])[0]), up_card]
                    else:
                        next_move = hard_hands.loc[str(total(player_hands[i])[0]), up_card]
                    if next_move == "D" :
                        if len(player_hands[i]) ==2:
                            player_hands[i].append(draw_card(current_deck, count_cards, running_count))
                            bet_hands[i] *= 2
                            break
                        else:
                            player_hands[i].append(draw_card(current_deck, count_cards, running_count))
                    elif next_move == "Ds":
                        if len(player_hands[i]) ==2:
                            player_hands[i].append(draw_card(current_deck, count_cards, running_count))
                            bet_hands[i] *= 2
                            break
                        else:
                            break
                        
                    elif next_move == "S":
                        break
                    else:
                        player_hands[i].append(draw_card(current_deck, count_cards, running_count))

        # dealer turn
        while total(dealer_hand)[0] < 17 or (total(dealer_hand)[1] and total(dealer_hand)[0] == 17):
            dealer_hand.append(draw_card(current_deck, count_cards, running_count))
        
        
        if count_cards:
            total_count = running_count / math.ceil(len(current_deck) / 52)
            bet = initial_bet * total_count
            
        

                
        
        # final check
        for i in range(len(player_hands)):
            if total(player_hands[i])[0] > 21 or (total(player_hands[i])[0] < total(dealer_hand)[0] and total(dealer_hand)[0] <= 21):
                money_change -= bet_hands[i]
                losses += 1
            elif total(dealer_hand)[0] > 21 or total(player_hands[i])[0] > total(dealer_hand)[0]:
                money_change += bet_hands[i]
                wins += 1
            else:
                ties += 1
        rounds -= 1
    
    return money_change, wins, ties, losses


print(game(100, 10000, count_cards=False))
            
                
                
                
