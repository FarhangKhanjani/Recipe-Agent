import json
import os
import sys
from .agent import root_agent, get_recipe_from_ingredients

def main():
    """
    Main entry point for running the agent via proxy.
    Reads agent input from environment variable and prints result to stdout.
    """
    # Get input from environment variable
    agent_input = os.environ.get('AGENT_INPUT')
    if not agent_input:
        print(json.dumps({"error": "No input provided"}))
        return
    
    try:
        # Parse input
        input_data = json.loads(agent_input)
        
        # Check for ingredients in the input data
        if 'ingredients' in input_data:
            ingredients = input_data['ingredients']
            # Use the get_recipe_from_ingredients function
            recipe = get_recipe_from_ingredients(ingredients)
            print(json.dumps(recipe))
        else:
            # If no specific ingredients, use the root agent
            response = root_agent.process(input_data.get('prompt', ''))
            print(json.dumps({"response": response}))
            
    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    main() 