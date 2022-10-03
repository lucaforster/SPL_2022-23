import random

numWuerfel = 6
sumPlayer = 0
sumComputer = 0
gameOver = False

while gameOver == False:
  mode = int(input("1: Starten\n2: Beenden\nAuswahl: "))
  if mode == 1:
    for i in range(numWuerfel):
      player = input("Beliebige Taste drücken\n")
      playerWuerfel = random.randint(1, 6)
      sumPlayer += playerWuerfel

      print(f"Du hast {playerWuerfel} gewürfelt!")

      compWuerfel = random.randint(1, 6)
      sumComputer += compWuerfel

      print(f"Der Computer hat {compWuerfel} gewürfelt!")

      print(f"Spieler Gesamtpunkte: {sumPlayer}, Computer Gesamtpunkte: {sumComputer}\n")

    if sumPlayer == sumComputer:
      print("Unentschieden\n")
    elif sumPlayer > sumComputer:
      print("Spieler hat gewonnen\n")
    else:
      print("Computer hat gewonnen\n")

  if mode == 2:
    gameOver == True
    quit()
    
