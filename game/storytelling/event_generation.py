from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.data_loading import load_data

class EventGenerator:
    def __init__(self):
        self.llm = Ollama(model="llama3")
        self.world_history = load_data("data/lore/world_history.txt")

    def generate_event_prompt(self, player_context):
        prompt = PromptTemplate(
            input_variables=["world_history", "player_context"],
            template="""
            Given the following world history:
            {world_history}

            And the current player context:
            {player_context}

            Generate a compelling and contextually relevant event prompt that could occur in the game world. The event should be based on the player's actions, choices, and current state, and should introduce an unexpected or challenging situation that requires the player's attention and decision-making. The event should also tie into the larger narrative and world-building elements of the game.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        event_prompt = chain.run(world_history=self.world_history, player_context=player_context)
        return event_prompt

    def generate_event_details(self, event_prompt):
        prompt = PromptTemplate(
            input_variables=["world_history", "event_prompt"],
            template="""
            Given the following world history:
            {world_history}

            And the event prompt:
            {event_prompt}

            Generate detailed information about the event, including:
            1. Event Description: A vivid and immersive description of the event, including any notable characters, locations, or objects involved.
            2. Event Choices: A list of 2-3 meaningful choices the player can make in response to the event, each with potential consequences.
            3. Event Consequences: A brief description of the potential outcomes and consequences of each choice the player can make.
            4. Event Narrative: A short narrative that sets the context and stakes for the event, tying it into the larger game world and story.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        event_details = chain.run(world_history=self.world_history, event_prompt=event_prompt)
        return event_details

    def generate_event_outcome(self, event_details, player_choice):
        prompt = PromptTemplate(
            input_variables=["world_history", "event_details", "player_choice"],
            template="""
            Given the following world history:
            {world_history}

            And the event details:
            {event_details}

            And the player's choice:
            {player_choice}

            Generate a detailed description of the outcome and consequences of the player's choice in response to the event. Consider how the choice impacts the game world, narrative, and character progression. Provide a clear and compelling resolution to the event based on the player's decision.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        event_outcome = chain.run(world_history=self.world_history, event_details=event_details, player_choice=player_choice)
        return event_outcome

    def generate_event(self, player_context):
        event_prompt = self.generate_event_prompt(player_context)
        print(f"\nEvent Prompt:\n{event_prompt}")

        event_details = self.generate_event_details(event_prompt)
        print(f"\nEvent Details:\n{event_details}")

        player_choice = input("\nEnter your choice: ")

        event_outcome = self.generate_event_outcome(event_details, player_choice)
        print(f"\nEvent Outcome:\n{event_outcome}")