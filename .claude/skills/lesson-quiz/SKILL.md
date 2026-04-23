---
name: lesson-quiz
description: Test your knowledge of a specific Hermes Agent topic. Usage: /lesson-quiz [topic]
version: 1.0.0
hermes:
  project: hermes-howto
  domain: learning
---

# Lesson Quiz Skill

Test your understanding of Hermes Agent topics covered in the Hermes Howto modules.

## Usage

```
/lesson-quiz [topic]
```

## Available Topics

- `quickstart` - Getting started with Hermes Agent
- `memory` - Persistent context and memory management

## How It Works

1. The skill loads quiz questions from the specified topic YAML file
2. Presents 5-10 multiple choice questions
3. Collects your answers
4. Scores the quiz and provides feedback with explanations

## Example

```
/lesson-quiz memory
```

This loads questions from `topics/memory.yaml` covering:
- MEMORY.md vs USER.md differences
- Memory file locations
- Memory tool commands
- Frozen snapshots
