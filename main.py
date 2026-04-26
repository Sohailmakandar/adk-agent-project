"""
main.py — Entry point to run the Smart Research Assistant Agent
Usage:
    python main.py                  # Interactive CLI chat
    python main.py --demo           # Run a demo with preset questions
"""

import argparse
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from agent import root_agent


APP_NAME = "smart_research_assistant"
USER_ID  = "user_01"


def run_agent(user_message: str, session_service, runner, session_id: str) -> str:
    """Send a message to the agent and return its response."""
    content = types.Content(
        role="user",
        parts=[types.Part(text=user_message)],
    )

    response_text = ""
    for event in runner.run(
        user_id=USER_ID,
        session_id=session_id,
        new_message=content,
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                response_text = event.content.parts[0].text
    return response_text


def demo_mode():
    """Run a pre-scripted demo showing all agent capabilities."""
    session_service = InMemorySessionService()
    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )
    session = session_service.create_session(
        app_name=APP_NAME, user_id=USER_ID
    )

    demo_questions = [
        "What time is it right now?",
        "Research the topic: Agent Development Kit by Google",
        "Calculate sqrt(144) + 2 ** 8",
        "What is the weather in Bangalore?",
        "Save a note titled 'ADK Facts' with content: ADK is Google's framework for building AI agents using Gemini models.",
        "List all my saved notes",
    ]

    print("\n" + "="*60)
    print("  SMART RESEARCH ASSISTANT — DEMO MODE")
    print("="*60)

    for question in demo_questions:
        print(f"\n🙋 USER: {question}")
        response = run_agent(question, session_service, runner, session.id)
        print(f"🤖 AGENT: {response}")
        print("-" * 60)


def interactive_mode():
    """Run an interactive chat loop."""
    session_service = InMemorySessionService()
    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )
    session = session_service.create_session(
        app_name=APP_NAME, user_id=USER_ID
    )

    print("\n" + "="*60)
    print("  SMART RESEARCH ASSISTANT — INTERACTIVE MODE")
    print("  Type 'exit' or 'quit' to stop.")
    print("="*60 + "\n")

    while True:
        user_input = input("🙋 You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit"):
            print("👋 Goodbye!")
            break
        response = run_agent(user_input, session_service, runner, session.id)
        print(f"🤖 Agent: {response}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Smart Research Assistant Agent")
    parser.add_argument(
        "--demo", action="store_true", help="Run in demo mode with preset questions"
    )
    args = parser.parse_args()

    if args.demo:
        demo_mode()
    else:
        interactive_mode()
