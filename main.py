import random
import colorama

class Unit:
	def __init__(self, entities, units=None):
		if entities is None:
			self.entities = []
		else:
			self.entities = entities
			
		if units is None:
			self.units = []
		else:
			self.units = units

# Parent class for all entities
class Entity:
	def __init__(self, name, health, weapons, armor=None):
		self.name = name
		self.health = health
		
		if weapons is None:
			self.weapons = []
		else:
			self.weapons = weapons
		
		if armor is None:
			self.armor = []
		else:
			self.armor = armor
			
	def update(self):
		if self.health <= 0:
			pass
		else:
			weapon_number = random.randint(0, len(self.weapons)-1)
			target = random.randint(0, len(self.opponents)-1)
			print(self.name, "fires his", self.weapons[weapon_number].name, "at", self.opponents[target].name + "!")
			self.weapons[weapon_number].fire(self.opponents[target])

# Parent class for all (ranged) weapons
class Weapon:
	def __init__(self, name, damage):
		self.name = name
		self.damage = damage
		
	def fire(self, target):
		rolled_damage = random.randint(int(self.damage / 2), self.damage)
		target.health -= rolled_damage
		print(target.name, "is dealt", rolled_damage, "point(s) of damage and has", target.health, "point(s) left.")
		if target.health <= 0:
			print(target.name, "is dead!")

def main():
    # Define weapons and entities
    Kalash = Weapon("kalash", 5)
    SlugPistol = Weapon("slug pistol", 3)
    RoadWarrior = Entity("road warrior", 10, [SlugPistol, Kalash])
    Opponent = Entity("road warrior's opponent", 10, [SlugPistol])
    
    # Define opponents
    RoadWarrior.opponents = [Opponent]
    Opponent.opponents = [RoadWarrior]
    
    # Run scenario
    for i in range(5):
        print("Begin turn", i + 1)
        RoadWarrior.update()
        Opponent.update()
        print("End turn", i + 1)
        
        if RoadWarrior.health <= 0 or Opponent.health <= 0:
            break
        
    if RoadWarrior.health <= 0:
        print(Opponent.name, "is victorious!")
    elif Opponent.health <= 0:
        print(RoadWarrior.name, "is victorious!")
    elif RoadWarrior.health > 0 and RoadWarrior.health > 0:
        print("Nobody won!")
        
if __name__ == '__main__':
    main()