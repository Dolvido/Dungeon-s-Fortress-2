import os
from utils.data_loading import load_data

class CharacterCreation:
    def __init__(self):
        self.races = load_data(os.path.join("data", "lore", "races.txt"))
        self.classes = load_data(os.path.join("data", "lore", "classes.txt"))

    def create_character(self):
        print("Welcome to Dungeon's Fortress!")
        print("Let's create your character.")

        # Choose race
        print("\nAvailable Races:")
        for i, race in enumerate(self.races, 1):
            print(f"{i}. {race['name']}")

        race_choice = int(input("Enter the number corresponding to your chosen race: "))
        selected_race = self.races[race_choice - 1]
        print(f"You have chosen the {selected_race['name']} race.")
        print(selected_race['description'])

        # Choose class
        print("\nAvailable Classes:")
        for i, cls in enumerate(self.classes, 1):
            print(f"{i}. {cls['name']}")

        class_choice = int(input("Enter the number corresponding to your chosen class: "))
        selected_class = self.classes[class_choice - 1]
        print(f"You have chosen the {selected_class['name']} class.")
        print(selected_class['description'])

        # Customize attributes
        attributes = selected_race['attributes'].copy()
        attributes.update(selected_class['attributes'])
        print("\nCharacter Attributes:")
        for attr, value in attributes.items():
            print(f"{attr}: {value}")

        print("\nYou can now distribute additional attribute points.")
        points_to_distribute = 5
        while points_to_distribute > 0:
            print(f"\nPoints remaining: {points_to_distribute}")
            attr_choice = input("Enter the attribute you want to increase (e.g., strength): ")
            if attr_choice in attributes:
                points = int(input("Enter the number of points to allocate: "))
                if points <= points_to_distribute:
                    attributes[attr_choice] += points
                    points_to_distribute -= points
                else:
                    print("Invalid number of points. Please try again.")
            else:
                print("Invalid attribute. Please try again.")

        print("\nFinal Character Attributes:")
        for attr, value in attributes.items():
            print(f"{attr}: {value}")

        # Create character object
        character = {
            'race': selected_race['name'],
            'class': selected_class['name'],
            'attributes': attributes
        }

        print("\nCharacter creation complete!")
        return character