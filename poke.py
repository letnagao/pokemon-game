#from pathlib import Path
#print(Path().home())

class Pokemon:
    def __init__(self, name, primary_type, max_hp):
        self.name = name
        self.primary_type = primary_type
        self.hp = max_hp
        self.max_hp = max_hp

    def __str__(self):
        return f"{self.name} ({self.primary_type} : {self.hp}/{self.max_hp})" 

    def feed(self):
        if self.hp < self.max_hp:
            self.hp += 1
            print(f"{self.name} has now {self.hp} HP.")
        else:
            print(f"{self.name} is full.")
    
    def battle(self, other):
        print("Battle:",self.name, other.name)
        result = self.typewheel(self.primary_type, other.primary_type)
        if result == "lose":
            self.hp -= 10
            print(f"{self.name} lost and now has {self.hp} HP.")
        print(f"{self.name} fought {other.name} and the result is a {result}")

    @staticmethod
    def typewheel(type1,type2):
        result = {0: "lose", 1: "win", -1: "tie"}
        game_map = {"water": 0, "fire": 1, "grass": 2}

        wl_matrix = [
            [-1, 1, 0], 
            [0, -1, 1],
            [1, 0, -1],
        ]

        wl_result = wl_matrix[game_map[type1]][game_map[type2]]
        return result [wl_result]

if __name__ == '__main__':
    bulbi = Pokemon(name="bulbasaur", primary_type="grass", max_hp=100)
    charm = Pokemon(name="charmander", primary_type="fire", max_hp=150)
    bulbi.battle(charm)
