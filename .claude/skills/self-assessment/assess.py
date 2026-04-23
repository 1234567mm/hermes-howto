#!/usr/bin/env python3
"""
Hermes Agent Self-Assessment Quiz Engine

Determines user proficiency level based on 8 topic questions.
Final level = mode of answers.
"""

import yaml
from pathlib import Path
from collections import Counter

SKILL_DIR = Path(__file__).parent
LEVELS_FILE = SKILL_DIR / "levels.yaml"


def load_levels() -> dict:
    with open(LEVELS_FILE) as f:
        return yaml.safe_load(f)


def mode_of_answers(answers: list[str]) -> str:
    counts = Counter(answers)
    return counts.most_common(1)[0][0]


def level_from_score(score: int, levels: dict) -> dict:
    for level_name, level_data in levels.items():
        low, high = map(int, level_data["score_range"].split("-"))
        if low <= score <= high:
            return level_name, level_data
    return "unknown", {}


QUESTIONS = [
    {
        "id": 1,
        "topic": "CLI Experience",
        "question": "How familiar are you with the Hermes Agent CLI?",
        "options": [
            {"label": "A", "text": "I've never used the CLI", "level": "beginner"},
            {"label": "B", "text": "I've used basic commands like /help and --version", "level": "intermediate"},
            {"label": "C", "text": "I use CLI daily for complex workflows", "level": "advanced"},
        ],
    },
    {
        "id": 2,
        "topic": "Memory Systems",
        "question": "Have you worked with persistent context and memory features?",
        "options": [
            {"label": "A", "text": "No, I start fresh each session", "level": "beginner"},
            {"label": "B", "text": "I've used session persistence occasionally", "level": "intermediate"},
            {"label": "C", "text": "I actively configure memory and context management", "level": "advanced"},
        ],
    },
    {
        "id": 3,
        "topic": "Skills",
        "question": "What is your experience with Hermes Agent skills?",
        "options": [
            {"label": "A", "text": "I don't know what skills are", "level": "beginner"},
            {"label": "B", "text": "I've used a few built-in skills", "level": "intermediate"},
            {"label": "C", "text": "I've created custom skills and configured skill sets", "level": "advanced"},
        ],
    },
    {
        "id": 4,
        "topic": "Delegation & Subagents",
        "question": "How comfortable are you with task delegation to subagents?",
        "options": [
            {"label": "A", "text": "I handle everything myself", "level": "beginner"},
            {"label": "B", "text": "I've delegated simple tasks to subagents", "level": "intermediate"},
            {"label": "C", "text": "I design complex multi-agent workflows", "level": "advanced"},
        ],
    },
    {
        "id": 5,
        "topic": "MCP (Model Context Protocol)",
        "question": "What is your experience with MCP integrations?",
        "options": [
            {"label": "A", "text": "Never heard of MCP", "level": "beginner"},
            {"label": "B", "text": "I've connected one or two MCP servers", "level": "intermediate"},
            {"label": "C", "text": "I build and maintain MCP server integrations", "level": "advanced"},
        ],
    },
    {
        "id": 6,
        "topic": "Voice Mode",
        "question": "Have you used Hermes Agent's voice interaction mode?",
        "options": [
            {"label": "A", "text": "No, I only use text", "level": "beginner"},
            {"label": "B", "text": "I've tried voice mode a few times", "level": "intermediate"},
            {"label": "C", "text": "I regularly use voice mode for hands-free work", "level": "advanced"},
        ],
    },
    {
        "id": 7,
        "topic": "Messaging Integrations",
        "question": "What is your experience with messaging platform integrations?",
        "options": [
            {"label": "A", "text": "I don't use messaging integrations", "level": "beginner"},
            {"label": "B", "text": "I've connected to Slack or Teams", "level": "intermediate"},
            {"label": "C", "text": "I manage multiple messaging gateway integrations", "level": "advanced"},
        ],
    },
    {
        "id": 8,
        "topic": "Cron & Scheduling",
        "question": "How experienced are you with scheduled tasks and cron jobs?",
        "options": [
            {"label": "A", "text": "I don't use scheduling features", "level": "beginner"},
            {"label": "B", "text": "I've set up a few scheduled tasks", "level": "intermediate"},
            {"label": "C", "text": "I build complex scheduled workflows with cron", "level": "advanced"},
        ],
    },
]


def run_quiz() -> dict:
    levels = load_levels()
    answers = []

    print("=" * 60)
    print("  HERMES AGENT SELF-ASSESSMENT")
    print("=" * 60)
    print()
    print("Answer 8 questions to find your proficiency level.")
    print("Each answer maps to: Beginner / Intermediate / Advanced")
    print()

    for q in QUESTIONS:
        print(f"Question {q['id']}: {q['topic']}")
        print(f"  {q['question']}")
        print()
        for opt in q["options"]:
            print(f"    {opt['label']}. {opt['text']}")
        print()

        while True:
            choice = input("Your answer (A/B/C): ").strip().upper()
            if choice in ("A", "B", "C"):
                break
            print("Please enter A, B, or C.")

        selected = next(o for o in q["options"] if o["label"] == choice)
        answers.append(selected["level"])

        level_names = {"beginner": "Beginner", "intermediate": "Intermediate", "advanced": "Advanced"}
        print(f"  -> {level_names[selected['level']]}")
        print()

    final_level = mode_of_answers(answers)
    level_name, level_data = level_from_score(
        sum(1 for a in answers if a == final_level), levels
    )

    score = sum(1 for a in answers if a == final_level)
    level_key = list(levels.keys())[list(levels.values()).index(level_data)] if level_data else final_level

    print("=" * 60)
    print("  RESULTS")
    print("=" * 60)
    print(f"  Your answers: {answers}")
    print(f"  Final level: {final_level.upper()}")
    print(f"  Recommended modules: {level_data.get('recommended_modules', 'N/A')}")
    print("=" * 60)

    return {
        "answers": answers,
        "level": final_level,
        "recommended_modules": level_data.get("recommended_modules", ""),
    }


if __name__ == "__main__":
    run_quiz()
