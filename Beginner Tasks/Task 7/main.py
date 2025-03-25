class Avenger:
    def __init__(self, name, age, gender, super_power, weapon, is_leader=False):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
        self.is_leader = is_leader

    def get_info(self):
        return (f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, "
                f"Super Power: {self.super_power}, Weapon: {self.weapon}")

    def is_leader(self):
        return self.is_leader


# Creating superheroes
super_heroes = [
    Avenger("Captain America", 100, "Male", "Super Strength", "Shield", True),
    Avenger("Iron Man", 48, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 35, "Male", "Fighting Skills", "Bow and Arrows")
]

# Displaying the information of each superhero
for hero in super_heroes:
    print(hero.get_info())
    print("Is Leader:", hero.is_leader)
