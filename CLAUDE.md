# CLAUDE.md - AI Assistant Guide for Bundle Image Creator

## Project Overview

**Bundle Image Creator** is a tool for creating and managing bundle images. This document provides comprehensive guidance for AI assistants working on this codebase.

**Repository**: yeemre94/bundle_image_creater
**Status**: Initial development phase
**Last Updated**: 2025-11-14

---

## Table of Contents

1. [Project Purpose](#project-purpose)
2. [Codebase Structure](#codebase-structure)
3. [Development Workflow](#development-workflow)
4. [Key Conventions](#key-conventions)
5. [Architecture Guidelines](#architecture-guidelines)
6. [Testing Strategy](#testing-strategy)
7. [Git Workflow](#git-workflow)
8. [Common Tasks](#common-tasks)
9. [Troubleshooting](#troubleshooting)

---

## Project Purpose

The Bundle Image Creator is designed to:
- Create bundled images from multiple source files
- Process and optimize image bundles
- Provide a streamlined workflow for image bundling operations
- Support various image formats and configurations

---

## Codebase Structure

### Current Structure

```
bundle_image_creater/
├── .git/                 # Git repository data
├── CLAUDE.md            # This file - AI assistant guide
└── [To be organized as project grows]
```

### Recommended Future Structure

```
bundle_image_creater/
├── src/                 # Source code
│   ├── core/           # Core bundling logic
│   ├── utils/          # Utility functions
│   ├── config/         # Configuration management
│   └── cli/            # Command-line interface (if applicable)
├── tests/              # Test files
│   ├── unit/          # Unit tests
│   ├── integration/   # Integration tests
│   └── fixtures/      # Test fixtures and sample data
├── docs/               # Documentation
│   ├── api/           # API documentation
│   └── guides/        # User guides
├── examples/           # Example usage and sample bundles
├── scripts/            # Build and deployment scripts
├── .github/            # GitHub workflows and templates
├── package.json        # Node.js dependencies (if applicable)
├── README.md           # User-facing documentation
├── CLAUDE.md           # This file
├── .gitignore          # Git ignore patterns
└── LICENSE             # License file
```

---

## Development Workflow

### Setting Up Development Environment

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd bundle_image_creater
   ```

2. **Install dependencies** (once package.json exists)
   ```bash
   npm install
   # or
   pip install -r requirements.txt
   # or equivalent for chosen language
   ```

3. **Run tests**
   ```bash
   npm test
   # or equivalent command
   ```

### Branching Strategy

- **Main branch**: Production-ready code
- **Development branches**: Follow pattern `claude/claude-md-*` for AI-assisted development
- **Feature branches**: `feature/<feature-name>`
- **Bug fixes**: `fix/<issue-description>`

### Making Changes

1. Create or switch to appropriate branch
2. Make changes incrementally
3. Write/update tests
4. Update documentation
5. Commit with clear messages
6. Push to remote branch

---

## Key Conventions

### Code Style

**To be determined based on chosen language. Suggestions:**

#### For JavaScript/TypeScript:
- Use ES6+ features
- Prefer `const` over `let`, avoid `var`
- Use async/await over callbacks
- Follow Airbnb or Standard style guide
- Use meaningful variable names
- Maximum line length: 100 characters

#### For Python:
- Follow PEP 8 style guide
- Use type hints
- Maximum line length: 88 characters (Black formatter)
- Use descriptive variable names
- Prefer explicit over implicit

### Naming Conventions

- **Files**: `kebab-case.js` or `snake_case.py`
- **Classes**: `PascalCase`
- **Functions/Methods**: `camelCase` (JS) or `snake_case` (Python)
- **Constants**: `UPPER_SNAKE_CASE`
- **Private members**: Prefix with `_` or use private fields

### Documentation

- **All public functions**: Must have documentation comments
- **Complex logic**: Inline comments explaining why, not what
- **API changes**: Update relevant documentation immediately
- **README**: Keep user-facing documentation up to date

### Error Handling

- Use specific error types/classes
- Provide meaningful error messages
- Log errors appropriately
- Handle edge cases gracefully
- Never silently fail

---

## Architecture Guidelines

### Core Principles

1. **Modularity**: Keep components loosely coupled
2. **Single Responsibility**: Each module does one thing well
3. **DRY (Don't Repeat Yourself)**: Reuse code through functions/modules
4. **KISS (Keep It Simple)**: Prefer simple solutions
5. **Testability**: Write code that's easy to test

### Image Processing

- Support common formats: JPG, PNG, GIF, WebP, SVG
- Handle large files efficiently (streaming, chunking)
- Provide progress feedback for long operations
- Implement proper memory management
- Consider using established libraries (Sharp, Pillow, ImageMagick)

### Configuration Management

- Use configuration files (JSON, YAML, or .env)
- Support command-line arguments
- Provide sensible defaults
- Validate configuration on startup
- Document all configuration options

### Performance Considerations

- Profile before optimizing
- Use caching where appropriate
- Implement parallel processing for batch operations
- Monitor memory usage
- Optimize for common use cases

---

## Testing Strategy

### Test Coverage Goals

- **Unit tests**: 80%+ coverage
- **Integration tests**: All critical paths
- **Edge cases**: Comprehensive coverage

### Test Organization

```
tests/
├── unit/
│   ├── test_bundler.py
│   ├── test_image_processor.py
│   └── test_utils.py
├── integration/
│   ├── test_end_to_end.py
│   └── test_cli.py
└── fixtures/
    ├── sample_images/
    └── expected_outputs/
```

### Testing Best Practices

- **Arrange-Act-Assert** pattern
- Use descriptive test names
- One assertion per test (when possible)
- Mock external dependencies
- Clean up test artifacts
- Use fixtures for test data

### Running Tests

```bash
# Run all tests
npm test

# Run with coverage
npm run test:coverage

# Run specific test file
npm test -- path/to/test

# Run in watch mode
npm test -- --watch
```

---

## Git Workflow

### Commit Messages

Follow conventional commits format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Test changes
- `chore`: Build/tooling changes

**Examples:**
```
feat(bundler): add support for WebP images

Implements WebP image format support in the bundler core.
Includes compression options and quality settings.

Closes #123

fix(cli): handle missing input file gracefully

Previously, missing input files caused uncaught errors.
Now displays user-friendly error message and exits cleanly.
```

### Git Commands for AI Assistants

```bash
# Check status
git status

# Create and switch to new branch
git checkout -b feature/new-feature

# Stage changes
git add <files>

# Commit with message
git commit -m "feat: add new feature"

# Push to remote (ALWAYS use -u for new branches)
git push -u origin <branch-name>

# Note: Branch must start with 'claude/' for AI assistant work
```

### Retry Logic for Network Operations

If `git push` or `git fetch` fails due to network errors:
- Retry up to 4 times
- Use exponential backoff: 2s, 4s, 8s, 16s
- Log each retry attempt
- Fail gracefully after final attempt

---

## Common Tasks

### Adding a New Feature

1. **Plan the feature**
   - Define requirements
   - Design architecture
   - Identify affected components

2. **Create feature branch**
   ```bash
   git checkout -b feature/feature-name
   ```

3. **Implement incrementally**
   - Write tests first (TDD approach)
   - Implement minimal functionality
   - Refactor and optimize
   - Update documentation

4. **Test thoroughly**
   - Run unit tests
   - Run integration tests
   - Test edge cases
   - Manual testing

5. **Commit and push**
   ```bash
   git add .
   git commit -m "feat: description"
   git push -u origin feature/feature-name
   ```

### Fixing a Bug

1. **Reproduce the bug**
   - Create failing test case
   - Document expected vs actual behavior

2. **Identify root cause**
   - Use debugger
   - Add logging
   - Check related code

3. **Implement fix**
   - Minimal changes
   - Verify test passes
   - Check for similar bugs

4. **Commit with reference**
   ```bash
   git commit -m "fix: description (fixes #issue-number)"
   ```

### Refactoring Code

1. **Ensure tests exist**
   - Write missing tests first
   - Verify all tests pass

2. **Make small changes**
   - One refactoring at a time
   - Run tests frequently
   - Commit each logical change

3. **Document changes**
   - Update comments
   - Update documentation
   - Note breaking changes

### Updating Dependencies

1. **Check for updates**
   ```bash
   npm outdated
   ```

2. **Update incrementally**
   - Update one dependency at a time
   - Run tests after each update
   - Check for breaking changes

3. **Update lock file**
   ```bash
   npm install
   ```

4. **Commit changes**
   ```bash
   git commit -m "chore(deps): update package-name to vX.X.X"
   ```

---

## Troubleshooting

### Common Issues

#### Git Push Fails with 403

**Cause**: Branch name doesn't follow required pattern
**Solution**: Ensure branch starts with `claude/` and ends with session ID

```bash
# Correct format
git push -u origin claude/claude-md-xxxxx...
```

#### Tests Fail After Dependency Update

**Cause**: Breaking changes in updated package
**Solution**:
1. Check package changelog
2. Update code to match new API
3. Consider pinning version if needed

#### Out of Memory During Image Processing

**Cause**: Processing very large images or too many images simultaneously
**Solution**:
1. Implement streaming where possible
2. Process images in batches
3. Add memory limits
4. Use image resizing/optimization

#### Build Fails

**Cause**: Various (dependencies, syntax, configuration)
**Solution**:
1. Check error message carefully
2. Verify all dependencies installed
3. Clear build cache
4. Check for syntax errors
5. Verify configuration files

---

## AI Assistant Guidelines

### When Making Changes

1. **Always read before editing**
   - Use Read tool before Edit tool
   - Understand context fully

2. **Prefer editing over creating**
   - Edit existing files when possible
   - Only create new files when necessary

3. **Use appropriate tools**
   - Read: For viewing files
   - Edit: For modifying existing files
   - Write: Only for new files
   - Bash: For terminal commands
   - Grep/Glob: For searching

4. **Track progress**
   - Use TodoWrite for complex tasks
   - Mark tasks as in_progress/completed
   - Keep one task in_progress at a time

5. **Test changes**
   - Run tests after changes
   - Verify builds succeed
   - Check for regressions

### Communication

- Be concise and clear
- Focus on technical accuracy
- Provide code references with `file:line`
- Explain decisions and trade-offs
- Ask for clarification when needed

### Security

- Never commit secrets or credentials
- Validate all inputs
- Sanitize file paths
- Prevent command injection
- Follow OWASP guidelines
- Use parameterized queries
- Implement rate limiting where appropriate

### Performance

- Profile before optimizing
- Use appropriate data structures
- Cache expensive operations
- Minimize I/O operations
- Use async/parallel processing
- Monitor resource usage

---

## Project-Specific Notes

### Image Bundle Format

**To be defined**: Document the expected format for image bundles
- Input format specifications
- Output format specifications
- Metadata handling
- Compression settings

### Supported Operations

**To be defined**: List all supported bundling operations
- Combine multiple images
- Resize/optimize images
- Apply filters/transformations
- Generate thumbnails
- Extract images from bundles

### Configuration Options

**To be defined**: Document all configuration parameters
- Image quality settings
- Compression algorithms
- Output formats
- Batch processing options
- Memory/performance limits

---

## Resources

### Documentation

- [README.md](./README.md) - User-facing documentation
- [API Documentation](./docs/api/) - API reference (to be created)
- [Contributing Guide](./CONTRIBUTING.md) - For external contributors (to be created)

### External Resources

- Image processing best practices
- Performance optimization guides
- Security guidelines for file handling
- Relevant library documentation

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-11-14 | Initial CLAUDE.md creation |

---

## Notes for Future Updates

This document should be updated when:
- Project structure changes significantly
- New conventions are adopted
- New tools or libraries are integrated
- Deployment process changes
- New security considerations arise
- Performance requirements change

**Last Review**: 2025-11-14
**Next Review**: After first major feature implementation
