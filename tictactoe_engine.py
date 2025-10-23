# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 15:53:47 2025

@author: Peter Keller
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 15:52:42 2025

@author: Peter im Keller
"""

# Der folgende Code stammt zu großen Teilen aus Woche05, ich habe nur einige 
# Kleinigkeiten angepasst. 
# Bemerkung: Zu Testzwecken gibt es eine neue Methode: get_random_board
   
# Modulabhängigkeit von random!

import random

# =============================================================================
# Funktionen
# =============================================================================

# display game info +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# =============================================================================
# Spieltitel ausgeben
def display_title():

    print("="*30 + "\n" + "Tic-Tac-Toe – Three in a Row!" + "\n" + "="*30 + "\n")


# =============================================================================
# Startbildschirm mit Anleitung ausgeben
def display_initial_screen():    
    # Einmal den Titel
    display_title()
    
    # # Am Anfang werden einmal die Instruktionen angezeigt
    # # Spielerei, um Dateien in Python zu testen
    # # Achtung: die Datei instructions.txt liegt im selben Verzeichnis, wie
    # # die .py Datei
    # with open("E:\Peter\Weiterbildung\Python\Woche05\instructions.txt","r") as file:
    #     print(file.read())
    
    print('''
    ====================================================================
    Anleitung
    ====================================================================

    Die Spieler markieren abwechselnd ein freies Feld mit ihrem Symbol.
    Spieler A markiert mit "X", und Spieler B mit "O". Gewonnen hat, wer
    als erstes eine Reihe mit drei gleichen Symbolen hat. Das Spiel endet
    unentschieden, wenn es keine freien Felder mehr gibt und noch niemand
    gewonnen hat.

    Die Felder auf dem Spielbrett sind nummiert wie der Ziffernblock auf
    der Tastatur:

    ┏━━━┳━━━┳━━━┓
    ┃ 7 ┃ 8 ┃ 9 ┃
    ┣━━━╋━━━╋━━━┫
    ┃ 4 ┃ 5 ┃ 6 ┃
    ┣━━━╋━━━╋━━━┫
    ┃ 1 ┃ 2 ┃ 3 ┃
    ┗━━━┻━━━┻━━━┛

    Ein Spieler macht einen Eintrag, indem die entsprechende Feldnummer
    eingegeben wird.

    ====================================================================


    ''')
    # Warte auf irgendeine Taste, um das Spiel zu starten
    idle_until_key_pressed()

# end display game info +++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Punktestand +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# =============================================================================
# Spielstand updaten
def update_scores(is_tie, player, scores, win_index):
    # Hier ist das Spielende definitiv erreicht
    # aber eventuell mit untentschieden
    if is_tie:
        print("Das Spiel ist unentschieden ausgegangen!")
        return scores
    else:
        print(f"{player} hat diese Runde gewonnen.")
        scores[win_index] += 1
        return scores
        
# =============================================================================
# Spielstand ausgeben
def print_score(scores:list[int,int]):
    print(f"Es steht {scores[0]}:{scores[1]}")

# End punktestand +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Interaction methods +++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# =============================================================================
# Stoppt das Spiel bis der Spieler irgendeine Taste drückt, z.b. Enter
def idle_until_key_pressed():
    while True:
        ui = input("Weiter mit Enter")
        if ui != None:
            break
    print("\n"*20)


# =============================================================================
# Spielernamen abfragen (two_player_mode)
def get_player_names(number_of_players=2)-> list[str,str]:
    player_A = input("Spieler 1, gib Deinen Namen ein: ")
    if number_of_players == 2:
        player_B = input("Spieler 2, gib Deinen Namen ein: ")
    else:
        player_B = "Computer"
    
    return [player_A, player_B]


# =============================================================================
# Abfrage, ob noch eine Runde gespielt werden soll
def another_round()->bool:
    # abfrage ob noch eine Runde
    decision = input("Noch eine Runde (j/n)? ").strip().lower()
    
    if decision == "j":
        return True
    else:
        return False

# =============================================================================
def get_user_choice(current_player,current_symbol)->int:
    # eingabefehler abfangen
    while True:
        try:
            return int(input(f"{current_player} ({current_symbol}), wähle ein Feld (Felder 1-9): "))                
            break   
            # abbruch der while schleife falls die Eingabe korrektes Format hat
        except ValueError:
            print("Ungültige Eingabe!")

# End interaction methods +++++++++++++++++++++++++++++++++++++++++++++++++++++            

# =============================================================================
# Darstellung des Boards
def draw_board(board):
    
    # Lösche Konsoleninhalt
    # os.system('cls')
    # Spyder macht verrückte Sachen mit der Ausgabe, daher lieber so
    # Dadurch wird die Illusion erzeugt, dass das Spielfeld statisch angezeigt
    # würde
    # print("\n"*20)
    
    # Titel
    display_title()
    
    # Definiere old-school unicode tableaux 
    # so soll es ausgegeben werden
    # ┏━━━┳━━━┳━━━┓
    # ┃   ┃   ┃   ┃
    # ┣━━━╋━━━╋━━━┫
    # ┃   ┃   ┃   ┃
    # ┣━━━╋━━━╋━━━┫
    # ┃   ┃   ┃   ┃
    # ┗━━━┻━━━┻━━━┛

    # oberer Rand
    print("┏━━━┳━━━┳━━━┓")
    
    # Mittelzeilen mit Board-Zustand
    # Brute force, weil kleine Struktur (der String wird wegen Kompabilität
    # zum Ziffernblock auf der Tastatur umgekehrt ausgelesen!!)
    print("┃ " + board[7] + " ┃ " + board[8] + " ┃ " + board[9] + " ┃")
    print("┣━━━╋━━━╋━━━┫")
    print("┃ " + board[4] + " ┃ " + board[5] + " ┃ " + board[6] + " ┃")
    print("┣━━━╋━━━╋━━━┫")
    print("┃ " + board[1] + " ┃ " + board[2] + " ┃ " + board[3] + " ┃")
    
    # unterer Rand
    print("┗━━━┻━━━┻━━━┛")

    # print("\n" + "="*30 + "\n")


# =============================================================================
# Verfügbarkeit des eingegebenen Feldes testen
def is_available(pos,board) -> bool:
    # Eingabe testen
    if (int(pos) > 9 and int(pos) < 1):
        print("Nur Zahlen 1-9 eingeben!")
        return False
    else:
        if board[pos] == " ":
            return True
        else:
            return False
        
# =============================================================================
# ist die übergebene Linie eine Gewinnerlinie?
def is_winning_line(key:str, board:list)->bool:
    # string in position umwanden
    key_0, key_1, key_2 = int(key[0]), int(key[1]), int(key[2])
    
    return (board[key_0] == board[key_1] == board[key_2] != " ")
    
# =============================================================================
# Das Board checken, ob schon irgendwo eine Dreier-Reihe vorhanden
# hier hilft das Dictionary
def check_game_end(board)-> [bool,bool]:
    
    # hash-Table für die Gewinnreihen
    # Mit den Keys kann man auf die Einträge der Liste zurückgreifen
    winning_options = {
        '789', # erste Zeile
        '456', # zweite Zeile
        '123', # dritte Zeile
        '147', # erste Spalte
        '258', # zweite Spalte
        '369', # dritte Spalte
        '357', # Diagonale
        '159'  # Anti-diagonale
    } # Name doof!
    
    win_detected = False
    win_key = ""
    
    # alle möglichen Linien durchchecken
    for key in winning_options:
        win_detected |= is_winning_line(key, board)
        # Nur eine Gewinnoption existiert zu jeder Zeit
        if (win_detected):
            win_key = key
            break
    
    # falls Gewinn vorliegt die Farben anpassen
    if win_detected:
        for char in win_key:
            board[int(char)] = mark_green(board[int(char)])
    
    # Rückgabefälle
    if win_detected:
        return True, False # Gewinnreihe, kein Tie, Spielende!
    elif not win_detected and is_full(board):
        return True, True # keine Gewinnreihe, Tie, Spielende!
    else:
        return False, False # Spiel geht weiter
    
    
# =============================================================================
# Testen, ob das Spielbrett vollständig ausgefüllt ist
def is_full(board:list)->bool:
    # teste alle Reihen ob belegt
    row1_full = (board[7] != " ") and (board[8] != " ") and (board[9] != " ")
    row2_full = (board[4] != " ") and (board[5] != " ") and (board[6] != " ")
    row3_full = (board[1] != " ") and (board[2] != " ") and (board[3] != " ")
    
    # Ergebnis zurückgeben
    return row1_full and row2_full and row3_full

# =============================================================================
# einen String mit grünem Hintergrund markieren
mark_green = lambda s: "\033[42m" + s + "\033[0m"

# =============================================================================
# Spielbrett aktualisieren    
def update_board(pos: int, symb:str, board):
    board[pos] = symb


# =============================================================================
# leeres Feld erzeugen
# Statt String lieber Liste mit Strings, so ist die Datenstruktur mutable
# und im Gewinnfall kann ich die entsprechenden Felder für die Konsolen-
# ausgabe einfärben

# Das Dollarzeichen ist ein Platzhalter
# so ist user-eingabe 1:1 mit der Datenstruktur verbunden ohne Indexshift
def get_empty_board():
    return list("$"+" "*9) # casting trick


# =============================================================================
# zufälliges Spielbrett erzeugen, wobei es noch keinen Gewinn gibt
# eigentlich unnötig, war aber beim entwickeln der ai nützlich
# erzeugt Boards die evtl durch echtes Spielen nicht erreicht werden können!
def get_random_board()->list[str]:
    
    # flag, um sicher zu stellen, dass noch keiner gewonnen hat
    valid_board = False
    
    # solange samplen bis passendes Board bereitsteht
    while not valid_board:
        tmp = get_empty_board()
        for i in range(1,10):
            # das mit dem [0] ist irgendwie dämlich :(
            tmp[i] = random.choices([' ', 'X', 'O'])[0]   
        
        # Fall wo weder unentschieden noch gewinn vorliegt
        valid_board = not (check_game_end(tmp)[0] or check_game_end(tmp)[1])
        
        if valid_board:
            break
    
    return tmp