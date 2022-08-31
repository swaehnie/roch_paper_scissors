# title: Schere, Stein, Papier
# rev: 31.08.2022
# created: 31.08.2022
# created by: swaehnie
# contact: swaehnie (https://github.com/swaehnie)
# repository: https://github.com/swaehnie/rock_paper_scissors
# 

import random

languagepack_de = ["Schere", "Stein", "Papier", "Auswahl: Schere, Stein, Papier? ", "Unentschieden", "PC hat gewonnen!", "Du hast gewonnen!"]

languagepack_eng = ["rock", "paper", "scissors", "Selection: rock, paper, scissors? ", "Draw", "PC has won!", "You have won!"]

languagepack_fr = ["pierre", "ciseaux", "papier", "Sélection: pierre, ciseaux, papier? ", "Match nul", "Le PC a gagné", "Tu as gagné" ]

#check language
language = input("englisch (e), deutsch (d), français (f) ")
if language == "e":
    symbols = languagepack_eng [0:3]
    symbols_language = symbols
    text_player_choice = languagepack_eng [3]
    text_winnings = languagepack_eng [4:7]
    
if language == "d":
    symbols = languagepack_de [0:3]
    symbols_language = symbols
    text_player_choice = languagepack_de [3]
    text_winnings = languagepack_de [4:7]
    
if language == "f":
    symbols = languagepack_fr [0:3]
    symbols_language = symbols
    text_player_choice = languagepack_fr [3]
    text_winnings = languagepack_fr [4:7]

# game
main = 1
while main == 1:
    print("symbols:", symbols)
    print("symbols_language:", symbols_language)
    print("text_player_choice: ", text_player_choice)
    print("text_winnings:", text_winnings)
    # pc choice
    random.shuffle(symbols)
    # print(symbols)
    symbol_choice_pc = random.choice(symbols)
    # print(symbol_choice_pc)

    # player choice
    if language == "d":
        symbol_choice_player = input (text_player_choice+" ").capitalize()
    else:
        symbol_choice_player = input (text_player_choice+" ")


    if symbol_choice_player in symbols:
        print (symbol_choice_pc+" vs "+symbol_choice_player)
        
        if symbol_choice_pc == symbol_choice_player: print(text_winnings[0])
    
        # pc winnings
        # Schere vs Papier
        if symbol_choice_pc == symbols_language[0] and symbol_choice_player == symbols_language[2]:
            print(text_winnings[1])
        # Stein vs Schere
        if symbol_choice_pc == symbols_language[1] and symbol_choice_player == symbols_language[0]:
            print(text_winnings[1])
        # Papier vs Stein
        if symbol_choice_pc == symbols_language[2] and symbol_choice_player == symbols_language[1]:
            print(text_winnings[1])
    
        # player winnings
        # Schere vs Papier
        if symbol_choice_player == symbols_language[0] and symbol_choice_pc == symbols_language[2]:
            print(text_winnings[2])
        # Stein vs Schere
        if symbol_choice_player == symbols_language[1] and symbol_choice_pc == symbols_language[0]:
            print(text_winnings[2])
        # Papier vs Stein
        if symbol_choice_player == symbols_language[2] and symbol_choice_pc == symbols_language[1]:
            print(text_winnings[2])
    
    else:
        print ("Falsche Eingabe")
    
    # Again?
    while 1:
        play_again = input ("Noch einmal spielen (Y/N)? ").capitalize()
        if play_again == "N":
            print ("Schade! Bis zum nächsten mal!")
            main = 0
            break
            
        if play_again == "Y":
            print("Ok, noch eine Runde!")
            break
        
        else:
            print("Falsche Eingabe")
            input_wrong = 1

print("Spielende")
