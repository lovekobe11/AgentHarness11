import os
from dotenv import load_dotenv
from agent import AgentHarness

load_dotenv()

def main():
    harness = AgentHarness()
    print("🤖 Agent Harness ready. Type a question (or 'exit').")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ("exit", "quit"):
            break
        try:
            answer = harness.run(user_input)
            print(f"Agent: {answer}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
