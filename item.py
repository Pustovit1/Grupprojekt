# Lista på inventory
import random
class Item():
    def __init__(self,name):
        self.name = name
        self.strength = random.randint(1,10)
    
    def get_rarity_item(self):
        if 0 < self.strength <= 5:
            return "Common Rusty Sword"
        elif 5 < self.strength <= 7:
            return "Uncommon Iron Sword"
        elif 7 < self.strength <= 9:
            return "Epic Diamond Sword"
        elif 9 < self.strength <= 10:
            return "LEGENDARY Mythril Sword"


# Basera item rarity på dess strength

Sword_item = Item("Rusty sword")

print(Sword_item.name)
print(Sword_item.get_rarity_item())
print(str(Sword_item.strength) +  " STRENGTH")
