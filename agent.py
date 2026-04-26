"""
Smart Research Assistant Agent
Built using Google Agent Development Kit (ADK)
Track 3 - Engineer AI Agents with ADK
"""

from google.adk.agents import Agent
from tools import (
    search_topic,
    summarize_text,
    save_note,
    list_notes,
    get_current_time,
    calculate,
    weather_info,
)

# ─────────────────────────────────────────────
#  Root Agent Definition
# ─────────────────────────────────────────────
root_agent = Agent(
    name="smart_research_assistant",
    model="gemini-2.0-flash",
    description=(
        "A Smart Research Assistant Agent that helps users research topics, "
        "summarize content, save notes, do calculations, and fetch weather info."
    ),
    instruction="""
    You are a Smart Research Assistant. Your job is to help the user:

    1. RESEARCH topics using the search_topic tool
    2. SUMMARIZE long text using the summarize_text tool
    3. SAVE important notes using the save_note tool
    4. LIST saved notes using the list_notes tool
    5. CALCULATE math expressions using the calculate tool
    6. GET WEATHER information using the weather_info tool
    7. TELL the current time using the get_current_time tool

    Always be helpful, concise, and accurate.
    When the user asks to research something, use search_topic first, 
    then offer to summarize or save the result.
    
    If you are unsure which tool to use, ask the user for clarification.
    """,
    tools=[
        search_topic,
        summarize_text,
        save_note,
        list_notes,
        get_current_time,
        calculate,
        weather_info,
    ],
)
