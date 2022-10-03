
class Bankomat:
  def init(self):
    self.kontostand = 0

  def einzahlen(self, betrag):
    self.kontostand += betrag
    print(f"Sie haben diesen Betrag {betrag}€ eingezahlt!")

  def abheben(self, betrag):
    self.kontostand -= betrag
    print(f"Sie haben diesen Betrag {betrag}€ abgehoben!")

  def kontostandAnzeigen(self):
    print(f"Der derzeitige Kontostand ist: {self.kontostand}€")

  def beenden(self):
    exit()

bankomat = Bankomat()
auswahl = 0
while auswahl != 4:
  print("Optionen: \n 1. Einzahlen \n 2. Abheben \n 3. Kontostand \n 4. beenden")
  auswahl = int(input("Eingabe: "))
  if auswahl == 1:
    betrag = int(input("Betrag: "))
    bankomat.einzahlen(betrag)
  elif auswahl == 2:
    betrag = int(input("Betrag: "))
    bankomat.abheben(betrag)
  elif auswahl == 3:
    bankomat.kontostandAnzeigen()
  elif auswahl == 4:
    bankomat.beenden()
