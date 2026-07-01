from tools.text_summarizer import text_summarizer
from tools.get_weather import get_weather
from tools.web_search import web_search
from tools.calculator import calculator


VALID_TOOLS = {
    "calculator": {
        "name": "Calculator",
        "description": "A tool for performing mathematical calculations.",
        "function": calculator,
        "input_format": "expression",
        "required_args": ["expression"],
        "return_format": int,
    },

    "web_search": {
        "name": "Web Search",
        "description": "A tool for searching the web.",
        "function": web_search,
        "input_format": "query",
        "required_args": ["query"],
        "return_format": list,
    },

    "get_weather": {
        "name": "Weather Checker",
        "description": "A tool for checking the weather.",
        "function": get_weather,
        "input_format": "location",
        "required_args": ["location"],
        "return_format": dict,
    },
    
    "text_summarizer": {
        "name": "Text Summarizer",
        "description": "A tool for summarizing text.",
        "function": text_summarizer,
        "input_format": "text",
        "required_args": ["text"],
        "return_format": str,
    }
}