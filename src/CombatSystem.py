import os
import random
import time
import d20


class CombatSystem:
    def __init__(self):
        self.__combat_style = None
        self.__roll_modifiers = {
            "Melee": 0,
            "Magic": 0,
            "Ranged": 0
        }
        self.victories = 0

    def character_select(self):
        # os.system("cls")
        print("Select your character:\nWarrior\tMage\tRanger")
        self.__combat_style = input()
        if self.__combat_style not in ["Warrior", "Mage", "Ranger"]:
            print("You have to input available character")
            time.sleep(2)
            self.character_select()
        if self.__combat_style == "Warrior":
            self.__roll_modifiers["Melee"] = 4
            self.__roll_modifiers["Magic"] = -2
            self.__roll_modifiers["Ranged"] = 1
        if self.__combat_style == "Mage":
            self.__roll_modifiers["Melee"] = -2
            self.__roll_modifiers["Magic"] = 4
            self.__roll_modifiers["Ranged"] = -1
        if self.__combat_style == "Ranger":
            self.__roll_modifiers["Melee"] = 2
            self.__roll_modifiers["Magic"] = 1
            self.__roll_modifiers["Ranged"] = 4

        print("You have chosen: " + self.__combat_style)
        print("Your modifiers are:")
        for k, v in self.__roll_modifiers.items():
            print(k, v)

    def generate_battle(self, monster=""):
        monsters = [
            "Goblin",
            "Rat",
            "Slime"
        ]
        if monster == "":
            monster = random.choice(monsters)
            print("You have encountered:", monster + "!")
        print("Make action:\nSlash\tFireball\tBow")
        action = input()
        if action not in ["Slash", "Fireball", "Bow"]:
            print("Action unavailable")
            time.sleep(2)
            self.generate_battle(monster)

        user_roll = d20.roll("1d20")
        monster_roll = d20.roll("1d20")

        if action == "Slash":
            user_roll = d20.roll("1d20" + "+" + str(list(self.__roll_modifiers.values())[0]))
            if monster == "Goblin":
                monster_roll = d20.roll("1d20" + "-4")
            if monster == "Rat":
                monster_roll = d20.roll("1d20" + "+2")
            if monster == "Slime":
                monster_roll = d20.roll("1d20" + "+4")

        if action == "Fireball":
            user_roll = d20.roll("1d20" + "+" + str(list(self.__roll_modifiers.values())[1]))
            if monster == "Goblin":
                monster_roll = d20.roll("1d20")
            if monster == "Rat":
                monster_roll = d20.roll("1d20" + "-2")
            if monster == "Slime":
                monster_roll = d20.roll("1d20" + "-4")

        if action == "Bow":
            user_roll = d20.roll("1d20" + "+" + str(list(self.__roll_modifiers.values())[2]))
            if monster == "Goblin":
                monster_roll = d20.roll("1d20")
            if monster == "Rat":
                monster_roll = d20.roll("1d20" + "+4")
            if monster == "Slime":
                monster_roll = d20.roll("1d20" + "-2")

        print("Your roll is:", user_roll)
        print("Monster roll is:", monster_roll)
        if user_roll.total > monster_roll.total:
            print("You have won the battle")
            self.victories += 1
        else:
            print("You just got your ass beaten by", monster + "!")
