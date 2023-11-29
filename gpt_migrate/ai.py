from langchain.chat_models import ChatOpenAI
from config import OPENAI_API_KEY
import os
import openai
from utils import parse_code_string

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

class AI:
    """A class representing an AI model for code generation and interaction.

    Attributes:
        temperature (float): Controls the randomness of the output.
        max_tokens (int): The maximum number of tokens to generate.
        model_name (str): The name of the model used for AI operations.
    """
    
    def __init__(self, model="gpt-4-32k", temperature=0.1, max_tokens=10000):
        """Initializes the AI object with the specified model, temperature, and token limit.
        
        Args:
            model (str, optional): The model name to initialize. Defaults to "gpt-4-32k".
            temperature (float, optional): Randomness of the output. Defaults to 0.1.
            max_tokens (int, optional): The maximum number of tokens to generate. Defaults to 10000.
        
        If the specified model is not available, it defaults to "gpt-3.5-turbo".
        """
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.model_name = model
        try:
            # check to see if model is available to user
            _ = ChatOpenAI(model_name=model)
        except Exception as e:
            print(e)
            self.model_name = "gpt-3.5-turbo"
    
    def write_code(self, prompt):
        """Generates code based on the provided prompt.
        
        Args:
            prompt (str): The prompt text to generate code for.
        
        Returns:
            A tuple that contains parsed code based on AI response or a string if instructions were provided.
        """
        message = [{"role": "user", "content": str(prompt)}]
        response = openai.ChatCompletion.create(
            messages=message,
            stream=False,
            model=self.model_name,
            max_tokens=self.max_tokens,
            temperature=self.temperature
        )
        if response["choices"][0]["message"]["content"].startswith("INSTRUCTIONS:"):
            # Return instructions if provided by the model
            return ("INSTRUCTIONS:", "", response["choices"][0]["message"]["content"][14:])
        else:
            # Parse and return generated code triples
            code_triples = parse_code_string(response["choices"][0]["message"]["content"])
            return code_triples

    def run(self, prompt):
        """Interacts with the AI based on the provided prompt in a chat-like fashion.
        
        Args:
            prompt (str): The prompt text for the AI to respond to.
        
        Returns:
            A string representing the AI's continuous chat responses.
        """
        message = [{"role": "user", "content": str(prompt)}]
        response = openai.ChatCompletion.create(
            messages=message,
            stream=True,
            model=self.model_name,
            max_tokens=self.max_tokens,
            temperature=self.temperature
        )
        chat = ""
        # Accumulate the content of each message chunk into chat
        for chunk in response:
            delta = chunk["choices"][0]["delta"]
            msg = delta.get("content", "")
            chat += msg
        return chat