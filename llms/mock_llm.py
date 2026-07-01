import json

def mock_llm_json_response(prompt: str) -> str:
    """
    Simulates a response from a language model based on the provided prompt.

    Args:
        prompt (str): The input prompt for which the language model should generate a response.

    Returns:
        str: The simulated response from the language model.
    """
    # Placeholder implementation - replace with actual LLM integration
    if any(keyword in prompt.lower() for keyword in ["weather", "temperature", "forecast"]):
        city = prompt.split("in")[-1].strip()  # Extract city from prompt
        
        return json.dumps({
            "tool_name": "get_weather",
            "args": {
                "location": city,
                "unit": "Celsius"  # Default unit for weather information
            }
        })
    
    elif any(keyword in prompt.lower() for keyword in ["calculate", "math", "compute"]):
        expression = prompt.split(maxsplit=2)[-1].strip()  # Extract expression from prompt
        
        return json.dumps({
            "tool_name": "calculator",
            "args": {
                "expression": expression
            }
        })
    
    elif any(keyword in prompt.lower() for keyword in ["search", "find", "lookup"]):
        query = prompt.split(maxsplit=2)[-1].strip()  # Extract search query from prompt
        
        return json.dumps({
            "tool_name": "web_search",
            "args": {
                "query": query
            }
        })
    
    elif any(keyword in prompt.lower() for keyword in ["summarize", "summary", "condense"]):
        text = prompt.split(maxsplit=1)[-1].strip()  # Extract text to summarize from prompt
        
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
    

def mock_llm_tool_response(tool_name: str, result: str) -> str: 
    """
    Simulates a response from a language model after executing a tool.

    Args:
        tool_name (str): The name of the tool that was executed.
        result (str): The result returned by the executed tool.

    Returns:
        str: The simulated response from the language model.
    """
    responses = {
        "calculator":
            lambda r: f"The result of your calculation is: {r}.",

        "web_search": 
            lambda r: (
                f"Here are the search results for your query:\n\n"
                + "\n".join([f"- {item}" for item in r]),
            ),

        "text_summarizer": 
            lambda r: (
                f"Here is the summary of the text:\n\n{r}",
            ),
            
        "get_weather": 
            lambda r: (
                f"Here is the weather information for your location:\n\n"
                f"{r['temperature']} with {r['condition']} conditions." 
                f"The humidity is {r['humidity']}% and the wind speed is {r['wind_speed']} km/h.",
            )
    }

    formatter = responses.get(
        tool_name, 
        lambda r: f"Tool '{tool_name}' executed successfully with result: {r}."
    )
    return f"LLM Response: {formatter(result)}"