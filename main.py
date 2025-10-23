# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 09:58:25 2025

@author: Peter Keller

# Projekt 6: Erstellung eines mathematischen Moduls (Erweitert)

## Projektbeschreibung

Erweitere dein eigenes Python-Modul für mathematische Funktionen, `mymathmodule`, durch zusätzliche Funktionen und Variablen. Dieses fortgeschrittene Projekt soll das Verständnis für die Konzepte von Modulen in Python vertiefen und die Wiederverwendbarkeit von Code fördern. Du wirst lernen, wie man eigene Funktionen in einer Moduldatei definiert und diese dann in anderen Python-Programmen verwendet.

### Funktionen und Variablen in `mymathmodule.py`:

- **`mittelwert(a, b)`**: Berechnet den Mittelwert von zwei Zahlen `a` und `b`.
- **`fac(n)`**: Berechnet die Fakultät der Zahl `n`.
- **`e`**: Die eulersche Zahl `e`, definiert als eine Variable.

### Nutzung des Moduls:

1. **Import im Hauptprogramm**: Importiere das Modul in deinem Hauptprogramm, 
z.B. `main.py`.
2. **Aufruf von Modulfunktionen**: Nutze die Funktionen des Moduls, um 
mathematische Berechnungen durchzuführen.

### Aufgaben und Anforderungen:

- **Aufgabe 1**: Implementiere die Funktion `fac(n)` im Modul und rufe sie in 
    `main.py` auf.
- **Aufgabe 2**: Definiere die eulersche Zahl `e` im Modul und verwende sie in
    `main.py`.
- **Aufgabe 3**: Importiere die eulersche Zahl `e` aus dem Python-Modul `math` in `main.py` und vergleiche die Werte.
- **Aufgabe 4**: Importiere das Modul `platform` und rufe die Funktion `system()` auf, um das Betriebssystem zu identifizieren.
- **Aufgabe 5**: Nutze das Modul `time`, um die aktuelle Zeit mit `ctime()` auszugeben.
- **Aufgabe 6**: Generiere eine Zufallszahl zwischen 1 und 20 mit `randint` aus dem Modul `random` und berechne deren Fakultät mit `fac(n)`.

### Abgabe:

Die Abgabe erfolgt in Form von zwei Python-Skripten (*.py Dateien):

1. **`mymathmodule.py`**: Das erweiterte Modul mit den neuen Funktionen und Variablen.
2. **`main.py`**: Ein Python-Skript, das dein Modul und die externen Module importiert und die Funktionen daraus nutzt, um die Aufgaben zu lösen.

Stelle sicher, dass das Hauptprogramm (`main.py`) und das Modul (`mymathmodule.py`) korrekt zusammenarbeiten. 

Inkludiere eine kurze Dokumentation in `main.py`, die die Ausführung der zusätzlichen Aufgaben und deine Beobachtungen beschreibt.
"""

import mymathmodule as mmm
import math, platform, time
from random import randint as r

# Aufgabe 1
n = 5
print(f"Fakultät von {n} ist {mmm.fac(n)}.")

# Aufgabe 2
print(f"Die Eulersche Zahl ist ca. {mmm.EULER_E}.")

# Aufgabe 3
print(f"Die Eulersche Zahl ist ca. {math.e}.")

# Aufgabe 4
print("Du arbeitest auf", platform.system())

# Aufgabe 5 
print("Jetzt: ", time.ctime())

# Aufgabe 6
print("Ich ziehe eine zufällige Zahl:", n:=r(1,20))
print(f"Die Fakultät von {n} ist: {mmm.fac(n)}")