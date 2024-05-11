from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.data_loading import load_data

class PlayerChoices:
    def __init__(self):
        self.llm = Ollama(model="llama3")
        self.world_history = load_data("data/lore/world_history.txt")
        self.player_choices_data = load_data("data/dialogues/player_choices.txt")

    def generate_choices(self, context):
        prompt = PromptTemplate(
            input_variables=["world_history", "context"],
            template="""
            Given the following world history:
            {world_history}

            And the current context:
            {context}

            Generate a list of 3-4 meaningful and contextually relevant choices for the player to decide from. Each choice should be distinct, align with the player's potential goals or motivations, and have consequences that shape the narrative and game world. Provide a brief description of each choice.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        generated_choices = chain.run(world_history=self.world_history, context=context)
        return generated_choices

    def evaluate_choice(self, choice, context):
        prompt = PromptTemplate(
            input_variables=["world_history", "choice", "context"],
            template="""
            Given the following world history:
            {world_history}

            And the current context:
            {context}

            The player has chosen the following option:
            {choice}

            Evaluate the consequences and impact of this choice on the game world, narrative, and character progression. Consider how it aligns with the player's goals, affects relationships with NPCs, and shapes future events. Provide a detailed description of the outcome and any relevant updates to the game state.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        choice_evaluation = chain.run(world_history=self.world_history, choice=choice, context=context)
        return choice_evaluation

    def present_choices(self, context):
        generated_choices = self.generate_choices(context)
        print("\nPlayer Choices:")
        for i, choice in enumerate(generated_choices.split("\n"), start=1):
            print(f"{i}. {choice.strip()}")

        player_input = input("\nEnter your choice (1-4): ")
        selected_choice = generated_choices.split("\n")[int(player_input) - 1].strip()
        
        choice_outcome = self.evaluate_choice(selected_choice, context)
        print(f"\nChoice Outcome:\n{choice_outcome}")
        
        return selected_choice, choice_outcome