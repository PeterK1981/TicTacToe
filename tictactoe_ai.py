# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 16:20:44 2025

@author: Peter Keller
"""

# ich versuche mal im Sinne von RL eine Scorefunktion zu definieren,
# die man theoretisch als Grundlage für einen Lernalgorithmus nehmen könnte

# Basic Idea: Wähle zufällig aus den bestbewertesten Indize ('greedy strategy')

# für randomisierte Auswahl
import random

# finde die Reihen, die für gegebenen Index überprüft werden müssen
def get_win_lines(board: list[str], index: int)->list[str]:
    # definiere ein dictionary das für jeden Index die passenden
    # zu prüfenden Lines ausgibt, dank Ziffernblock einfach :D
    # jeweils ohne den index
    win_lines_per_index = {
        1: ['23','47','59'],
        2: ['13','58'],
        3: ['12','69','57'],
        4: ['56','17'],
        5: ['46','28','19','37'],
        6: ['45','39'],
        7: ['89','14','35'],
        8: ['79','25'],
        9: ['36','78','15']
        }
    
    # raussuchen der entsprechenden zu prüfenden Linien
    return win_lines_per_index[index]    

# finde alle indize, in die man noch etwas eintragen kann
def get_empty_indices(board: list[str])->list[int]:
    indices = []
    
    for i in range(1,10):
        if board[i] == ' ':
            indices.append(i)
    
    return indices

# Bewertungsfunktion oder scoring
def scoring(board:list[str])->list[int]:
    # Für jetzt: nehme an, Computer spielt O!!
    
    # hier muss bewertet werden, wie gut die einzelnen Züge sind
    # score function für eine Linie
    # "__" (Zeile leer)
    # "X_" oder "_X" (dem Gegner den Zug vermiesen) 
    # für "O_" oder "_O" (Chance beim nächsten Comp.-zug zu gewinnen)
    # für "OX" oder "XO" (vorteilhaft, führt eventuell zu unentschieden)
    # "XX" (dann könnte der Gegner im nächsten Zug gewinnen!)
    # "OO" (Gewinnzug)
    
    # die optimale score function müsste man trainieren!
    # noch ist es relativ einfach gegen die ai zu gewinnen
    # auch, weil bei gleichem score zufällig gewählt wird. 
    # zum Beispiel könnte man den score erhöhen für den Fall,
    # das schon ein O in der Reihe steht!
    score_dic = {
            "  " : 0,
            "X " : 1,
            " X" : 1,
            "O " : 2,
            " O" : 2,
            "OX": 0,
            "XO": 0,
            "XX": 8,
            "OO": 9
        }
    
    # Erinnerung: Feld 0 ist bedeutungslos, erhält aber 1:1 indizierung
    # von Ziffernblock
    scores = [0]*10 
    
    # erstmal alle leeren Felder finden
    # list von ints
    indices_to_check = get_empty_indices(board)
    
    # für jeden index wird für jede gewinnlinie der score zusammenaddiert
    for index in indices_to_check:
        win_lines = get_win_lines(board, index)
        for line in win_lines:
            pattern = board[int(line[0])]+board[int(line[1])]
            scores[index] += score_dic[pattern]
    
    return scores
    
    
# Implementation zufälliger valider Move
def suggest_random_move(board: list[str]) -> int:
    
    available = get_empty_indices(board)
    
    return random.choices(available)[0]
  
# implementation einer einfachen ai
def get_best_choice(scores:list[int])->int:
    max_indices = []
    max_score = 0
    
    # find the max 
    # ich will hier kein pandas benutzen, da gibt es argmax
    # findet den höchsten score
    for score in scores:
        if score > max_score:
            max_score = score
        
    # sammelt alle indize mit max score ein
    for i in range(1,10):
        if scores[i] == max_score:
            max_indices.append(i)
            
    # falls es mehrere Indize geben sollte, wähle eins zufällig
    return random.choices(max_indices)[0]

# Ausgabe des Scorings zum Debuggen und gucken was die AI macht    
def display_scoring(scores:list[int]):
    # geklaut aus draw_board
    # oberer Rand
    print("scoring")
    print("┏━━━┳━━━┳━━━┓")
    
    s=[]
    # scores zu string carsten
    for i in range(10):
        s.append(str(scores[i]))
    
    # Mittelzeilen mit Board-Zustand
    # Brute force, weil kleine Struktur (der String wird wegen Kompabilität
    # zum Ziffernblock auf der Tastatur umgekehrt ausgelesen!!)
    print("┃ " + s[7] + " ┃ " + s[8] + " ┃ " + s[9] + " ┃")
    print("┣━━━╋━━━╋━━━┫")
    print("┃ " + s[4] + " ┃ " + s[5] + " ┃ " + s[6] + " ┃")
    print("┣━━━╋━━━╋━━━┫")
    print("┃ " + s[1] + " ┃ " + s[2] + " ┃ " + s[3] + " ┃")
    
    # unterer Rand
    print("┗━━━┻━━━┻━━━┛")
    
# Einen 'guten' Move vorschlagen
def suggest_move(board: list[str], symbol='X') -> int:
    # Scoring erzeugen und einen der besten Moves zufällig wählen
    scores = scoring(board)
    display_scoring(scores)
    return get_best_choice(scores)

