---
name: blog-draft
description: Draft a blog post from ideas and resources. Use when users want to write a blog post, create content from research, or draft articles. Guides through research, brainstorming, outlining, and iterative drafting with version control.
---

# Blog Draft Skill

Draft a blog post from ideas and resources. This skill guides through research, brainstorming, outlining, and iterative drafting with version control.

## User Input

```text
$ARGUMENTS
```

User should provide:
- **Idea/Topic**: The main concept or theme for the blog post
- **Resources**: URLs, files, or references to research (optional but recommended)
- **Target audience**: Who the blog post is for (optional)
- **Tone/Style**: Formal, casual, technical, etc. (optional)

## Execution Flow

Follow these steps sequentially:

### Step 0: Create Project Folder

1. Generate folder name using format: `YYYY-MM-DD-short-topic-name`
2. Create the folder structure:
   ```
   blog-posts/
   └── YYYY-MM-DD-short-topic-name/
       └── resources/
   ```
3. Confirm folder creation with user before proceeding.

### Step 1: Research & Resource Collection

1. Create `resources/` subfolder in the blog post directory
2. For each provided resource:
   - **URLs**: Fetch and save key information to `resources/` as markdown files
   - **Files**: Read and summarize in `resources/`
   - **Topics**: Use web search to gather up-to-date information

### Step 2: Brainstorm & Clarify

1. Present main themes, potential angles, key points, and gaps
2. Ask clarifying questions about main takeaway, target length, and emphasis
3. **Wait for user responses before proceeding.**

### Step 3: Propose Outline

Create a structured outline including meta information, proposed structure, and sources to cite.

### Step 4: Save Approved Outline

Once user approves, save to `OUTLINE.md` in the blog post folder.

### Step 5: Commit Outline (if in git repo)

Stage new files, create commit with message: `docs: Add outline for blog post - [topic-name]`

### Step 6: Write Draft

Based on the approved outline, write the full blog post draft including:
- Engaging introduction with hook
- Clear section headers
- Supporting evidence and examples from research
- **Citations**: All factual claims MUST cite the original source

### Step 7: Iterate or Finalize

**If user requests changes:**
- Increment version number (v0.2, v0.3, etc.)
- Save as `draft-v[X.Y].md`
- Repeat review process

**If user approves:**
- Confirm the final draft version
- Optionally rename to `final.md`

## Output Files Structure

```
blog-posts/
└── YYYY-MM-DD-topic-name/
    ├── resources/
    │   ├── source-1-name.md
    │   └── source-2-name.md
    ├── OUTLINE.md
    ├── draft-v0.1.md
    └── draft-v0.2.md (if iterations)
```

## Citation Requirements

Every data point, statistic, or comparison MUST have an inline citation:
- Use numbered references [1], [2], etc.
- Link citations to References section at end
- Example: "Studies show that 65% of developers prefer TypeScript [1]"
