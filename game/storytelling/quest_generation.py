from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.data_loading import load_data

class QuestGenerator:
    def __init__(self):
        self.llm = Ollama(model="llama3")
        self.world_history = load_data("data/lore/world_history.txt")

    def generate_quest_prompt(self, player_context):
        prompt = PromptTemplate(
            input_variables=["world_history", "player_context"],
            template="""
            Given the following world history:
            {world_history}

            And the current player context:
            {player_context}

            Generate a compelling and contextually relevant quest prompt for the player. The quest should align with the player's goals, abilities, and progression level. It should present a clear objective, challenges to overcome, and potential rewards upon completion. The quest should also tie into the larger narrative and world-building elements of the game.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        quest_prompt = chain.run(world_history=self.world_history, player_context=player_context)
        return quest_prompt

    def generate_quest_details(self, quest_prompt):
        prompt = PromptTemplate(
            input_variables=["world_history", "quest_prompt"],
            template="""
            Given the following world history:
            {world_history}

            And the quest prompt:
            {quest_prompt}

            Generate detailed information about the quest, including:
            1. Quest Objectives: A clear and concise list of goals the player must achieve to complete the quest.
            2. Quest Challenges: Descriptions of the obstacles, enemies, or puzzles the player will face during the quest.
            3. Quest Rewards: A list of items, experience points, or other benefits the player will receive upon completing the quest.
            4. Quest Narrative: A brief narrative that sets the context and motivation for the quest, tying it into the larger game world and story.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        quest_details = chain.run(world_history=self.world_history, quest_prompt=quest_prompt)
        return quest_details

    def generate_quest_update(self, quest_details, player_actions):
        prompt = PromptTemplate(
            input_variables=["world_history", "quest_details", "player_actions"],
            template="""
            Given the following world history:
            {world_history}

            And the quest details:
            {quest_details}

            And the player's actions:
            {player_actions}

            Generate an update on the quest status based on the player's actions. Determine if the player has made progress towards completing the quest objectives, encountered any new challenges or surprises, or triggered any significant events. Provide a brief summary of the quest update and any relevant changes to the game state.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        quest_update = chain.run(world_history=self.world_history, quest_details=quest_details, player_actions=player_actions)
        return quest_update

    def generate_quest(self, player_context):
        quest_prompt = self.generate_quest_prompt(player_context)
        print(f"\nQuest Prompt:\n{quest_prompt}")

        quest_details = self.generate_quest_details(quest_prompt)
        print(f"\nQuest Details:\n{quest_details}")

        player_actions = ""
        while True:
            action = input("\nEnter your action (or 'complete' to finish the quest): ")
            if action.lower() == 'complete':
                break
            player_actions += f"{action}\n"

            quest_update = self.generate_quest_update(quest_details, player_actions)
            print(f"\nQuest Update:\n{quest_update}")

        print("\nQuest completed!")