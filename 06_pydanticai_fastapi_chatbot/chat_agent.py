from pydantic_ai import Agent
from dotenv import load_dotenv
from constant import MODEL_SMALL, MODEL_MEDIUM, MODEL_LARGE

#override eventual cahching
load_dotenv(override=True)
agent = Agent(model=MODEL_SMALL,
               system_prompt="Be a joking programming nerd, always answer with a programming joke. ALso add in some emoji to make it funnie",
               retries=1
               )

