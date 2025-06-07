# pip install openai-agents
# pip install python-dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
print(gemini_api_key)
# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Translator Agent
translator = Agent(
    name = 'translator agent',
    instructions = 
    """You are a translator agent. Translate from Urdu language to English language.""" 
)

print("Welcome to the Urdu-to-English Translator!")
print("Type 'exit' to quit.\n")

# Initiating the loop
while True:
    user_input = input("Enter an Urdu sentence to translate: ")

    # Exit condition
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting translator. Goodbye!")
        break

    # Run the translation
    response = Runner.run_sync(
        translator,
        input=user_input,
        run_config=config
    )

    # Show translation
    print(response.final_output)