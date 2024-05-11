import os
from utils.data_loading import load_data

class CharacterCustomization:
    def __init__(self, character):
        self.character = character
        self.skills = load_data(os.path.join("data", "lore", "skills.txt"))

    def customize_attributes(self):
        print("\nCharacter Attribute Customization:")
        print("You have 10 points to distribute among your attributes.")

        attributes = self.character['attributes']
        points_to_distribute = 10

        while points_to_distribute > 0:
            print(f"\nPoints remaining: {points_to_distribute}")
            print("Current Attributes:")
            for attr, value in attributes.items():
                print(f"{attr}: {value}")

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

        self.character['attributes'] = attributes
        print("\nAttribute customization complete.")

    def customize_skills(self):
        print("\nCharacter Skill Customization:")
        print("You have 5 skill points to distribute.")

        skill_points = 5
        selected_skills = []

        while skill_points > 0:
            print(f"\nSkill points remaining: {skill_points}")
            print("Available Skills:")
            for i, skill in enumerate(self.skills, 1):
                print(f"{i}. {skill['name']}")

            skill_choice = int(input("Enter the number corresponding to the skill you want to learn: "))
            if 1 <= skill_choice <= len(self.skills):
                selected_skill = self.skills[skill_choice - 1]
                if selected_skill not in selected_skills:
                    selected_skills.append(selected_skill)
                    skill_points -= 1
                else:
                    print("You have already selected that skill.")
            else:
                print("Invalid skill choice. Please try again.")

        self.character['skills'] = selected_skills
        print("\nSkill customization complete.")

    def display_customized_character(self):
        print("\nCustomized Character:")
        print(f"Race: {self.character['race']}")
        print(f"Class: {self.character['class']}")

        print("\nAttributes:")
        for attr, value in self.character['attributes'].items():
            print(f"{attr}: {value}")

        print("\nSkills:")
        for skill in self.character['skills']:
            print(f"- {skill['name']}: {skill['description']}")

    def customize_character(self):
        self.customize_attributes()
        self.customize_skills()
        self.display_customized_character()