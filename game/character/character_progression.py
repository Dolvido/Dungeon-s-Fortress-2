import os
from utils.data_loading import load_data

class CharacterProgression:
    def __init__(self, character):
        self.character = character
        self.experience_points = 0
        self.level = 1
        self.skill_points = 0
        self.equipment = []
        self.spells = []
        self.abilities = []

        self.load_progression_data()

    def load_progression_data(self):
        self.equipment = load_data(os.path.join("data", "resources", "equipment.txt"))
        self.spells = load_data(os.path.join("data", "resources", "spells.txt"))
        # Add more data loading for abilities, etc.

    def gain_experience(self, amount):
        self.experience_points += amount
        print(f"Gained {amount} experience points.")
        self.check_level_up()

    def check_level_up(self):
        required_exp = 100 * self.level  # Example level-up threshold
        if self.experience_points >= required_exp:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.skill_points += 5  # Example skill points per level
        print(f"Congratulations! You have reached level {self.level}.")
        print(f"You have {self.skill_points} skill points to allocate.")
        self.allocate_skill_points()

    def allocate_skill_points(self):
        while self.skill_points > 0:
            print(f"\nAvailable skill points: {self.skill_points}")
            skill_choice = input("Enter the skill you want to improve (e.g., strength): ")
            if skill_choice in self.character['attributes']:
                points = int(input("Enter the number of points to allocate: "))
                if points <= self.skill_points:
                    self.character['attributes'][skill_choice] += points
                    self.skill_points -= points
                else:
                    print("Invalid number of points. Please try again.")
            else:
                print("Invalid skill. Please try again.")

    def acquire_equipment(self, item_name):
        item = next((item for item in self.equipment if item['name'] == item_name), None)
        if item:
            self.character['equipment'].append(item)
            print(f"You have acquired the {item['name']}.")
        else:
            print(f"Equipment '{item_name}' not found.")

    def learn_spell(self, spell_name):
        spell = next((spell for spell in self.spells if spell['name'] == spell_name), None)
        if spell:
            self.character['spells'].append(spell)
            print(f"You have learned the {spell['name']} spell.")
        else:
            print(f"Spell '{spell_name}' not found.")

    def acquire_ability(self, ability_name):
        # Similar to acquire_equipment and learn_spell
        pass

    def display_character_status(self):
        print("\nCharacter Status:")
        print(f"Level: {self.level}")
        print(f"Experience Points: {self.experience_points}")
        print(f"Skill Points: {self.skill_points}")
        print("\nAttributes:")
        for attr, value in self.character['attributes'].items():
            print(f"{attr}: {value}")
        print("\nEquipment:")
        for item in self.character['equipment']:
            print(f"- {item['name']}")
        print("\nSpells:")
        for spell in self.character['spells']:
            print(f"- {spell['name']}")
        # Display abilities and other progression-related information