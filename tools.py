"""
tools.py — Custom Tools for Smart Research Assistant Agent
Each function is decorated with @tool so ADK can register it.
"""

import json
import math
import datetime
import os
from google.adk.tools import tool


# ─────────────────────────────────────────────
# 1. SEARCH TOOL (simulated — replace with real API)
# ─────────────────────────────────────────────
@tool
def search_topic(query: str) -> dict:
    """
    Searches for information about a given topic.
    In production, connect this to Google Search API or SerpAPI.

    Args:
        query: The topic or question to search for.

    Returns:
        A dict with 'title', 'summary', and 'source'.
    """
    # ── Simulated search results (replace with real API call) ──
    mock_results = {
        "title": f"Research Results: {query}",
        "summary": (
            f"Here is a simulated research summary for '{query}'. "
            "In a production environment, this would pull live results "
            "from Google Search API, Wikipedia API, or any other knowledge source. "
            "The agent uses this data to give informed, grounded answers."
        ),
        "source": "Simulated Knowledge Base (replace with Google Search API)",
    }
    return mock_results


# ─────────────────────────────────────────────
# 2. SUMMARIZE TOOL
# ─────────────────────────────────────────────
@tool
def summarize_text(text: str, max_sentences: int = 3) -> dict:
    """
    Summarizes a given block of text into a shorter version.

    Args:
        text: The long text to summarize.
        max_sentences: Maximum number of sentences to include (default: 3).

    Returns:
        A dict with 'original_length', 'summary', and 'sentence_count'.
    """
    sentences = [s.strip() for s in text.split(".") if s.strip()]
    selected = sentences[:max_sentences]
    summary = ". ".join(selected) + ("." if selected else "")

    return {
        "original_length": len(text),
        "summary": summary,
        "sentence_count": len(selected),
    }


# ─────────────────────────────────────────────
# 3. SAVE NOTE TOOL
# ─────────────────────────────────────────────
NOTES_FILE = "notes.json"

@tool
def save_note(title: str, content: str) -> dict:
    """
    Saves a note with a title and content to local storage.

    Args:
        title: Short title for the note.
        content: The body/content of the note.

    Returns:
        A dict confirming the note was saved with a timestamp.
    """
    notes = []
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            notes = json.load(f)

    note = {
        "id": len(notes) + 1,
        "title": title,
        "content": content,
        "saved_at": datetime.datetime.now().isoformat(),
    }
    notes.append(note)

    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)

    return {"status": "saved", "note_id": note["id"], "title": title}


# ─────────────────────────────────────────────
# 4. LIST NOTES TOOL
# ─────────────────────────────────────────────
@tool
def list_notes() -> dict:
    """
    Lists all saved notes.

    Returns:
        A dict with a list of all saved notes.
    """
    if not os.path.exists(NOTES_FILE):
        return {"notes": [], "count": 0}

    with open(NOTES_FILE, "r") as f:
        notes = json.load(f)

    return {"notes": notes, "count": len(notes)}


# ─────────────────────────────────────────────
# 5. GET CURRENT TIME TOOL
# ─────────────────────────────────────────────
@tool
def get_current_time() -> dict:
    """
    Returns the current date and time.

    Returns:
        A dict with 'date', 'time', and 'timezone'.
    """
    now = datetime.datetime.now()
    return {
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "timezone": "Local System Time",
        "iso": now.isoformat(),
    }


# ─────────────────────────────────────────────
# 6. CALCULATOR TOOL
# ─────────────────────────────────────────────
@tool
def calculate(expression: str) -> dict:
    """
    Evaluates a safe mathematical expression.

    Args:
        expression: A math expression string, e.g. "2 + 2", "sqrt(16)", "3 ** 4".

    Returns:
        A dict with 'expression' and 'result'.
    """
    allowed_names = {
        k: v for k, v in math.__dict__.items() if not k.startswith("_")
    }
    allowed_names.update({"abs": abs, "round": round})

    try:
        result = eval(expression, {"__builtins__": {}}, allowed_names)  # noqa: S307
        return {"expression": expression, "result": result}
    except Exception as e:
        return {"expression": expression, "error": str(e)}


# ─────────────────────────────────────────────
# 7. WEATHER INFO TOOL (simulated)
# ─────────────────────────────────────────────
@tool
def weather_info(city: str) -> dict:
    """
    Retrieves current weather information for a given city.
    In production, connect this to OpenWeatherMap API or similar.

    Args:
        city: The name of the city (e.g., "Bangalore", "London").

    Returns:
        A dict with weather details.
    """
    # ── Simulated weather data ──
    return {
        "city": city,
        "temperature_celsius": 28,
        "condition": "Partly Cloudy",
        "humidity_percent": 65,
        "wind_kph": 12,
        "note": "Simulated data — connect to OpenWeatherMap API for live results.",
    }
