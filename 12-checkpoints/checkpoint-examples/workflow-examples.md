# Checkpoint Workflows

Example checkpoint workflows for common scenarios.

## Before/After Refactor

### Scenario
Refactoring a critical module with potential for breaking changes.

### Workflow

```bash
# Create checkpoint before starting
checkpoint create before-user-module-refactor

# Perform refactoring
[refactor user module...]

# Test changes
[run tests...]

# If successful, continue
# If issues, restore
checkpoint restore before-user-module-refactor
```

### Output

```
Checkpoint created: before-user-module-refactor (abc123)

[After refactoring and test failure:]

Restoring checkpoint abc123...
Restore complete. All files and context restored.
```

## Iteration with Feedback

### Scenario
Implementing feature with iterative review cycles.

```bash
# Initial implementation
checkpoint create implementation-v1

# First review
checkpoint create post-review-1

# Address feedback
checkpoint branch post-review-1 implementation-v2

# Continue development
[implement changes...]

checkpoint create implementation-v2-done
```

## Parallel Experimentation

### Scenario
Testing two different approaches.

```bash
# Baseline state
checkpoint create baseline

# Approach A
checkpoint branch baseline approach-a
[implement approach A...]
checkpoint create approach-a-result

# Compare to baseline
checkpoint restore baseline

# Approach B
checkpoint branch baseline approach-b
[implement approach B...]
checkpoint create approach-b-result

# Compare approaches
checkpoint diff approach-a approach-b
```

## Long-Running Task Recovery

### Scenario
Recovering from interrupted work.

```bash
# Checkpoint before long task
checkpoint create before-migration

# Start migration
[run migration...]

# If interrupted, recover
checkpoint restore before-migration

# Resume from where left off
[continue migration...]
```
