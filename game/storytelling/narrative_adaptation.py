from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.data_loading import load_data

class NarrativeAdapter:
    def __init__(self):
        self.llm = Ollama(model="llama3")
        self.world_history = load_data("data/lore/world_history.txt")

    def adapt_narrative(self, player_context, player_choices, game_events):
        prompt = PromptTemplate(
            input_variables=["world_history", "player_context", "player_choices", "game_events"],
            template="""
            Given the following world history:
            {world_history}

            And the current player context:
            {player_context}

            And the player's choices:
            {player_choices}

            And the recent game events:
            {game_events}

            Generate a narrative adaptation that incorporates the player's choices and recent game events into the ongoing story. The adapted narrative should:
            1. Reflect the consequences of the player's choices and their impact on the game world and characters.
            2. Integrate the recent game events seamlessly into the narrative, ensuring coherence and consistency.
            3. Foreshadow potential future developments and challenges based on the player's actions and the current state of the game world.
            4. Maintain the overall tone, theme, and style of the game's narrative while adapting to the player's unique path.

            Provide a compelling and immersive narrative adaptation that engages the player and shapes the unfolding story.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        adapted_narrative = chain.run(world_history=self.world_history, player_context=player_context, player_choices=player_choices, game_events=game_events)
        return adapted_narrative

    def update_world_history(self, adapted_narrative):
        self.world_history += f"\n\n{adapted_narrative}"

    def generate_adapted_narrative(self, player_context, player_choices, game_events):
        adapted_narrative = self.adapt_narrative(player_context, player_choices, game_events)
        self.update_world_history(adapted_narrative)
        return adapted_narrative