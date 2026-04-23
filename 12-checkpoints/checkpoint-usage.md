# Checkpoint Usage

Create, manage, and recover from checkpoints in Hermes.

## Creating Checkpoints

### Manual Checkpoint

```
checkpoint create before-refactor
```

### Auto Checkpoint

Auto-checkpoints occur:
- Before major operations (refactor, deploy)
- After significant milestones
- At configured intervals

### Checkpoint Naming

Use descriptive names:
```
checkpoint create after-feature-complete
checkpoint create before-database-migration
checkpoint create code-review-pending
```

## Listing Checkpoints

```
checkpoint list
```

Output:
```
ID         Name                    Created              Status
---------  ----------------------  -------------------  --------
abc123     before-refactor         2024-01-15 10:30     available
def456     after-feature          2024-01-15 11:45     available
ghi789     pending-review         2024-01-15 14:20     available
```

## Restoring Checkpoints

### Full Restore

```
checkpoint restore abc123
```

Restores:
- Conversation history
- Modified files
- Tool execution state
- Variables and context

### Selective Restore

Restore only specific components:

```
checkpoint restore abc123 --history
checkpoint restore abc123 --files
checkpoint restore abc123 --context
```

## Branching from Checkpoints

Create an alternate timeline:

```
checkpoint branch abc123 alternate-approach
```

This creates a new conversation branch without affecting the original.

## Managing Checkpoints

### Delete Old Checkpoints

```
checkpoint delete abc123
checkpoint delete --older-than 30d
checkpoint delete --all
```

### Export Checkpoint

```
checkpoint export abc123 --format zip
checkpoint export abc123 --output /path/to/backup
```

### Compare Checkpoints

```
checkpoint diff abc123 def456
```

## Workflows

### Before Major Changes

```
# 1. Review current state
checkpoint create before-major-change

# 2. Perform changes
[make changes...]

# 3. If issues arise, recover
checkpoint restore before-major-change
```

### Iteration with Review

```
# 1. Complete initial implementation
checkpoint create iteration-1-done

# 2. Request review
[review feedback...]

# 3. If changes needed, branch and iterate
checkpoint branch iteration-1-done iteration-2

# 4. Resume from branch
checkpoint restore iteration-2
```

### Parallel Approaches

```
# 1. Create baseline
checkpoint create baseline

# 2. Branch for approach A
checkpoint branch baseline approach-a

# 3. Switch to approach B
checkpoint restore baseline
checkpoint branch baseline approach-b

# 4. Compare results
checkpoint diff approach-a approach-b
```

## Best Practices

1. **Name descriptively** — Include context in names
2. **Regular checkpoints** — Before risky operations
3. **Clean up** — Delete old checkpoints periodically
4. **Document important ones** — Add descriptions
5. **Test restoration** — Verify recovery works
