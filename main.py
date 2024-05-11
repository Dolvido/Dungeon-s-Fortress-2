import os
from langchain.llms import OpenAI
from game.character.character_creation import CharacterCreation
from game.character.character_progression import CharacterProgression
from game.character.character_customization import CharacterCustomization
from game.world.world_generation import WorldGenerator
from game.world.dungeon_generation import DungeonGenerator
from game.world.fortress_generation import FortressGenerator
from game.gameplay.exploration import ExplorationHandler
from game.gameplay.combat import CombatHandler
from game.gameplay.puzzles import PuzzleGenerator
from game.gameplay.resource_management import ResourceManager
from game.dialogue.dialogue_system import DialogueSystem
from game.dialogue.npc_interaction import NPCInteraction
from game.dialogue.player_choices import PlayerChoices
from game.storytelling.quest_generation import QuestGenerator
from game.storytelling.event_generation import EventGenerator
from game.storytelling.narrative_adaptation import NarrativeAdapter

def main():
    # Initialize game components
    character_creation = CharacterCreation()
    character_progression = CharacterProgression(character_creation.create_character())
    character_customization = CharacterCustomization(character_progression.character)
    world_generator = WorldGenerator()
    dungeon_generator = DungeonGenerator()
    fortress_generator = FortressGenerator()
    exploration_handler = ExplorationHandler()
    combat_handler = CombatHandler()
    puzzle_generator = PuzzleGenerator()
    resource_manager = ResourceManager()
    dialogue_system = DialogueSystem()
    npc_interaction = NPCInteraction()
    player_choices = PlayerChoices()
    quest_generator = QuestGenerator()
    event_generator = EventGenerator()
    narrative_adapter = NarrativeAdapter()

    # Game loop
    while True:
        # World generation
        world_generator.generate_world()

        # Dungeon and fortress generation
        dungeon_generator.generate_dungeon("The Cursed Catacombs")
        fortress_generator.generate_fortress("Fortress of the Forgotten")

        # Exploration
        exploration_handler.handle_exploration("dense forest", "search for hidden ruins")

        # Combat
        combat_handler.handle_combat("goblin warriors", "attack with sword", "dodge and counterattack")

        # Puzzles
        puzzle_generator.generate_puzzle("riddle")

        # Resource management
        resource_manager.generate_resource("item", "Healing Potion")

        # Dialogue and NPC interaction
        dialogue_system.engage_in_dialogue("Mysterious Stranger")
        npc_interaction.interact_with_npc("Wise Old Sage")

        # Player choices
        context = "The player encounters a fork in the road, leading to two different paths."
        player_choice, choice_outcome = player_choices.present_choices(context)

        # Quest generation
        quest_generator.generate_quest("The player receives a mysterious letter from an old friend.")

        # Event generation
        event_generator.generate_event("The player stumbles upon an ancient ruins deep in the forest.")

        # Narrative adaptation
        player_context = "The player has completed the main quest and saved the kingdom from the evil sorcerer."
        game_events = "The player's actions have brought peace and prosperity to the land."
        adapted_narrative = narrative_adapter.generate_adapted_narrative(player_context, player_choice, game_events)
        print(f"\nAdapted Narrative:\n{adapted_narrative}")

        # Check if the player wants to continue or quit the game
        choice = input("\nDo you want to continue playing? (yes/no): ")
        if choice.lower() != "yes":
            break

    print("Thank you for playing Dungeon's Fortress!")

if __name__ == "__main__":
    main()