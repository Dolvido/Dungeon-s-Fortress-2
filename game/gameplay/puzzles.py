from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.data_loading import load_data

class PuzzleGenerator:
    def __init__(self):
        self.llm = Ollama(model="llama3")
        self.world_history = load_data("data/lore/world_history.txt")

    def generate_puzzle_description(self, puzzle_type):
        prompt = PromptTemplate(
            input_variables=["world_history", "puzzle_type"],
            template="""
            Given the following world history:
            {world_history}

            Generate a detailed and engaging description of a {puzzle_type} puzzle that the player encounters in the game world. Include details about the puzzle's appearance, mechanics, and any clues or hints that may help the player solve it. The description should create a sense of intrigue and challenge for the player.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        puzzle_description = chain.run(world_history=self.world_history, puzzle_type=puzzle_type)
        return puzzle_description

    def generate_puzzle_solution(self, puzzle_description):
        prompt = PromptTemplate(
            input_variables=["world_history", "puzzle_description"],
            template="""
            Given the following world history:
            {world_history}

            And the following puzzle description:
            {puzzle_description}

            Generate a clear and concise solution to the puzzle. The solution should be logical and consistent with the puzzle's mechanics and any provided clues or hints. Avoid revealing the solution directly to the player.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        puzzle_solution = chain.run(world_history=self.world_history, puzzle_description=puzzle_description)
        return puzzle_solution

    def generate_puzzle_reward(self, puzzle_type):
        prompt = PromptTemplate(
            input_variables=["world_history", "puzzle_type"],
            template="""
            Given the following world history:
            {world_history}

            Generate a description of a suitable reward for solving a {puzzle_type} puzzle. The reward should be meaningful and valuable to the player, such as a unique item, a piece of lore, or a new ability. The description should create a sense of excitement and accomplishment for the player.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        puzzle_reward = chain.run(world_history=self.world_history, puzzle_type=puzzle_type)
        return puzzle_reward

    def generate_puzzle(self, puzzle_type):
        puzzle_description = self.generate_puzzle_description(puzzle_type)
        puzzle_solution = self.generate_puzzle_solution(puzzle_description)
        puzzle_reward = self.generate_puzzle_reward(puzzle_type)

        print(f"\n{puzzle_type.capitalize()} Puzzle:")
        print(puzzle_description)
        print(f"\nSolution (not revealed to the player): {puzzle_solution}")
        print(f"\nReward: {puzzle_reward}")