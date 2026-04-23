# Code Review Checklist

Use this checklist when reviewing code:

## Security
- [ ] Input validation on all user inputs
- [ ] Proper authentication/authorization checks
- [ ] No hardcoded credentials or secrets
- [ ] Parameterized queries (no SQL injection)
- [ ] Output encoding for XSS prevention
- [ ] Secure crypto usage (no custom crypto)
- [ ] No sensitive data in logs

## Performance
- [ ] No N+1 query patterns
- [ ] Appropriate indexing on databases
- [ ] Efficient algorithm complexity
- [ ] Proper caching where needed
- [ ] No memory leaks
- [ ] Lazy loading where appropriate

## Code Quality
- [ ] Single responsibility per function
- [ ] Clear, descriptive naming
- [ ] No magic numbers/strings
- [ ] Proper error handling
- [ ] Unit tests exist and pass
- [ ] No code duplication

## Maintainability
- [ ] Code is self-documenting
- [ ] Comments explain why, not what
- [ ] No commented-out code
- [ ] Consistent style
- [ ] No dead code
- [ ] Dependencies are up-to-date
