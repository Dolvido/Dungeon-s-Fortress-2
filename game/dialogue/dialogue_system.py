from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.data_loading import load_data

class DialogueSystem:
    def __init__(self):
        self.llm = Ollama(model="llama3")
        self.world_history = load_data("data/lore/world_history.txt")
        self.npc_dialogues = load_data("data/dialogues/npc_dialogues.txt")
        self.player_choices = load_data("data/dialogues/player_choices.txt")

    def generate_npc_dialogue(self, npc_name, conversation_history):
        prompt = PromptTemplate(
            input_variables=["world_history", "npc_name", "conversation_history"],
            template="""
            Given the following world history:
            {world_history}

            And the following conversation history with the NPC {npc_name}:
            {conversation_history}

            Generate a coherent and contextually relevant response from the NPC. The response should be engaging, reflect the NPC's personality and knowledge, and progress the conversation in a meaningful way. Take into account any choices or actions made by the player in the conversation history.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        npc_response = chain.run(world_history=self.world_history, npc_name=npc_name, conversation_history=conversation_history)
        return npc_response

    def generate_player_choices(self, npc_name, conversation_history):
        prompt = PromptTemplate(
            input_variables=["world_history", "npc_name", "conversation_history"],
            template="""
            Given the following world history:
            {world_history}

            And the following conversation history with the NPC {npc_name}:
            {conversation_history}

            Generate a list of 3-4 coherent and contextually relevant choices for the player to respond with. Each choice should be distinct, reflect the player's potential intentions or goals, and progress the conversation in a different direction. Consider the NPC's personality and the conversation history when generating the choices.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        player_choices = chain.run(world_history=self.world_history, npc_name=npc_name, conversation_history=conversation_history)
        return player_choices

    def update_world_state(self, conversation_history):
        prompt = PromptTemplate(
            input_variables=["world_history", "conversation_history"],
            template="""
            Given the following world history:
            {world_history}

            And the following conversation history:
            {conversation_history}

            Analyze the conversation history and identify any key information, events, or decisions that should be updated in the world state. Provide a concise summary of the updates, focusing on the most relevant and impactful elements that will shape the game world and future interactions.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        world_state_update = chain.run(world_history=self.world_history, conversation_history=conversation_history)
        return world_state_update

    def engage_in_dialogue(self, npc_name):
        conversation_history = ""
        print(f"\nStarting conversation with {npc_name}...")

        while True:
            npc_response = self.generate_npc_dialogue(npc_name, conversation_history)
            print(f"\n{npc_name}: {npc_response}")
            conversation_history += f"\nNPC: {npc_response}\n"

            player_choices = self.generate_player_choices(npc_name, conversation_history)
            print("Player choices:")
            for i, choice in enumerate(player_choices.split("\n"), start=1):
                print(f"{i}. {choice.strip()}")

            player_input = input("\nEnter your choice (1-4) or 'quit' to end the conversation: ")
            if player_input.lower() == "quit":
                break

            player_choice = player_choices.split("\n")[int(player_input) - 1].strip()
            print(f"\nPlayer: {player_choice}")
            conversation_history += f"Player: {player_choice}\n"

        world_state_update = self.update_world_state(conversation_history)
        print("\nWorld State Update:")
        print(world_state_update)