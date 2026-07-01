from conceptual_tool_using_ai_assistant.guardrails.valid_tools import calculator
from conceptual_tool_using_ai_assistant.guardrails.valid_tools import web_search
from conceptual_tool_using_ai_assistant.guardrails.valid_tools import get_weather
from conceptual_tool_using_ai_assistant.guardrails.valid_tools import text_summarizer


TOOLS = {
    "calculator": calculator,
    "web_search": web_search,
    "get_weather": get_weather,
    "text_summarizer": text_summarizer,
}