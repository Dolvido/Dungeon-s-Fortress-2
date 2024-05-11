from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.data_loading import load_data

class CombatHandler:
    def __init__(self):
        self.llm = Ollama(model="llama3")
        self.world_history = load_data("data/lore/world_history.txt")

    def generate_enemy_description(self, enemy_type):
        prompt = PromptTemplate(
            input_variables=["world_history", "enemy_type"],
            template="""
            Given the following world history:
            {world_history}

            Generate a detailed and immersive description of a {enemy_type} enemy that the player encounters in combat. Include details about the enemy's appearance, abilities, and any notable characteristics. The description should create a sense of challenge and excitement for the player.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        enemy_description = chain.run(world_history=self.world_history, enemy_type=enemy_type)
        return enemy_description

    def generate_combat_result(self, player_action, enemy_action):
        prompt = PromptTemplate(
            input_variables=["world_history", "player_action", "enemy_action"],
            template="""
            Given the following world history:
            {world_history}

            In the current combat encounter, the player takes the following action:
            {player_action}

            The enemy responds with the following action:
            {enemy_action}

            Generate a detailed and engaging description of the combat result, including the consequences of the player's action and the enemy's response. The result should be balanced and provide a sense of progress or challenge for the player.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        combat_result = chain.run(world_history=self.world_history, player_action=player_action, enemy_action=enemy_action)
        return combat_result

    def handle_combat(self, enemy_type, player_action, enemy_action):
        enemy_description = self.generate_enemy_description(enemy_type)
        print(f"\nEncountering {enemy_type.capitalize()} Enemy:")
        print(enemy_description)

        combat_result = self.generate_combat_result(player_action, enemy_action)
        print(f"\nCombat Result:")
        print(f"Player Action: {player_action}")
        print(f"Enemy Action: {enemy_action}")
        print(combat_result)