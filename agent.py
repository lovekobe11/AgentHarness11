import os
import json
from openai import OpenAI
from tools import TOOLS, execute_tool

class AgentHarness:
    def __init__(self, model="gpt-4o", max_iterations=10):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model
        self.max_iterations = max_iterations
        self.messages = [
            {"role": "system", "content": (
                "You are a helpful assistant that can use tools to answer user questions. "
                "If you need to use a tool, return a valid function call. "
                "If you have enough information, answer directly. "
                "Always reason step by step."
            )}
        ]

    def run(self, user_query: str) -> str:
        self.messages.append({"role": "user", "content": user_query})
        iteration = 0

        while iteration < self.max_iterations:
            iteration += 1
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                tools=TOOLS,
                tool_choice="auto",
                temperature=0.2
            )
            msg = response.choices[0].message

            # If no tool call, we have a final answer
            if not msg.tool_calls:
                final_answer = msg.content or ""
                self.messages.append({"role": "assistant", "content": final_answer})
                return final_answer

            # Process tool calls
            self.messages.append(msg)  # assistant message with tool_calls
            for tool_call in msg.tool_calls:
                function_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)
                print(f"[Agent] Calling tool '{function_name}' with {arguments}")

                result = execute_tool(function_name, arguments)

                # Append tool result to conversation
                self.messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                })

        return "I'm sorry, I couldn't complete the task within the allowed steps."
