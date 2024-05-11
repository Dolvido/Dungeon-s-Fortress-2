from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.data_loading import load_data

class FortressGenerator:
    def __init__(self):
        self.llm = OpenAI(openai_api_key=api_key)
        self.world_history = load_data("data/lore/world_history.txt")

    def generate_fortress_description(self, fortress_name):
        prompt = PromptTemplate(
            input_variables=["world_history", "fortress_name"],
            template="""
            Given the following world history:
            {world_history}

            Generate a detailed and immersive description of the {fortress_name} fortress, including its location, architecture, defenses, and any notable features or inhabitants. The description should create a sense of grandeur and intrigue, making players want to explore and conquer the fortress.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        fortress_description = chain.run(world_history=self.world_history, fortress_name=fortress_name)
        return fortress_description

    def generate_area_description(self, area_type):
        prompt = PromptTemplate(
            input_variables=["world_history", "area_type"],
            template="""
            Given the following world history:
            {world_history}

            Generate a vivid and immersive description of a {area_type} area within a fortress. Include details about the area's appearance, any notable objects or features, and potential challenges or encounters players might face. The description should create a sense of excitement and anticipation for players.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        area_description = chain.run(world_history=self.world_history, area_type=area_type)
        return area_description

    def generate_npc_description(self, npc_type):
        prompt = PromptTemplate(
            input_variables=["world_history", "npc_type"],
            template="""
            Given the following world history:
            {world_history}

            Generate an intriguing and detailed description of a {npc_type} NPC that players might encounter within a fortress. Include details about the NPC's appearance, personality, role, and any potential interactions or quests they might offer. The description should make players want to engage with the NPC and learn more about their story.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        npc_description = chain.run(world_history=self.world_history, npc_type=npc_type)
        return npc_description

    def generate_fortress(self, fortress_name):
        fortress_description = self.generate_fortress_description(fortress_name)
        print(f"\n{fortress_name} Description:")
        print(fortress_description)

        area_types = ["gatehouse", "courtyard", "keep", "barracks", "throne room"]
        for area_type in area_types:
            area_description = self.generate_area_description(area_type)
            print(f"\n{area_type.capitalize()} Area Description:")
            print(area_description)

        npc_types = ["guard", "servant", "noble", "prisoner", "merchant"]
        for npc_type in npc_types:
            npc_description = self.generate_npc_description(npc_type)
            print(f"\n{npc_type.capitalize()} NPC Description:")
            print(npc_description)