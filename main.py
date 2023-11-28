import re

def play():
    while True:
            svar = input("Vill du spela? ").capitalize() # Frågar om man vill spela eller inte
            if svar == "Nej":
                quit()
            elif svar == "Ja": 
             print("We play")
             return 
            print("Svara med 'Ja' eller 'Nej'. Tack")
class Player:
    def __init__(self, name, strength, hp, lvl):
       self.name = name 
       self.strength = 5
       self.hp = 10
       self.lvl = 1
namn = ""
while True:
    namn = input("Skriv ditt namn: ")
    if re.match('^[A-Za-z]+$',namn):
        break
    else:
        print("Du kan endast ha bokstäver i ditt namn!")
def stats():
    print(f"""Ditt namn är:{player1.name} 
        Din hälsa är {player1.hp} 
        Din lvl är{player1.lvl} 
        Din styrka är{player1.strength}""")

player1 = Player(namn,5,10,1)
play()
stats()