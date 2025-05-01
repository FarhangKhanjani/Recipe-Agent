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

def get_recipe_from_ingredients(ingredients):
    """
    Generate a simple recipe using only the provided ingredients.
    
    Args:
        ingredients (list): A list of ingredient strings
        
    Returns:
        dict: A recipe dictionary containing title, ingredients, and instructions
    """
    # Ensure we have at least two ingredients
    if len(ingredients) < 2:
        raise ValueError("At least two ingredients are required to create a recipe")
    
    # Generate a simple title based on the main ingredients
    main_ingredients = ingredients[:3]  # Use up to 3 ingredients in the title
    title = " and ".join(main_ingredients).title() + " Recipe"
    
    # Format the ingredients list
    formatted_ingredients = [f"- {ingredient}" for ingredient in ingredients]
    
    # Create simple instructions
    instructions = [
        f"1. Prepare all {len(ingredients)} ingredients.",
        f"2. Combine {', '.join(ingredients[:-1])} in a bowl.",
        f"3. Add {ingredients[-1]} and mix well.",
        "4. Serve and enjoy!"
    ]
    
    return {
        "title": title,
        "ingredients": formatted_ingredients,
        "instructions": instructions
    }