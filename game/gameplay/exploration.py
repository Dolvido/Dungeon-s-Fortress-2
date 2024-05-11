from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.data_loading import load_data

class ExplorationHandler:
    def __init__(self, api_key):
        self.llm = Ollama(model="llama3")
        self.world_history = load_data("data/lore/world_history.txt")

    def generate_area_description(self, area_type):
        prompt = PromptTemplate(
            input_variables=["world_history", "area_type"],
            template="""
            Given the following world history:
            {world_history}

            Generate a vivid and immersive description of a {area_type} area that the player is exploring. Include details about the area's appearance, notable features, and any potential points of interest or interactable objects. The description should create a sense of atmosphere and encourage the player to investigate further.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        area_description = chain.run(world_history=self.world_history, area_type=area_type)
        return area_description

    def generate_exploration_result(self, player_action):
        prompt = PromptTemplate(
            input_variables=["world_history", "player_action"],
            template="""
            Given the following world history:
            {world_history}

            The player takes the following action during exploration:
            {player_action}

            Generate a descriptive and engaging result of the player's action, including any discoveries, encounters, or consequences. The result should be coherent with the game world and provide a sense of progress or revelation to the player.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        exploration_result = chain.run(world_history=self.world_history, player_action=player_action)
        return exploration_result

    def handle_exploration(self, area_type, player_action):
        area_description = self.generate_area_description(area_type)
        print(f"\nExploring {area_type.capitalize()} Area:")
        print(area_description)

        exploration_result = self.generate_exploration_result(player_action)
        print(f"\nResult of Action: {player_action}")
        print(exploration_result)