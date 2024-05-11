from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.data_loading import load_data

class DungeonGenerator:
    def __init__(self):
        self.llm = Ollama(model="llama3")
        self.world_history = load_data("data/lore/world_history.txt")

    def generate_dungeon_description(self, dungeon_name):
        prompt = PromptTemplate(
            input_variables=["world_history", "dungeon_name"],
            template="""
            Given the following world history:
            {world_history}

            Generate a detailed and immersive description of the {dungeon_name} dungeon, including its layout, architecture, atmosphere, and any notable features or inhabitants. The description should create a sense of mystery and danger, enticing players to explore the dungeon.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        dungeon_description = chain.run(world_history=self.world_history, dungeon_name=dungeon_name)
        return dungeon_description

    def generate_room_description(self, room_type):
        prompt = PromptTemplate(
            input_variables=["world_history", "room_type"],
            template="""
            Given the following world history:
            {world_history}

            Generate a vivid and immersive description of a {room_type} room within a dungeon. Include details about the room's appearance, any notable objects or features, and potential challenges or encounters players might face. The description should create a sense of excitement and anticipation for players.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        room_description = chain.run(world_history=self.world_history, room_type=room_type)
        return room_description

    def generate_encounter_description(self, encounter_type):
        prompt = PromptTemplate(
            input_variables=["world_history", "encounter_type"],
            template="""
            Given the following world history:
            {world_history}

            Generate an engaging and challenging description of a {encounter_type} encounter that players might face within a dungeon. Include details about the encounter's setup, the enemies or obstacles involved, and the potential rewards or consequences. The description should create a sense of tension and require strategic thinking from players.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        encounter_description = chain.run(world_history=self.world_history, encounter_type=encounter_type)
        return encounter_description

    def generate_dungeon(self, dungeon_name):
        dungeon_description = self.generate_dungeon_description(dungeon_name)
        print(f"\n{dungeon_name} Description:")
        print(dungeon_description)

        room_types = ["entrance", "corridor", "chamber", "treasure room", "boss room"]
        for room_type in room_types:
            room_description = self.generate_room_description(room_type)
            print(f"\n{room_type.capitalize()} Room Description:")
            print(room_description)

        encounter_types = ["trap", "puzzle", "combat", "boss fight"]
        for encounter_type in encounter_types:
            encounter_description = self.generate_encounter_description(encounter_type)
            print(f"\n{encounter_type.capitalize()} Encounter Description:")
            print(encounter_description)