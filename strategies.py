import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ruleset = 6 decks, dealer hits on soft 17, double after split, no surrender, dealer peek, no insurance, only 1 split for aces and 3 splits for other cards, payouts is 3:2, 5 players total

hard_hands = {
    '2':  ['H', 'H', 'H', 'H', 'D', 'D', 'D', 'H', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    '3':  ['H', 'H', 'H', 'H', 'D', 'D', 'D', 'H', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    '4':  ['H', 'H', 'H', 'H', 'D', 'D', 'D', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    '5':  ['H', 'H', 'H', 'H', 'D', 'D', 'D', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    '6':  ['H', 'H', 'H', 'H', 'D', 'D', 'D', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
    '7':  ['H', 'H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S'],
    '8':  ['H', 'H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S'],
    '9':  ['H', 'H', 'H', 'H', 'H', 'H', 'D', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S'],
    '10': ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S'],
    'A':  ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S']
}

soft_hands = {
    '2':  ['H', 'H', 'H', 'H', 'H', 'D', 'S', 'S'],
    '3':  ['H', 'H', 'H', 'H', 'D', 'D', 'S', 'S'],
    '4':  ['H', 'H', 'H', 'D', 'D', 'D', 'S', 'S'],
    '5':  ['H', 'H', 'D', 'D', 'D', 'D', 'S', 'S'],
    '6':  ['H', 'H', 'D', 'D', 'D', 'D', 'D', 'S'],
    '7':  ['H', 'H', 'H', 'H', 'H', 'S', 'S', 'S'],
    '8':  ['H', 'H', 'H', 'H', 'H', 'S', 'S', 'S'],
    '9':  ['H', 'H', 'H', 'H', 'H', 'H', 'S', 'S'],
    '10': ['H', 'H', 'H', 'H', 'H', 'H', 'S', 'S'],
    'A':  ['H', 'H', 'H', 'H', 'H', 'H', 'S', 'S']
}

pairs = {
    '2':  ['SP', 'SP', 'H', 'D', 'SP', 'SP', 'SP', 'SP', 'S', 'SP'],
    '3':  ['SP', 'SP', 'H', 'D', 'SP', 'SP', 'SP', 'SP', 'S', 'SP'],
    '4':  ['SP', 'SP', 'H', 'D', 'SP', 'SP', 'SP', 'SP', 'S', 'SP'],
    '5':  ['SP', 'SP', 'SP', 'D', 'SP', 'SP', 'SP', 'SP', 'S', 'SP'],
    '6':  ['SP', 'SP', 'SP', 'D', 'SP', 'SP', 'SP', 'SP', 'S', 'SP'],
    '7':  ['SP', 'SP', 'H', 'D', 'SP', 'SP', 'SP', 'SP', 'S', 'SP'],
    '8':  ['H', 'H', 'H', 'D', 'H', 'H', 'SP', 'SP', 'S', 'SP'],
    '9':  ['H', 'H', 'H', 'D', 'H', 'H', 'SP', 'SP', 'S', 'SP'],
    '10': ['H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S'],
    'A':  ['H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S']
}

df_hard_hands = pd.DataFrame(hard_hands, index = ['5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'])
df_soft_hands = pd.DataFrame(soft_hands, index= ['13', '14', '15', '16', '17', '18', '19', '20'])
df_pairs = pd.DataFrame(pairs, index = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A'])

    

