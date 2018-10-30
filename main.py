import random

#Class for all player and hostile characters
class Character:
    def __init__(self, name):
        self.name = name
        self.health = 10

        Fists = Weapon('Fists', '1')
        self.weapon = Fists

    def fight(self):
        #Choose an enemy
        enemy = random.choice(self.opponents)

        #Hit enemy
        if self.health > 0:
            self.weapon.use(enemy)
        if enemy.health <= 0:
            print(self.name,'killed',enemy.name)
            self.opponents.remove(enemy)

#Class for all weapons
class Weapon:
    def __init__(self,name,damage='1d4'):
        self.name = name
        self.damage = damage

    def use(self,target):
        rolled_damage = roll(self.damage)
        target.health -= rolled_damage
        print(target.name,'is dealt',rolled_damage,'and has',max(target.health,0),'hitpoints remaining!')

#Used to roll dice to calculate damage and other random events
def roll(dice_str):
    if dice_str.isdigit():
        return int(dice_str)
    dice_num = int(dice_str[:dice_str.find('d')])
    dice_sides = int(dice_str[dice_str.find('d')+1:])
    output = 0
    for die in range(dice_num):
        output += random.randint(1,dice_sides)
    return output

#Used to battle two teams of characters
def battle(team1,team2):
    turn = 1
    while any(team_member.health > 0 for team_member in team1) > 0 and any(enemy.health > 0 for enemy in team2):
        print('Starting turn',turn)
        for team_member in team1:
            team_member.fight()
        for enemy in team2:
            enemy.fight()
        print('Ending turn',turn)
        turn += 1
        
#Create Weapons
Sword = Weapon('Sword','1d6')

#Create Characters
Player = Character('Player')
Enemy = Character('Enemy')
Enemy2 = Character('Enemy2')

#Give weapon to character
Player.weapon = Sword

#Set up teams
team1 = [Player]
team2 = [Enemy,Enemy2]

#Update teams with enemies
for team_member in team1:
    team_member.opponents = team2
for team_member in team2:
    team_member.opponents = team1

#Battle
battle(team1,team2)
