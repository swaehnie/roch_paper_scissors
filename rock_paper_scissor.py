# title: Schere, Stein, Papier
# rev: 31.08.2022
# created: 31.08.2022
# created by: swaehnie
# contact: swaehnie (https://github.com/swaehnie)
# repository: https://github.com/swaehnie/rock_paper_scissors
# 

import random

symbols_de = ["Schere", "Stein", "Papier"]
symbols_eng = ["rock", "paper", "scissors"]
symbols_fr = ["pierre", "ciseaux", "papier"]


main = 1

# game
while main ==1:
    # pc choice
    random.shuffle(symbols_de)
    # print(symbols)
    symbol_choice_pc = random.choice(symbols_de)
    # print(symbol_choice_pc)

    # player choice
    symbol_choice_player = input ("Auswahl: Schere, Stein, Papier? ").capitalize()

    if symbol_choice_player in symbols_de:
        print (symbol_choice_pc+" vs "+symbol_choice_player)
        
        if symbol_choice_pc == symbol_choice_player: print("Unentschieden")
    
        # pc winnings
        if symbol_choice_pc == "Schere" and symbol_choice_player == "Papier": print("PC hat gewonnen!")
        if symbol_choice_pc == "Stein" and symbol_choice_player == "Schere": print("PC hat gewonnen!")
        if symbol_choice_pc == "Papier" and symbol_choice_player == "Stein": print("PC hat gewonnen!")
    
        # player winnings
        if symbol_choice_player == "Schere" and symbol_choice_pc == "Papier": print("Du hast gewonnen!")
        if symbol_choice_player == "Stein" and symbol_choice_pc == "Schere": print("Du hast gewonnen!")
        if symbol_choice_player == "Papier" and symbol_choice_pc == "Stein": print("Du hast gewonnen!")
    
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
