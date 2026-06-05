import datetime
import math
import json

# A tool is a function plus a schema.
# Using OpenAI function-calling format.
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Perform a mathematical calculation. Supports basic arithmetic and math functions like sqrt, sin, etc.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The mathematical expression to evaluate, e.g., '2+2' or 'sqrt(16)'"
                    }
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_datetime",
            "description": "Get the current date and time in ISO format.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    }
]

def execute_tool(name: str, arguments: dict) -> str:
    """Execute a tool by name with given arguments and return the result as a string."""
    try:
        if name == "calculator":
            expr = arguments.get("expression", "")
            # Safe evaluation: limit to mathematical functions
            allowed_names = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
            result = eval(expr, {"__builtins__": {}}, allowed_names)
            return str(result)
        elif name == "get_current_datetime":
            return datetime.datetime.now().isoformat()
        else:
            return f"Error: Unknown tool '{name}'"
    except Exception as e:
        return f"Error executing tool '{name}': {str(e)}"
