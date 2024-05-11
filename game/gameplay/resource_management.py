from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.data_loading import load_data

class ResourceManager:
    def __init__(self):
        self.llm = OpenAI(openai_api_key=api_key)
        self.world_history = load_data("data/lore/world_history.txt")
        self.items = load_data("data/resources/items.txt")
        self.equipment = load_data("data/resources/equipment.txt")
        self.spells = load_data("data/resources/spells.txt")

    def generate_resource_description(self, resource_type, resource_name):
        prompt = PromptTemplate(
            input_variables=["world_history", "resource_type", "resource_name"],
            template="""
            Given the following world history:
            {world_history}

            Generate a detailed and immersive description of a {resource_type} called {resource_name}. Include details about its appearance, properties, and potential uses within the game world. The description should create a sense of value and importance for the player.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        resource_description = chain.run(world_history=self.world_history, resource_type=resource_type, resource_name=resource_name)
        return resource_description

    def generate_crafting_recipe(self, item_name):
        prompt = PromptTemplate(
            input_variables=["world_history", "item_name"],
            template="""
            Given the following world history:
            {world_history}

            Generate a crafting recipe for an item called {item_name}. Include the required resources, their quantities, and a step-by-step guide on how to craft the item. The recipe should be clear, concise, and consistent with the game world's lore and mechanics.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        crafting_recipe = chain.run(world_history=self.world_history, item_name=item_name)
        return crafting_recipe

    def generate_resource_effect(self, resource_name):
        prompt = PromptTemplate(
            input_variables=["world_history", "resource_name"],
            template="""
            Given the following world history:
            {world_history}

            Generate a description of the effect or benefit of using the resource called {resource_name}. The effect should be meaningful and impactful within the game world, such as enhancing character abilities, providing temporary buffs, or unlocking new possibilities. The description should create a sense of excitement and motivation for the player to acquire and utilize the resource.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        resource_effect = chain.run(world_history=self.world_history, resource_name=resource_name)
        return resource_effect

    def generate_resource(self, resource_type, resource_name):
        resource_description = self.generate_resource_description(resource_type, resource_name)
        print(f"\n{resource_name} ({resource_type}) Description:")
        print(resource_description)

        if resource_type == "item":
            crafting_recipe = self.generate_crafting_recipe(resource_name)
            print(f"\nCrafting Recipe for {resource_name}:")
            print(crafting_recipe)

        resource_effect = self.generate_resource_effect(resource_name)
        print(f"\nEffect of {resource_name}:")
        print(resource_effect)