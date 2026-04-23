<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/hermes-howto-logo-dark.svg">
  <img alt="Hermes How To" src="../resources/logos/hermes-howto-logo.svg">
</picture>

# Cron Quick Start

Get started with scheduled tasks and automation in minutes.

## Prerequisites

- Hermes installed and configured
- Basic understanding of tasks in Hermes

## Step 1: Check Cron Status

```
Show me the current cron configuration and scheduled jobs
```

This displays:
- Active scheduled jobs and their next run time
- Job status (enabled/disabled)
- Recent execution history

## Step 2: Schedule Your First Job

### Simple Hourly Task

```
Schedule a task to run every hour that checks system status
```

This creates a job configuration:

```yaml
name: hourly-status
schedule: "0 * * * *"
task:
  prompt: "Run system status check and report any issues"
  tool: default
```

### Daily Morning Report

```
Schedule a task to run every weekday at 9 AM that summarizes project activity
```

```yaml
name: daily-report
schedule: "0 9 * * 1-5"
task:
  prompt: "Generate a summary of project commits, issues, and pull requests from the last 24 hours"
  tool: default
```

### Weekly Summary

```
Schedule a task to run every Sunday at midnight that creates a weekly summary
```

```yaml
name: weekly-summary
schedule: "0 0 * * 0"
task:
  prompt: "Create a comprehensive weekly summary including: completed tasks, pending items, and next week's priorities"
  tool: default
```

## Step 3: List Scheduled Jobs

```
List all cron jobs currently configured
```

You should see your newly added jobs with:
- Job name and description
- Next scheduled run time
- Enabled/disabled status

## Step 4: Run a Job Manually

```
Run the hourly-status job now
```

## Cron Expression Reference

### Common Patterns

| Pattern | Expression | Meaning |
|---------|------------|---------|
| Every hour | `0 * * * *` | Minute 0 of every hour |
| Every 15 minutes | `*/15 * * * *` | Every 15 minutes |
| Every day at 9am | `0 9 * * *` | 9:00 AM daily |
| Every weekday at 9am | `0 9 * * 1-5` | 9:00 AM Monday-Friday |
| First of month | `0 0 1 * *` | Midnight on 1st |
| Every Sunday | `0 0 * * 0` | Sunday at midnight |
| Twice daily | `0 9,17 * * *` | 9 AM and 5 PM |

### Special Strings

| String | Equivalent | Meaning |
|--------|------------|---------|
| `@hourly` | `0 * * * *` | Every hour |
| `@daily` | `0 0 * * *` | Every day at midnight |
| `@weekly` | `0 0 * * 0` | Every Sunday at midnight |
| `@monthly` | `0 0 1 * *` | First of month |
| `@yearly` | `0 0 1 1 *` | January 1st |

## Job Configuration Options

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Unique job identifier |
| `schedule` | string | Cron expression |
| `task.prompt` | string | Task to execute |

### Optional Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `description` | string | - | Human-readable description |
| `enabled` | boolean | true | Whether job runs on schedule |
| `timeout` | number | 300 | Max execution time in seconds |
| `timezone` | string | local | Timezone for schedule |
| `on_failure` | string | log | Action on failure: log, retry, stop |
| `notify` | boolean | false | Send notification on completion |

## Interval-Based Scheduling

For simple intervals without cron expressions:

```yaml
name: health-check
interval: "15m"  # Every 15 minutes
task:
  prompt: "Check service health endpoints"
```

```
5m    - Every 5 minutes
1h    - Every hour
6h    - Every 6 hours
1d    - Every day
1w    - Every week
```

## Troubleshooting

### Job Not Running

1. Verify job is enabled: `cron list`
2. Check cron expression is valid
3. Ensure Hermes is running
4. Review execution history for errors

```
Show me the execution history for the hourly-status job
```

### Invalid Cron Expression

- Use a cron expression validator
- Check field ranges (minute: 0-59, hour: 0-23)
- Ensure day-of-week uses correct values (0=Sunday, 6=Saturday)

### Task Timeout

Increase timeout for long-running tasks:

```yaml
name: long-task
schedule: "0 9 * * *"
timeout: 3600  # 1 hour
task:
  prompt: "Run comprehensive analysis"
```

## Next Steps

- [webhook-triggers.md](webhook-triggers.md) — Configure webhook event triggers
- [cron-examples/](cron-examples/) — Ready-to-use configurations
