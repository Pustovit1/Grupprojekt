import re
import random
from random import randint


def play():
    while True:
            svar = input("Vill du spela? ").capitalize() # Frågar om man vill spela eller inte
            if svar == "Nej":
                quit()
            elif svar == "Ja": 
             print("We play")
             return 
            print("Svara med 'Ja' eller 'Nej'. Tack")
play()
class Player:
    def __init__(self, name, strength, hp, lvl):
       self.name = name 
       self.strength = strength
       self.hp = hp
       self.lvl = lvl

class Door:
    def __init__(self,number):
        self.number = number

def stats():
    print(f"""Ditt namn är:{player1.name} 
              Din hälsa är {player1.hp} 
              Din lvl är {player1.lvl} 
              Din styrka är {player1.strength}""")

def Namn():
    namn = ""
    while True:
        namn = input("Skriv ditt namn: ")
        if re.match('^[A-Za-z]+$',namn):
            break
        else:
            print("Du kan endast ha bokstäver i ditt namn!")
    return namn
player1 = Player(Namn(),5,10,1)
class Item():
    def __init__(self):
        self.name = random.choice(["Sword of Extermination","Muramasa","Mjolnir","Excalibur","Baxcalibur", "Zangetsu"] )
        self.strength = random.randint(1,10)
    
    def get_rarity_item(self):
        if 0 < self.strength <= 5:
            return "Common"
        elif 5 < self.strength <= 7:
            return "Uncommon"
        elif 7 < self.strength <= 9:
            return "Epic"
        elif 9 < self.strength <= 10:
            return "LEGENDARY"



# Basera item rarity på dess strength
Weapon_item = Item()
print(Weapon_item.get_rarity_item())
print(Weapon_item.name, str(Weapon_item.strength) +  " STRENGTH")




def chest_event():
    global player1
    print("Chest")

monster_str = random.randint(player1.strength-5,player1.strength+5)

def monster_event():
    global player1
    print("(#'Д')")
    print("Oj, ett monster!")
    
    if monster_str>player1.strength+3:
        print("den verkar vara stark...")
    elif player1.strength>monster_str+3:
        print("...men, den ser ganska svag ut!")
    
    if monster_str > player1.strength:
        print("monstret var starkare än vad du trodde och du blir skadad! du springer snabbt till nästa dörr...")
        player_hp=player_hp-1
    elif monster_str > player1.strength:
        print("Du dödar monstret och går vidare till nästa rum")


def trap_event():
    print("Trap (-hp)")
    global player1
    player1.hp = player1.hp-1
    
random_number = randint(0,2)
door = Door(random_number)


if door.number == 0:
    print("Congratulations, you found a chest")
    chest_event()
elif door.number == 1:
    monster_event()
elif door.number == 2:
    print("Trap")
    trap_event()
