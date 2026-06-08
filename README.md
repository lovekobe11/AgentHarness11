# Agent Harness

A minimal, extensible AI agent harness using OpenAI's function‑calling API.  

## Architecture

- **Agent loop** (`agent.py`): Manages conversation, tool execution, and LLM calls.
- **Tools** (`tools.py`): Collection of functions with schema (calculator, datetime).
- **Entry** (`main.py`): Simple interactive CLI.

## How to run

1. `python -m venv venv && source venv/bin/activate`
2. `pip install -r requirements.txt`
3. Create a `.env` file with `OPENAI_API_KEY=your_key`
4. `python main.py`

## Extending with new tools

Add a function in `tools.py`, add its schema to the `TOOLS` list, and handle execution in `execute_tool`. The harness automatically picks it up.

## Why this matters for Cloudera

This harness can be connected to any LLM endpoint by swapping the `OpenAI` client. 
