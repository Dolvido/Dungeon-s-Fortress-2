from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.data_loading import load_data

class WorldGenerator:
    def __init__(self):
        self.llm = Ollama(model="llama3")
        self.world_history = load_data("data/lore/world_history.txt")

    def generate_world_description(self):
        prompt = PromptTemplate(
            input_variables=["world_history"],
            template="""
            Given the following world history:
            {world_history}

            Generate a detailed and immersive description of the fantasy world, including its geography, nations, cultures, and notable landmarks. The description should be engaging and provide a sense of the world's richness and depth.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        world_description = chain.run(world_history=self.world_history)
        return world_description

    def generate_faction_description(self, faction_name):
        prompt = PromptTemplate(
            input_variables=["world_history", "faction_name"],
            template="""
            Given the following world history:
            {world_history}

            Generate a detailed description of the {faction_name} faction, including their culture, beliefs, goals, and relationship with other factions in the world. The description should provide a clear understanding of the faction's role and significance in the world.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        faction_description = chain.run(world_history=self.world_history, faction_name=faction_name)
        return faction_description

    def generate_region_description(self, region_name):
        prompt = PromptTemplate(
            input_variables=["world_history", "region_name"],
            template="""
            Given the following world history:
            {world_history}
           Generate a vivid and immersive description of the {region_name} region, including its landscapes, climate, flora, fauna, and any notable settlements or points of interest. The description should paint a picture of the region and its unique characteristics.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        region_description = chain.run(world_history=self.world_history, region_name=region_name)
        return region_description

    def generate_world(self):
        world_description = self.generate_world_description()
        print("World Description:")
        print(world_description)

        factions = ["Human Empire", "Elven Kingdom", "Dwarven Clans", "Orcish Horde"]
        for faction in factions:
            faction_description = self.generate_faction_description(faction)
            print(f"\n{faction} Description:")
            print(faction_description)

        regions = ["Frostpeak Mountains", "Whispering Forests", "Scorched Deserts", "Misty Isles"]
        for region in regions:
            region_description = self.generate_region_description(region)
            print(f"\n{region} Description:")
            print(region_description)