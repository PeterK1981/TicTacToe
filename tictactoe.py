# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 15:52:42 2025

@author: Peter Keller
"""


# =============================================================================
# Main
# =============================================================================
def main():
    import tictactoe_engine as engine
    import tictactoe_ai as ai
    
    # Spielmatrix initialisieren
    # Namenskonflikt mit der geladenen Bibliothek
    board = engine.get_empty_board()
    
    # Spielstand
    scores = [0,0]
    
    # "Startbildschirm mit Bedienungsanleitung
    # Hier unsicher, ob das in 
    engine.display_initial_screen()
    
    # Spielernamen abfragen
    players = engine.get_player_names(number_of_players=1)
    
    # Symbols for players
    # noch in engine?
    symbol_dic = {
        players[0]: "X",
        players[1]: "O",
    }
    
    # Spielzug Zähler, um zwischen den Symbolen zu alternieren
    draw = 1
    
    # Spielstatus
    game_ended = False
    is_tie = False
    round_ended = False
    
    # Beim Start das noch leere Board anzeigen   
    engine.draw_board(board)

    while not game_ended and not round_ended:
        
        current_player = players[(draw+1) % 2]
        current_symbol = symbol_dic[current_player]
        
        # Usereingabe vom aktuellen Spieler abfragen
        if current_player == 'Computer':
            pos = ai.suggest_move(board)
        else:
            pos = engine.get_user_choice(current_player, current_symbol)
        
        # pos ist nun mit Sicherheit int, könnte aber noch auf ein nicht
        # existierendes Feld verweisen, oder das gewählte Feld ist schon 
        # belegt
        if 0 < pos < 10  and engine.is_available(pos, board):
            engine.update_board(pos, current_symbol, board)
            
            # Spielzug um eins erhöhen
            draw += 1
            
            # update Abbruchbedingung
            round_ended, is_tie = engine.check_game_end(board)
            
            # Nach erfolgreicher Eintragung, Anzeige erneuern
            engine.draw_board(board)
        else:
            print("Feld belegt oder ungültig!")
        
        # Wenn eine Runde zu Ende ist, passiert das:    
        if round_ended:
            # Spielstand updaten
            scores = engine.update_scores(is_tie, players[draw % 2], scores, draw % 2)
            # Spielstand ausgeben
            engine.print_score(scores)
        
            if engine.another_round():
                # Nach Bestätigung einer neuen Runde wird alles zurückgesetzt
                round_ended, game_ended, is_tie = False, False, False
                board = engine.get_empty_board()
                engine.draw_board(board)
                # Es fängt der Spieler mit X an, jedes Mal
                # Könnte man randomisieren
                draw = 1 
            else:
                # Andernfalls wird der Spielstand mit Spielendemessage ausgegeben
                if scores[0] > scores[1]:
                    print(f"{players[0]} hat insgesamt gewonnen!")
                elif scores[0] < scores[1]:
                    print(f"{players[1]} hat insgesamt gewonnen!")
                else:
                    print("Unentschieden!")
                print("Danke für's Spielen!")

# =============================================================================
if __name__ == "__main__":
    main()

