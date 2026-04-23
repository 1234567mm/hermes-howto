#!/usr/bin/env python3
"""
Quiz Generator for Hermes Howto

Generates quizzes from topic YAML files to test user understanding
of Hermes Agent features.
"""

import argparse
import random
import sys
from pathlib import Path
from typing import Any

import yaml


def load_topic_questions(topic: str) -> list[dict[str, Any]]:
    """Load quiz questions from a topic YAML file."""
    topics_dir = Path(__file__).parent / "topics"
    topic_file = topics_dir / f"{topic}.yaml"

    if not topic_file.exists():
        available = [f.stem for f in topics_dir.glob("*.yaml")]
        raise FileNotFoundError(
            f"Topic '{topic}' not found. Available topics: {', '.join(available)}"
        )

    with open(topic_file, "r") as f:
        data = yaml.safe_load(f)

    return data.get("questions", [])


def present_question(question: dict[str, Any], question_num: int, total: int) -> str:
    """Present a question and get the user's answer."""
    print(f"\n--- Question {question_num}/{total} ---")
    print(f"\n{question['question']}\n")

    choices = question["choices"]
    for i, choice in enumerate(choices, 1):
        print(f"  {i}. {choice['text']}")

    while True:
        try:
            answer = input("\nYour answer (1-4): ").strip()
            choice_num = int(answer)
            if 1 <= choice_num <= len(choices):
                return choices[choice_num - 1]["key"]
            print("Please enter a number between 1 and", len(choices))
        except ValueError:
            print("Please enter a valid number.")


def score_quiz(
    questions: list[dict[str, Any]], answers: list[str]
) -> dict[str, Any]:
    """Calculate the quiz score and generate feedback."""
    total = len(questions)
    correct = 0
    results = []

    for question, user_answer in zip(questions, answers):
        is_correct = user_answer == question["correct_answer"]
        if is_correct:
            correct += 1

        # Find the correct choice text
        correct_choice = next(
            c["text"]
            for c in question["choices"]
            if c["key"] == question["correct_answer"]
        )

        results.append(
            {
                "question": question["question"],
                "user_answer": user_answer,
                "correct_answer": question["correct_answer"],
                "correct_text": correct_choice,
                "is_correct": is_correct,
                "explanation": question.get("explanation", ""),
            }
        )

    score_pct = (correct / total) * 100 if total > 0 else 0

    return {
        "total": total,
        "correct": correct,
        "score_pct": score_pct,
        "results": results,
    }


def print_results(results: dict[str, Any]) -> None:
    """Print quiz results and feedback."""
    print("\n" + "=" * 50)
    print("QUIZ RESULTS")
    print("=" * 50)

    print(f"\nScore: {results['correct']}/{results['total']} ({results['score_pct']:.0f}%)")

    if results["score_pct"] >= 90:
        print("Excellent! You've mastered this topic!")
    elif results["score_pct"] >= 70:
        print("Good job! You have a solid understanding.")
    elif results["score_pct"] >= 50:
        print("Not bad! Review the topics you missed.")
    else:
        print("Keep learning! Review the module content.")

    print("\n--- Detailed Results ---")
    for i, r in enumerate(results["results"], 1):
        status = "CORRECT" if r["is_correct"] else "INCORRECT"
        print(f"\n{i}. [{status}] {r['question']}")
        if not r["is_correct"]:
            print(f"   Your answer: {r['user_answer']}")
            print(f"   Correct: {r['correct_text']}")
        if r["explanation"]:
            print(f"   Explanation: {r['explanation']}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a quiz for a Hermes topic")
    parser.add_argument(
        "topic",
        nargs="?",
        default="quickstart",
        help="Topic to quiz on (default: quickstart)",
    )
    parser.add_argument(
        "--questions",
        type=int,
        default=5,
        help="Number of questions to ask (default: 5, max: 10)",
    )
    parser.add_argument(
        "--shuffle",
        action="store_true",
        help="Shuffle question order",
    )

    args = parser.parse_args()

    try:
        all_questions = load_topic_questions(args.topic)

        if args.shuffle:
            random.shuffle(all_questions)

        # Limit to requested number (5-10)
        num_questions = max(5, min(args.questions, 10))
        questions = all_questions[:num_questions]

        print(f"\n=== Hermes Howto Quiz: {args.topic.upper()} ===")
        print(f"Answer {len(questions)} questions about {args.topic}\n")

        answers = []
        for i, q in enumerate(questions, 1):
            answer = present_question(q, i, len(questions))
            answers.append(answer)

        results = score_quiz(questions, answers)
        print_results(results)

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
