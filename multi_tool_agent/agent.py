import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent



RECIPE_MAKER_AGENT = Agent(
        model = "gemini-2.0-flash",
        name="recipe_maker_agent",
        instruction="""
            You are a recipe generator agent.

            Input: A list of ingredients (only ingredients, no quantities or steps).
    
            Your task: Based only on the provided ingredients, write a full and realistic cooking recipe, including:
            A short title for the dish.
            Step-by-step instructions on how to prepare and cook the dish.
            Mention the use of all ingredients naturally during the instructions.

            Rules:
            Do not ask for missing ingredients.
            Do not invent extra ingredients not given.
            You may creatively assume basic things (like water, salt, pepper, oil) are available if necessary.
            Make sure the recipe is clear, easy to follow, and logical.

            Tone: Friendly, clear, and practical.""",

        description="Handles providing a recipe based on a list of ingredients.", # Crucial for delegation  
        tools=[],
    )


root_agent = Agent(
    name="recipe_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the recipe."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the recipe."
    ),
    tools=[],
    sub_agents=[RECIPE_MAKER_AGENT],    
)