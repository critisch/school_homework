# Schulhausaufgaben
# Python Rechner

# Aufgaben
#Schreibe ein Programm, dass 3 Zahlen einliest. Die ersten
#beiden beschreiben die Werte, mit denen gerechnet wird
#die letzte Zahl beschreibt die Operation (1 ist +, 2 ist -
# 3 ist *, 4 ist /)

num1 = int(input("Bitte gib die erste Zahl ein: ")) # Zahl 1 eingeben
num2 = int(input("Bitte gib die zweite Zahl ein: ")) # Zahl 2 eingeben
op = int(input("Bitte gib die Operation ein: ")) # Operation eingeben

if op == 1: # Wenn Operation = 1 ist, dann
    # Plus rechnen
    print(f"Summe: {num1 + num2}")
elif op == 2: # Wenn Operation = 2 ist, dann
    # Minus rechnen
    print(f"Summe: {num1 - num2}")
elif op == 3: # Wenn Operation = 3 ist, dann
    print(f"Summe: {num1 * num2}")
    # Mal rechnen
elif op == 4: # Wenn Operation = 4 ist, dann
    # Geteilt rechnen
    print(f"Summe: {num1 / num2}")
else: # Wenn Operation != 1, 2, 3 oder 4 ist, dann
    print("Fehlerhafte Eingabe")