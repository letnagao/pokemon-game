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
        self.hp += 1

if __name__ == '__main__':
    print(Pokemon(name="bulbasaur", primary_type="grass"))
    print(Pokemon(name="charmander", primary_type="fire"))

