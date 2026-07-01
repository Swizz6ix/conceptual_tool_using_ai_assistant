import json

from utilities.extract_text import extract_text_from_prompt
from utilities.extract_query import extract_query_from_prompt
from utilities.extract_expression import extract_expression_from_prompt
from utilities.extract_location import extract_location_from_prompt
from utilities.extract_expression import math_confidence_check

def mock_llm_json_response(prompt: str) -> str:
    """
    Simulates a response from a language model based on the provided prompt.

    Args:
        prompt (str): The input prompt for which the language model should generate a response.

    Returns:
        str: The simulated response from the language model.
    """

    prompt_lower = prompt.lower()
    if any(keyword in prompt_lower for keyword in ["weather", "temperature", "forecast"]):
        city = extract_location_from_prompt(prompt_lower)  # Extract city from prompt
        
        return json.dumps({
            "tool_name": "get_weather",
            "args": {
                "location": city,
                "unit": "Celsius"  # Default unit for weather information
            }
        })
    
    elif math_confidence_check(prompt_lower) >= 3:  # Check if the prompt is likely a math expression
        expression = extract_expression_from_prompt(prompt_lower)  # Extract expression from prompt

        return json.dumps({
            "tool_name": "calculator",
            "args": {
                "expression": expression
            }
        })
    
    elif any(keyword in prompt_lower for keyword in ["search", "find", "lookup"]):
        print(f"\n[LLM Prompt===>]: {prompt_lower}")
        query = extract_query_from_prompt(prompt_lower)  # Extract search query from prompt

        return json.dumps({
            "tool_name": "web_search",
            "args": {
                "query": query
            }
        })
    
    elif any(keyword in prompt_lower for keyword in ["summarize", "summary", "condense"]):
        text = extract_text_from_prompt(prompt_lower)  # Extract text to summarize from prompt

        return json.dumps({
            "tool_name": "text_summarizer",
            "args": {
                "text": text
            }
        })
    else:
        return json.dumps({
            "tool_name": "unknown",
            "args": {
                "prompt": prompt
            }
        })
    

def mock_llm_tool_response(tool_name: str, result: str, user_name: str) -> str: 
    """
    Simulates a response from a language model after executing a tool.

    Args:
        tool_name (str): The name of the tool that was executed.
        result (str): The result returned by the executed tool.
        user_name (str): The name of the user.

    Returns:
        str: The simulated response from the language model.
    """
    responses = {
        "calculator":
            lambda r: f"{user_name}, the result of your calculation is: {r}.",

        "web_search": 
            lambda r: (
                f"{user_name}, here are the search results for your query:\n\n"
                + "\n".join([f"- {item}" for item in r]),
            ),

        "text_summarizer": 
            lambda r: (
                f"{user_name}, here is the summary of the text:\n\n{r}",
            ),
            
        "get_weather": 
            lambda r: (
                f"{user_name}, here is the weather information in {r['location']}:\n\n"
                f"{r['temperature']} with {r['conditions']} conditions." 
                f"The humidity is {r['humidity']}% and the wind speed is {r['wind_speed']} km/h.",
            )
    }

    formatter = responses.get(
        tool_name, 
        lambda r: f"Dear {user_name}, Tool '{tool_name}' executed successfully with result:\n{r}."
    )
    return f"LLM Response: {formatter(result)}"