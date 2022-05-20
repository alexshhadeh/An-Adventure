import os
import time


class CombatSystem:
    def __init__(self):
        self.__combat_style = None
        self.__roll_modifiers = {
            "Melee": 0,
            "Magic": 0,
            "Ranged": 0
        }

    def character_select(self):
        # os.system("cls")
        print("Select your character:\nWarrior\tMage\tRanger")
        self.__combat_style = input()
        if self.__combat_style not in ["Warrior", "Mage", "Ranger"]:
            print("You have to input available character")
            time.sleep(3)
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
