# Creating Your SOUL

A step-by-step guide to designing, writing, and refining your Hermes personality.

## Overview

Creating an effective SOUL requires:

1. Defining core traits
2. Setting communication style
3. Writing behavioral rules
4. Testing and refining

## Step 1: Identify Your Purpose

Ask yourself:

- What is Hermes's primary role?
- Who are the main users?
- What should interactions feel like?

**Example:**

| Question | Answer |
|----------|--------|
| Role | Senior code reviewer |
| Users | Junior to mid-level developers |
| Feel | Patient mentor, direct feedback |

## Step 2: Choose Core Traits

Select 3-5 traits that define personality:

### Trait Selection Matrix

```
                 Introverted                    Extroverted
              ┌─────────────────┬─────────────────────┐
   Structured │    Analytical   │      Professional   │
              ├─────────────────┼─────────────────────┤
   Flexible   │    Creative     │      Friendly       │
              └─────────────────┴─────────────────────┘
```

### Common Trait Combinations

| Role | Traits |
|------|--------|
| Code Reviewer | analytical, direct, thorough |
| Technical Writer | clear, patient, thorough |
| Debugging Buddy | patient, curious, helpful |
| Senior Mentor | patient, encouraging, direct |
| Creative Partner | creative, bold, curious |

**Exercise:** Write down your 3-5 traits:

```
1. _______________
2. _______________
3. _______________
4. _______________
5. _______________
```

## Step 3: Define Communication Style

### Tone

Choose based on context:

| Tone | Best For | Example |
|------|----------|---------|
| professional | Formal reports, business | "I'll analyze the requirements..." |
| casual | Debugging, quick questions | "Hey, let's figure this out" |
| friendly | Onboarding, explanations | "Great question! Here's how..." |
| formal | Academic, specifications | "The system shall..." |

### Vocabulary

| Level | When to Use |
|-------|-------------|
| technical | Developers, precise communication |
| simple | Non-technical users, onboarding |
| creative | Brainstorming, presentations |
| academic | Research, detailed analysis |

### Sentence Style

| Style | Characteristics |
|-------|----------------|
| clear | Well-structured, logical flow |
| concise | Short, high-density information |
| elaborate | Detailed examples, thorough |
| storytelling | Narrative, context-rich |

**Exercise:** Complete your style profile:

```
Tone: _______________
Vocabulary: _______________
Sentence Style: _______________
```

## Step 4: Write Response Patterns

Standardize common interactions:

### Essential Patterns

```yaml
response_patterns:
  greeting: "How do you want to open conversations?"
  farewell: "How do you say goodbye?"
  error: "How do you acknowledge problems?"
  clarification: "How do you ask for more info?"
```

### Pattern Examples

#### Professional Reviewer

```yaml
response_patterns:
  greeting: "I'm ready to review. Share the code when convenient."
  farewell: "Review complete. Let me know if you have questions."
  error: "I encountered an issue during analysis: [specific problem]."
  clarification: "To give you the best feedback, could you clarify [topic]?"
```

#### Friendly Mentor

```yaml
response_patterns:
  greeting: "Hey! What are we working on today?"
  farewell: "You've got this! I'm here when you need me."
  error: "Oops, ran into a snag: [issue]. Let me try a different approach."
  clarification: "I want to make sure I understand — are you asking about X or Y?"
```

## Step 5: Define Behavioral Rules

Control how Hermes acts:

```yaml
behavioral:
  show_reasoning: true/false
  ask_clarifying: true/false
  suggest_improvements: true/false
  admit_limitations: true/false
  challenge_assumptions: true/false
```

### Rule Guide

| Setting | When ON | When OFF |
|---------|---------|---------|
| show_reasoning | Debugging, learning | Quick answers |
| ask_clarifying | Ambiguous requests | Clear requests |
| suggest_improvements | Review tasks | Exploratory tasks |
| admit_limitations | Always (recommended) | Rarely |
| challenge_assumptions | Expert users | Novice users |

## Step 6: Write the Body Content

Structure your SOUL's personality:

### Template Structure

```markdown
# [Personality Name]

[1-2 sentence elevator pitch]

## Communication Style

[How to communicate in different situations]

## Behavioral Guidelines

[Specific rules for interactions]

## Expertise Presentation

[How to deliver knowledge]

## Response Examples

[Sample interactions]
```

### Content Writing Tips

1. **Be specific** — "Use code examples" not "be helpful"
2. **Avoid contradictions** — Don't say "be concise" and "be thorough"
3. **Think of examples** — Include real response snippets
4. **Consider edge cases** — How to handle disagreement, confusion

## Step 7: Create Response Examples

Show, don't tell. Include:

### Greeting Examples

```
[For a friendly mentor]
User: Hey, I need help with my code
Hermes: Hey! Happy to help. What language/framework?
```

### Error Handling

```
User: Why did my deploy fail?
Hermes: Deploy failed with exit code 137 (OOM killed). This usually 
means the container exceeded memory limits. Let me check your config...
```

### Clarification

```
User: Make it faster
Hermes: I can optimize this, but "faster" could mean:
  - Lower latency (faster response)
  - Higher throughput (more requests/sec)
  - Lower resource usage (cheaper)
Which aspect matters most for your use case?
```

## Step 8: Test and Refine

### Testing Checklist

- [ ] Does it feel consistent across conversations?
- [ ] Are the traits reflected in responses?
- [ ] Is communication style appropriate?
- [ ] Do response patterns sound natural?
- [ ] Are behavioral rules followed?

### Refinement Process

1. Use your SOUL for a week
2. Note responses that feel "off"
3. Update the SOUL.md
4. Repeat

### Common Issues

| Issue | Fix |
|-------|-----|
| Too generic | Add specific examples/rules |
| Too rigid | Relax constraints, add flexibility |
| Contradictory | Remove conflicting traits/rules |
| Sounds forced | Naturalize response patterns |

## Complete Example

See [personality-examples/tech-mentor.md](personality-examples/tech-mentor.md) for a full personality implementation.

## Quick Reference

### Trait Quick Picker

**Primary (choose 2-3):**
- helpful, creative, analytical, direct, patient, bold

**Secondary (choose 2-4):**
- curious, thorough, precise, friendly, humorous, diplomatic

### Style Combinations

| Role | Tone | Vocab | Style |
|------|------|-------|-------|
| Code Reviewer | professional | technical | clear |
| Teacher | friendly | simple | elaborate |
| Peer | casual | technical | concise |
| Expert | professional | technical | clear |

## Next Steps

1. Browse [personality-examples/](personality-examples/) for templates
2. Create your own SOUL.md using this guide
3. Place at `~/.claude/SOUL.md` or `.claude/SOUL.md`
4. Test and iterate
