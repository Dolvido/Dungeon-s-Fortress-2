from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.data_loading import load_data

class NPCInteraction:
    def __init__(self, api_key):
        self.llm = Ollama(model="llama3")
        self.world_history = load_data("data/lore/world_history.txt")
        self.npc_dialogues = load_data("data/dialogues/npc_dialogues.txt")

    def generate_npc_response(self, npc_name, player_input, conversation_history):
        prompt = PromptTemplate(
            input_variables=["world_history", "npc_name", "player_input", "conversation_history"],
            template="""
            Given the following world history:
            {world_history}

            And the following conversation history with the NPC {npc_name}:
            {conversation_history}

            The player says: {player_input}

            Generate a coherent and contextually relevant response from the NPC. The response should be engaging, reflect the NPC's personality and knowledge, and address the player's input appropriately. Take into account any previous interactions or information from the conversation history.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        npc_response = chain.run(world_history=self.world_history, npc_name=npc_name, player_input=player_input, conversation_history=conversation_history)
        return npc_response

    def generate_npc_action(self, npc_name, conversation_history):
        prompt = PromptTemplate(
            input_variables=["world_history", "npc_name", "conversation_history"],
            template="""
            Given the following world history:
            {world_history}

            And the following conversation history with the NPC {npc_name}:
            {conversation_history}

            Generate a description of an action that the NPC takes based on the conversation. The action should be coherent, reflect the NPC's personality and goals, and be relevant to the context of the conversation. Consider any previous interactions or information from the conversation history.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        npc_action = chain.run(world_history=self.world_history, npc_name=npc_name, conversation_history=conversation_history)
        return npc_action

    def update_npc_state(self, npc_name, conversation_history):
        prompt = PromptTemplate(
            input_variables=["world_history", "npc_name", "conversation_history"],
            template="""
            Given the following world history:
            {world_history}

            And the following conversation history with the NPC {npc_name}:
            {conversation_history}

            Analyze the conversation history and update the NPC's state based on the interactions. Consider any changes in the NPC's attitude, knowledge, or relationship with the player. Provide a concise summary of the updated NPC state.
            """
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        npc_state_update = chain.run(world_history=self.world_history, npc_name=npc_name, conversation_history=conversation_history)
        return npc_state_update

    def interact_with_npc(self, npc_name):
        conversation_history = ""
        print(f"\nStarting interaction with {npc_name}...")

        while True:
            player_input = input("\nPlayer: ")
            conversation_history += f"Player: {player_input}\n"

            npc_response = self.generate_npc_response(npc_name, player_input, conversation_history)
            print(f"\n{npc_name}: {npc_response}")
            conversation_history += f"NPC: {npc_response}\n"

            npc_action = self.generate_npc_action(npc_name, conversation_history)
            print(f"\n{npc_name} {npc_action}")
            conversation_history += f"NPC Action: {npc_action}\n"

            npc_state_update = self.update_npc_state(npc_name, conversation_history)
            print(f"\nNPC State Update: {npc_state_update}")

            choice = input("\nDo you want to continue the interaction? (yes/no): ")
            if choice.lower() != "yes":
                break