import random
import time

class Player:
    # Class variables that are shared among ALL players
    player_list = [] #Each time we create a player, we will push them into this list.
    player_count = 0

    def __init__(self, name, alive = True):
        ## These instance variables should be unique to each user. Every user will HAVE a name, but each user will probably have a different name.
        self.name = name
        self.strength = random.randint(8, 12) # The stat values will all be random, but within a range of reasonableness
        self.defense = random.randint(8, 12)
        self.speed = random.randint(8, 12)
        self.max_health = random.randint(36, 48) # The max health value will be random, but higher than the others.
        self.health = self.max_health # Set the current health equal to the max health.
        self.magic = random.randint(8, 12)
        self.alive = alive
        self.skip_turn = False
        print("Player " + self.name + " has entered the game. \n  Strength: " + str(self.strength) + "\n  Defense: " + str(self.defense) + "\n  Speed: " + str(self.speed) + "\n  Magic: " + str(self.magic) + "\n  Maximum health: " + str(self.max_health) + ".\n")
        ## We're going to also manipulate the two class variables - While each user has their own specific defense or strength, the users all share the class variables defined above this method.
        Player.player_list.append(self) ## The player will be added to the list of players.
        Player.player_count += 1 ## The player count should go up by one.
        print("There are currently " + str(Player.player_count) + " player(s) in the game.\n\n")

    def attack(self, target):
        ## With a CLI, we want to print out all the information our users need to play this game.
        ## Let's show the attacker and defender's names here.
        print("Player " + self.name + " attacks " + target.name + "!!!")
        print(self.name + "'s strength is " + str(self.strength) + " and target " + target.name + "'s defense is " + str(target.defense) + ".")
        ## The battle will go differently depending on who is stronger.
        if self.strength < target.defense:
            print("Due to the target's strong defense, the attack only does half damage...")
            damage = self.strength / 2
        elif self.strength > target.defense:
            print("Since the target is weaker than you are, the attack does double damage!")
            damage = self.strength * 2
        else:
            print("These players are evenly matched. The attack goes through normally.")
            damage = self.strength
        target.health -= damage
        if target.health < 0:
            target.health = 0
        ## Let's print out the new totals so that we know the final results of the fight.
        print(target.name + " now has " + str(target.health) + "/" + str(target.max_health) + " health remaining.\n\n")
        self.check_health(target)

    def heal(self):
        self.health += self.magic
        print(f"{self.name} is healing . . .  {self.magic} health restored!")
        print(f"{self.name} now has {self.health}/{self.max_health} health remaining.")

    def special_attack(self, target):
        print("Player " + self.name + " uses their SPECIAL ATTACK on " + target.name + "!!!")
        print(self.name + "'s strength is " + str(self.strength) + " and target " + target.name + "'s defense is " + str(target.defense) + ".")
        ## The battle will go differently depending on who is stronger.
        if self.strength < target.defense:
            print("Due to the target's strong defense, the special attack only does half damage...")
            damage = self.strength
        elif self.strength > target.defense:
            print("Since the target is weaker than you are, the special attack does double damage!")
            damage = self.strength * 4
        else:
            print("These players are evenly matched. The special attack goes through normally.")
            damage = self.strength * 2
        target.health -= damage
        if target.health < 0:
            target.health = 0
        ## Let's print out the new totals so that we know the final results of the fight.
        print(target.name + " now has " + str(target.health) + "/" + str(target.max_health) + " health remaining.\n\n")
        self.check_health(target)
        self.skip_turn = True

    def check_health(self, target):
        if target.health == 0:
            target.alive = False
            time.sleep(0.8)
            print(f"{target.name} has been defeated!\n")
            time.sleep(0.8)
            print(f"{self.name.upper()} WINS!\n")
            exit()


## All other methods you code for the player class will fit best below this line.
## Make sure to indent instance methods properly so the computer knows they're part of the class.


class Battle:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def start(self):
        while self.player1.health > 0 and self.player2.health > 0:
            time.sleep(0.8)
            self.player1.attack(self.player2)
            time.sleep(0.8)
            self.player2.attack(self.player1)
